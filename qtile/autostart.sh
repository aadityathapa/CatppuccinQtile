#!/bin/sh
nitrogen --restore &
picom &
mate-session &
udiskie &
nm-applet &
volumeicon &
dunst &
flameshot &

xinput set-prop "Synaptics TM3096-001" "libinput Tapping Enabled" 1 &
xinput set-prop "Synaptics TM3096-001" "libinput Natural Scrolling Enabled" 1 &
xsetroot -cursor_name left_ptr &

setxkbmap gb &
