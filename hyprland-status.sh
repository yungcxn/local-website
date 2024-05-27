# open window via hyprland that watches status.sh output 
# create alacritty window floating and in corner of screen 100x100

hyprctl dispatch exec [floating] 'alacritty -e watch -t -n 3 /home/can/local-website/status.sh'