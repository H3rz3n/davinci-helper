#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
#   

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULES IMPORT
import sys, gi, os, subprocess, threading, locale, gettext

# IMPORTAZIONE DEI MODULI DELLE FUNZIONI
# FUNCTION MODULES IMPORT
from .function_2 import installation_script

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Gio', '2.0')

# IMPORTO I MODULI NECESSARI DA GI
# IMPORTING THE NECESSARY MODULES FROM GI
from gi.repository import Gtk, Adw, Gdk, Gio, GLib

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



# FUNZIONE CHE AVVIA L'INSTALLAZIONE DI DAVINCI RESOLVE
# FUNCTION THAT STARTS THE DAVINCI RESOLVE INSTALLATION WIZARD
def installation_script(file_path):

    #-----------------------------------------------------------------------------------------------------

    # ACQUISISCO LA DIRECTORY DI DOWNLOAD DELL'UTENTE 
    # ACQUIRING THE USER'S DOWNLOAD DIRECTORY
    download_directory = subprocess.Popen("xdg-user-dir DOWNLOAD", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    download_directory_output, download_directory_err = download_directory.communicate()

    #-----------------------------------------------------------------------------------------------------

    # DEFINISCO IL PERCORSO DI ESTRAZIONE DELL'INSTALLER
    # DEFINING THE INSTALLER EXTRACTION PATH
    folder_path = download_directory_output.strip() + "/davinci_resolve_installer"

    #-----------------------------------------------------------------------------------------------------

    # CREO LA CARTELLA IN CUI ESTRARRE L'INSTALLER
    # CREATING THE FOLDER WHERE TO EXTRACT THE INSTALLER
    make_folder = subprocess.Popen(f"mkdir -p {folder_path}", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    make_folder_output, make_folder_err = make_folder.communicate()

    #-----------------------------------------------------------------------------------------------------

    # ESTRAZIONE DELL'INSTALLER 
    # INSTALLER EXTRACTION
    unzip = subprocess.Popen(f"unzip -o {file_path} -d {folder_path}",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    unzip_output, unzip_err = unzip.communicate()

    # STAMPO I LOG E GLI ERRORI
    # PRINT ANY LOGS AND ERRORS
    print(unzip_output)
    print(unzip_err)

    # CONTROLLO SE SONO PRESENTI ERRORI DOPO L'ESECUZIONE DEL PROGRAMMA E LI RIMANDO AL PROGRAMMA PRINCIPALE
    # CHECKING FOR ERRORS AFTER RUNNING THE PROGRAM AND RETURN THEM TO THE MAIN PROGRAM
    if unzip_output.find("unzip:  cannot find or open") == 0 :

        # RESTITUISCO UN ERRORE INERENTE ALL'ESTRAZIONE DEL FILE DI INSTALLAZIONE
        # RETURNING AN ERROR ABOUT THE EXTRACTION OF THE INSTALLER FILE
        error_type="Extraction"
        error_log = (_(f"DEBUG : There was an error extracting the DaVinci Resolve installer.\n\n{unzip_output}\n {unzip_err} \n\nPlease open an issue and paste those logs on the project GitHub page  :\nhttps://github.com/H3rz3n/davinci-helper/issues"))
        print(error_log)
        return  error_type, error_log
        exit()

    #-----------------------------------------------------------------------------------------------------

    # AVVIO DEL PROGRAMMA DI INSTALLAZIONE
    # STARTING THE INSTALLATION WIZARD
    start_wizard = subprocess.Popen(f"cd {folder_path} && SKIP_PACKAGE_CHECK=1 ./*.run",shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    start_wizard_output, start_wizard_err = start_wizard.communicate()

    # STAMPO I LOG E GLI ERRORI
    # PRINT ANY LOGS AND ERRORS
    print(start_wizard_output)
    print(start_wizard_err)

    # CONTROLLO SE SONO PRESENTI ERRORI DOPO L'ESECUZIONE DEL PROGRAMMA E LI RIMANDO AL PROGRAMMA PRINCIPALE
    # CHECKING FOR ERRORS AFTER RUNNING THE PROGRAM AND RETURN THEM TO THE MAIN PROGRAM
    if start_wizard_err != None:

        # RESTITUISCO UN ERRORE INERENTE ALL'INSTALLAZIONE
        # RETURNING AN ERROR ABOUT THE INSTALLATION
        error_type="Install"
        error_log = (_(f"DEBUG : There was an error starting the install wizard of DaVinci Resolve.\n\n{start_wizard_err} \n\nPlease open an issue and paste those logs on the project GitHub page :\nhttps://github.com/H3rz3n/davinci-helper/issues"))
        print(error_log)
        return  error_type, error_log
        exit()

    else:

        # RESTITUISCO L'ASSENZA DI ERRORI
        # RETURNING THE ABSENCE OF ERRORS
        error_log="Nothing to say, all clear. Here's a bit of Lorem Ipsum just for fun : \n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec laoreet tristique enim, id semper augue tincidunt non. Aliquam ut rhoncus augue, non commodo justo. Suspendisse quis mauris a lectus ullamcorper consectetur quis sed nisi. Fusce non ex sed nibh consequat egestas ac et lectus. Donec urna ligula, euismod vitae posuere ac, tincidunt vitae augue. Pellentesque porttitor volutpat lacus nec eleifend. Curabitur laoreet orci augue, in malesuada dui cursus eu. Pellentesque sapien nibh, mollis luctus egestas a, euismod elementum lacus. Quisque tristique odio sed ultricies fermentum."        
        error_type="No"
        return error_type, error_log
        exit()

    #-----------------------------------------------------------------------------------------------------

    




