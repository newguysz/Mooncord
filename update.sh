#!bin/bash
echo "Welcome to the Moon updater. Moon will now update."
rm -rf Moon
echo "Removed old version"
echo"Installing new version"
git clone https://github.com/7ua/Moon && cd Moon && mv moon.sh ~ && mv update.sh ~ && cd 
