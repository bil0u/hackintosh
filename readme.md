## OpenCore Hackintosh

On this repo you will find the configuration of my Coffee Lake hackintosh that i use everyday for working and gaming.

It's running an **Intel 9900K** CPU on the **Z390 Aorus Master**

### Bootloader

This hackintosh runs on [OpenCore v0.6.0 release](https://github.com/acidanthera/OpenCorePkg) from [acidanthera](https://github.com/acidanthera)

You can find the install guide [here](https://dortania.github.io/OpenCore-Install-Guide)


### Configuration

I'm currently running **macOS 10.13.6 build 17G14019** vanilla with `iMac18,3` SMBIOS and Windows 10 on the same drive.

Have a look at my [hardware](/hardware.md), [bios settings](/bios_settings.md), [config](/config.md), and [notes](/notes.md) !

### Tools

I added some custom tools:
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


### What's working

- [x] Ethernet
- [x] Wi-Fi (via Broadcom BCM94360CD + PCIe connection via internal adapter)
- [x] Onboard Audio (including digital audio)
- [x] APFS
- [x] All USB ports at full 3.x speed
- [x] iMessage
- [x] App Store
- [x] Facetime
- [x] AirPlay
- [x] Power Nap
- [x] NVRAM
- [ ] Bluetooth (via Broadcom BCM94360CD + USB connection via internal adapter)
	- Airdrop
	- Handoff
	- Continuity
- [ ] Sleep/Wake
- [ ] Perfect sound quality

### Tasks :


- **Done** :

	- [x] Patch CFG Lock
	- [x] Fix NVRAM
	- [x] Fix EC and USBX
	- [x] Fix System clocks
	- [x] Fix CPU power management
	- [x] Map USB


- **Short term** :

	- [ ] Fix sleep/wake
	- [ ] Fix audio cracklings/sync
	- [ ] Enable iGPU full acceleration
	- [ ] Overclock CPU @ 5.0 GHz
	- [ ] Fix bluetooth issues (maybe buy a BCM943602CDP card ?)


- **Long term** :

	- [ ] Upgrade GPU to a Radeon VII 16GB
	- [ ] Update to macOS 10.15
