#!/usr/bin/bash
clear
version="2.4.0"

if [ -d "/home/$USER/build_davinci_helper" ]; then
    rm -rf "/home/$USER/build_davinci_helper"
fi

mkdir -p "/home/$USER/build_davinci_helper"
cp -r * "/home/$USER/build_davinci_helper"
cd "/home/$USER/build_davinci_helper"

mv davinci-helper davinci-helper-${version}

tar -cvzf davinci-helper-${version}.tar.gz davinci-helper-${version}

mv davinci-helper-${version}.tar.gz "/home/$USER/rpmbuild/SOURCES/"
rpmbuild -bb davinci-helper.spec 


sudo dnf remove -y davinci-helper
sudo dnf install -y /home/$USER/rpmbuild/RPMS/noarch/davinci-helper-${version}-1.noarch.rpm --disablerepo=*


#cp /home/$USER/rpmbuild/RPMS/noarch/davinci-helper-${version}-1.noarch.rpm /home/$USER/Pubblici/Test_Davinci_Helper
#cd .. 
#rm -rf "/home/$USER/build_davinci_helper"
#rm "/home/$USER/rpmbuild/SOURCES/davinci-helper-${version}.tar.gz"


