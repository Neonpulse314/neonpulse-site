---
title: "Acoustic Tractor Beams: The Technology That Moves Objects With Sound"
date: 2026-03-21
description: "Sound can lift objects, rotate them, and hold them suspended in mid-air without touching them. This has been demonstrated in labs around the world. The gap between that demonstration and a useful device comes down to one number: scale."
section_label: "engineering"
tags: ["physics", "acoustics", "engineering", "sound", "levitation"]
---

In 2015, researchers at the University of Bristol levitated small polystyrene beads using sound alone — not touching them, not using any field the objects interacted with magnetically or electrically, just sound waves converging from multiple directions. The beads held position, rotated, and moved on command.

The physics is real. The applications that follow from it are not yet real. The gap is a problem of scale, and scale turns out to be harder than it looks.

## Why Sound Can Push Things

Sound is pressure waves — alternating compressions and rarefactions moving through a medium. When sound hits an object, it transfers momentum. This is acoustic radiation pressure, and it has been understood since the late nineteenth century.

For most sounds at most intensities, the force is negligible. But when you concentrate enough acoustic energy at the right frequency and phase, the force becomes large enough to overcome gravity for small objects. The key is not just intensity — it is the spatial structure of the sound field.

A tractor beam specifically requires a sound field that can push from multiple directions simultaneously, creating a region of low pressure that holds the object in place. The technique that works in current demonstrations is called a "holographic acoustic trap" — an array of small ultrasonic transducers, each emitting a wave, all coordinated so their interference pattern produces a stable pressure minimum exactly where you want the object.

The ultrasound frequency used (typically 40 kHz) is above human hearing. At that frequency, the wavelength is about 8 millimetres in air. Objects smaller than the wavelength are the ones that levitate stably. Objects much larger than the wavelength are not.

## What Has Been Demonstrated

The demonstrations are real and reproducible:

In 2016, the Bristol group showed that objects could not just be held but actively moved — translated through space and rotated — by updating the phase pattern in the transducer array in real time. The objects were polystyrene spheres a few millimetres across.

In 2018, a team at the University of São Paulo demonstrated levitation of objects up to 50 millimetres — roughly the size of a grape — by using higher power and a redesigned transducer array. This was the largest acoustic levitation of a solid object in air at the time.

In 2019, researchers showed that acoustic tractor beams could work in water as well as air, which matters for applications involving liquids and biological samples.

In 2020, work from the University of Tokyo demonstrated real-time manipulation of objects through visual feedback — a system that could track where an object drifted and correct automatically. The levitation was becoming a tool, not just a demonstration.

The capability is not in dispute. The question is what you do with it.

## The Scale Problem

The fundamental constraint comes from the relationship between wavelength and object size. An acoustic tractor beam works by creating a stable pressure trap, and the stability of that trap requires the object to be smaller than or comparable to the acoustic wavelength.

At 40 kHz in air, the wavelength is 8.5 mm. Objects up to about that size levitate stably. To levitate larger objects, you need longer wavelengths, which means lower frequencies, which means more powerful sources, which means more heat and structural complexity.

At audible frequencies (below 20 kHz), the wavelengths are long enough to levitate objects of centimetre scale — but the sound intensities required are extreme. The human ear becomes relevant at these frequencies; the equipment becomes larger and louder.

The largest demonstrated acoustic levitation in air, as of current published work, involves objects roughly the size of a coin. Levitating a ball bearing is a demonstration. Levitating a component in a manufacturing line is a different engineering problem.

## What Would Make It Useful

Two applications are plausible at the current demonstrated scale:

**Contactless manipulation of biological samples.** In laboratory settings, acoustic levitation allows you to handle droplets of liquid, cells in suspension, or small tissue samples without touching them. This matters because touching introduces contamination and mechanical stress. Several research groups are developing acoustic manipulation platforms for lab-on-a-chip applications — processing biological samples through acoustic fields rather than pipettes and mechanical actuators. At millimetre scale, this works now.

**Pharmaceutical manufacturing.** Some drug compounds are sensitive enough that physical contact during processing changes their crystalline structure, which changes how they dissolve and how effective they are. Acoustic levitation lets you process these compounds in air, at any orientation, without a container wall. Industrial acoustic levitation for pharmaceutical applications is being developed by multiple companies. The scale remains small, but pharmaceutical applications often involve small quantities of expensive materials — small scale is not necessarily a disqualification.

What is not yet plausible: moving objects at human scale, assembling components in open air on a production line, or anything resembling science fiction depictions of tractor beams lifting large objects at distance.

## Where the Engineering Is Stuck

The transducer array is the limiting factor. Current demonstrations use arrays of 256 or 512 small ultrasonic emitters, each controlled independently in phase and amplitude. This produces impressive results for small objects in controlled conditions. Scaling to larger objects requires either lower frequencies (with all the associated problems) or much more powerful arrays (with heat dissipation problems).

Heat is the specific bottleneck. Acoustic transducers are not perfectly efficient. At high power, they heat up. The heating changes their resonant frequency, which shifts their acoustic output, which disrupts the trap. Maintaining a stable acoustic trap at high power requires either cooling systems or transducer materials that handle heat better than current piezoelectrics.

There is also a problem of range. The demonstrations are tabletop — objects suspended centimetres from the transducer surface. At greater distances, the acoustic field spreads and weakens. A long-range acoustic tractor beam would require a much larger array, more power, and better beam-forming algorithms to maintain a stable trap.

## The Margin

Acoustic tractor beams work. They work reliably enough that multiple research groups have commercialized the underlying technology for laboratory instruments. The company Ultrahaptics (now Ultraleap) uses phased ultrasonic arrays to produce tactile feedback in mid-air — not levitation, but the same physics, now in commercial hardware used for automotive interfaces and medical displays.

The gap between "demonstrated in a laboratory" and "useful in a factory" is not a gap of physics. The physics closed. The gap is engineering: transducer efficiency, heat management, control systems, and the hard constraint that the wavelength-to-object-size ratio sets an upper bound that current frequencies cannot lift.

Moving a 5mm polystyrene bead in a university lab is not the same as moving a 50mm steel bolt on an assembly line. But the path from one to the other is a path of engineering, and it is the kind of path that historically gets walked.

---

**Sources:** Marzo et al., "Holographic acoustic elements for manipulation of levitated objects," *Nature Communications* (2016). Foresti et al., "Acoustofluidic contactless transport and handling of matter in air," *PNAS* (2013). Melde et al., "Holograms for acoustics," *Nature* (2016). Zang et al., "Acoustic levitation of larger objects," *Physical Review Applied* (2018). Ultraleap company documentation (2024).
