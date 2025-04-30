#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO FIND DAVINCI RESOLVE
# EXIT 2 - IT WAS IMPOSSIBLE TO FIND A SUPPORTED VERSION OF DAVINCI
# EXIT 3 - IT WAS IMPOSSIBLE TO CREATE THE SECURE FOLDER
# EXIT 4 - IT WAS IMPOSSIBLE TO MOVE THE LIBS INSIDE THE SECURE FOLDER

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale

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

# FUNCTION THAT CHECKS IF DAVINCI IS INSTALLED AND IF THE HIS VERSION IS SUPPORTED
def check_davinci_version ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING DAVINCI DIRECTORY PATH
    davinci_folder = subprocess.run("ls /opt/", shell=True,  capture_output=True, text=True )

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF DAVINCI RESOLVE IS INSTALLED
    if davinci_folder.stdout.find("resolve") == -1 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to find the DaVinci Resolve installation folder in /opt/resolve."))
        print(_("If you haven't done it already, please install DaVinci Resolve and try again."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING INFO ABOUT WHICH VERSION OF DAVINCI IS INSTALLED
    davinci_info = subprocess.run("cat /opt/resolve/docs/Welcome.txt", shell=True,  capture_output=True, text=True )

    #-----------------------------------------------------------------------------------------------------

    # CHECKING WHICH VERSION OF DAVINCI IS INSTALLED
    if davinci_info.stdout.find("18") != -1 :

        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print(_("DaVinci Resolve 18.x.x was found in the system"))
        print("")

        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 18 POST INSTALLATION PATCH
        post_installation_18_19_20()
        
    elif davinci_info.stdout.find("19") != -1 :

        # STAMPA LA VERSIONE DI DAVINCI IN USO
        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print(_("DaVinci Resolve 19.x.x was found in the system"))
        print("")

        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 19 POST INSTALLATION PATCH
        post_installation_18_19_20()

    elif davinci_info.stdout.find("20") != -1 :

        # STAMPA LA VERSIONE DI DAVINCI IN USO
        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print(_("DaVinci Resolve 20.x.x was found in the system"))
        print("")

        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 19 POST INSTALLATION PATCH
        post_installation_18_19_20()
        
    else :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : An installed version of DaVinci that is not currently supported was found."))
        print(_("Please visit the GitHub page to find which version of DaVinci Resolve are supported."))
        print("")
        print("https://github.com/H3rz3n/davinci-helper")
        print("")
        exit(2)

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT APPLYS THE DAVINCI 18 POST INSTALLATION PATCH
def post_installation_18_19_20 ():

    #-----------------------------------------------------------------------------------------------------

    # READING DAVINCI RESOLVE LIBRARIES LIST
    lib_davinci = subprocess.run("ls /opt/resolve/libs", shell=True,  capture_output=True, text=True )

    # RESETTING THE COUNTER OF THE LIBRARIES TO REMOVE
    lib_to_move = ""

    # CERCO libglib*
    # SEARCHING FOR libglib*
    if lib_davinci.stdout.find("libglib") != -1 :
        lib_to_move = lib_to_move + " libglib*"

    # CERCO libgio*
    # SEARCHING FOR libgio*
    if lib_davinci.stdout.find("libgio") != -1 :
        lib_to_move = lib_to_move + " libgio*"

    # CERCO libgmodule*
    # SEARCHING FOR libgmodule*
    if lib_davinci.stdout.find("libgmodule") != -1 :
        lib_to_move = lib_to_move + " libgmodule*"

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THERE ARE LIBRARIES TO REMOVE
    if lib_to_move == "" :

        # PRINTING THE MESSAGE THAT THE PROGRAM FAILED TO EXECUTE BECAUSE IT IS NOT NECESSARY
        print(_("The libraries were already moved inside the secure folder. There was no need to do anything."))
        print("")
        exit(0)

    #-----------------------------------------------------------------------------------------------------

    # REMOVE EXCESS SPACE FROM THE LIST OF THE LIBRARIES TO MOVE
    lib_to_move = lib_to_move.lstrip(' ')

    # PRINTING THE WARNING MESSAGGE ABOUT THE LIBRARIES THAT WILL BE MOVED
    print(_("The following libraries will be moved in a secure folder :"))
    print(lib_to_move)
    print("")

    #-----------------------------------------------------------------------------------------------------

    # CREATING A SECURE FOLDER WHERE MOVE THE LIBRARIES TO REMOVE
    make_folder = subprocess.run("mkdir /opt/resolve/libs/disabled_libraries", shell=True,  capture_output=True, text=True )

    # CHECKING IF THE DISABLED LIBRARIES FOLDER HAS BEEN CREATED SUCCESSFULLY
    if make_folder.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : It was impossible to create the secure folder where to move the libraries in /opt/resolve/libs/disabled_libraries."))
        print(_("Try again granting the app root permission or create it by yourself."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print(make_folder.stdout)
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(3)
    
    #-----------------------------------------------------------------------------------------------------

    # MOVING THE LIBRARIES TO DISABLED FOLDER
    moving_libs = subprocess.run(f"cd /opt/resolve/libs && mv {lib_to_move} /opt/resolve/libs/disabled_libraries", shell=True,  capture_output=True, text=True )

    # CHECKING IF THE DISABLED LIBRARIES FOLDER HAS BEEN CREATED SUCCESSFULLY
    if moving_libs.returncode != 0 :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : There was an error moving the libraries inside the secure folder in /opt/resolve/libs/disabled_libraries. Try again granting the app root permission or move it by yourself."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print(moving_libs.stdout)
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(4)
    
    else :

        # PRINTING THE MESSAGE THAT THE PROGRAM HAS BEEN EXECUTED SUCCESSFULLY
        print(_("The libraries were correctly moved inside the secure folder."))
        print("")
        exit(0)

    #-----------------------------------------------------------------------------------------------------

   



# STARTING THE FUNCTION THAT CHECKS IF DAVINCI IS INSTALLED AND IF THE HIS VERSION IS SUPPORTED
check_davinci_version()





    
    
    
    
    

    
    
    
    
    
    
    

