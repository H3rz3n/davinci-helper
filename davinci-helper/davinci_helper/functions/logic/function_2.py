#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO EXTRACT THE INSTALLER IN THE DESIGNED FOLDER
# EXIT 2 - IT WAS IMPOSSIBLE TO START THE DAVINCI INSTALLATION WIZARD

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, gi, os, subprocess, threading, locale, gettext

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





#-----------------------------------------------------------------------------------------------------

# ACQUIRING FILE PATH FROM LAST FUNCTION
file_path = sys.argv[1]

#-----------------------------------------------------------------------------------------------------

# ACQUIRING THE USER'S DOWNLOAD DIRECTORY
download_directory = subprocess.run("xdg-user-dir DOWNLOAD", shell=True, capture_output=True, text=True)

#-----------------------------------------------------------------------------------------------------

# DEFINING THE INSTALLER EXTRACTION PATH
folder_path = download_directory.stdout.strip() + "/davinci_resolve_installer"

#-----------------------------------------------------------------------------------------------------

# CREATING THE FOLDER WHERE TO EXTRACT THE INSTALLER
subprocess.run(f"mkdir -p {folder_path}", shell=True, capture_output=True, text=True)

#-----------------------------------------------------------------------------------------------------

# INSTALLER EXTRACTION
unzip = subprocess.run(f"unzip -o {file_path} -d {folder_path}",shell=True, capture_output=True, text=True)

# CHECKING FOR ERRORS AFTER RUNNING THE PROGRAM AND RETURN THEM TO THE MAIN PROGRAM
if unzip.returncode != 0 :

    print(_("DEBUG : There was an error extracting the DaVinci Resolve installer :"))
    print(unzip.stdout)
    print("")
    print(_("Please open an issue report and paste this error code on the project GitHub page :"))
    print("")
    print("https://github.com/H3rz3n/davinci-helper/issues")
    print("")
    exit(1)

#-----------------------------------------------------------------------------------------------------

# STARTING THE INSTALLATION WIZARD
start_wizard = subprocess.run(f"cd {folder_path} && SKIP_PACKAGE_CHECK=1 ./*.run",shell=True, capture_output=True, text=True)

# CHECKING FOR ERRORS AFTER STARTING THE INSTALLATION WIZARD AND RETURN THEM TO THE MAIN PROGRAM
if start_wizard.returncode != 0 :

    # DELETING THE FOLDER WHERE WE EXTRACTED THE INSTALLER
    subprocess.run(f"rm -r {folder_path}", shell=True, capture_output=True, text=True)
    
    print(_("DEBUG : There was an error launching the DaVinci Resolve installation wizard :"))
    print(start_wizard.stdout)
    print("")
    print(_("Please open an issue report and paste this error code on the project GitHub page :"))
    print("")
    print("https://github.com/H3rz3n/davinci-helper/issues")
    print("")
    exit(2)

else:

    # DELETING THE FOLDER WHERE WE EXTRACTED THE INSTALLER
    subprocess.run(f"rm -r {folder_path}", shell=True, capture_output=True, text=True)
    
    exit(0)

#-----------------------------------------------------------------------------------------------------





