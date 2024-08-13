#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
#   

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale

#-----------------------------------------------------------------------------------------------------

# DEFINISCO I PERCORSI DEI FILE DI TRADUZIONE
# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

#-----------------------------------------------------------------------------------------------------

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO LOCALE
# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
locale.bindtextdomain('davinci-helper', locale_path)

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO GETTEXT
# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE GETTEXT MODULE
gettext.bindtextdomain('davinci-helper', locale_path)

# COMUMICO A GETTEXT QUALE FILE USARE PER TRADURRE IL PROGRAMMA
# TELLING GETTEXT WHICH FILE TO USE FOR THE TRANSLATION OF THE APP
gettext.textdomain('davinci-helper')

# COMUNICO A GETTEXT IL SEGNALE DI TRADUZIONE
# TELLING GETTEXT THE TRANSLATE SIGNAL
_ = gettext.gettext

#-----------------------------------------------------------------------------------------------------

# FUNZIONE CHE CONTROLLA SE DAVINCI È INSTALLATO E SE LA VERSIONE È COMPATIBILE
# FUNCTION THAT CHECKS IF DAVINCI IS INSTALLED AND IF THE HIS VERSION IS SUPPORTED
def check_davinci_version ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUISICO IL PERCORSO DELLA DIRECTORY DI DAVINCI
    # ACQUIRING DAVINCI DIRECTORY PATH
    davinci_folder = subprocess.Popen("ls /opt/", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    davinci_folder_output, davinci_folder_error = davinci_folder.communicate()

    # CONTROLLO CHE DAVINCI RESOLVE SIA INSTALLATO
    # CHECKING IF DAVINCI RESOLVE IS INSTALLED
    if davinci_folder_output.find("resolve") == -1 :

        # STAMPO IL MESSAGGI DI ERRORE
        # PRINTING THE ERROR MESSAGE
        print("")
        print(_("DEBUG : It was impossible to find the DaVinci Resolve installation folder in /opt/resolve. If you have not done it already, please install DaVinci Resolve and try again."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)

    #-----------------------------------------------------------------------------------------------------

    # ACQUISICO LE INFORMAZIONI SULLA VERSIONE DI DAVINCI INSTALLATA
    # ACQUIRING INFO ABOUT WHICH VERSION OF DAVINCI IS INSTALLED
    davinci_info = subprocess.Popen("cat /opt/resolve/docs/Welcome.txt", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    davinci_info_output, davinci_info_error = davinci_info.communicate()


    # CONTROLLO QUALE VERSIONE DI DAVINCI È STATA INSTALLATA
    # CHECKING WHICH VERSION OF DAVINCI IS INSTALLED
    if davinci_info_output.find("18") != -1 :

        # STAMPA LA VERSIONE DI DAVINCI IN USO
        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print("")
        print(_("DaVinci Resolve 18.x.x was found in the system"))
        print("")

        # AVVIO LA FUNZIONE CHE APPLICA LA PATCH POST-INSTALLAZIONE DI DAVINCI 18
        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 18 POST INSTALLATION PATCH
        post_installation_18()
        
    elif davinci_info_output.find("19") != -1 :

        # STAMPA LA VERSIONE DI DAVINCI IN USO
        # PRINTING WHICH VERSION OF DAVINCI IS IN USE
        print("")
        print(_("DaVinci Resolve 19.x.x was found in the system"))
        print("")

        # AVVIO LA FUNZIONE CHE APPLICA LA PATCH POST-INSTALLAZIONE DI DAVINCI 19
        # STARTING THE FUNCTION THAT APPLYS THE DAVINCI 19 POST INSTALLATION PATCH
        post_installation_19()
        
    else :

        # STAMPO IL MESSAGGIO DI ERRORE
        # PRINTING THE ERROR MESSAGE
        print("")
        print(_("DEBUG : An installed version of DaVinci that is not currently supported was found. Please visit the GitHub page to find which version of DaVinci Resolve are supported."))
        print("https://github.com/H3rz3n/davinci-helper")
        print("")
        exit(1)

    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE APPLICA LA PATCH POST-INSTALLAZIONE DI DAVINCI 18
# FUNCTION THAT APPLYS THE DAVINCI 18 POST INSTALLATION PATCH
def post_installation_18 ():

    #-----------------------------------------------------------------------------------------------------

    # LETTURA DELLE LIBRERIE DI DAVINCI RESOLVE
    # READING DAVINCI RESOLVE LIBRARIES LIST
    lib_davinci = subprocess.Popen("ls /opt/resolve/libs", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    lib_davinci_output, lib_davinci_error = lib_davinci.communicate()

    # AZZERO IL CONTATORE DELLE LIBRERIE DA RIMUOVERE
    # RESETTING THE COUNTER OF THE LIBRARIES TO REMOVE
    lib_to_move = ""

    # CERCO libglib*
    # SEARCHING FOR libglib*
    if lib_davinci_output.find("libglib") != -1 :
        lib_to_move = lib_to_move + " libglib*"

    # CERCO libgio*
    # SEARCHING FOR libgio*
    if lib_davinci_output.find("libgio") != -1 :
        lib_to_move = lib_to_move + " libgio*"

    # CERCO libgmodule*
    # SEARCHING FOR libgmodule*
    if lib_davinci_output.find("libgmodule") != -1 :
        lib_to_move = lib_to_move + " libgmodule*"

    # CONTROLLO SE CI SONO LIBRERIE DA RIMUOVERE
    # CHECKING IF THERE ARE LIBRARIES TO REMOVE
    if lib_to_move == "" :

        # STAMPO IL MESSAGGIO DI MANCATA ESECUZIONE DEL PROGRAMMA PERCHÈ NON NECESSARIO
        # PRINTING THE MESSAGE THAT THE PROGRAM FAILED TO EXECUTE BECAUSE IT IS NOT NECESSARY
        print("")
        print(_("The libraries were already moved inside the secure folder. There was no need to execute the function."))
        print("")
        exit(0)

    # ELIMINO LO SPAZIO IN ECCESSO DALLA LISTA DELLE LIBRERIE DA SPOSTARE
    # REMOVE EXCESS SPACE FROM THE LIST OF THE LIBRARIES TO MOVE
    lib_to_move = lib_to_move.lstrip(' ')

    # STAMPO IL MESSAGGIO DI AVVISO DELLE LIBRERIE CHE VERRANNO SPOSTATE
    # PRINTING THE WARNING MESSAGGE ABOUT THE LIBRARIES THAT WILL BE MOVED
    print("")
    print(_("The following libraries will be moved in a secure folder :"))
    print(lib_to_move)
    print("")

    #-----------------------------------------------------------------------------------------------------

    # CREAZIONE CARTELLA SICURA PER LE LIBRERIE DA RIMUOVERE
    # CREATING A SECURE FOLDER WHERE MOVE THE LIBRARIES TO REMOVE
    make_folder = subprocess.Popen("mkdir /opt/resolve/libs/disabled_libraries", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    make_folder_output, make_folder_error = make_folder.communicate()

    # ACQUISISCO LA LISTA DEI FILE NELLA CARTELLA LIBS
    # ACQUIRING FILE LIST IN LIBS FOLDER
    lib_davinci = subprocess.Popen("ls /opt/resolve/libs", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    lib_davinci_output, lib_davinci_error = lib_davinci.communicate()

    # CONTROLLO SE LA CARTELLA DELLE LIBRERIE DISABILITATE È STATA CREATA CORRETTAMENTE
    # CHECKING IF THE DISABLED LIBRARIES FOLDER HAS BEEN CREATED SUCCESSFULLY
    if lib_davinci_output.find("disabled_libraries") == -1 :

        # STAMPO IL MESSAGGI DI ERRORE
        # PRINTING THE ERROR MESSAGE
        print("")
        print(_("DEBUG : It was impossible to create the secure folder where to move libraries in /opt/resolve/libs/disabled_libraries. Try again granting the app root permission or create it by yourself."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)
    
    #-----------------------------------------------------------------------------------------------------

    # SPOSTO LE LIBRERE NELLA CARTELLA DELLE LIBRERIE DISABILITATE
    # MOVING THE LIBRARIES TO DISABLED FOLDER
    moving_libs = subprocess.Popen(f"cd /opt/resolve/libs && mv {lib_to_move} /opt/resolve/libs/disabled_libraries", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    moving_libs_output, moving_libs_error = moving_libs.communicate()

    # ACQUISISCO LA LISTA DEI FILE NELLA CARTELLA DISABLED LIBRARIES
    # ACQUIRING FILE LIST IN DISABLED LIBRARIES FOLDER
    lib_disabled = subprocess.Popen("ls /opt/resolve/libs/disabled_libraries", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True )
    lib_disabled_output, lib_disabled_error = lib_disabled.communicate()

    # CONTROLLO SE LA CARTELLA DELLE LIBRERIE DISABILITATE È STATA CREATA CORRETTAMENTE
    # CHECKING IF THE DISABLED LIBRARIES FOLDER HAS BEEN CREATED SUCCESSFULLY
    if (lib_disabled_output.find("libglib") == -1) or (lib_disabled_output.find("libgio") == -1) or (lib_disabled_output.find("libgmodule") == -1) :

        # STAMPO IL MESSAGGI DI ERRORE
        # PRINTING THE ERROR MESSAGE
        print("")
        print(_("DEBUG : There was an error moving the libraries inside the secure folder in /opt/resolve/libs/disabled_libraries. Try again granting the app root permission or move it by yourself."))
        print("")
        print(_("Please open an issue report and paste this error code on the project GitHub page :"))
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)
    
    else :

        # STAMPO IL MESSAGGIO DI AVVENUTA ESECUTIONE DEL PROGRAMMA CON SUCCESSO
        # PRINTING THE MESSAGE THAT THE PROGRAM HAS BEEN EXECUTED SUCCESSFULLY
        print("")
        print(_("The libraries were correctly moved inside the secure folder."))
        print("")
        exit(0)

    #-----------------------------------------------------------------------------------------------------

   



# FUNZIONE CHE APPLICA LA PATCH POST-INSTALLAZIONE DI DAVINCI 19
# FUNCTION THAT APPLYS THE DAVINCI 19 POST INSTALLATION PATCH
def post_installation_19 ():

    #-----------------------------------------------------------------------------------------------------

    print("Currently in development, sorry")
    exit(1)

    #-----------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------
#----------------------------------------------  MAIN ------------------------------------------------
#-----------------------------------------------------------------------------------------------------

# AVVIO LA FUNZIONE CHE CONTROLLA SE DAVINCI È INSTALLATO E SE LA VERSIONE È COMPATIBILE
# STARTING THE FUNCTION THAT CHECKS IF DAVINCI IS INSTALLED AND IF THE HIS VERSION IS SUPPORTED
check_davinci_version()





    
    
    
    
    

    
    
    
    
    
    
    

