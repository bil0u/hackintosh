## Windows Installation

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

---