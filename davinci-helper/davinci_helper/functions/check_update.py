#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale, subprocess, pathlib, requests

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
class build_check_update_window ():

    # IMPORTO GLI ATTRIBUTI E METODI DALLA CLASSE MADRE UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE
        check_update_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        check_update_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
		# IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        check_update_window_builder.add_from_file(f"{ui_path}/check_update.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.check_update_window = check_update_window_builder.get_object("check_update_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.check_update_window.set_transient_for(parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.icon = check_update_window_builder.get_object("check_update_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.title_text = check_update_window_builder.get_object("check_update_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.check_update_sub_title_text = check_update_window_builder.get_object("check_update_sub_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.check_update_download_update_button = check_update_window_builder.get_object("check_update_download_update_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.check_update_exit_button = check_update_window_builder.get_object("check_update_exit_button")

        #-----------------------------------------------------------------------------------------------------

        # CHIUDO LA FINESTRA DELLA FUNZIONE 4 ALLA PRESSIONE DEL BOTONE
        # CLOSE THE FUNCTION 4 WINDOW WHEN THE BUTTON IS PRESSED
        self.check_update_exit_button.connect('clicked', lambda button: self.check_update_window.destroy())

        # AVVIO LA FUNZIONE CHE MOSTRA I LOG
        # STARTING THE FUNCTION THAT SHOWS THE LOGS
        self.check_update_download_update_button.connect('clicked', self.open_github_page)

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE AVVIA MOSTRA LA FINESTRA IN CASO DI AGGIORNAMENTO TROVATO
    # FUNCTION THAT SHOWS THE WINDOWS IF THE THERE IS AN UPDATE
    def show_update_found_window (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO SUCCESSO
        # LOADING THE ICON FILE IN CASE OF SUCCESS
        self.icon.set_from_file(f"{icon_path}/davinci-helper-icon.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO SUCCESSO
        # LOADING TITLE TEXT IN CASE OF SUCCESS
        self.title_text.set_text(_("A new update is available"))

        # CARICO IL TESTO DEL SOTTOTITOLO DI IN CASO SUCCESSO
        # LOADING SUBTITLE TEXT IN CASE OF SUCCESS
        self.check_update_sub_title_text.set_text(_("Has been found a new version of this app on the official GitHub repository.\nWe recommend you to update it before starting using it."))
        
        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.check_update_window.present()

        #-----------------------------------------------------------------------------------------------------

    



    # FUNZIONE CHE AVVIA LO SCRIPT DELLA FUNZIONE 1
    # FUNCTION THAT STARTS THE FUNCTION 1 SCRIPT
    def show_update_not_found_window (self):

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO SUCCESSO
        # LOADING THE ICON FILE IN CASE OF SUCCESS
        self.icon.set_from_file(f"{icon_path}/function_icons/success.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO SUCCESSO
        # LOADING TITLE TEXT IN CASE OF SUCCESS
        self.title_text.set_text(_("You're using the latest version"))

        # CARICO IL TESTO DEL SOTTOTITOLO DI IN CASO SUCCESSO
        # LOADING SUBTITLE TEXT IN CASE OF SUCCESS
        self.check_update_sub_title_text.set_text(_("No new version of the app was found in the official GitHub repository.\nYou're already using the latest version and you can use the app without issues."))

        # AVVIO LA FUNZIONE CHE MOSTRA I LOG
        # STARTING THE FUNCTION THAT SHOWS THE LOGS
        self.check_update_download_update_button.hide()
        
        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.check_update_window.present()

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE CONTROLLA LA PRESENZA DI AGGIORNAMENTI
    # FUNCTION THAT CHECKS IF THERE ARE NEW APP UPDATES
    def check_update (self):

        #-----------------------------------------------------------------------------------------------------

        # DEFINISCO LE VARIABILI AMBIENTALI
        # SETTING THE ENVIRONMENT VARIABLES 
        owner = "H3rz3n"
        repo = "davinci-helper"
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest" 
        app_version = "v1.0.1"

        # OTTENGO L'ULTIMA VERSIONE DA GITHUB
        # OBTAINING THE LATEST VERSION FROM GITHUB
        response = requests.get(url)

        # CONTROLLO SE LA RICHIESTA HA AVUTO SUCCESSO :
        # CHECKING IF THE REQUEST HAD SUCCESS
        if response.status_code == 200:

            # ESTRAGGO LE INFORMAZIONI DELLA RISPOSTA IN UN DIZIONARIO
            # EXTRACTING THE RESPONDE INFO IN A DICTIONARY
            latest_release = response.json()

            # ESTRAGGO IL NUMERO DI VERSIONE
            # EXTRACTING THE VERSION NUMBER
            remote_version = latest_release["tag_name"]

            # CONTROLLO SE LA VERSIONE REMOTA È UNA NUOVA VERSIONE
            # CHECKING IF THE REMOTE VERSION IS A NEW VERSIONE
            if app_version != remote_version :

                # AVVIO LA FUNZIONE CHE MOSTRA LA PRESENZA DI AGGIORNAMENTI
                # STARTING THE FUNCTION THAT SHOWS THE NEW UPDATE PRESENCE
                self.show_update_found_window()

            else :

                # AVVIO LA FUNZIONE CHE MOSTRA LA L'ASSENZA DI AGGIORNAMENTI
                # STARTING THE FUNCTION THAT SHOWS THAT THERE ARE NO NEW UPDATE
                self.show_update_not_found_window()

            
        else :

            # AVVIO LA FUNZIONE CHE MOSTRA LA L'ASSENZA DI AGGIORNAMENTI
            # STARTING THE FUNCTION THAT SHOWS THAT THERE ARE NO NEW UPDATE
            self.show_update_not_found_window()


        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE APRE LA PAGINA DI DONWLOAD DELL'ULTIMA VERSIONE
    # FUNCTION THAT OPENS THE LATEST VERSION DOWNLOAD PAGE
    def open_github_page(self, widget) :

        #-----------------------------------------------------------------------------------------------------

        # IMPOSTO IL LINK DELLA PAGINA DI DOWNLOAD
        # SETTONG THE DOWNLOAD PAGE LINK
        url = "https://github.com/H3rz3n/davinci-helper/releases/latest"

        # USO LA FUNZIONE GIO PER APRIRE IL LINK NEL BROWSER DI DEFAULT
        # USING GIO TO OPEN THE URL IN THE DEFAULT WEB BROWSER
        Gio.AppInfo.launch_default_for_uri(url)

        #-----------------------------------------------------------------------------------------------------





# FUNZIONE CHE CONTROLLA LA PRESENZA DI AGGIORNAMENTI IN AUTOMATICO
# FUNCTION THAT CHECKS IF THERE ARE NEW APP UPDATES
def check_update_autostart (parent):

    #-----------------------------------------------------------------------------------------------------

    # DEFINISCO LE VARIABILI AMBIENTALI
    # SETTING THE ENVIRONMENT VARIABLES 
    owner = "H3rz3n"
    repo = "davinci-helper"
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest" 
    app_version = "v1.0.1"

    # OTTENGO L'ULTIMA VERSIONE DA GITHUB
    # OBTAINING THE LATEST VERSION FROM GITHUB
    response = requests.get(url)

    # CONTROLLO SE LA RICHIESTA HA AVUTO SUCCESSO :
    # CHECKING IF THE REQUEST HAD SUCCESS
    if response.status_code == 200:

        # ESTRAGGO LE INFORMAZIONI DELLA RISPOSTA IN UN DIZIONARIO
        # EXTRACTING THE RESPONDE INFO IN A DICTIONARY
        latest_release = response.json()

        # ESTRAGGO IL NUMERO DI VERSIONE
        # EXTRACTING THE VERSION NUMBER
        remote_version = latest_release["tag_name"]

        # CONTROLLO SE LA VERSIONE REMOTA È UNA NUOVA VERSIONE
        # CHECKING IF THE REMOTE VERSION IS A NEW VERSIONE
        if app_version != remote_version :

            # GENERO LA FINESTRA AGGIORNAMENTO USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
            # CREATING THE UPDATE  WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
            check_update_window = build_check_update_window(parent)

            # AVVIO LA FUNZIONE CHE MOSTRA LA PRESENZA DI AGGIORNAMENTI
            # STARTING THE FUNCTION THAT SHOWS THE NEW UPDATE PRESENCE
            check_update_window.show_update_found_window()

        


    #-----------------------------------------------------------------------------------------------------
