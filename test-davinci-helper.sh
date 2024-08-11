#!/usr/bin/bash
clear
tar -cvzf davinci-helper-1.0.tar.gz davinci-helper-1.0
mv davinci-helper-1.0.tar.gz /home/lorenzo/rpmbuild/SOURCES/
rpmbuild -bb davinci-helper.spec 
sudo dnf remove -y davinci-helper
sudo dnf install -y '/home/lorenzo/rpmbuild/RPMS/noarch/davinci-helper-1.0-1.fc40.noarch.rpm' --disablerepo=*
cp /home/lorenzo/rpmbuild/RPMS/noarch/davinci-helper-1.0-1.fc40.noarch.rpm /home/lorenzo/Pubblici/Test_Davinci_Helper




