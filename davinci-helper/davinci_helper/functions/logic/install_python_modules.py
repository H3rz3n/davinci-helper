#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO INSTALL MOVIEPY PYTHON MODULE

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, pkg_resources

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





# FUNCTION THAT WILL CHECK IF IS NECESSARY TO INSTALLA THE MOVIEPY MODULE
def check_installed_modules ():

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE INSTALLED PACKAGES LIST
    module_list = subprocess.run("pip list", shell=True, capture_output=True, text=True)

    # CHECKING IF THE MOVIEPY MODULE IS INSTALLED
    if module_list.stdout.find("moviepy") == -1:
        
        # INSTALLING THE MODULE
        install_python_modules()
    
    else :
    
        # PRINTING THE SUCCESSFUL STATE
        print(_("Moviepy python module was already installed. There was no need to install it "))
        print("")
        exit(0)    


    #-----------------------------------------------------------------------------------------------------







# FUNTION THAT WILL INSTALL THE NECESSARY PYTHON MODULES
def install_python_modules ():

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING THE MOVIEPY MODULE
    moviepy_install = subprocess.run("pip install moviepy", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE WERE ERRORS
    if moviepy_install.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to install the python module moviepy."))
        print("")
        print(moviepy_install.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)

    else :

        # PRINTING THE SUCCESSFUL STATE
        print(_("Moviepy python module was successfully installed. Now you can use DaVinci Converter "))
        print("")
        exit(0)
    #-----------------------------------------------------------------------------------------------------







# LAUNCHING THE SCRIPT
check_installed_modules()





















        







