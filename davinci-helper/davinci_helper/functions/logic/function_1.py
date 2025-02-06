#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO RETRIEVE WHAT IS THE INSTALLED VERSION OF FEDORA LINUX
# EXIT 2 - IT WAS IMPOSSIBLE TO RETRIEVE THE INSTALLED LIBRARIES LIST
# EXIT 3 - IT WAS IMPOSSIBLE TO INSTALL THE MISSING LIBRARIES. PROBABLY FAULTY INTERNET OR BROKEN DNF

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





# FUNCTION THAT READ THE LIST OF THE INSTALLED LIBRARIES
def get_libraries_list ():

    #-----------------------------------------------------------------------------------------------------

    # READING INSTALLED LIBRARY LIST
    library_list = subprocess.run("dnf list --installed | grep lib", shell=True, capture_output=True, text=True)

    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON WHETHER THERE ARE ERRORS OR NOT
    if library_list.returncode == 0: 

        # RESTITUISCE IL VALORE AL PROGRAMMA
        # RETURNS VALUE TO THE SCRIPT
        return library_list.stdout

    else:
        print(_("DEBUG : There was an error reading the library list :"))
        print(library_list.stderr)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(2)

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT CHECK WHICH LIBRARIES ARE MISSING IN FEDORA 38-39-40
def check_dependencies_40 (library_list_output):
    
    #-----------------------------------------------------------------------------------------------------
    
    # CHECKING IF ALL THE LIBRARIES NEEDED ARE INSTALLED
    lib_to_install = ""
    
    # SEARCHING FOR libxcrypt-compat
    if library_list_output.find('libxcrypt-compat') == -1 :
        lib_to_install = lib_to_install + " libxcrypt-compat"
    
    # SEARCHING FOR libcurl
    if library_list_output.find('libcurl') == -1 :
        lib_to_install = lib_to_install + " libcurl"
    
    # SEARCHING FOR libcurl-devel
    if library_list_output.find('libcurl-devel') == -1 :
        lib_to_install = lib_to_install + " libcurl-devel"
    
    # SEARCHING FOR mesa-libGLU
    if library_list_output.find('mesa-libGLU') == -1 :
        lib_to_install = lib_to_install + " mesa-libGLU"
    
    # SEARCHING FOR zlib-ng-compat
    if library_list_output.find('zlib') == -1 :
        lib_to_install = lib_to_install + " zlib"

    #-----------------------------------------------------------------------------------------------------

    # CHEKING IF THERE ARE MISSING LIBRARIES
    if lib_to_install != "" :

        # REMOVE EXCESS SPACE FROM THE LIST OF THE LIBRARIES TO INSTALL
        lib_to_install = lib_to_install.lstrip(' ')

        # PRINTING THE LIST OF THE LIBRARIES TO INSTALL
        print(_(f"The following libraries will be installed because they are missing :"))
        print(lib_to_install )
        print("")

        # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING LIBRARIES
        libraries_installation(lib_to_install)
    
    else:

        # PRINTING THE MISSING OF LIBRARIES TO INSTALL
        print(_("There are no missing libraries to install, you can now install DaVinci Resolve"))
        print("")

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT CHECK WHICH LIBRARIES ARE MISSING IN FEDORA 38-39-40
def check_dependencies_41 (library_list_output):
    
    #-----------------------------------------------------------------------------------------------------
    
    # CHECKING IF ALL THE LIBRARIES NEEDED ARE INSTALLED
    lib_to_install = ""
    
    # SEARCHING FOR libxcrypt-compat
    if library_list_output.find('libxcrypt-compat') == -1 :
        lib_to_install = lib_to_install + " libxcrypt-compat"
    
    # SEARCHING FOR libcurl
    if library_list_output.find('libcurl') == -1 :
        lib_to_install = lib_to_install + " libcurl"
    
    # SEARCHING FOR libcurl-devel
    if library_list_output.find('libcurl-devel') == -1 :
        lib_to_install = lib_to_install + " libcurl-devel"
    
    # SEARCHING FOR mesa-libGLU
    if library_list_output.find('mesa-libGLU') == -1 :
        lib_to_install = lib_to_install + " mesa-libGLU"

    # SEARCHING FOR zlib-ng-compat
    if library_list_output.find('fuse-libs') == -1 :
        lib_to_install = lib_to_install + " fuse-libs"

    #-----------------------------------------------------------------------------------------------------

    # CHEKING IF THERE ARE MISSING LIBRARIES
    if lib_to_install != "" :

        # REMOVE EXCESS SPACE FROM THE LIST OF THE LIBRARIES TO INSTALL
        lib_to_install = lib_to_install.lstrip(' ')

        # PRINTING THE LIST OF THE LIBRARIES TO INSTALL
        print(_(f"The following libraries will be installed because they are missing :"))
        print(lib_to_install )
        print("")

        # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING LIBRARIES
        libraries_installation(lib_to_install)
    
    else:

        # PRINTING THE MISSING OF LIBRARIES TO INSTALL
        print(_("There are no missing libraries to install, you can now install DaVinci Resolve"))
        print("")

    #-----------------------------------------------------------------------------------------------------






# FUNCTION THAT INSTALL THE MISSING LIBRARIES IN THE SYSTEM
def libraries_installation (lib_to_install):

    #-----------------------------------------------------------------------------------------------------

    # INSTALLING THE MISSING LIBRARIES
    package_install = subprocess.run(f"dnf install -y {lib_to_install}",shell=True, capture_output=True, text=True)

    # PRINTING IN THE TERMINAL THE RESULT DEPENDING ON IF THERE ARE ERRORS OR NOT
    if package_install.returncode == 0 : 
        print(package_install.stdout)
    
    else:
        print(_("DEBUG : There was an error installing the missing libraries :"))
        print("")
        print(package_install.stdout)
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(3)

    #-----------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------
#----------------------------------------------  MAIN ------------------------------------------------
#-----------------------------------------------------------------------------------------------------


# ACQUIRING THE USED VERSION OF FEDORA
os_version = check_fedora_version()



# ACQUIRING THE INSTALLED LIBRARIES LIST
library_list = get_libraries_list()



# CHECKING IF IS INSTALLED FEDORA 40
if os_version.find("40") != -1 :

    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    check_dependencies_40(library_list)

# CHECKING IF IS INSTALLED FEDORA 41
elif os_version.find("41") != -1 :

    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    check_dependencies_41(library_list)

# CHECKING IF IS INSTALLED FEDORA 42
elif os_version.find("42") != -1 :

    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    check_dependencies_41(library_list)

# CHECKING IF IS INSTALLED FEDORA RAWHIDE
elif os_version.find("Rawhide") != -1 :

    # EXECUTION OF THE FUNCTION THAT INSTALL THE MISSING DEPENDENCIES
    check_dependencies_41(library_list)








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

