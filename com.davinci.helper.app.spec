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

%description
DaVinci Helper is an application to assist with various tasks related to DaVinci.

%prep
%setup


%install

# CREAZIONE DELLE CARTELLE IN /USR/LIB/NOME-PROGRAMMA
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}
mkdir -p %{buildroot}/usr/lib/%{name}/src
mkdir -p %{buildroot}/usr/lib/%{name}/data
mkdir -p %{buildroot}/usr/lib/%{name}/po


# COPIA I FILE DATI
cp -a data/* %{buildroot}/usr/lib/%{name}/data/

# COPIA I FILE ESEGUIBILI
cp -a src/* %{buildroot}/usr/lib/%{name}/src/

# COPIA I FILE DI TRADUZIONE
cp -a po/* %{buildroot}/usr/lib/%{name}/po/



# CREA LO SCRIPT DI AVVIO
cat > %{buildroot}%{_bindir}/%{name} <<-EOF
#!/bin/bash
%{python3} /usr/lib/%{name}/src/main.py
EOF



# Applica i permessi di esecuzione ai file
chmod 0755 %{buildroot}%{_bindir}/%{name}

install -Dm644 %{_builddir}/%{name}-%{version}/data/icons/davinci-helper.desktop %{buildroot}%{_datadir}/applications/davinci-helper.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/data/icons/davinci-helper-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/davinci-helper-icon.svg
install -D -m 0644 %{_builddir}/%{name}-%{version}/data/polkit/com.davinci.helper.app.policy %{buildroot}/%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy






%files

# Elenco delle directory incluse
%dir /usr/lib/%{name}/
%dir /usr/lib/%{name}/data/
%dir /usr/lib/%{name}/src/
%dir /usr/lib/%{name}/po/


#Elenco dei file inclusi
%{_bindir}/%{name}
/usr/lib/%{name}/data/*
/usr/lib/%{name}/src/*
/usr/lib/%{name}/po/*
%{_datadir}/applications/davinci-helper.desktop
%{_datadir}/icons/hicolor/scalable/apps/davinci-helper-icon.svg
%{_datadir}/polkit-1/actions/com.davinci.helper.app.policy


%license LICENSE
%doc README.md


%post
update-desktop-database &> /dev/null || :

%changelog
* Wed Jul 03 2024 Your Name <your.email@example.com> - 1.0-1
- Initial package creation
