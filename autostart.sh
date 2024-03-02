#!/bin/sh
/home/lava/.screenlayout/portrait_monitor.sh
~/aqua_arch/osx_minimal_wallpaper.sh

picom &
disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh &
disown

# Start welcome
#eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
disown # start polkit agent from GNOME

nm-applet &
disown
xfce4-clipman &
disown
blueman-tray &
disown
flameshot &
disown
syncthing &
disown
smb4k &
disown
