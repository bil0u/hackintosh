# Issues

Here you will find some personal notes about some problems i encountered and the steps i followed to solve them.

---

## Secondary drive(s) does not appear in Windows Explorer

Some of your drives does not appear in Windows Explorer but are visible normally on macOS ?

1. Open Explorer

2. Right click on `This PC`, then `Manage`

3. On the left column, click `Disk management`

4. Select the problematic drive, right click, then `Change drive letter and paths`

   > If your drive does not appear in Disk Management, then these steps will not help you at all

5. Click add, then select a letter and you're good to go !

#### Hey, the problem is still here after reboot !

Don't panic, just try this :

1. Open Run or cmd

2. Type `diskpart` then hit enter

3. In diskpart shell :

   - type `list volume`
   - then `select volume X` (where `X` is the number corresponding with your problematic drive)
   - then `attributes volume clear hidden`
   - then `exit`

4. Reboot your computer and voilà, you should be OK now !

---

## macOS audio issues

Audio crackles, stop and/or desynchronizes on macOS, even with `AppleALC.kext` and `layout-id=16`.

This fix worked for me :

1. Open `Audio MIDI Setup.app` located under `/Applications/Utilities`
2. Select your sound output on the left panel
3. Under `Format (Bitrate)`, try all values starting from the biggest value (the lower one in the list)

My preset : `2-channel 32-bit 96.0kHz floating point number`

---

## LED/fans stays on when computer is off

Fix: Enable `ErP` in BIOS

---

## Bluetooth device needs to be paired again when i switch OS

When switching from Windows to macOS and vice versa, my Apple Magic Keyboard needs to be paired each time.

The followings steps solves the issue :

1. Boot in Windows
2. Pair your device
3. Restart and boot in macOS
4. Pair your device
5. In a terminal, type :
   ```shell
   sudo defaults read /private/var/root/Library/Preferences/com.apple.Bluetoothd.plist LinkKeys
   ```
6. The output looks like this :
   ```shell
   {
       "11-22-33-44-55-66" =    {
           "aa-bb-cc-dd-ee-ff" = <01122334 45566778 89900112 23344556>;
       };
   }
   ```
   Find your link key and copy it. If you're unsure which link key is which, you can find the MAC address of your device by option-clicking the Bluetooth applet in your menu bar and expanding the connected device you want to share.
   Here `11-22-33-44-55-66` would be your bluetooth chip MAC address, `aa-bb-cc-dd-ee-ff` would be your device MAC adress, and `01122334 45566778 89900112 23344556` the link key you should copy.
7. Then convert your key's endianness (little endian to big endian).
   It's pretty simple, using the key above :

   ```
   Little endian :
   01122334 45566778 89900112 23344556 == 01|12|23|34|45|56|67|78|89|90|01|12|23|34|45|56
                                          A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P

   Big endian :
   56453423 12019089 78675645 34231201 == 56|45|34|23|12|01|90|89|78|67|56|45|34|23|12|01
                                          P  O  N  M  L  K  J  I  H  G  F  E  D  C  B  A
   ```

   So your final key would be `56453423 12019089 78675645 34231201`

8. Save your converted key and your device MAC adress somewhere you can retrieve it in Windows.
9. Boot in Windows with the device **TURNED OFF**
10. Open `regedit` and browse to the bluetooth keys : `HKLM\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Keys`
    > If you do not see anything on the regedit panel when you select the `Keys` directory, right click on it, then select `Permissions`, and take the ownership by adding your user account in the list. Then reload regedit.
11. Replace the existing key matching the device's MAC address with the key that you converted in the earlier step
12. Power off your computer.
13. Power on your computer with the device turned on.

> Note: If you're using an Apple device such as a Keyboard or Trackpad, do not plug the device into your computer for charging. Doing so will cause the link keys to change requiring you to repeat this process again.
