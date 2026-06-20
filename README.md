# Can I Use Linux?

Can I use Linux on my device? Yes, most likely.

This project aims to provide a simple system for non-technical users to validate whether their device can be used with Linux, and if any missing functionalities  (while rare) could be seen. This information may be available to technical users via simple searches online or just trying with live versions, but is currently missing in a easy-to-navigate format.

To solve this, the project is composed of 2 main knowledge bases:
- Static information on the suport available for specific components (CPUs, network, ...), to be aggregated to compose known devices expected compatiblity
- Actual confirmation by users for specific devices

This should be displayed in a simple website, providing a page for each known device and the respective high level compatiblity.
We will also try to provide in-depth information of what (if anything) is not working or bugged, with repsective kernel & main operating systems available.

Please note this is an open-source project, and thus the level of details and precision may vary. We will also track if specific compatiblity opinions are actual opinions or verified.

## Why do we need this?

Technical users have no issues with just trying to install Linux in any of its flavors on a device, as they know how to fix issues or revert back to the previous OS (either by know-how or just ability to look for information).

A non-technical user (anyone which has ever only used a device as is, without ever opering a terminal) will get scared at any of the following points in no particular order:
- Hearing of or about Linux
- Linux distros
- Thinking about replacing the whole operating system
- Configuration of a device
- Warranty(?) of the device
- What to do if something breaks

This project will not target all these questions as their answer changes based on device and preference (and country of the user for warranty and other legal technicalities).

## What we track exactly

Each device has its own peculiarities, due to the combination of components and eventual proprietary software connected to it.

We aim to track:
- All devices reported directly or found online, with a focus on commercial devices (laptops especially)
- All related features of a device, including the most minimal ones (e.g. power management, biometric sensors, ...)
- Information on the official Linux kernel and respective primary Linux distros

We will try to keep the knowledge of this project high-level and focus of component families (e.g. CPU series and not individual models, same for GPUs and other components). The same should apply for devices - it is irrelevant to keep separate tracking for devices where the CPU generation does not change but only its power capacity (e.g. Intel 5-7-9 of the same generation is irrelevant) or storage/RAM capacities, but we should track when there are things which would affect compatibility.

## How we display it

For each device tracked, we will provide a single page with its name, a simple image (if available) and a high-level evaluation of compatilility between:
- None (not working)
- Experimental (usable by tech users for experiments)
- Decent (common features supported, like keyword and display)
- good (most features supported, some minor quality of life ones missing)
- full (all features supported)

## License

This project uses the GPL-2.0 license.