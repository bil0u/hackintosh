## Configuration

This is my configuration for OpenCore 0.6.0 release version (everyday use)

#### ACPI

> So what are DSDTs and SSDTs ?  
> Well, these are tables present in your firmware that outline hardware devices like USB controllers, CPU threads, embedded controllers, system clocks and such. A DSDT can be seen as the body holding most of the info with smaller bits of info being passed by the SSDT.
> You can think of the DSDT as the building blueprints with SSDTs being sticky notes outlining extra details to the project

→ Location : `EFI/OC/ACPI/`

- `SSDT-AWAC.aml`
- `SSDT-BRG0.aml`
- `SSDT-EC-USBX.aml`
- `SSDT-GPRW.aml`
- `SSDT-PLUG.aml`
- `SSDT-PMC.aml`
- `SSDT-SBUS-MCHC.aml`

#### UEFI Drivers

> Firmware drivers are drivers used by OpenCore in the UEFI environment.  
> They're mainly required to boot a machine, either by extending OpenCore's patching ability or showing you different types of drives in the OpenCore picker(ie. HFS drives.

→ Location : `EFI/OC/Drivers/`

- `HFSPlus.efi`
- `NvmExpressDxe.efi`
- `OpenCanopy.efi`
- `OpenRuntime.efi`

#### Kexts

> A kext is a kernel extension.  
> You can think of this as a driver for macOS.

→ Location : `EFI/OC/Kexts/`

| Kext                                                                 | Version |
| -------------------------------------------------------------------- | ------- |
| AppleALC                                                             | 1.6.8   |
| IntelBluetoothFirmware                                               | 2.1.0   |
| IntelBluetoothInjector                                               | 2.1.0   |
| IntelMausi                                                           | 1.0.7   |
| itlwm                                                                | 2.1.0   |
| Lilu                                                                 | 1.5.9   |
| NVMeFix                                                              | 1.0.9   |
| RestrictEvents                                                       | 1.0.6   |
| WhateverGreen                                                        | 1.5.6   |
| USBPower                                                             | Custom  |
| VirtualSMC + sensors : <br> <li>SMCProcessor</li><li>SMCSuperIO</li> | 1.2.8   |

> Note : USBPower.kext is a custom kext for Z390 Aorus Master + Phanteks Evolv X as i use the front panel USB3 and USB-C. You should build your own

#### config.plist

> I mention only values that that must be set or i have added. See the sample config.plist provided in the OpenCore [docs](https://github.com/acidanthera/OpenCorePkg/tree/master/Docs).
> I followed the _Desktop Coffee Lake_ [config guide](https://dortania.github.io/OpenCore-Install-Guide/config.plist/coffee-lake.html#starting-point)

For full details, see the config file [here](/EFI/OC/config.plist)

- ### Root

  > ⚠️ Not up to date ⚠️
  > _Does not reflect yet the current config_

  - #### ACPI
    - ##### Add
      - **SSDT-AWAC**
      - **SSDT-BRG0**
      - **SSDT-EC-USBX**
      - **SSDT-GPRW**
      - **SSDT-PLUG**
      - **SSDT-PMC**
      - **SSDT-SBUS-MCHC**
  - #### Booter
    - ##### Quirks
      - **DevirtualizeMmio** [Boolean] : `True`
      - **EnableWriteUnprotector** [Boolean] : `False`
      - **ProtectUefiServices** [Boolean] : `True`
      - **RebuildAppleMemoryMap** [Boolean] : `True`
      - **SyncRuntimePermissions** [Boolean] : `True`
  - #### DeviceProperties
    - ##### Add
      - **PciRoot(0x0)/Pci(0x1f,0x3)**
        - **layout-id** [Data] : `<10000000>`
      - **PciRoot(0x0)/Pci(0x2,0x0)**
        - **igfxfw** [Data] : `<02000000>`
  - #### Kernel
    - ##### Add
      - **Lilu**
      - **VirtualSMC**
      - **AppleALC**
      - **IntelMausi**
      - **SMCProcessor**
      - **SMCSuperIO**
      - **USBMap**
      - **WhateverGreen**
      - **XHCI-unsupported**
    - ##### Quirks
      - **AppleCpuPmCfgLock** [Boolean] : `False`
      - **AppleXcpmCfgLock** [Boolean] : `False`
      - **DisableIOMapper** [Boolean] : `True`
      - **LapicKernelPanic** [Boolean] : `False`
      - **PanicNoKextDump** [Boolean] : `True`
      - **PowerTimeoutKernelPanic** [Boolean] : `True`
      - **XhciPortLimit** [Boolean] : `False`
  - #### Misc
    - ##### Boot
      - **HibernateMode** [String] : `None`
      - **PickerAttributes** [Number] : `1`
      - **PickerMode** [String] : `External`
    - ##### Debug
      - **AppleDebug** [Boolean] : `False`
      - **ApplePanic** [Boolean] : `False`
      - **DisableWatchDog** [Boolean] : `False`
      - **Target** [Number] : `3`
    - ##### Security
      - **AllowNvramReset** [Boolean] : `True`
      - **AllowSetDefault** [Boolean] : `True`
      - **BootProtect** [String] : `Bootstrap`
      - **Vault** [String] : `Optional`
      - **ScanPolicy** [Number] : `0`
    - ##### Tools
      - **OpenShell**
  - #### NVRAM
    - **WriteFlash** [Boolean] : `True`
    - ##### Add
      - **4D1EDE05-38C7-4A6A-9CC6-4BCCA8B38C14**
        - **UIScale** [Data] : `<01>`
        - **DefaultBackgroundColor** [Data] : `<00000000>`
      - **4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102**
        - **rtc-blacklist** [Data] : `<>`
      - **7C436110-AB2A-4BBB-A880-FE41995C9F82**
        - **boot-args** [String] : `debug=0x100 keepsyms=1 nvda_drv_vrl=1`
        - **csr-active-config** [Data] : `<00000000>`
        - **prev-lang:kbd** [String] : `en-US:0`
  - #### PlatformInfo
