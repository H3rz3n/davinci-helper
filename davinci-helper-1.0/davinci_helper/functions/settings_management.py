#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale, subprocess, pathlib

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib

#-----------------------------------------------------------------------------------------------------

# DEFINISCO I PERCORSI DEI FILE CSS
# DEFINING CSS FILES PATH
css_path = os.path.join("/usr/share/davinci-helper/data/css")

# DEFINISCO I PERCORSI DEI FILE UI
# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")

# DEFINISCO I PERCORSI DEI FILE IMMAGINE
# DEFINING IMAGES FILES PATH
icon_path = os.path.join("/usr/share/davinci-helper/data/icons")

# DEFINISCO I PERCORSI DEI FILE DI TRADUZIONE
# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

# DEFINISCO I PERCORSI DEI FILE DI IMPOSTAZIONE
# DEFINING SETTINGS FILES PATH
home_dir = os.path.expanduser("~")
settings_path = os.path.join(f"{home_dir}/.config/")

#-----------------------------------------------------------------------------------------------------

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO LOCALE
# ASSOCIATE THE NAME OF THE TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
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





# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE WINDOW
class build_reset_settings_window ():

    # IMPORTO GLI ATTRIBUTI E METODI DALLA CLASSE MADRE UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE
        reset_settings_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        reset_settings_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
		# IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        reset_settings_window_builder.add_from_file(f"{ui_path}/reset_settings.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.reset_settings_window = reset_settings_window_builder.get_object("reset_settings_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.reset_settings_window.set_transient_for(parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.icon = reset_settings_window_builder.get_object("reset_settings_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.title_text = reset_settings_window_builder.get_object("reset_settings_title_text")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO SUCCESSO
        # LOADING THE ICON FILE IN CASE OF SUCCESS
        self.icon.set_from_file(f"{icon_path}/function_icons/success.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO SUCCESSO
        # LOADING TITLE TEXT IN CASE OF SUCCESS
        self.title_text.set_text(_("The default settings has\nbeen loaded successfully"))
        
        #-----------------------------------------------------------------------------------------------------






    # FUNZIONE CHE AVVIA LO SCRIPT DELLA FUNZIONE 1
    # FUNCTION THAT STARTS THE FUNCTION 1 SCRIPT
    def show_reset_settings_window (self):

        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.reset_settings_window.present()

        #-----------------------------------------------------------------------------------------------------






# FUNZIONE CHE CREA E COPIA NELLA CARTELLA LE IMPOSTAZIONI PREDEFINITE
# FUNCTION THAT CREATE THE SETTINGS FOLDER AND COPY INSIDE IT THE DEFAULT SETTINGS
def install_default_settings ():

    #-----------------------------------------------------------------------------------------------------

    # CREO LA CARTELLA DELLE IMPOSTAZIONI
    # CREATING THE SETTINGS FOLDER
    create_folder = subprocess.run(f"mkdir -p '{settings_path}/davinci_helper'",shell=True, text=True)

    # COPIO LE IMPOSTAZIONI PREDEFINITE
    # COPYING THE DEFAULT SETTINGS
    copy_default_settings =  subprocess.run(f"cp /usr/share/davinci-helper/data/settings/davinci_helper_settings {settings_path}/davinci_helper/",shell=True, text=True)

    #-----------------------------------------------------------------------------------------------------





# FUNZIOME CHE CONTROLLA L'ESISTENZA ED I FILE DI IMPOSTAZIONE
# FUNCTION THAT CHEKS THE EXISTENCE AND THE FILES INSIDE THE SETTINGS FOLDER
def check_settings_existence ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUISISCO L'ESISTENZA DEI FILE DI IMPOSTAZIONE
    # ACQUIRING THE EXISTENCE OF THE SETTINGS FILE
    flag_settings = pathlib.Path(f'{settings_path}/davinci_helper/davinci_helper_settings')

    #-----------------------------------------------------------------------------------------------------

    # CONTROLLO SE ESISTE IL FILE DI IMPOSTAZIONI
    # CHECKING THE EXISTENCE SETTINGS FILE
    if not flag_settings.exists() :

        # AVVIO LA FUNZIONE CHE INSTALLA LE IMPOSTAZIONI PREDEFINITE
        # STARTING THE FUNCTION THAT INSTALL THE DEFAULT SETTINGS
        install_default_settings()


    #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE RIPRISTINA LE IMPOSTAZIONI PREDEFINITE
# FUNCTION THAT RESTORES THE DEFAULT SETTINGS
def restore_settings() :

    #-----------------------------------------------------------------------------------------------------

    # ELIMINO LE IMPOSTAZIONI DELL'UTENTE
    # DELETING USER SETTINGS
    delete_user_settings = subprocess.run(f"rm {settings_path}/davinci_helper/davinci_helper_settings",shell=True, text=True)


    # COPIO LE IMPOSTAZIONI PREDEFINITE
    # COPYING THE DEFAULT SETTINGS
    copy_default_settings =  subprocess.run(f"cp /usr/share/davinci-helper/data/settings/davinci_helper_settings {settings_path}/davinci_helper/",shell=True, text=True)

    #-----------------------------------------------------------------------------------------------------