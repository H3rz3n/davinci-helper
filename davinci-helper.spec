# NAME OF THE APP EXECUTABLE
Name:           davinci-helper

# APP VERSION
Version:        2.3.3

# RELEASE AND DISTRIBUTION VERSION
Release:        1

# SHORT SUMMARY OF WHAT THE APP DOES
Summary:        The best DaVinci Resolve companion app on Linux

# PUBBLICATION LICENSE
License:        GPL-3.0

# WEB ADDRESS OF THE APP GITHUB
URL:            https://github.com/H3rz3n/davinci-helper

# COMPILATION SOURCE https://github.com/H3rz3n/davinci-helper/blob/testing/
Source0:        %{name}-%{version}.tar.gz 

# COMPILATION ARCHITECTURE
BuildArch:      noarch

# DEPENDENCIES REQUIRED FOR COMPILATION
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: pyproject-rpm-macros

# DEPENDENCIES REQUIRED FOR EXECUTION
Requires: gtk4
Requires: libadwaita

# DISABLING THE AUTOMATIC DEPENDENCIES GENERATOR
%undefine __python_requires
%{?python_disable_dependency_generator}

# REMOVING SHEBANG OPTIONS
%undefine _py3_shebang_s
%undefine _py3_shebang_P

# APP FUNCTIONS DESCRIPTION
%description
DaVinci Helper is the ultimate app to help you install and run DaVinci Resolve on Fedora Linux.

# PREPARATION OPERATIONS FOR COMPILATION
%prep
%autosetup

# APP COMPILATION
%build
%pyproject_wheel

# APP INSTALLATION
%install
%pyproject_install

install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.desktop %{buildroot}%{_datadir}/applications/com.davinci.helper.app.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.svg  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.davinci.helper.app.svg
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.svg %{buildroot}%{_datadir}/app-info/icons/hicolor/scalable/apps/com.davinci.helper.app.svg
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.metainfo.xml %{buildroot}%{_metainfodir}/com.davinci.helper.app.metainfo.xml

install -Dm644 %{_builddir}/%{name}-%{version}/data/polkit/com.davinci.helper.app.policy %{buildroot}/%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy
install -Dm644 %{_builddir}/%{name}-%{version}/data/polkit/com.davinci.helper.app.rules %{buildroot}/%{_datadir}/polkit-1/rules.d/com.davinci.helper.app.rules

# LIST OF FILES INSTALLED BY THE APP AND THEIR LOCATIONS INSIDE THE SYSTEM
%files

# LIST OF FILES INCLUDED IN THE EQUIPMENT OF THE PACKAGE AND THEIR POSITION
%license LICENSE
%doc README.md

# LIST OF THE INSTALLED DIRECTORY AND THEIR POSITION
%{python3_sitelib}/davinci_helper*
%{_datadir}/davinci-helper/*

# LIST OF THE INSTALLED FILES AND THEIR POSITION
%{_bindir}/%{name}
%{_datadir}/applications/com.davinci.helper.app.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.davinci.helper.app.svg
%{_datadir}/app-info/icons/hicolor/scalable/apps/com.davinci.helper.app.svg
%{_metainfodir}/com.davinci.helper.app.metainfo.xml
%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy
%{_datadir}/polkit-1/rules.d/com.davinci.helper.app.rules

# POST INSTALLATION OPERATIONS
%post
update-desktop-database &> /dev/null || :

# CHANGELOG OF THE VERSION 
%changelog
* Fri Feb 07 2025 Lorenzo Maiuri <lorenzo.maiuri@ik.me> - 2.3.3-1
- Fixed support for native use of.run installer wizard file.

* Thu Feb 06 2025 Lorenzo Maiuri <lorenzo.maiuri@ik.me> - 2.3.2-1
- Added support for Nobara 41.
- Added experimental support for Fedora 42.
- Added experimental support for Fedora Rawhide.
- Added for using .run installer wizard file.
- Added support for Intel iGPUs.
- Added support for more AMD iGPUs.
- Fixed uppercase file extension not correctly detected.
- Fixed the conversion of files with spaces in their names.
- Fixed support for Nvidia mobile GPUs.
- Fixed italian translation.
- Fixed ffmpeg non-free installation.



