## BIOS Settings

Bios revision `F11c`. Optimized defaults + following settings :

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


### Patched :

Variable | Code | Value | Tool
--- | --- | --- | ---
**CFG Lock** | `0x5C1` | `0x0` | CFGLock.efi or ModGrubShell.efi
