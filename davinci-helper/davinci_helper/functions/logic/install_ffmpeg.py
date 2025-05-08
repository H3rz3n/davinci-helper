#
# Copyright 2025 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO ADD THE RPM FUSION REPOSITORY
# EXIT 2 - IT WAS IMPOSSIBLE TO INSTALL FFMPEG
# EXIT 3 - IT WAS IMPOSSIBLE TO SWAP FFMPEG
# EXIT 4 - IT WAS IMPOSSIBLE TO INSTALL THE CODECS
# EXIT 5 - IT WAS IMPOSSIBLE TO UPDATE THE MULTIMEDIA GROUP

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale

# NOT STANDARD MODULES IMPORT
import davinci_helper.functions.logic.utility as utility

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
    check_ffmpeg = subprocess.run("dnf list --installed | grep ffmpeg", shell=True, capture_output=True, text=True )

    # CHECKING IF FFMPEG IS ALREADY INSTALLED
    if check_ffmpeg.stdout.find("ffmpeg-free") != -1 :

        # RETURNING THE PRESENCE VALUE
        return "Lite"

    elif check_ffmpeg.stdout.find("ffmpeg") != -1 : 

        # RETURNING THE PRESENCE VALUE
        return "Full"

    else :

        # RETURNING THE PRESENCE VALUE
        return "None"

    #-----------------------------------------------------------------------------------------------------



# FUNCTION THAT WILL INSTALL FFMPEG FROM RPM FUSION REPOSITORY
def install_ffmpeg ():

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING FFMPEG FROM RPM FUSION
    ffmpeg_install = subprocess.run("dnf install -y ffmpeg", shell=True, capture_output=True, text=True)

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
    ffmpeg_swap = subprocess.run("dnf swap -y ffmpeg-free ffmpeg --allowerasing", shell=True, capture_output=True, text=True)

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



