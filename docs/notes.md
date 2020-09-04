### Notes

Here you will find some personal notes about some problems i encountered and the steps i followed to solve them.


#### Windows Installation

I choosed to install OpenCore, macOS and Windows on the same drive.

I first installed macOS and OpenCore, then Windows.


1. Create the Windows 10 USB installer with one of these two methods :
	- Microsoft's `Windows 10 Media Creation Tool`, works only from a PC (I picked this method)
	- From command line with [this method](https://www.freecodecamp.org/news/how-make-a-windows-10-usb-using-your-mac-build-a-bootable-iso-from-your-macs-terminal/) if you're using a Mac.


2. Create a new exFat partition on the boot drive. Choose a decent size as you do not want to create a mess trying to enlarge it in the future.

3. Power off your computer and disconnect physically all secondary drives, only the boot drive should remain.
> You can disconnect them virtually by disabling drives from your BIOS if you have the option.

4. Boot through OpenCore, then on the Windows USB installer.

5. On the disk selection menu, select the exFat partition you created before and delete it. Then, select the ` unused space` and continue the install. **DO NOT** create a partition but only select the unused space you created by removing the partition.

6. The install should work properly now ! If not, Google is your friend :) What worked for me could not work for you.


#### Secondary drive(s) does not appear in Windows Explorer

Some of your drives does not appear in Windows Explorer but are visible normally on macOS ?

1. Open Explorer

2. Right click on `This PC`, then `Manage`

3. On the left column, click `Disk management`

4. Select the problematic drive, right click, then `Change drive letter and paths`
> If your drive does not appear in Disk Management, then these steps will not help you at install

5. Click add, then select a letter and you're good to go !

###### Hey, the problem is still here after reboot !

Don't panic, just try this :

1. Open Run or cmd

2. Type `diskpart` then hit enter

3. In diskpart shell :
	- type `list volume`
	- then `select volume X` (where `X` is the number corresponding with your problematic drive)
	- then `attributes volume clear hidden`
	- then 	`exit`


4. Reboot your computer and voilà, you should be OK now !


#### macOS audio issues

Audio crackles, stop and/or desynchronizes on macOS, even with `AppleALC.kext` and `layout-id=16`.

This fix worked for me :

- Open `Audio MIDI Setup.app` located under `/Applications/Utilities`
- Select your sound output on the left panel
- Under `Format (Bitrate)`, try all values starting from the biggest value (the lower one in the list)

My preset : `2-channel 32-bit 96.0kHz floating point number`
