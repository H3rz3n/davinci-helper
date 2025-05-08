#
# Copyright 2025 Lorenzo Maiuri
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, requests

#-----------------------------------------------------------------------------------------------------

# NOT STANDARD MODULES IMPORT
from ..gui.settings_management_dialog_gui import setting_management_dialog_class
#-----------------------------------------------------------------------------------------------------

# NOT STANDARD MODULES IMPORT
from . import app_info

#-----------------------------------------------------------------------------------------------------

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

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



# FUNCTION THAT CHECKS IF THERE ARE NEW APP UPDATES
def check_update ():

    #-----------------------------------------------------------------------------------------------------

    # SETTING VARIABLES DEFAULT VALUE
    remote_version = ""
    remote_changelog = ""

    #-----------------------------------------------------------------------------------------------------

    # SETTING THE ENVIRONMENT VARIABLES 
    owner = "H3rz3n"
    repo = "davinci-helper"
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest" 

    #-----------------------------------------------------------------------------------------------------

    # GETTING IF THERE IS A WORKING INTERNET CONNECTION
    ping = subprocess.run("ping -c 1 1.1.1.1", shell=True, capture_output=True, text=True)

    # CHECKING IF THERE IS A WORKING INTERNET CONNECTION
    if ping.returncode == 0 :

        # OBTAINING THE LATEST VERSION FROM GITHUB
        response = requests.get(url)

        # CHECKING IF THE REQUEST HAD SUCCESS
        if response.status_code == 200:

            # EXTRACTING THE RESPONDE INFO IN A DICTIONARY
            latest_release = response.json()

            # EXTRACTING THE VERSION NUMBER
            remote_version = latest_release["tag_name"]

            # EXTRACTING THE REMOTE CHANGELOG NUMBER
            remote_changelog = latest_release["body"]


            # CHECKING IF THE REMOTE VERSION IS A NEW VERSIONE
            if app_info.app_version != remote_version :

                return True, remote_version, remote_changelog, app_info.app_version

            else :

                return False, remote_version, remote_changelog, app_info.app_version

    else :

        return False, remote_version, remote_changelog, app_info.app_version

    #-----------------------------------------------------------------------------------------------------