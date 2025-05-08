#
# Copyright 2025 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, re

#-----------------------------------------------------------------------------------------------------

# FUNCTION THAT CHECK WHICH VERSION OF FEDORA IS INSTALLED
def check_fedora_version ():

    #-----------------------------------------------------------------------------------------------------
    
    # READING WHICH VERSION OF FEDORA IS INSTALLED
    os_info = subprocess.run("hostnamectl", shell=True, capture_output=True, text=True)

    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON WHETHER THERE ARE ERRORS OR NOT
    if os_info.returncode == 0: 

        # CHECKING WHIC VERSION OF FEDORA IS USED
        if os_info.stdout.find("Fedora Linux 40") != -1 :
        
            # SETTING THE FOUND OS VERSION
            os_version = "Fedora Linux 40"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))
        
        elif os_info.stdout.find("Fedora Linux 41") != -1 :
            
            # SETTING THE FOUND OS VERSION
            os_version = "Fedora Linux 41"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif os_info.stdout.find("Fedora Linux 42") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Fedora Linux 42"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif ((os_info.stdout).lower()).find("rawhide") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Fedora Linux Rawhide"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))
        
        elif os_info.stdout.find("Nobara Linux 40") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Nobara Linux 40"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif os_info.stdout.find("Nobara Linux 41") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Nobara Linux 41"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif os_info.stdout.find("Nobara Linux 42") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Nobara Linux 42"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif os_info.stdout.find("Ultramarine Linux 40") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Ultramarine Linux 40"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif os_info.stdout.find("Ultramarine Linux 41") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Ultramarine Linux 41"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))

        elif os_info.stdout.find("Ultramarine Linux 42") != -1 :

            # SETTING THE FOUND OS VERSION
            os_version = "Ultramarine Linux 42"

            # PRINT THE FEDORA VERSION
            print(_("You are using a supported OS version : {os_version_placeholder}").format(os_version_placeholder = os_version))


        

        # RETURNS VALUE TO THE SCRIPT
        return os_version
        
    else:
        print(_("DEBUG : There was an error reading what OS is installed :"))
        print("")
        print(os_info.stderr)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)

    #-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------

# FUNCTION THAT ADDS THE RPM FUSION REPOSITORY
def add_repository():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF RPM FUSION REPO IS ALREADY INSTALLED
    rpm_fusion_repo_check = subprocess.run("dnf repolist", shell=True, capture_output=True, text=True )

    # CHECKING IF RPM FUSION REPO IS ALREADY INSTALLED
    if rpm_fusion_repo_check.stdout.find("rpmfusion-free") != -1 and rpm_fusion_repo_check.stdout.find("rpmfusion-nonfree"):

        # PRINTING THE MESSAGE
        print(_("The RPM Fusion repository had already been added to the system, there was no need to add it."))
        print("")

    else :
    
        # ADDING THE RPM FUSION REPOSITORY
        adding_repo = subprocess.run("dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if adding_repo.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to add the RPM Fusion Free and Non-Free repository."))
            print(_("Check your network connection and try again or add it by yourself."))
            print("")
            print(adding_repo.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("")
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")
            exit(2)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The RPM Fusion Free and Non-Free repository have been successfully added."))
            print("")

    #-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
























