#!bin/bash
echo "Welcome to the Mooncord updater. Mooncord will now update."
sleep 2
rm -rf Mooncord
echo "Removed old version"
sleep 1
echo "Installing new version"
#de-crease sleep time
sleep 1
git clone https://github.com/7ua/Mooncord && cd Mooncord && mv mooncord.sh ~ && mv update.sh ~ && cd
clear
echo "Moon was updated & re-installed."
