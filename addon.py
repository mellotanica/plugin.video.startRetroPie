import xbmcgui
import subprocess

answer = xbmcgui.Dialog().yesno("Start RetroPie?", "Restart the system and boot into RetroPie menu?");
if answer:
    subprocess.call("/home/osmc/nextBootRetroPie")
    xbmc.executebuiltin('Reboot()')


