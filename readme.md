# Coffee-Lake Hackintosh

On this repo you will find the configuration of my hackintosh that i use everyday for working and gaming.

It's been a long journey since the purchase of the components fixing bugs and testing different bootloaders, but it runs incredibly smooth now, and i'm so much happy with it.

## Bootloader

This hackintosh runs on [OpenCore v0.6.5 release](https://github.com/acidanthera/OpenCorePkg) from [acidanthera](https://github.com/acidanthera).
> I was previously using Clover, never again !


## Configuration

I'm currently running **macOS 10.13.6 build 17G14019** vanilla and **Windows 10** on the same drive.

Quick hardware tour :  **Intel Core i9 9900-K** & **NVIDIA GeForce GTX 1080 Ti** on the **Gigabyte Z390 Aorus Master**.  
*→ Full hardware list [here](/docs/hardware.md)*

I followed these install steps :

1. **macOS + OpenCore** : official dortania [install guide](https://dortania.github.io/OpenCore-Install-Guide).
2. **Windows 10** : the steps described [here](/docs/windows_install.md)

Have a look at the [bios settings](/docs/bios_settings.md) and [config](/docs/config.md) I use.

## Tools

I built some useful tools, feel free to use them :

- [manage_config](/tools/manage_config.py) : useful for clear secrets in your config.plist before adding it to version control.
    ```shell script
    usage: python3 tools/manage_config.py [-h] [-c CONFIG] [-b BACKUP] {backup,clean,restore}

    Manage OpenCore configuration secrets

    positional arguments:
      {backup,clean,restore}
                        command to execute. clean makes also a backup

    optional arguments:
      -h, --help        show this help message and exit
      -c CONFIG, --config CONFIG
                        target configuration
      -b BACKUP, --backup BACKUP
                        backup file destination. we recommend to put a .json extension
    ```

- [custom_atm](/tools/custom_atm.py): customizes the 'About this Mac' panel.
    ```shell script
    usage: python3 tools/custom_atm.py [-h] [--system-logo SYSTEM_LOGO] [--model-name MODEL_NAME] [--processor-name PROCESSOR_NAME]

    Customizes 'About this Mac' section of a macOS system

    optional arguments:
      -h, --help        show this help message and exit
      --system-logo SYSTEM_LOGO
                        system logo to use. logo format must be TIFF
      --model-name MODEL_NAME
                        custom model name
      --processor-name PROCESSOR_NAME
                        custom processor name
    ```


## Achievements

- [x] Ethernet
- [x] Wi-Fi + Bluetooth (via On-board Intel Wireless AC 9560)
- [x] Onboard Audio (including digital audio)
- [x] All USB ports at full 3.x speed
- [x] APFS
- [x] iCloud, iMessage, AppStore, FaceTime, AirPlay
- [x] Power Nap
- [x] NVRAM
- [x] Sleep/Wake


### Tasks :


- **Done** :

	- [x] Patch CFG Lock
	- [x] Fix NVRAM
	- [x] Fix EC and USBX
	- [x] Fix System clocks
	- [x] Fix CPU power management
	- [x] Map USB
	- [x] Fix sleep/wake
	- [x] Fix audio cracklings/stop/desync ([notes](/docs/issues.md))
	- [x] Fix Bluetooth
	- [x] Fix Magic Keyboard pairing issue when switching OS ([notes](/docs/issues.md))


- **Short term** :

	- [ ] Enable iGPU full acceleration
	- [ ] Overclock CPU @ 5.0 GHz
	- [ ] Buy a native/supported wireless card (Maybe a BCM943602CDP ?)


- **Long term** :

	- [ ] Upgrade GPU to a Radeon VII 16GB
	- [ ] Update to macOS 10.15
