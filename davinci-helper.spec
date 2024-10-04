# NAME OF THE APP EXECUTABLE
Name:           davinci-helper

# APP VERSION
Version:        2.0.0

# RELEASE AND DISTRIBUTION VERSION
Release:        1

# SHORT SUMMARY OF WHAT THE APP DOES
Summary:        The best DaVinci Resolve companion app on Linux

# PUBBLICATION LICENSE
License:        GPL-3.0

# WEB ADDRESS OF THE APP GITHUB
URL:            https://github.com/H3rz3n/davinci-helper

# COMPILATION SOURCE
Source0:        https://github.com/H3rz3n/davinci-helper/blob/testing/%{name}-%{version}.tar.gz

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
Requires: python3-pip

# DISABLING THE AUTOMATIC DEPENDENCIES GENERATOR
%undefine __python_requires
%{?python_disable_dependency_generator}

#
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
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/davinci_helper_icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/davinci_helper_icon.svg
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.metainfo.xml %{buildroot}%{_datadir}/metainfo/com.davinci.helper.app.metainfo.xml

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
%{_datadir}/icons/hicolor/scalable/apps/davinci_helper_icon.svg
%{_datadir}/metainfo/com.davinci.helper.app.metainfo.xml
%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy
%{_datadir}/polkit-1/rules.d/com.davinci.helper.app.rules

# POST INSTALLATION OPERATIONS
%post
update-desktop-database &> /dev/null || :
sudo systemctl restart polkit
pip install moviepy

# CHANGELOG OF THE VERSION
%changelog
* Fri Oct 04 2024 Lorenzo Maiuri <lorenzo.maiuri@gmail.com> - 2.0.0-1
- Full Adwaita UI.
- Added support for DaVinci 19.
- Added support for Fedora 41.
- Added support for video conversion.
- Minor bug fixes and improved performance.

* Sat Aug 17 2024 Lorenzo Maiuri <lorenzo.maiuri@gmail.com> - 1.1.0-1
- Added AMD GPU support.

* Sat Aug 17 2024 Lorenzo Maiuri <lorenzo.maiuri@gmail.com> - 1.0.1-1
- Switched license to GPL-3.0

* Tue Aug 13 2024 Lorenzo Maiuri <lorenzo.maiuri@gmail.com> - 1.0.0-1
- Initial release
