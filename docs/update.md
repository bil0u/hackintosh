
# Updating OpenCore

## Prerequisites

- [ ] Download [OpenCore latest release](https://github.com/acidanthera/opencorepkg/releases)
- [ ] Fetch the latest drivers
- [ ] Fetch the latest kexts
- [ ] Download and update needed tools


## Instructions


1. Copy the actual EFI folder on a USB key EFI partition (USB key partition format must be GUID)
2. Replace the following files with latest OpenCore release ones :  
    - `EFI/BOOT/BOOTx64.efi`
    - `EFI/OC/OpenCore.efi`
    - `EFI/OC/Drivers/OpenRuntime.efi`
    - `EFI/OC/Drivers/OpenCanopy.efi` (If you use it)
    > My two cents : you should use the DEBUG version of these files first, it will be easier to troubleshoot
3. Replace the drivers you need with the latest ones
4. Do the same with the kexts
5. Using OCConfigCompare, compare the `config.plist` from the USB key's EFI with the Sample.plist from latest OC release
    > You can add `-v` option to the boot flags, useful for debug
6. Use ProperTree to edit your `config.plist` according to the output of OCConfigCompare
7. Run `ocvalidate` (located in `<OC_Release>/Utilities/ocvalidate`) with your updated config.plist
8. **Boot !**
    > If it fails, my advice is to recreate a clean EFI folder using [OpenCore documentation](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/opencore-efi.html)
9. If you used the DEBUG version:
    - replace the files from step 2 with the ones from the RELEASE version.
    - delete `-v` option from your `config.plist` boot args
    - boot again to make sure everything still works
10. Copy over your USB key EFI folder to your local drive.
11. Restart.
12. You're done ! 🎉



## Download links

### Apps / Tools

- [ProperTree](https://github.com/corpnewt/ProperTree)
- [OCConfigCompare](https://github.com/corpnewt/OCConfigCompare)
- [HeliPort](https://github.com/OpenIntelWireless/HeliPort/releases)

### Drivers

- [HfsPlus](https://github.com/acidanthera/OcBinaryData/blob/master/Drivers/HfsPlus.efi)

### Kexts

- [Lilu](https://github.com/acidanthera/lilu/releases)
- [WhateverGreen](https://github.com/acidanthera/whatevergreen/releases)
- [AppleALC](https://github.com/acidanthera/applealc/releases)
- [IntelMausi](https://github.com/acidanthera/IntelMausi/releases)
- [VirtualSMC](https://github.com/acidanthera/virtualsmc/releases)
- [itlwm](https://github.com/OpenIntelWireless/itlwm/releases)
- [IntelBluetoothFirmware](https://github.com/OpenIntelWireless/IntelBluetoothFirmware/releases)


