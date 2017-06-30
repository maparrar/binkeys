WID=`xdotool search --title "Google Chrome" | head -1`
xdotool windowactivate $WID
xdotool key shift+ctrl+alt+Left
