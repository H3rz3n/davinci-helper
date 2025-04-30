#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - UNUSED
# EXIT 2 - IT WAS IMPOSSIBLE TO ADD THE RPM FUSION REPOSITORY
# EXIT 3 - IT WAS IMPOSSIBLE TO INSTALL THE GPU DRIVER

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, re

#-----------------------------------------------------------------------------------------------------

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale") 

# DEFINING THE SUPPORTED GPU LIST FILE 
gpu_database_path = os.path.join("//usr/share/davinci-helper/data/gpu_support")

#-----------------------------------------------------------------------------------------------------

# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
locale.bindtextdomain('davinci-helper', locale_path)

# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE GETTEXT MODULE
gettext.bindtextdomain('davinci-helper', locale_path)

# TELLING GETTEXT WHICH FILE TO USE FOR THE TRANSLATION OF THE APP
gettext.textdomain('davinci-helper')

# TELLING GETTEXT THE TRANSLATE SIGNAL
_ = gettext.gettext

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





# FUNCTION THAT STARTS THE NVIDIA DRIVER INSTALLATION
def install_nvidia_driver():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    nvidia_driver_check = subprocess.run("dnf list --installed | grep akmod-nvidia ; dnf list --installed | grep xorg-x11-drv-nvidia-cuda", shell=True, capture_output=True, text=True ).stdout

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    if nvidia_driver_check.find("akmod-nvidia") != -1 and ((nvidia_driver_check.find("xorg-x11-drv-nvidia-cuda") != -1)) :

        # PRINTING THE MESSAGE
        print(_("The proprietary Nvidia GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLING THE NVIDIA PROPRIETARY DRIVER  
        nvidia_driver_install = subprocess.run("dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if nvidia_driver_install.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the proprietary Nvidia GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(nvidia_driver_install.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The proprietary Nvidia GPU driver has been successfully installed."))
            print("")

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT STARTS THE AMD GPU DRIVER INSTALLATION
def install_amd_driver():

    #-----------------------------------------------------------------------------------------------------
    
    # ACQUIRING IF IS ALREADY INSTALLED THE AMD DRIVER
    amd_driver_check = subprocess.run("dnf list --installed | grep rocm ; dnf list --installed | grep freeworld", shell=True, capture_output=True, text=True ).stdout

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF IS ALREADY INSTALLED THE AMD DRIVER         
    if (amd_driver_check.find("rocm-opencl") != -1) and (amd_driver_check.find("rocm-smi") != -1) and (amd_driver_check.find("rocm-core") != -1) and (amd_driver_check.find("rocm-hip") != -1) :

        # PRINTING THE MESSAGE
        print(_("The open source AMD GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLING THE AMD DRIVER  
        amd_driver_install = subprocess.run("dnf install -y rocm-opencl rocm-smi rocm-core rocm-hip", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if amd_driver_install.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the open source AMD GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(amd_driver_install.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

    #-----------------------------------------------------------------------------------------------------
        
    # CHECKING IF IS ALREADY INSTALLED THE MESA FREEWORLD DRIVER         
    if (amd_driver_check.find("mesa-va-drivers-freeworld") != -1) and (amd_driver_check.find("mesa-vdpau-drivers-freeworld") != -1):

        # PRINTING THE MESSAGE
        print(_("The MESA Freeworld drivers were already installed on the system, there was no need to install it."))
        print("")

    else :

        # SWAPPING THE MESA TO THE COMPLETE VERSION
        mesa_driver_swap = subprocess.run("dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld && dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld && dnf swap -y mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686 && dnf swap -y mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if mesa_driver_swap.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to swap the MESA GPU driver with the complete version."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(mesa_driver_swap.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The MESA GPU driver has been successfully swapped with the complete version."))
            print("")

    #-----------------------------------------------------------------------------------------------------
    




# FUNCTION THAT STARTS THE INTEL GPU DRIVER INSTALLATION
def install_intel_driver_40_41():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF IS ALREADY INSTALLED THE COMPLETE INTEL DRIVER
    intel_driver_check = subprocess.run("dnf list --installed | grep intel-compute-runtime ; dnf list --installed | grep intel-opencl ; dnf list --installed | grep freeworld", shell=True, capture_output=True, text=True ).stdout

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF IS ALREADY INSTALLED THE COMPLETE INTEL DRIVER
    if intel_driver_check.find("intel-compute-runtime") != -1 and ((intel_driver_check.find("intel-opencl") != -1)) :

        # PRINTING THE MESSAGE
        print(_("The complete Intel GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLING THE COMPLETE INTEL DRIVER  
        intel_driver_install = subprocess.run("dnf install -y intel-compute-runtime intel-opencl", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if intel_driver_install.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the complete Intel GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(intel_driver_install.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The complete Intel driver has been successfully installed."))
            print("")



    # CHECKING IF IS ALREADY INSTALLED THE MESA FREEWORLD DRIVER         
    if (intel_driver_check.find("mesa-va-drivers-freeworld") != -1) and (intel_driver_check.find("mesa-vdpau-drivers-freeworld") != -1):

        # PRINTING THE MESSAGE
        print(_("The MESA Freeworld drivers were already installed on the system, there was no need to install it."))
        print("")

    else :

        # SWAPPING THE MESA TO THE COMPLETE VERSION
        mesa_driver_swap = subprocess.run("dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld && dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if mesa_driver_swap.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to swap the MESA GPU driver with the complete version."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(mesa_driver_swap.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The MESA GPU driver has been successfully swapped with the complete version."))
            print("")

    #-----------------------------------------------------------------------------------------------------

# FUNCTION THAT STARTS THE INTEL GPU DRIVER INSTALLATION
def install_intel_driver_42():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF IS ALREADY INSTALLED THE COMPLETE INTEL DRIVER
    intel_driver_check = subprocess.run("dnf list --installed | grep intel-media-driver ; dnf list --installed | grep libva-intel-media-driver", shell=True, capture_output=True, text=True ).stdout

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF IS ALREADY INSTALLED THE COMPLETE INTEL DRIVER
    if intel_driver_check.find("libva-intel-media-driver") == -1 and ((intel_driver_check.find("intel-media-driver") != -1)) :

        # PRINTING THE MESSAGE
        print(_("The complete Intel GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLING THE COMPLETE INTEL DRIVER  
        intel_driver_install = subprocess.run("dnf swap -y libva-intel-media-driver intel-media-driver --allowerasing", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if intel_driver_install.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the complete Intel GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(intel_driver_install.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The complete Intel driver has been successfully installed."))
            print("")

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

# ACQUIRING THE OS VERSION IN USE
os_version = check_fedora_version()

#-----------------------------------------------------------------------------------------------------

# ACQUIRING THE GPU VENDOR
gpu_lspci = subprocess.run("lspci | grep -Ei 'vga|display'", shell=True, capture_output=True, text=True )

# MAKING LOWERCASE ALL THE STRING CHARACTER
gpu_lspci = gpu_lspci.stdout.lower()

#-----------------------------------------------------------------------------------------------------

# CHECKING IF THE VENDOR IS NVIDIA
if gpu_lspci.find("nvidia") != -1 :

    # STARTING THE DRIVER INSTALLATION
    install_nvidia_driver()

# CHECKING IF THE VENDOR IS AMD
if gpu_lspci.find("amd") != -1 :

    #CHECKING WHICH VERSION OF THE IS IN USE
    if os_version.find("40") or os_version.find("41"):

        # STARTING THE DRIVER INSTALLATION
        install_amd_driver_40_41()

    else :

        # STARTING THE DRIVER INSTALLATION
        install_amd_driver_42()

# CHECKING IF THE VENDOR IS INTEL
if gpu_lspci.find("intel") != -1 :

    #CHECKING WHICH VERSION OF THE IS IN USE
    if os_version.find("40") or os_version.find("41"):

        # STARTING THE DRIVER INSTALLATION
        install_intel_driver_40_41()

    else :

        # STARTING THE DRIVER INSTALLATION
        install_intel_driver_42()

#-----------------------------------------------------------------------------------------------------