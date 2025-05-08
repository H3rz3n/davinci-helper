#
# Copyright 2025 Lorenzo Maiuri
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, pathlib

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



# FUNCTION THAT CHEKS THE EXISTENCE OF FILES FROM A PREVIOUS INSTALLATION INSIDE THE SETTINGS FOLDER
def check_settings_existence ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING THE EXISTENCE OF THE SETTINGS FILE
    flag_settings = pathlib.Path(f'{settings_path}/davinci_helper/davinci_helper_settings')

    #-----------------------------------------------------------------------------------------------------

    # CHECKING THE EXISTENCE SETTINGS FILE
    if not flag_settings.exists() :

        # STARTING THE FUNCTION THAT INSTALL THE DEFAULT SETTINGS
        install_default_settings()

    else :

        # ACQUIRING IF THE SETTINGS NEED TO BE REPLACED AFTER A MAJOR UPDATE
        unsuported, unsupported_version = check_settings_version()

        # CHECKING IF THE SETTINGS NEED TO BE REPLACED FOR A MAJOR UPDATE
        if unsuported == True :

            # UPDATING THE SETTINGS TO A NEW VERSION
            update_settings(unsupported_version)

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT CREATE THE SETTINGS FOLDER AND COPY INSIDE IT THE DEFAULT SETTINGS
def install_default_settings ():

    #-----------------------------------------------------------------------------------------------------

    # CREATING THE SETTINGS FOLDER
    create_folder = subprocess.run(f"mkdir -p '{settings_path}/davinci_helper'",shell=True, text=True)

    # COPYING THE DEFAULT SETTINGS
    copy_default_settings =  subprocess.run(f"cp /usr/share/davinci-helper/data/settings/davinci_helper_settings {settings_path}/davinci_helper/",shell=True, text=True)

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT RESTORES THE DEFAULT SETTINGS
def restore_settings() :

    #-----------------------------------------------------------------------------------------------------

    # DELETING USER SETTINGS
    delete_user_settings = subprocess.run(f"rm {settings_path}/davinci_helper/davinci_helper_settings",shell=True, text=True)

    # COPYING THE DEFAULT SETTINGS
    copy_default_settings =  subprocess.run(f"cp /usr/share/davinci-helper/data/settings/davinci_helper_settings {settings_path}/davinci_helper/",shell=True, text=True)

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL CHECK IF CURRENTLY IS IN USE AL OLDER AND UNSUPPORTED VERSION OF THE SETTINGS
def check_settings_version ():

    #-----------------------------------------------------------------------------------------------------

    # REAGING ONE LINE AT TIME THE SETTINGS LIST
    with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'r', encoding='utf-8') as file :

        # READING THE FILE
        lines = file.readlines()

        # CHECKING WHICH UI IS NECESSARY TO SHOW
        if lines[0].find("v2.1") == -1 :
            
            # RETURNING THAT IS CURRENTLY IN USE AN UNSUPPORTED VERSION
            return True, lines[0]

        else :

            # RETURNING THAT IS CURRENTLY IN USE AN SUPPORTED VERSION
            return False, lines[0]

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL UPDATE AN OLD VERSION OF THE SETTINGS TO A NEWER VERSION
def update_settings (unsupported_version):

    #-----------------------------------------------------------------------------------------------------

    # CHECKING FROM WHICH VERSION WE ARE UPDATING
    if unsupported_version.find("v1.") :

        # REPLACING ALL THE PREVIEWS SETTINGS BECAUSE THERE IS NOTHING IMPORTANT TO PRESERVE
        restore_settings()
    
    elif unsupported_version.find("v2.0.0") :

        # REPLACING ALL THE PREVIEWS SETTINGS BECAUSE THERE IS NOTHING IMPORTANT TO PRESERVE
        restore_settings()
    '''
    elif unsupported_version.find("v3.") :
    '''

    #-----------------------------------------------------------------------------------------------------



# FUNCTION THAT WILL CHANGE THE SETTINGS OF THE UI TO SHOW WHEN THE FUNCTION IS CORRECTLY EXECUTED
def flag_ffmpeg_as_installed ():

    #-----------------------------------------------------------------------------------------------------

    # RESETTING THE COUNTERS
    line_number = 0

    # REAGING ONE LINE AT TIME THE SETTINGS LIST
    with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'r', encoding='utf-8') as file :

        # ACQUIRING FILE CONTENT    
        file_content = file.readlines()

    #-----------------------------------------------------------------------------------------------------
        
    # READING LINE BY LINE THE FILE DUMP
    for line in file_content :
        
        # FINDING THE VISIBILITY SETTINGS
        if line.find("FFMPEG_INSTALLED = FALSE") != -1 :

            # SETTING THE SPLASH SCREEN AS VISIBLE
            file_content[line_number] = "FFMPEG_INSTALLED = TRUE\n"

            # EXTING THE CICLE IN A SECURE WAY
            break

        # ADDING 1 TO THE COUNTER
        line_number = line_number + 1

    #-----------------------------------------------------------------------------------------------------

    # OVERWRITING THE PREVIOUS SETTINGS    
    with open(f"{settings_path}/davinci_helper/davinci_helper_settings", 'w', encoding='utf-8') as file :

        # WRITING THE CONTENT INSIDE THE FILE
        file.writelines(file_content)

    #-----------------------------------------------------------------------------------------------------