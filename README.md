<p align="center">
  <img src="/screenshot/git_hub_thumbnail.png" alt="Banner" width="600"/>
</p>

## What is DaVinci Helper :
DaVinci Helper is a companion app that will simplify the installation and the use of BlackMagic DaVinci Resolve (both Free and Studio version) on Linux. This app is written using Python and has a GUI based on GTK4 and Adwaita. 

Currently **this program supports only Fedora Linux** in all his spins and derivatives. If the project will receive good feedback by the community I will make a version for Debian-based systems like Linux Mint and Ubuntu.

<p align="center">
  <img src="/screenshot/01.png" alt="Banner"/>
</p>

## What this app does :
DaVinci Helper will help you with :
- The installation of all the necessary dependencies to correctly install and start DaVinci Resolve
- Starting the official installation wizard
- Applying all the necessary post install tricks to properly start DaVinci Resolve
- Installing the necessary GPU drivers to make to correctly use your graphic card with DaVinci Resolve
- Converting the video to make them work with DaVinci Resolve Free

## What version of DaVinci are currently supported
Currently the app support DaVinci Resolve 18.x.y and 19.x.x, both in the Free and Studio version.

## What OSs are currently supported by the latest version
Currently the app was tested on these OSs :
- Fedora 41 - All spins
- Fedora 40 - All spins
- Nobara 40

## What OSs are supported by an older version of the app
Currently the app was tested on these OSs :
- Fedora 39 - All spins - [Use V1.1.0](https://github.com/H3rz3n/davinci-helper/releases/tag/v1.1.0) - Support only DaVinci Resolve 18.x.x
- Fedora 38 - All spins - [Use V1.1.0](https://github.com/H3rz3n/davinci-helper/releases/tag/v1.1.0) - Support only DaVinci Resolve 18.x.x
- Nobara 39 - All spins - [Use V1.1.0](https://github.com/H3rz3n/davinci-helper/releases/tag/v1.1.0) - Support only DaVinci Resolve 18.x.x
- Nobara 39 - All spins - [Use V1.1.0](https://github.com/H3rz3n/davinci-helper/releases/tag/v1.1.0) - Support only DaVinci Resolve 18.x.x

## What GPUs are currently supported
Currently are supported the following GPUs :
- **Nvidia :** from `1xxx` series to `4xxx` series
- **AMD :** from `5xxx` series to `7xxx`

## Supported localization :
- English
- Italian
- French (Coming soon)
- Spanish (Coming soon)
- German (Coming soon)
- Japanese (Coming soon)

 ## How install DaVinci Helper in Fedora 40 and 41
 The most simple way to install and keep updated DaVinci Helper is to add the project COPR repository to your repository list and simply install it with the DNF packet manager.

### Adding the project COPR repository
Open a terminal window and paste this instruction : 
```
sudo dnf copr enable -y herzen/davinci-helper
```

### Installing the app
Open a terminal window and paste this instruction :  
```
sudo dnf install -y davinci-helper
```

## How install DaVinci Helper in Fedora 38 and 39
Download the legacy version of the app, then open a terminal window paste the following command :
```
sudo dnf install -y
```
Then drag and drop the app package `.rpm` file or write the path to the app package.

## I want to contribute to the project, what can I do ?
If you want to contribute to this project you can help us [testing the GPU drivers](https://github.com/H3rz3n/davinci-helper/discussions), translating the app or [making a donation](https://www.paypal.com/donate/?hosted_button_id=CPCG2RFAV82T8) to support the work needed for the maintenance and the continue update to keep up with the latest DaVinci and Fedora versions.




























<br><br><br><br><br><br>Tags : davinci linux fix ; davinci fedora fix ; davinci fedora does not start ; davinci linux gpu error ; davinci linux error ; davinci fedora gpu error ; davinci fedora zlib ; davinci fedora mesa-libGLU ; davinci fedora libraries ; davinci fedora does not start ; davinci fedora don't start ;



