#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale, subprocess

# IMPORTAZIONE DEI MODULI PER LE FUNZIONI
# FUNCTION MODULES IMPORT
from .functions.settings_management import check_settings_existence, restore_settings, build_reset_settings_window
from .functions.check_update import build_check_update_window, check_update_autostart
from .functions.function_1_gui import build_function_1
from .functions.function_2_gui import build_function_2
from .functions.function_3_gui import build_function_3
from .functions.function_4_gui import build_function_4
from .functions.about_gui import build_about_window

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
settings_path = os.path.join(f"{home_dir}/.config/davinci_helper")

#-----------------------------------------------------------------------------------------------------

# IMPORTO IL FILE CSS PER LA DEFINIZIONE DEGLI STILI
# IMPORTING THE CSS FILE FOR STYLES DEFINITION
css_provider = Gtk.CssProvider()
css_provider.load_from_path(f'{css_path}/style-dark.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

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

# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA PRINCIPALE
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE MAIN WINDOW
class build_main_window(Adw.Application):

    #-----------------------------------------------------------------------------------------------------

    # IMPORTO GLI ATTRIBUTI E METODI DELLA CLASSE MADRE ADW.APPLICATION" UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, **kwargs):

        #-----------------------------------------------------------------------------------------------------

        super().__init__(**kwargs)

        #-----------------------------------------------------------------------------------------------------

        # FORZO IL TEMA SCURO SU TUTTI I DISPOSITIVI
        # FORCING THE DARK THEME ON ALL DEVICES
        style_manager = Adw.StyleManager.get_default()
        style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

        #-----------------------------------------------------------------------------------------------------

        # RICAVO E COLLEGO LA VOCE DEL MENU A TENDINA A AD UNA FUNZIONE 
        # LINKING TO A FUNCTION THE HAMBURGER MENU ITEM
        check_update_action = Gio.SimpleAction.new("check_update", None)
        check_update_action.connect("activate", self.check_update)
        self.add_action(check_update_action)

        # RICAVO E COLLEGO LA VOCE DEL MENU A TENDINA A AD UNA FUNZIONE 
        # LINKING TO A FUNCTION THE HAMBURGER MENU ITEM
        reset_settings_action = Gio.SimpleAction.new("reset_settings", None)
        reset_settings_action.connect("activate", self.reset_settings)
        self.add_action(reset_settings_action)

        # RICAVO E COLLEGO LA VOCE DEL MENU A TENDINA A AD UNA FUNZIONE 
        # LINKING TO A FUNCTION THE HAMBURGER MENU ITEM
        show_about_action = Gio.SimpleAction.new("show_about", None)
        show_about_action.connect("activate", self.show_about_window)
        self.add_action(show_about_action)

        #-----------------------------------------------------------------------------------------------------

        # RICHIAMO LA FUNZIONE "CONNECT" UTILIZZANDO COME PARAMETRI "ACTIVATE" E LA FUNZIONE DI GENERAZIONE DELLA FINESTRA PRINCIPALE
        # CALLING THE CONNECT FUNCTION USING AS PARAMETERS "ACTIVATE" AND THE MAIN WINDOW CREATOR FUNCTION
        self.connect('activate', self.main_window_activation)

        #-----------------------------------------------------------------------------------------------------




    # AVVIO DELLA FUNZIONE CHE GENERA LA FINESTRA PRINCIPALE E LA MANDA A SCHERMO
    # STARTING THE FUNCTION THAT CREATES THE MAIN WINDOW AND DIPLAYS IT
    def main_window_activation (self, app):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA PRINCIPALE
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE MAIN WINDOW
        main_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        main_window_builder.set_translation_domain('davinci-helper')

		# IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA PRINCIPALE
		# IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        main_window_builder.add_from_file(f"{ui_path}/main_window.ui")

        # OTTENGO LA FINESTRA PRINCIPALE ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE MAIN WINDOW AND HER CHILD FROM THE UI FILE
        self.main_window = main_window_builder.get_object("main_window")

        # IMPOSTO LA FINESTRA PRINCIPALE PER FAR CHIUDERE IL PROGRAMMA ALLA CHIUSURA DELLA FINESTRA
        # SETTING THE MAIN WINDOW TO CLOSE THE APP AFTER ALL APP WINDOWS ARE CLOSED
        self.main_window.set_application(self)

        # ACQUISISCO L'OGGETTO DELLA FINESTRA MADRE
        # ACQUIRING MAIN WINDOW OBJECT
        self.parent = self.main_window
        
        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.main_window.present()

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_icon_1 = main_window_builder.get_object("main_window_icon_1")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_icon_2 = main_window_builder.get_object("main_window_icon_2")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_icon_3 = main_window_builder.get_object("main_window_icon_3")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_icon_4 = main_window_builder.get_object("main_window_icon_4")

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_text_title_1 = main_window_builder.get_object("main_window_text_title_1")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_text_title_2 = main_window_builder.get_object("main_window_text_title_2")
        
        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_text_title_3 = main_window_builder.get_object("main_window_text_title_3")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_text_title_4 = main_window_builder.get_object("main_window_text_title_4")

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_function_button_1 = main_window_builder.get_object("main_window_function_button_1")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_function_button_2 = main_window_builder.get_object("main_window_function_button_2")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_function_button_3 = main_window_builder.get_object("main_window_function_button_3")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_function_button_4 = main_window_builder.get_object("main_window_function_button_4")

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_info_button_1 = main_window_builder.get_object("main_window_info_button_1")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_info_button_2 = main_window_builder.get_object("main_window_info_button_2")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_info_button_3 = main_window_builder.get_object("main_window_info_button_3")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.main_window_info_button_4 = main_window_builder.get_object("main_window_info_button_4")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA
        # LOADING THE ICON FILE
        self.main_window_icon_1.set_from_file(f"{icon_path}/main_icons/F1.svg")

        # CARICO IL FILE DELL'ICONA
        # LOADING THE ICON FILE
        self.main_window_icon_2.set_from_file(f"{icon_path}/main_icons/F2.svg")

        # CARICO IL FILE DELL'ICONA
        # LOADING THE ICON FILE
        self.main_window_icon_3.set_from_file(f"{icon_path}/main_icons/F3.svg")

        # CARICO IL FILE DELL'ICONA
        # LOADING THE ICON FILE
        self.main_window_icon_4.set_from_file(f"{icon_path}/main_icons/F4.svg")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL TESTO DEL TITOLO 
        # LOADING TITLE TEXT
        self.main_window_text_title_1.set_text(_("Install DaVinci\ndependencies"))

        # CARICO IL TESTO DEL TITOLO 
        # LOADING TITLE TEXT
        self.main_window_text_title_2.set_text(_("Launch DaVinci\nResolve installer"))

        # CARICO IL TESTO DEL TITOLO 
        # LOADING TITLE TEXT
        self.main_window_text_title_3.set_text(_("Apply DaVinci post\ninstallation fix"))

        # CARICO IL TESTO DEL TITOLO 
        # LOADING TITLE TEXT
        self.main_window_text_title_4.set_text(_("Check and install the\ncorrect GPU driver"))

        #-----------------------------------------------------------------------------------------------------

        # APRI LA FINESTRA DELLA FUNZIONE 1
        # OPEN THE FUNCTION 1 WINDOW
        self.main_window_function_button_1.connect('clicked', self.function_1_window_activation)

        # APRI LA FINESTRA DELLA FUNZIONE 2
        # OPEN THE FUNCTION 2 WINDOW
        self.main_window_function_button_2.connect('clicked', self.function_2_window_activation)

        # APRI LA FINESTRA DELLA FUNZIONE 3
        # OPEN THE FUNCTION 3 WINDOW
        self.main_window_function_button_3.connect('clicked', self.function_3_window_activation)

        # APRI LA FINESTRA DELLA FUNZIONE 4
        # OPEN THE FUNCTION 4 WINDOW
        self.main_window_function_button_4.connect('clicked', self.function_4_window_activation)

        #-----------------------------------------------------------------------------------------------------

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 1
        # OPEN THE INFO WINDOW OF FUNCTION 1
        self.main_window_info_button_1.connect('clicked', self.info_window_1_activation)

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 2
        # OPEN THE INFO WINDOW OF FUNCTION 2
        self.main_window_info_button_2.connect('clicked', self.info_window_2_activation)

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 3
        # OPEN THE INFO WINDOW OF FUNCTION 3
        self.main_window_info_button_3.connect('clicked', self.info_window_3_activation)
        
        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 4
        # OPEN THE INFO WINDOW OF FUNCTION 4
        self.main_window_info_button_4.connect('clicked', self.info_window_4_activation)
        
        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE CHE CONTROLLA SE È NECESSARIO MOSTRARE L'AVVISO
        # STARTING THE FUNCTION THAT CHEKS IF IS NECESSARY TO SHOW THE WARNING
        start_splash_screen = self.check_splash_screen()

        # CONTROLLO SE È NECESSARIO AVVIARE LA SPLASH SCREEN
        # CHECKING IF IS NECESSARY TO SHOW THE SPLASH SCREEN
        if start_splash_screen == True :

            # AVVIO LA FUNZIONE CHE MOSTRA LA FINESTRA DI SPLASH SCREEN
            # STARTING THE FUNCTION THAT SHOWS THE SPLASH SCREEN
            self.show_splash_screen()

        # AVVIO IL CONTROLLO DEGLI AGGIORNAMENTI
        # STARTING THE UPDATE CHECK
        else :

            # CONTROLLO LA PRESENZA DI AGGIORNAMENTI
            # CHECKING IF THERE ARE NEW APP UPDATES
            check_update_autostart(self.main_window)
        
        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE AVVIO IL CONTROLLO DEGLI AGGIORNAMENTI
    # FUNCTION THAT STARTS THE UPDATE CHECK
    def check_update (self, action, test):

        #-----------------------------------------------------------------------------------------------------

        # GENERO LA FINESTRA AGGIORNAMENTO USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE UPDATE  WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.check_update_window = build_check_update_window(self.main_window)

        # CONTROLLO LA PRESENZA DI AGGIORNAMENTI
        # CHECKING IF THERE ARE NEW APP UPDATES
        self.check_update_window.check_update()

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE RIPRISTINA LE IMPOSTAZIONI PREDEFINITE
    # FUNCTION THAT RESTORES THE DEFAULT SETTINGS
    def reset_settings (self, action, test):

        # AVVIO LA FUNZIONE CHE RIPRISTINA LE IMPOSTAZIONI PREDEFINITE
        # STARTING THE FUNCTION THAT RESTORES THE DEFAULT SETTINGS
        restore_settings()

        # GENERO LA FINESTRA INFO USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE INFO WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.reset_settings_window = build_reset_settings_window(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.reset_settings_window.show_reset_settings_window()





    # FUNZIONE CHE MOSTRA LA FINESTRA DI INFORMAZIONI SUL PROGRAMMA
    # FUNCTION THAT SHOWS THE ABOUT THIS APP WINDOW
    def show_about_window (self, action, test):

        #-----------------------------------------------------------------------------------------------------
        
        # GENERO LA FINESTRA DI INFORMAZIONI SUL PROGRAMMA USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE ABOUT THIS APP WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.about_window = build_about_window(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.about_window.show_about_window()

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 1
    # FUNCTION THAT SHOWS THE FUNCTION 1 WINDOW
    def function_1_window_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # GENERO LA FINESTRA FUNZIONE 1 USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE FUNCTION 1 WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.function_window_1 = build_function_1(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA DELLA FUNZIONE 1 ED I SUOI CHILD
        # PRINTING TO SCREEN THE FUNCTION 1 WINDOW AND HER CHILDS
        self.function_window_1.start_function()

        #-----------------------------------------------------------------------------------------------------

        



    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 2
    # FUNCTION THAT SHOWS THE FUNCTION 2 WINDOW
    def function_2_window_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # GENERO LA FINESTRA FUNZIONE 2 USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE FUNCTION 2 WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.function_window_2 = build_function_2(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA DELLA FUNZIONE 2 ED I SUOI CHILD
        # PRINTING TO SCREEN THE FUNCTION 2 WINDOW AND HER CHILDS
        self.function_window_2.print_window()

        #-----------------------------------------------------------------------------------------------------




    
    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 3
    # FUNCTION THAT SHOWS THE FUNCTION 3 WINDOW
    def function_3_window_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # GENERO LA FINESTRA FUNZIONE 3 USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE FUNCTION 3 WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.function_window_3 = build_function_3(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA DELLA FUNZIONE 3 ED I SUOI CHILD
        # PRINTING TO SCREEN THE FUNCTION 3 WINDOW AND HER CHILDS
        self.function_window_3.start_function()

        #-----------------------------------------------------------------------------------------------------




    
    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 4
    # FUNCTION THAT SHOWS THE FUNCTION 4 WINDOW
    def function_4_window_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # GENERO LA FINESTRA FUNZIONE 4 USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE FUNCTION 4 WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        self.function_window_4 = build_function_4(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA DELLA FUNZIONE 4 ED I SUOI CHILD
        # PRINTING TO SCREEN THE FUNCTION 4 WINDOW AND HER CHILDS
        self.function_window_4.start_function()

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 1
    # FUNCTION THAT SHOW THE WINDOW OF THE FUNCTION 1
    def info_window_1_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        info_1_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        info_1_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
        # IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        info_1_window_builder.add_from_file(f"{ui_path}/info_function_1.ui")
        
        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_1 = info_1_window_builder.get_object("info_window_1")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.info_window_1.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.info_window_1.present()

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_1_info_text = info_1_window_builder.get_object("info_window_1_info_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_1_exit_button = info_1_window_builder.get_object("info_window_1_exit_button")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL TESTO DI INFO
        # LOADING THE INFO TEXT
        self.info_window_1_info_text.set_text(_("This part of the software will install all the dependencies necessary to correctly launch the installation and the execution of DaVinci Resolve. The script will detect your Fedora version and the libraries installed and using this information it will install only the packages needed. This script does not diffuse any information about you or your system, the internet connection is required only if there are some missing libraries"))

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.info_window_1_exit_button.connect('clicked', lambda button: self.info_window_1.destroy())

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 2
    # FUNCTION THAT SHOW THE WINDOW OF THE FUNCTION 2
    def info_window_2_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        info_2_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        info_2_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
        # IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        info_2_window_builder.add_from_file(f"{ui_path}/info_function_2.ui")
        
        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_2 = info_2_window_builder.get_object("info_window_2")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.info_window_2.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.info_window_2.present()

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_2_info_text = info_2_window_builder.get_object("info_window_2_info_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_2_exit_button = info_2_window_builder.get_object("info_window_2_exit_button")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL TESTO DI INFO
        # LOADING THE INFO TEXT
        self.info_window_2_info_text.set_text(_("This part of the software asks you to indicate the DaVinci Resolve installer path and runs it with the necessary patch to allow it to work properly."))

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.info_window_2_exit_button.connect('clicked', lambda button: self.info_window_2.destroy())

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 3
    # FUNCTION THAT SHOW THE WINDOW OF THE FUNCTION 3
    def info_window_3_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        info_3_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        info_3_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
        # IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        info_3_window_builder.add_from_file(f"{ui_path}/info_function_3.ui")
        
        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_3 = info_3_window_builder.get_object("info_window_3")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.info_window_3.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.info_window_3.present()

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_3_info_text = info_3_window_builder.get_object("info_window_3_info_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FIL
        self.info_window_3_exit_button = info_3_window_builder.get_object("info_window_3_exit_button")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL TESTO DI INFO
        # LOADING THE INFO TEXT
        self.info_window_3_info_text.set_text(_("This part of the software will put some of the dependencies shipped with DaVinci Resolve in a safe folder, in order to make it use the system one's"))

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.info_window_3_exit_button.connect('clicked', lambda button: self.info_window_3.destroy())

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 4
    # FUNCTION THAT SHOW THE WINDOW OF THE FUNCTION 4
    def info_window_4_activation (self, widget):

        #-----------------------------------------------------------------------------------------------------
        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        info_4_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        info_4_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
        # IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        info_4_window_builder.add_from_file(f"{ui_path}/info_function_4.ui")
        
        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_4 = info_4_window_builder.get_object("info_window_4")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.info_window_4.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.info_window_4.present()

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_4_info_text = info_4_window_builder.get_object("info_window_4_info_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.info_window_4_exit_button = info_4_window_builder.get_object("info_window_4_exit_button")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL TESTO DI INFO
        # LOADING THE INFO TEXT
        self.info_window_4_info_text.set_text(_("This part of the software will check what GPU you are using and then, if it is supported, it will check if the correct drivers are installed. If it finds missing or outdated drivers the software will install them to make your GPU fully support DaVinci Resolve."))

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.info_window_4_exit_button.connect('clicked', lambda button: self.info_window_4.destroy())

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE CONTROLLA SE È NECESSARIO MOSTRARE LA SPLASH SCREEN
    # FUNCTION THAT CHEKS IF IS NECESSARY TO SHOW THE SPLASH SCREEN
    def check_splash_screen(self):

        #-----------------------------------------------------------------------------------------------------

        # AZZERO I CONTATORI
        # RESETTING THE COUNTERS
        start_splash_screen = False

        # LEGGO LA LISTA DELLE IMPOSTAZIONI RIGA PER RIGA 
        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper_settings", 'r', encoding='utf-8') as file :

            for line in file :

                # CONTROLLO SE È NECESSARIO MOSTRARE LA SPLASH SCREEN
                # CHECKING IF IS NECESSARY TO SHOW THE SPLASH SCREEN
                if line.find("SHOW_WELCOME_SPLASH_SCREEN") != -1 and line.find("TRUE") != -1 :

                    # IMPOSTO COME NECESSARIO IL MOSTRARE LA SPLASH SCREEN
                    # SETTING AD NECESSARY TO SHOW THE SPLASH SCREEN
                    start_splash_screen = True
                
        #-----------------------------------------------------------------------------------------------------

        # RESTITUISCO AL PROGRAMMA SE È NECESSARIO MOSTRARE LA SPLASH SCREEN
        # RETURNING TO THE APP IF IS NECESSARY TO SHOW THE SPLASH SCREEN
        return start_splash_screen

        #-----------------------------------------------------------------------------------------------------     





    # FUNZIONE CHE MOSTRA SPLASH SCREEN
    # FUNCTION THAT SHOW THE SPLASH SCREEN
    def show_splash_screen (self):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        welcome_messagge_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        welcome_messagge_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
        # IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        welcome_messagge_window_builder.add_from_file(f"{ui_path}/welcome_messagge_splash_screen.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.welcome_messagge_window = welcome_messagge_window_builder.get_object("welcome_messagge_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.welcome_messagge_window.set_transient_for(self.parent)

        # AVVIO IL CONTROLLO DEGLI AGGIORNAMENTI ALLA CHIUSURA DELLA FINESTRA
        # STARTING THE UPDATE CHECK WHEN THE WINDOW IS CLOSED
        self.welcome_messagge_window.connect("close-request", lambda window: check_update_autostart(self.main_window))
        

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_icon = welcome_messagge_window_builder.get_object("welcome_messagge_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_title_text = welcome_messagge_window_builder.get_object("welcome_messagge_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_sub_title_text = welcome_messagge_window_builder.get_object("welcome_messagge_sub_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_sub_title_text_2 = welcome_messagge_window_builder.get_object("welcome_messagge_sub_title_text_2")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_sub_title_text_3 = welcome_messagge_window_builder.get_object("welcome_messagge_sub_title_text_3")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_no_see_switch = welcome_messagge_window_builder.get_object("welcome_messagge_no_see_switch")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.welcome_messagge_exit_button = welcome_messagge_window_builder.get_object("welcome_messagge_exit_button")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA
        # LOADING THE ICON FILE
        self.welcome_messagge_icon.set_from_file(f"{icon_path}/davinci-helper-icon.svg")

        # CARICO IL TESTO DEL TITOLO
        # LOADING TITLE TEXT
        self.welcome_messagge_title_text.set_text(_('''You have successfully\ninstalled DaVinci Helper !'''))

        # CARICO IL TESTO DEL SOTTOTITOLO
        # LOADING THE SUBTITLE TEXT
        self.welcome_messagge_sub_title_text.set_text(_('''Thank you for trusting us and installing DaVinci Helper. We hope that\nthis app will make the installation of DaVinci Resolve easier for you.'''))

        # CARICO IL TESTO DEL SOTTOTITOLO
        # LOADING THE SUBTITLE TEXT
        self.welcome_messagge_sub_title_text_2.set_text(_('''This app is not affiliated in any way with BlackMagic Design,\nit's only a community project and comes without any guarantees.'''))

        # CARICO IL TESTO DEL SOTTOTITOLO
        # LOADING THE SUBTITLE TEXT
        #self.welcome_messagge_sub_title_text_3.set_text(_('''If you find this app useful please consider to help us
        #developing this app or making a donation to the project.'''))
        paragraph_3 = '''If you find this app useful and want to improve it please\nconsider to help us <a href="https://github.com/H3rz3n/davinci-helper">developing</a> this app or <a href="https://www.example.com">making a donation</a>  to the project.'''
        self.welcome_messagge_sub_title_text_3.set_markup(paragraph_3)

        # AVVIO LA FUNZIONE CHE CAMBIA LE IMPOSTAZIONI DI VISIBILITÀ DELLA SPLASH SCREEN
        # STARTING THE FUNCTION THAT CHANGES THE VISIBILITY SETTINGS OF THE SPLASH SCREEN
        self.welcome_messagge_no_see_switch.connect("notify::active", self.change_spash_screen_status)

        # CHIUDO LA FINESTRA DI BENVENUTO ALLA PRESSIONE DEL BOTONE
        # CLOSING THE WELCOME WINDOW WHEN THE BUTTON IS PRESSED
        self.welcome_messagge_exit_button.connect('clicked', lambda button: (self.welcome_messagge_window.destroy(), check_update_autostart(self.main_window) ))

        # MOSTRO LA FINESTRA DI AVVISO
        # SHOWING THE WARNING WINDOW
        self.welcome_messagge_window.present()

        #-----------------------------------------------------------------------------------------------------

    



    # FUNZIONE CHE CAMBIA LE IMPOSTAZIONI DI VISIBILITÀ DELLA SPLASH SCREEN
    # FUNCTION THAT CHANGES THE SPLASH SCREEN VISIBILITY SETTINGS
    def change_spash_screen_status(self, widget, status):

        #-----------------------------------------------------------------------------------------------------

        # AZZERO I CONTATORI
        # RESETTING THE COUNTERS
        line_number = 0

        # LEGGO LA LISTA DELLE IMPOSTAZIONI RIGA PER RIGA 
        # REAGING ONE LINE AT TIME THE SETTINGS LIST
        with open(f"{settings_path}/davinci_helper_settings", 'r', encoding='utf-8') as file :

            # ACQUISICO IL CONTENUTO DEL FILE
            # ACQUIRING FILE CONTENT    
            file_content = file.readlines()
        
        # SCORRO IL FILE DUMP RIGA PER RIGA
        # READING LINE BY LINE THE FILE DUMP
        for line in file_content :
            
            # TROVO L'IMPOSTAZIONE DI VISIBILITÀ
            # FINDING THE VISIBILITY SETTINGS
            if line.find("SHOW_WELCOME_SPLASH_SCREEN") != -1 and line.find("TRUE") != -1 :

                # IMPOSTO LA SPLASH SCREEN COME NASCOSTA
                # SETTING THE SPLASH SCREEN AS HIDDEN
                file_content[line_number] = "SHOW_WELCOME_SPLASH_SCREEN = FALSE\n"

                # ESCO DAL CICLO IN MODO SICURO
                # EXTING THE CICLE IN A SECURE WAY
                break

            elif line.find("SHOW_WELCOME_SPLASH_SCREEN") != -1 and line.find("FALSE") != -1 :

                # IMPOSTO LA SPLASH SCREEN COME VISIBILE
                # SETTING THE SPLASH SCREEN AS VISIBLE
                file_content[line_number] = "SHOW_WELCOME_SPLASH_SCREEN = TRUE\n"

                # ESCO DAL CICLO IN MODO SICURO
                # EXTING THE CICLE IN A SECURE WAY
                break

            # AUMENTO IL CONTATORE
            # ADDING 1 TO THE COUNTER
            line_number = line_number + 1

        # SOVRASCRIVO LE PRECEDENTI IMPOSTAZIONI
        # OVERWRITING THE PREVIOUS SETTINGS    
        with open(f"{settings_path}/davinci_helper_settings", 'w', encoding='utf-8') as file :

            # SCRIVO IL CONTENUTO NEL FILE
            # WRITING THE CONTENT INSIDE THE FILE
            file.writelines(file_content)
                
        #-----------------------------------------------------------------------------------------------------









# FUNZIONE DI AVVIO DEL PROGRAMMA
# APP STARTING FUNCTION
def main():

    #-----------------------------------------------------------------------------------------------------

    # AVVIO LA FUNZIONE CHE CONTROLLA L'ESISTENZA DELLE IMPOSTAZIONI
    # STARTING THE FUNCTION THAT CHECKS IF THE SETTINGS EXIST
    check_settings_existence()

    #
    #
    #_ = set_language()
    #print("Prova")

    # ASSEGNANAZIONE DELL'ID DEL PROGRAMMA E COPIA DELLA CLASSE DELLA FINESTRA PRINCIPALE NELLA VARIABILE CHE RAPPRESENTA LA FINESTRA DEL PROGRAMMA
    # ASSIGNING THE APP ID AND COPY OF THE MAIN WINDOW CLASS IN A VARIABLE
    app_gui = build_main_window(application_id="com.davinci.helper.app")

    # AVVIO DELLA FINESTRA PRINCIPALE
    # STARTING THE MAIN WINDOW
    app_gui.run(sys.argv)

    #-----------------------------------------------------------------------------------------------------








#-----------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    #
    #    
    main()

