Name:           davinci-helper
Version:        1.0
Release:        1%{?dist}
Summary:        DaVinci Helper Application

License:        CC-BY-NC-SA
URL:            http://example.com/davinci-helper
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
Requires:       python3
Requires:       gtk4
Requires:       libadwaita

#
#
%description
DaVinci Helper is the ultime app to help you install and run Davinci Resolve on Fedora Linux.

#
#
%prep
%setup


%install










install -Dm644 %{_builddir}/%{name}-%{version}/data/icons/davinci-helper.desktop %{buildroot}%{_datadir}/applications/davinci-helper.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/data/icons/davinci-helper-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/davinci-helper-icon.svg
install -D -m 0644 %{_builddir}/%{name}-%{version}/data/polkit/davinci-helper.policy %{buildroot}/%{_datadir}/polkit-1/actions/davinci-helper.policy






%files

# Elenco delle directory incluse
#


# Elenco dei file inclusi
# 
%{_bindir}/%{name}
%{python3_sitelib}/davinci_helper*

#
#
%{_datadir}/applications/davinci-helper.desktop
%{_datadir}/icons/hicolor/scalable/apps/davinci-helper-icon.svg
%{_datadir}/polkit-1/actions/davinci-helper.policy

#
#
%license LICENSE
%doc README.md



#
#
%post
update-desktop-database &> /dev/null || :
sudo systemctl restart polkit



#
#
%changelog
* Wed Jul 03 2024 Your Name <your.email@example.com> - 1.0-1
- Initial package creation
