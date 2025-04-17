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
    # Use a safer way to check file existence before reading
    welcome_file_path = "/opt/resolve/docs/Welcome.txt"
    if not os.path.exists(welcome_file_path):
        print(_("DEBUG : Welcome.txt not found at {path}.").format(path=welcome_file_path))
        print(_("Could not determine DaVinci Resolve version."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(2) # Use unsupported version error for now

    davinci_info = subprocess.run(f"cat {welcome_file_path}", shell=True,  capture_output=True, text=True )

    #-----------------------------------------------------------------------------------------------------

    # CHECKING WHICH VERSION OF DAVINCI IS INSTALLED
    if davinci_info.stdout.find("18") != -1 :

        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print(_("DaVinci Resolve 18.x.x was found in the system"))
        print("")

        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 18 POST INSTALLATION PATCH
        post_installation_18()
         
    elif davinci_info.stdout.find("19") != -1 :

        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print(_("DaVinci Resolve 19.x.x was found in the system"))
        print("")

        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 19 POST INSTALLATION PATCH
        post_installation_19()

    # --- START VERSION 20 SUPPORT ---
    elif davinci_info.stdout.find("20") != -1 :

        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print(_("DaVinci Resolve 20.x.x was found in the system"))
        print("")

        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 20 POST INSTALLATION PATCH
        post_installation_20()
    # --- END VERSION 20 SUPPORT ---
         
    else :

        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : An installed version of DaVinci that is not currently supported (or version could not be read) was found."))
        print(_("Currently supported major versions: 18, 19, 20."))
        print(_("Please visit the GitHub page to check for updates or report an issue."))
        print("")
        print("https://github.com/H3rz3n/davinci-helper")
        print("")
        exit(2)

    #-----------------------------------------------------------------------------------------------------


# FUNCTION THAT APPLYS THE DAVINCI 18 POST INSTALLATION PATCH
# (Also used by v19 and potentially v20 unless specific changes are needed)
def post_installation_18 ():

    #-----------------------------------------------------------------------------------------------------

    # Define paths
    libs_path = "/opt/resolve/libs"
    disabled_libs_path = os.path.join(libs_path, "disabled_libraries")
    
    # Check if libs path exists
    if not os.path.isdir(libs_path):
        print(_("DEBUG : DaVinci Resolve libraries folder not found at {path}.").format(path=libs_path))
        print(_("Cannot apply post-installation steps."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1) # Using Exit 1 as it's related to finding Resolve components

    # READING DAVINCI RESOLVE LIBRARIES LIST
    # Using os.listdir for better safety than shell=True
    try:
        lib_files = os.listdir(libs_path)
    except OSError as e:
        print(_("DEBUG : Error listing libraries in {path}: {error}").format(path=libs_path, error=e))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1) # Or a new specific error code

    # Libraries to potentially move (using patterns)
    libs_to_check = ["libglib-", "libgio-", "libgmodule-"] 
    lib_to_move_list = []

    # Find libraries matching the patterns
    for lib_pattern in libs_to_check:
        found = False
        for filename in lib_files:
            if filename.startswith(lib_pattern):
                # Add wildcard to match different versions (e.g., libglib-2.0.so.0)
                lib_to_move_list.append(lib_pattern + "*") 
                found = True
                break # Move to next pattern once one match is found

    # Convert list to space-separated string for the mv command
    lib_to_move = " ".join(lib_to_move_list)

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THERE ARE LIBRARIES TO MOVE
    if not lib_to_move:
        # Also check if the disabled folder already exists and contains expected files
        # This makes the check more robust
        already_done = False
        if os.path.isdir(disabled_libs_path):
             try:
                 disabled_files = os.listdir(disabled_libs_path)
                 if any(f.startswith(pattern.replace("*","")) for pattern in libs_to_check for f in disabled_files):
                     already_done = True
             except OSError:
                 pass # Ignore error listing disabled files, proceed as if not done

        if already_done:
             print(_("The necessary libraries appear to have been moved already. No action taken."))
             print("")
             exit(0)
        else:
             print(_("Could not find the specific libraries (libglib-*, libgio-*, libgmodule-*) in {path}.").format(path=libs_path))
             print(_("No action taken. This might be normal if DaVinci Resolve changed its included libraries."))
             print("")
             exit(0)


    #-----------------------------------------------------------------------------------------------------

    # PRINTING THE WARNING MESSAGGE ABOUT THE LIBRARIES THAT WILL BE MOVED
    print(_("The following libraries (or patterns) will be moved into a secure folder:"))
    print(lib_to_move)
    print("")

    #-----------------------------------------------------------------------------------------------------

    # CREATING A SECURE FOLDER WHERE MOVE THE LIBRARIES TO REMOVE
    # Check if it already exists first
    if not os.path.isdir(disabled_libs_path):
        print(_("Creating secure folder: {path}").format(path=disabled_libs_path))
        # Use try-except for better error handling
        try:
            os.makedirs(disabled_libs_path, exist_ok=True) # exist_ok=True handles race conditions
        except OSError as e:
             # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : Failed to create the secure folder {path}.").format(path=disabled_libs_path))
            print(_("Error: {error}").format(error=e))
            print(_("Try running the script with root privileges (sudo) or create the directory manually."))
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("")
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")
            exit(3)
    else:
        print(_("Secure folder {path} already exists.").format(path=disabled_libs_path))

    #-----------------------------------------------------------------------------------------------------

    # MOVING THE LIBRARIES TO DISABLED FOLDER
    # Using f-string and ensuring paths are quoted if they contain spaces (less likely here, but good practice)
    # Note: Using shell=True here for wildcard expansion (*) is convenient, but be aware of potential security risks if paths were user-controlled.
    move_command = f"mv {libs_path}/{lib_to_move.replace(' ', ' ' + libs_path + '/')} {disabled_libs_path}/"
    # Need to handle spaces in file paths correctly if mv is used with wildcards and multiple files.
    # A safer approach might be to loop and move files individually using Python's os.rename or shutil.move
    # But for simplicity with wildcards, we stick to shell=True for now.
    
    # Let's build the command more carefully for multiple patterns
    individual_moves = []
    for pattern in lib_to_move_list:
        individual_moves.append(f"mv {os.path.join(libs_path, pattern)} {disabled_libs_path}/")
    
    # Execute moves one pattern at a time to get better error info if one fails
    success = True
    failed_moves = []
    error_output = ""

    print(_("Moving libraries..."))
    for pattern in lib_to_move_list:
        command = f"mv {os.path.join(libs_path, pattern)} {disabled_libs_path}/"
        # print(f"Executing: {command}") # Uncomment for debugging
        moving_libs = subprocess.run(command, shell=True, capture_output=True, text=True)
        if moving_libs.returncode != 0:
            # Check if the error is "No such file or directory" - might happen if wildcard matches nothing
            if "No such file or directory" not in moving_libs.stderr:
                 success = False
                 failed_moves.append(pattern)
                 error_output += f"Failed to move {pattern}:\n{moving_libs.stderr}\n"
            # else: # Optional: report if a pattern matched nothing
            #    print(f"Warning: Pattern '{pattern}' did not match any files to move.")


    # CHECKING IF THE MOVE WAS SUCCESSFUL
    if not success:
        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : There was an error moving some libraries into the secure folder: {path}.").format(path=disabled_libs_path))
        print(_("Failed patterns: {patterns}").format(patterns=", ".join(failed_moves)))
        print(_("Try running the script with root privileges (sudo)."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("")
        print("Error Details:")
        print(error_output)
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(4)
     
    else:
        # PRINTING THE MESSAGE THAT THE PROGRAM HAS BEEN EXECUTED SUCCESSFULLY
        print(_("The necessary libraries were correctly moved into the secure folder."))
        print("")
        exit(0)

    #-----------------------------------------------------------------------------------------------------


# FUNCTION THAT APPLYS THE DAVINCI 19 POST INSTALLATION PATCH
def post_installation_19 ():

    #-----------------------------------------------------------------------------------------------------
     
    # Assuming v19 needs the same fixes as v18
    print(_("Applying post-installation steps for version 19 (using v18 method)..."))
    post_installation_18()

    #-----------------------------------------------------------------------------------------------------

# --- START VERSION 20 FUNCTION ---
# FUNCTION THAT APPLYS THE DAVINCI 20 POST INSTALLATION PATCH
def post_installation_20 ():

    #-----------------------------------------------------------------------------------------------------
    # !! Assumption !! 
    # This currently assumes version 20 requires the same library adjustments 
    # as version 18/19 (moving libglib*, libgio*, libgmodule*). 
    # If version 20 needs different steps, modify this function accordingly.
    # Check forums or documentation for DaVinci Resolve 20 on Linux for specific issues.
    
    print(_("Applying post-installation steps for version 20 (using v18/v19 method)..."))
    post_installation_18()

    #-----------------------------------------------------------------------------------------------------
# --- END VERSION 20 FUNCTION ---


# STARTING THE FUNCTION THAT CHECKS IF DAVINCI IS INSTALLED AND IF THE HIS VERSION IS SUPPORTED
check_davinci_version()