# FUNCTION THAT WILL CHECK ALL THE CODECS ARE ALREADY INSTALLED ON THE SYSTEM
def check_multimedia_codecs_presence (os_version):

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF FFMPEG IS ALREADY INSTALLED
    check_codecs = subprocess.run("dnf list --installed", shell=True, capture_output=True, text=True )

    # CHECKING IF ALL THE LIBRARIES NEEDED ARE INSTALLED
    lib_to_install = ""
    
    # SEARCHING
    if check_codecs.stdout.find('PackageKit-gstreamer-plugin') == -1 :
        lib_to_install = lib_to_install + " PackageKit-gstreamer-plugin"
    
    # SEARCHING
    if check_codecs.stdout.find('alsa-ucm') == -1 :
        lib_to_install = lib_to_install + " alsa-ucm"
    
    # SEARCHING
    if check_codecs.stdout.find('alsa-utils') == -1 :
        lib_to_install = lib_to_install + " alsa-utils"
    
    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugin-libav') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugin-libav"
    
    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugin-openh264') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugin-openh264"

    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugins-bad-free') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugins-bad-free"
    
    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugins-bad-freeworld') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugins-bad-freeworld"

    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugins-good') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugins-good"
    
    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugins-ugly') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugins-ugly"

    # SEARCHING
    if check_codecs.stdout.find('gstreamer1-plugins-ugly-free') == -1 :
        lib_to_install = lib_to_install + " gstreamer1-plugins-ugly-free"

    # SEARCHING
    if check_codecs.stdout.find('pipewire-alsa') == -1 :
        lib_to_install = lib_to_install + " pipewire-alsa"
    
    # SEARCHING
    if check_codecs.stdout.find('pipewire-gstreamer') == -1 :
        lib_to_install = lib_to_install + " pipewire-gstreamer"

    # SEARCHING
    if check_codecs.stdout.find('pipewire-pulseaudio') == -1 :
        lib_to_install = lib_to_install + " pipewire-pulseaudio"
    
    # SEARCHING
    if check_codecs.stdout.find('pipewire-utils') == -1 :
        lib_to_install = lib_to_install + " pipewire-utils"

    # SEARCHING
    if check_codecs.stdout.find('wireplumber') == -1 :
        lib_to_install = lib_to_install + " wireplumber"

    # SEARCHING
    if check_codecs.stdout.find('gstreamer-plugins-espeak') == -1 :
        lib_to_install = lib_to_install + " gstreamer-plugins-espeak"
    
    # SEARCHING
    if check_codecs.stdout.find('libavcodec-freeworld') == -1 :
        lib_to_install = lib_to_install + " libavcodec-freeworld"

    # SEARCHING
    if check_codecs.stdout.find('libheif-freeworld') == -1 :
        lib_to_install = lib_to_install + " libheif-freeworld"

    # SEARCHING
    if check_codecs.stdout.find('pipewire-codec-aptx') == -1 :
        lib_to_install = lib_to_install + " pipewire-codec-aptx"

    # SEARCHING
    if check_codecs.stdout.find('vlc-plugins-freeworld') == -1 :
        lib_to_install = lib_to_install + " vlc-plugins-freeworld"

    #-----------------------------------------------------------------------------------------------------

    # CHEKING IF THERE ARE MISSING LIBRARIES
    if lib_to_install != "" :

        # REMOVE EXCESS SPACE FROM THE LIST OF THE LIBRARIES TO INSTALL
        lib_to_install = lib_to_install.lstrip(' ')

        # PRINTING THE LIST OF THE LIBRARIES TO INSTALL
        print(_(f"The following libraries will be installed because they are missing :"))
        print(lib_to_install )
        print("")

        # RETURNING THE PRESENCE VALUE
        return "None", lib_to_install
    
    else:

        # PRINTING THE MISSING OF LIBRARIES TO INSTALL
        print(_("There are no missing codecs and libraries to install, you can now use DaVinci Converter"))
        print("")

        # RETURNING THE PRESENCE VALUE
        return "Full", lib_to_install

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL INSTALL ALL THE CODECS FROM RPM FUSION REPOSITORY
def install_codecs (lib_install_list):

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING FFMPEG FROM RPM FUSION
    codecs_install = subprocess.run(f"dnf install -y {lib_install_list}", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE WERE ERRORS
    if codecs_install.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to install the codecs and other libraries from RPM Fusion."))
        print("")
        print(codecs_install.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(4)

    else :

        # PRINTING THE SUCCESSFUL STATE
        print(_("All the codecs and missing libraries were successfully installed from RPM Fusion. Now you can use DaVinci Converter"))
        print("")

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL INSTALL ALL THE CODECS FROM RPM FUSION REPOSITORY
def update_multimedia_40_41 ():

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING FFMPEG FROM RPM FUSION
    multimedia_update = subprocess.run("dnf4 update -y @multimedia --setopt='install_weak_deps=False' --exclude=PackageKit-gstreamer-plugin", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE WERE ERRORS
    if multimedia_update.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to update the multimedia group."))
        print("")
        print(multimedia_update.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(5)

    else :

        # PRINTING THE SUCCESSFUL STATE
        print(_("All the codecs and missing libraries were successfully installed from RPM Fusion. Now you can use DaVinci Converter"))
        print("")

    #-----------------------------------------------------------------------------------------------------

# FUNCTION THAT WILL INSTALL ALL THE CODECS FROM RPM FUSION REPOSITORY
def update_multimedia_42 ():

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING FFMPEG FROM RPM FUSION
    multimedia_update = subprocess.run("dnf upgrade @multimedia --setopt='install_weak_deps=False' --exclude=PackageKit-gstreamer-plugin && dnf group install -y sound-and-video", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE WERE ERRORS
    if multimedia_update.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to update the multimedia group."))
        print("")
        print(multimedia_update.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(5)

    else :

        # PRINTING THE SUCCESSFUL STATE
        print(_("All the codecs and missing libraries were successfully installed from RPM Fusion. Now you can use DaVinci Converter"))
        print("")

    #-----------------------------------------------------------------------------------------------------


















#-----------------------------------------------------------------------------------------------------

# ACQUIRING IF FFMPEG FROM RPM FUSION IS INSTALLED
is_installed_ffmpeg = check_ffmpeg_presence()

#-----------------------------------------------------------------------------------------------------

# ACQUIRING WHICH VERSION OF FEDORA IS IN USE
os_version = utility.check_fedora_version()

#-----------------------------------------------------------------------------------------------------

# CHECKING IF FFMPEG FROM RPM FUSION IS INSTALLED
if is_installed_ffmpeg == "Lite" :

    #-----------------------------------------------------------------------------------------------------

    # ADDING RPM FUSION REPOSITORY
    utility.add_repository()

    # INSTALLING FFMPEG
    swap_ffmpeg()

    #-----------------------------------------------------------------------------------------------------

elif is_installed_ffmpeg == "None" :

    #-----------------------------------------------------------------------------------------------------

    # ADDING RPM FUSION REPOSITORY
    utility.add_repository()

    # INSTALLING FFMPEG
    install_ffmpeg()

    #-----------------------------------------------------------------------------------------------------

else :

    #-----------------------------------------------------------------------------------------------------

    # PRINTING THE MESSAGE
    print(_("FFMPEG was already installed on the system\nthere was no need to install it."))
    print("")

    #-----------------------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------------------

# ACQUIRING IF THE CODECS FROM RPM FUSION ARE INSTALLED
is_installed_multimedia_codecs, lib_install_list = check_multimedia_codecs_presence(os_version)

#-----------------------------------------------------------------------------------------------------

# CHECKING IF THE CODECS FROM RPM FUSION ARE INSTALLED
if is_installed_multimedia_codecs == "None" :

    #-----------------------------------------------------------------------------------------------------

    # ADDING RPM FUSION REPOSITORY
    utility.add_repository()

    # INSTALLING FFMPEG
    install_codecs(lib_install_list)

    # CHECKING WHICH VERSION OF THE OS IS IN USE
    if (os_version.find("40") != -1 or os_version.find("41") != -1) :

        # UPDATE MULTIMEDIA GROUP
        update_multimedia__40_41()

    else :

        # UPDATE MULTIMEDIA GROUP
        update_multimedia_42()
        
    exit(0)

    #-----------------------------------------------------------------------------------------------------

else :

    #-----------------------------------------------------------------------------------------------------

    # PRINTING THE MESSAGE
    print(_("All the codecs and libraries were already installed\non the system, there was no need to install it."))
    print("")

    exit(0)

    #-----------------------------------------------------------------------------------------------------