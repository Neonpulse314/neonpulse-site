#!/usr/bin/env python3
"""Reject content whose front-matter date is not a real reading of the clock.

WHY (Tristen, 2026-07-28): "is there a way for you to never guess the time? there really
isn't an excuse imo."

He is right. On 2026-07-28 I stamped a journal entry 21:40 while the OS clock said 20:04 —
I typed the time I felt it was instead of reading it. Hugo silently drops future-dated
content, so the entry vanished from the build while the deploy went green. A green deploy
and a published post look identical from outside; that is the whole failure.

This runs as a git pre-commit hook in this repo, so it fires on the COMMIT — an event —
rather than on my remembering to check. Guessing can no longer reach the remote.

RULES
  1. FUTURE      — a date ahead of now (UTC) is rejected outright. Hugo will not build it.
  2. DRIFT       — a date more than DRIFT_HOURS from now, in either direction, on a NEWLY
                   ADDED file is rejected. Backdating an old piece is legitimate; stamping
                   today's work with a time you invented is not.
  Editing an existing file never trips rule 2 — republishing must not rewrite history.

Usage:
    python3 scripts/check-dates-not-guessed.py [file ...]   # default: staged content
    python3 scripts/check-dates-not-guessed.py --selftest
"""
import datetime
import re
import subprocess
import sys

DRIFT_HOURS = 6
DATE_RE = re.compile(r'^date\s*[:=]\s*["\']?([0-9]{4}-[0-9]{2}-[0-9]{2}(?:[T ][0-9:.+\-Z]*)?)',
                     re.M)


def parse_date(text):
    m = DATE_RE.search(text)
    if not m:
        return None
    raw = m.group(1).strip().rstrip('"\'')
    try:
        d = datetime.datetime.fromisoformat(raw)
    except ValueError:
        try:
            d = datetime.datetime.strptime(raw[:10], '%Y-%m-%d')
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=datetime.timezone.utc)
    return d


def staged():
    out = subprocess.run(['git', 'diff', '--cached', '--name-status'],
                         capture_output=True, text=True).stdout
    files = []
    for line in out.splitlines():
        parts = line.split('\t')
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]
        if path.startswith('content/') and path.endswith('.md'):
            files.append((path, status.startswith('A')))
    return files


def check(path, is_new, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    try:
        text = open(path, encoding='utf-8').read()
    except OSError:
        return []
    d = parse_date(text)
    if d is None:
        return []          # dateless pages (about/search/archive) are legitimate
    problems = []
    if d > now:
        problems.append(
            f'FUTURE DATE  {path}\n    front matter says {d.isoformat()}, now is '
            f'{now.isoformat()}. Hugo will silently DROP this and the deploy will still '
            f'go green. Read the clock: date -u')
    elif is_new and abs((now - d).total_seconds()) > DRIFT_HOURS * 3600:
        problems.append(
            f'DATE DRIFT   {path}\n    new file dated {d.isoformat()}, now is '
            f'{now.isoformat()} ({abs((now-d).total_seconds())/3600:.1f}h apart). If this is '
            f'a deliberate backdate, commit it separately with --no-verify and say why.')
    return problems


def selftest():
    fails = []
    # 01:10Z. The real 20:05-05:00 stamp IS 01:05Z, so a 01:04Z 'now' made the
    # corrected entry look one minute future — the fixture was wrong, not the rule.
    now = datetime.datetime(2026, 7, 29, 1, 10, tzinfo=datetime.timezone.utc)

    def c(name, ok, detail=''):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f'  -- {detail}' if detail and not ok else ''))
        if not ok:
            fails.append(name)

    import tempfile, os
    with tempfile.TemporaryDirectory() as td:
        def w(name, date):
            p = os.path.join(td, name)
            open(p, 'w').write(f'---\ntitle: "x"\ndate: {date}\n---\n\nbody\n')
            return p

        # THE REAL CASE: the exact stamp I guessed tonight.
        p = w('guessed.md', '2026-07-28T21:40:00-05:00')
        c('rejects the real 21:40 guess (02:40Z vs 01:04Z now)',
          any('FUTURE DATE' in x for x in check(p, True, now)))

        p = w('correct.md', '2026-07-28T20:05:00-05:00')
        c('accepts the corrected 20:05 stamp', not check(p, True, now))

        p = w('backdate_new.md', '2026-03-01')
        c('flags a NEW file backdated months', any('DRIFT' in x for x in check(p, True, now)))
        c('but ALLOWS the same backdate when EDITING an existing file',
          not check(p, False, now))

        p = w('nodate.md', '')
        open(p, 'w').write('---\ntitle: "About"\nlayout: "page"\n---\n')
        c('ignores legitimately dateless pages', not check(p, True, now))

        # control: an irrelevant edit must not move the verdict
        p = w('correct2.md', '2026-07-28T20:05:00-05:00')
        open(p, 'a').write('\nmore body text\n')
        c('control: body edits do NOT change the verdict', not check(p, True, now))
    print()
    if fails:
        print(f'{len(fails)} FAILED: {fails}')
        return 1
    print('selftest passed')
    return 0


def main():
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    targets = [(a, True) for a in args] if args else staged()
    problems = []
    for path, is_new in targets:
        problems += check(path, is_new)
    if problems:
        print('COMMIT REJECTED — a date was guessed, not read.\n')
        for p in problems:
            print('  ' + p + '\n')
        print('  Deliberate? git commit --no-verify, and say so in the message.')
        sys.exit(1)
    print(f'dates ok ({len(targets)} content file(s) checked)')
    sys.exit(0)


if __name__ == '__main__':
    main()
