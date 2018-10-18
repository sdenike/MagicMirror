#  MagicMirror 2 install with Raspbian Stretch Lite - INCOMPLETE

## Update/Upgrade Raspbian Stretch

`sudo apt-get update`

`sudo apt-get upgrade`

## Install Xserver, LXDE-gui and lightdm:

`sudo apt-get install xinit xserver-xorg`

`sudo apt-get install lxde-core`

`sudo apt-get install lightdm`

## Let the LXDE-gui autostart:

`sudo raspi-config`

Go to "Boot Options" and change boot to "Desktop Autologin"

## Install the additional packages:

`sudo apt-get install git libxss1 libnss3 unclutter`

## Install MagicMirror with the Automatic Installer:

`curl -sL https://raw.githubusercontent.com/MichMich/MagicMirror/master/installers/raspberry.sh | bash`

## Go to MagicMirror folder:

`cd ~/MagicMirror`

## Install the app:

`npm install`

## Copy sample config.

`cp config/config.js.sample config/config.js`

## Go back to home folder:

`cd ..`

## Rotating the screen and hide Rainbow colored cube:

`sudo nano /boot/config.txt`

Add the following line:

`display_rotate=3`

`disable_splash=1`

## Auto Starting MagicMirror:

Install PM2 using NPM:

`sudo npm install -g pm2`

Starting PM2 on Boot:

`pm2 startup`

PM2 will now show you a command you need to execute.

The code is:

`sudo su -c "env PATH=$PATH:/usr/bin pm2 startup linux -u pi --hp /home/pi"`

### Make a MagicMirror start script:

go back to root:

`cd ~`

Create the start script:

`sudo nano mm.sh`

Add the following lines:

`cd ~/MagicMirror`

`DISPLAY=:0 npm start`

Save and close, using the commands CTRL-O and CTRL-X.

Make the shell script executable:

`chmod +x mm.sh`

You are now ready to the MagicMirror using this script using PM2.

### Starting your MagicMirror with PM2

`pm2 start mm.sh`

Alternatively, if you wish to automatically restart MagicMirror when you make config changes, you may want to use:

`pm2 start mm.sh --watch ~/MagicMirror/config/config.js`

### Enable restarting of the MagicMirror script:

`pm2 save`

## Disable the screensaver:

Go to LXDE-autostart config:

`sudo nano /etc/xdg/lxsession/LXDE/autostart` 

add the following lines:

`@xset s noblank`
`@xset s off`
`@xset -dpms`

Save and close, using the commands CTRL-O and CTRL-X.

Go to lightdm.conf:

`sudo nano /etc/lightdm/lightdm.conf`

add the following line below `[Seat:*]`:

`xserver-command=X -s 0 -dpms`

## Reboot the raspberry pi:

`sudo reboot`

EDIT : If the screensaver doesn't disable, try with the file 

`/home/pi/.config/lxsession/LXDE/autostart` instead of `/etc/xdg/lxsession/LXDE/autostart` and reboot after modifications

If PM2 does not start MM on reboot. If you are using PM 2.4.2, you may need to edit the TimeoutStartSec value in /etc/systemd/system/pm2-root.service if using slower based SBC's like the Pi. The default is 8s which is not long enough. Try 15s.