<p align="center">
  <img src="/screenshot/git_hub_thumbnail.png" alt="Banner" width="600"/>
</p>

<p align="center">
  <!-- Version badge -->
  <a href="https://github.com/H3rz3n/davinci-helper/releases">
    <img src="https://img.shields.io/github/v/release/H3rz3n/davinci-helper?style=flat" alt="Latest Release">
  </a>
  <!-- License badge -->
  <a href="https://github.com/H3rz3n/davinci-helper/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/H3rz3n/davinci-helper?style=flat" alt="License">
  </a>
  <!-- Issues badge -->
  <a href="https://github.com/H3rz3n/davinci-helper/issues">
    <img src="https://img.shields.io/github/issues/H3rz3n/davinci-helper?style=flat" alt="Issues">
  </a>
  <!-- Pull Requests badge -->
  <a href="https://github.com/H3rz3n/davinci-helper/pulls">
    <img src="https://img.shields.io/github/issues-pr/H3rz3n/davinci-helper?style=flat" alt="Pull Requests">
  </a>
  <!-- Stars badge -->
  <a href="https://github.com/H3rz3n/davinci-helper/stargazers">
    <img src="https://img.shields.io/github/stars/H3rz3n/davinci-helper?style=flat" alt="Stars">
  </a>
  <!-- Forks badge -->
  <a href="https://github.com/H3rz3n/davinci-helper/network/members">
    <img src="https://img.shields.io/github/forks/H3rz3n/davinci-helper?style=flat" alt="Forks">
  </a>
  <!-- COPR badge -->
  <a href="https://copr.fedorainfracloud.org/coprs/herzen/davinci-helper/">
    <img src="https://img.shields.io/badge/COPR-enabled-brightgreen?style=flat&logo=fedora" alt="Fedora COPR enabled">
  </a>
</p>

# DaVinci Helper

## What is DaVinci Helper?

**DaVinci Helper** is a companion app that simplifies the installation and use of BlackMagic DaVinci Resolve (both Free and Studio versions) on Linux.  
The app is written in Python and features a modern GTK4 + Adwaita interface.

> **Currently, DaVinci Helper officially supports only Fedora Linux** (all spins and derivatives).  
> If the project receives good feedback, I plan to release a version for Debian-based systems like Ubuntu and Linux Mint.

<p align="center">
  <img src="/screenshot/01_alt.png" alt="Screenshot"/>
</p>

---

## Main Features

DaVinci Helper will help you with:
- Installing all the required dependencies to get DaVinci Resolve running smoothly
- Launching the official DaVinci Resolve installation wizard
- Applying essential post-install tweaks so that DaVinci Resolve works out of the box
- Installing the necessary GPU drivers to ensure your graphics card works correctly with DaVinci Resolve
- Converting videos for compatibility with DaVinci Resolve Free

---

## Supported DaVinci Resolve Versions

- **DaVinci Resolve 18.x.y**
- **DaVinci Resolve 19.x.y**
- **DaVinci Resolve 20.x.y**
- Both Free and Studio versions are supported.

---

## Supported Operating Systems

Tested and working on:
- Fedora Rawhide (experimental)
- Fedora 42 (all spins)
- Fedora 41 (all spins)
- Fedora 40 (all spins)
- Nobara 41
- Nobara 40
- Ultramarine Linux 40 (experimental)
- Ultramarine Linux 41 (experimental)
- Ultramarine Linux 42 (experimental)

---

## Supported GPUs

- **Nvidia:** Desktop/mobile GPUs from the 1000 series to 5000 series
- **AMD:** Dedicated GPUs from 5000 to 9000 series, plus iGPUs 780M, 880M, 890M
- **Intel:** Intel ARC GPUs and some integrated GPUs

---

## Supported Languages

- English
- Italian
- French (Coming soon)
- Spanish (Coming soon)
- German (Coming soon)
- Japanese (Coming soon)

---

## How to Install DaVinci Helper on Fedora-based Distros

The easiest way to install and keep DaVinci Helper updated is by enabling the project’s COPR repository and installing it via DNF.

### 1. Enable the COPR Repository

Open a terminal and run:
```
sudo dnf copr enable -y herzen/davinci-helper
```

### 2. Install DaVinci Helper

Then, install the app with:
```
sudo dnf install -y davinci-helper
```


---

## How to Use DaVinci Helper

A complete, step-by-step tutorial is available [here](https://github.com/H3rz3n/How-install-DaVinci-Resolve-in-Fedora-Linux).

---

## Want to Contribute?

You can help DaVinci Helper grow by:
- [Testing GPU drivers](https://github.com/H3rz3n/davinci-helper/discussions)
- Translating the app into your language
- [Making a donation](https://www.paypal.com/donate/?hosted_button_id=CPCG2RFAV82T8) to support ongoing maintenance and development

---

## Project Roadmap

All details about upcoming features and plans are available on the [Project Roadmap page](https://github.com/H3rz3n/davinci-helper/wiki/Project-roadmap).

---

<br><br><br><br><br><br>

**Tags:**  
davinci resolve; davinci; resolve; linux; davinci resolve linux; davinci resolve fedora; davinci fedora; how install davinci linux; how install davinci fedora; how fix davinci linux; how fix davinci fedora; davinci fedora error; davinci linux error; fedora error; fedora davinci error; davinci fedora does not start; davinci linux gpu error; davinci fedora gpu error; davinci fedora zlib; davinci fedora mesa-libGLU; davinci fedora libraries; davinci fedora does not start; davinci fedora don't start;
