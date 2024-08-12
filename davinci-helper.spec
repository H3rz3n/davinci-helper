# NOME DELL'ESEGUIBILE DEL PROGRAMMA
# NAME OF THE APP EXECUTABLE
Name:           davinci-helper



# VERSIONE DEL PROGRAMMA
# APP VERSION
Version:        1.0



# VERSIONE E DISTRIBUZIONE DI RILASCIO
# RELEASE AND DISTRIBUTION VERSION
Release:        1%{?dist}



# BREVE RIASSUNTO DI COSA FA IL PROGRAMMA
# SHORT SUMMARY OF WHAT THE APP DOES
Summary:        The best DaVinci Resolve companion app on Linux



# LICENZA DI PUBBLICAZIONE
# PUBBLICATION LICENSE
License:        CC-BY-NC-SA



# INDIRIZZO WEB DEL GITHUB DEL PROGRAMMA
# WEB ADDRESS OF THE APP GITHUB
URL:            https://github.com/H3rz3n/davinci-helper



# SORGENTE DI COMPILAZIONE
# COMPILATION SOURCE
Source0:        %{name}-%{version}.tar.gz



# ARCHITETTURA DI COMPILAZIONE
# COMPILATION ARCHITECTURE
BuildArch:      noarch



# DIPENDENZE NECESSARIE PER LA COMPILAZIONE
# DEPENDENCIES REQUIRED FOR COMPILATION
BuildRequires:  python3
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel



# DIPENDENZE NECESSARIE PER L'ESECUZIONE
# DEPENDENCIES REQUIRED FOR EXCUTION
Requires:       python3
Requires:       gtk4
Requires:       libadwaita



# DESCRIZIONE DELLE FUNZIONI DEL PROGRAMMA
# APP FUNCTIONS DESCRIPTION
%description
DaVinci Helper is the ultime app to help you install and run DaVinci Resolve on Fedora Linux.



# OPERAZIONI DI PREPARAZIONE ALLA COMPILAZIONE
# PREPARATION OPERATIONS FOR COMPILATION
%prep
%setup



# COMPILAZIONE DEL PROGRAMMA
# APP COMPILATION
%build
%py3_build



# INSTALLAZIONE DEL PROGRAMMA
# APP INSTALLATION
%install
%py3_install

install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.desktop %{buildroot}%{_datadir}/applications/com.davinci.helper.app.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/davinci-helper-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/davinci-helper-icon.svg
install -Dm644 %{_builddir}/%{name}-%{version}/data/desktop/com.davinci.helper.app.metainfo.xml %{buildroot}%{_datadir}/metainfo/com.davinci.helper.app.metainfo.xml

install -Dm644 %{_builddir}/%{name}-%{version}/data/polkit/com.davinci.helper.app.policy %{buildroot}/%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy
install -Dm644 %{_builddir}/%{name}-%{version}/data/polkit/com.davinci.helper.app.rules %{buildroot}/%{_datadir}/polkit-1/rules.d/com.davinci.helper.app.rules


# ELENCO DEI FILE INSTALLATI DAL PROGRAMMA E DELLE LORO POSIZIONI NEL SISTEMA
# LIST OF FILES INSTALLED BY THE APP AND THEIR LOCATIONS INSIDE THE SYSTEM
%files

# ELENCO DEI FILE DI CORREDO DEL PACCHETTO E DELLE LORO POSIZIONI
# LIST OF FILES INCLUDED IN THE EQUIPMENT OF THE PACKAGE AND THEIR POSITION
%license LICENSE
%doc README.md

# ELENCO DELLE DIRECTORY INSTALLATE E DELLE LORO POSIZIONI
# LIST OF THE INSTALLED DIRECTORY AND THEIR POSITION
%{python3_sitelib}/davinci_helper*
%{_datadir}/davinci-helper/*

# ELENCO DEI FILE INSTALLATI E DELLE LORO POSIZIONI
# LIST OF THE INSTALLED FILES AND THEIR POSITION
%{_bindir}/%{name}
%{_datadir}/applications/com.davinci.helper.app.desktop
%{_datadir}/icons/hicolor/scalable/apps/davinci-helper-icon.svg
%{_datadir}/metainfo/com.davinci.helper.app.metainfo.xml
%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy
%{_datadir}/polkit-1/rules.d/com.davinci.helper.app.rules



# OPERAZIONI ESEGUITE POST INSTALLAZIONE
# POST INSTALLATION OPERATIONS
%post
update-desktop-database &> /dev/null || :
sudo systemctl restart polkit



# ELENCO DEI CAMBIAMENTI DELLA VERSIONE
# CHANGELOG OF THE VERSION
%changelog
* Wed Jul 03 2024 Lorenzo Maiuri <lorenzo.maiuri@gmail.com> - 1.0-1
- Initial package creation
