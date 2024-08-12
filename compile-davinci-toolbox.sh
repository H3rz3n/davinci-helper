#!/usr/bin/bash
clear
version="1.0"

mkdir -p "/home/$USER/build_davinci_toolbox"
cp -r * "/home/$USER/build_davinci_toolbox"
cd "/home/$USER/build_davinci_toolbox"

mv davinci-toolbox davinci-toolbox-${version}

tar -cvzf davinci-toolbox-${version}.tar.gz davinci-toolbox-${version}

mv davinci-toolbox-${version}.tar.gz /home/lorenzo/rpmbuild/SOURCES/
rpmbuild -bb davinci-toolbox.spec 
sudo dnf remove -y davinci-toolbox
sudo dnf install -y /home/lorenzo/rpmbuild/RPMS/noarch/davinci-toolbox-${version}-1.fc40.noarch.rpm --disablerepo=*
cp /home/lorenzo/rpmbuild/RPMS/noarch/davinci-toolbox-${version}-1.fc40.noarch.rpm /home/lorenzo/Pubblici/Test_Davinci_Helper




