#!/usr/bin/bash
clear
version="2.4.5"

mv davinci-helper davinci-helper-${version}
tar -cvzf davinci-helper-${version}.tar.gz davinci-helper-${version}
mv davinci-helper-${version} davinci-helper
