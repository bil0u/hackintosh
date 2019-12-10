## Coffee-Lake Hackintosh

Here is my personal hackintosh monster configuration. It's a perfect working and gaming station that i use everyday.

It runs **macOS 10.13.6** and **Windows 10**


## Hardware

Component | Model | Notes
--- | --- | ---
**Logic board** | `Gigabyte Z390 Aorus Master` | *Bios rev. F10*
**CPU** | `Intel Core i9 9900K` | *Stock frequency (OC planned)*
**GPU** | `MSI Nvidia GTX 1080Ti Gaming X Trio` |
**RAM** | `G.Skill Trident Z RGB 4x8GB @ 4133MHz` | *Model F4-4133C17Q-32GTZR*
**Storage** | <li>`Samsung SSD 970 Pro 512GB`</li><li>`Samsung SSD 970 Evo 1TB`</li> | *970 Pro : OS <li>256 GB APFS</li><li>256 GB NTFS</li> <br> 970 Evo : Data <li>1 TB ExFAT</li>*
**Network** | `Broadcom BCM94360CD` | *PCIe Expansion Card w/ antennas used*
**Power supply** | `Seasonic PRIME Ultra Titanium 750W` |
**Case** | `Phanteks Enthoo Evolv X Anthracite Grey` |
**Cooler** | `NZXT Kraken X72 AIO 360mm` |

---

## BIOS Settings

Bios revision `F10`. Optimized defaults + following settings :

Key | Value
--- | ---
**Tweaker** > **Extreme Memory Profile (X.M.P.)** | `Profile1`
**Settings** > **Platform Power** > **Platform Power Management** | `Enabled`
**Settings** > **Platform Power** > **DMI ASPM** | `Enabled`
**Settings** > **Platform Power** > **ErP** | `Enabled`
**Settings** > **IO Ports** > **Internal Graphics** | `Disabled`
**Settings** > **IO Ports** > **USB Configuration** > **XHCI Hand-Off** | `Enabled`
**Settings** > **IO Ports** > **USB Configuration** > **Port 60/40 Emulation** | `Enabled`
**Settings** > **Miscellaneous** > **Trusted Computing** > **Security Device Support** | `Disable`
**Boot** > **Windows 8/10 Features** | `Other OS`
**Boot** > **CSM Support** | `Disabled`
**Boot** > **Preferred Operating Mode** | `Advanced Mode`

> Note : VT-d is enabled by default, I keep it enabled as I need virtualization for Docker

---

## Clover

[Clover v2.5k-5100](https://github.com/CloverHackyColor/CloverBootloader/releases/tag/5100) is used. All paths mentioned below refers to the EFI partition

#### UEFI Drivers

All the drivers come from Clover v2.5k-5100.  
Location : `EFI/CLOVER/drivers/UEFI/`

- `ApfsDriverLoader`
- `AptioMemoryFix`
- `EmuVariableUefi`
- `FSInject`
- `HFSPlus`
- `NTFS`


#### Kexts

Location : `EFI/CLOVER/kexts/Other/`

Kext | Version
--- | ---
AppleALC | 1.4.4
IntelMausiEthernet | 2.4.1d1
Lilu | 1.4.0
USBMap | Custom
WhateverGreen | 1.3.5
FakeSMC & Sensors <br> <li>FakeSMC_CPUSensors</li><li>FakeSMC_GPUSensors</li><li>FakeSMC_LPCSensors</li><li>FakeSMC_SMMSensors</li> | 6.26-357-gceb835ea.1800

> Note : USBMap.kext is a custom kext for Z390 Aorus Master + Phanteks Evolv X as i use the front panel USB3 and USB-C. You should build your own

#### ACPI

Location : `EFI/CLOVER/ACPI/patched/`

- `SSDT-EC`
- `SSDT-UIAC`
- `SSDT-USBX`
- `SSDT-XOSI`

---

## TODO


- CPU Overclock @ 5.0 GHz
- Activating iGPU in order to get full graphics acceleration 
