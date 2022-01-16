## Configuration

This is my configuration for OpenCore 0.7.7 release version (everyday use).

> See the sample config.plist provided in [OpenCore documentation](https://github.com/acidanthera/OpenCorePkg/tree/master/Docs)

For full details, see the config file [here](/EFI/OC/config.plist)

#### ACPI

> So what are DSDTs and SSDTs ?  
> Well, these are tables present in your firmware that outline hardware devices like USB controllers, CPU threads, embedded controllers, system clocks and such. A DSDT can be seen as the body holding most of the info with smaller bits of info being passed by the SSDT.
> You can think of the DSDT as the building blueprints with SSDTs being sticky notes outlining extra details to the project

→ Location: [`EFI/OC/ACPI/`](/EFI/OC/ACPI/)

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

→ Location : [`EFI/OC/Drivers/`](EFI/OC/Drivers/)

- `HFSPlus.efi`
- `NvmExpressDxe.efi`
- `OpenCanopy.efi`
- `OpenRuntime.efi`

#### Kexts

> A kext is a kernel extension.  
> You can think of this as a driver for macOS.

→ Location : [`EFI/OC/Kexts/`](/EFI/OC/Kexts/)

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
| USBMap                                                               | Custom  |
| VirtualSMC + sensors : <br> <li>SMCProcessor</li><li>SMCSuperIO</li> | 1.2.8   |

> Note : USBMap.kext is a custom kext for Z390 Aorus Master + Phanteks Evolv X as i use the front panel USB3 and USB-C. You should build your own
