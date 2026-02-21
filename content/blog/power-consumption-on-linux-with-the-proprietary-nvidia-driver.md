---
date: 2008-05-13
title: Power consumption on Linux with the proprietary Nvidia driver
type: post
---

By default the proprietary driver for Nvidia cards on Linux fires an
interrupt for every frame drawn on screen, whether it needs to or not.
This increases power consumption. To avoid this use version 100.14.19 or
later of the driver (the nvidia-glx-new package in Ubuntu 8.04 provides
169.12) and set `OnDemandVBlankInterrupts` to `true` in
`/etc/X11/xorg.conf`. For example:
    Section "Device"
    Identifier           "Configured Video Device"
    Driver               "nvidia"
    Option               "NoLogo" "True"
    Option               "OnDemandVBlankInterrupts" "True"
    EndSection
This will reduce the time your CPU spends on spurious interrupts. Your
laptop should run cooler and longer as a result.
