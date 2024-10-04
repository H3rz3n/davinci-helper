#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO ADD THE RPM FUSION REPOSITORY
# EXIT 2 - IT WAS IMPOSSIBLE TO INSTALL FFMPEG

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale

#-----------------------------------------------------------------------------------------------------

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

# DEFINING SETTINGS FILES PATH
home_dir = os.path.expanduser("~")
settings_path = os.path.join(f"{home_dir}/.config")

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



# FUNCTION THAT WILL CHECK IF FFMPEG IS ALREADY INSTALLED ON THE SYSTEM
def check_ffmpeg_presence ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF FFMPEG IS ALREADY INSTALLED
    check_ffmpeg = subprocess.run("dnf list installed | grep ffmpeg", shell=True, capture_output=True, text=True )

    # CHECKING IF FFMPEG IS ALREADY INSTALLED
    if check_ffmpeg.stdout.find("ffmpeg-free") != -1 :

        # RETURNING THE PRESENCE VALUE
        return "Full"

    elif check_ffmpeg.stdout.find("ffmpeg") != -1 : 

        # RETURNING THE PRESENCE VALUE
        return "Lite"

    else :

        # RETURNING THE PRESENCE VALUE
        return "None"

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT ADDS THE RPM FUSION REPOSITORY
def add_repository ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF RPM FUSION REPO IS ALREADY INSTALLED
    rpm_fusion_repo_check = subprocess.run("dnf repolist", shell=True, capture_output=True, text=True )

    # CHECKING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    if rpm_fusion_repo_check.stdout.find("rpmfusion") != -1:

        # PRINTING THE MESSAGE
        print(_("The RPM Fusion repository had already been added to the system, there was no need to add it."))
        print("")

    else :
    
        # ADDING THE RPM FUSION REPOSITORY
        adding_repo = subprocess.run("dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm", shell=True, capture_output=True, text=True )

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
            exit(1)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The RPM Fusion Free and Non-Free repository have been successfully added."))
            print("")

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL INSTALL FFMPEG FROM RPM FUSION REPOSITORY
def install_ffmpeg ():

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING FFMPEG FROM RPM FUSION
    ffmpeg_install = subprocess.run("dnf install -y ffmpeg-free", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE WERE ERRORS
    if ffmpeg_install.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to install FFMPEG from RPM Fusion."))
        print("")
        print(ffmpeg_install.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(2)

    else :

        # PRINTING THE SUCCESSFUL STATE
        print(_("FFMPEG was successfully installed from RPM Fusion. Now you can use DaVinci Converter "))
        print("")




    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL SWAP FFMPEG VERSION USING THE ONE FROM RPM FUSION REPOSITORY
def swap_ffmpeg ():

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING FFMPEG FROM RPM FUSION
    ffmpeg_swap = subprocess.run("dnf swap -y ffmpeg ffmpeg-free --allowerasing", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE WERE ERRORS
    if ffmpeg_swap.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to swap the lite version FFMPEG with the one from RPM Fusion."))
        print("")
        print(ffmpeg_swap.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(3)

    else :

        # PRINTING THE SUCCESSFUL STATE
        print(_("FFMPEG lite was successfully swapped with FFMPEG full from RPM Fusion. Now you can use DaVinci Converter "))
        print("")

    #-----------------------------------------------------------------------------------------------------











#-----------------------------------------------------------------------------------------------------

# ACQUIRING IF FFMPEG FROM RPM FUSION IS INSTALLED
is_installed = check_ffmpeg_presence()

#-----------------------------------------------------------------------------------------------------

# CHECKING IF FFMPEG FROM RPM FUSION IS INSTALLED
if is_installed == "Lite" :

    #-----------------------------------------------------------------------------------------------------
    print("Started Lite")

    # ADDING RPM FUSION REPOSITORY
    add_repository()

    # INSTALLING FFMPEG
    swap_ffmpeg()

    #-----------------------------------------------------------------------------------------------------

elif is_installed == "None" :

    #-----------------------------------------------------------------------------------------------------

    print("Started None")

    # ADDING RPM FUSION REPOSITORY
    add_repository()

    # INSTALLING FFMPEG
    install_ffmpeg()

    #-----------------------------------------------------------------------------------------------------

else :

    #-----------------------------------------------------------------------------------------------------

    print("Full")

    # PRINTING THE MESSAGE
    print(_("FFMPEG was already installed on the system\nthere was no need to install it."))
    print("")

    exit(0)

    #-----------------------------------------------------------------------------------------------------