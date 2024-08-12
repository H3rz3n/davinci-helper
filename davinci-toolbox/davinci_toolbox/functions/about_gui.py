
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
# GitHub : https://github.com/H3rz3n/davinci-toolbox
#

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, threading, gettext, locale

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
css_path = os.path.join("/usr/share/davinci-toolbox/data/css")

# DEFINISCO I PERCORSI DEI FILE UI
# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-toolbox/data/ui")

# DEFINISCO I PERCORSI DEI FILE IMMAGINE
# DEFINING IMAGES FILES PATH
icon_path = os.path.join("/usr/share/davinci-toolbox/data/icons")

# DEFINISCO I PERCORSI DEI FILE DI TRADUZIONE
# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-toolbox/locale")

# DEFINISCO I PERCORSI DEI FILE DI IMPOSTAZIONE
# DEFINING SETTINGS FILES PATH
home_dir = os.path.expanduser("~")
settings_path = os.path.join(f"{home_dir}/.config/davinci_toolbox")

#-----------------------------------------------------------------------------------------------------

# IMPORTO IL FILE CSS PER LA DEFINIZIONE DEGLI STILI
# IMPORTING THE CSS FILE FOR STYLES DEFINITION
css_provider = Gtk.CssProvider()
css_provider.load_from_path(f'{css_path}/style-dark.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

#-----------------------------------------------------------------------------------------------------

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO LOCALE
# ASSOCIATE THE NAME OF THE TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE LOCALE MODULE
locale.bindtextdomain('davinci-toolbox', locale_path)

# ASSOCIA IL NOME DEL DIZIONARIO DI TRADUZIONE AL FILE CORRISPONDENTE PER IL MODULO GETTEXT
# ASSOCIATE THE NAME OF TRANSLATION DICTIONARY TO THIS FILE PATH FOR THE GETTEXT MODULE
gettext.bindtextdomain('davinci-toolbox', locale_path)

# COMUMICO A GETTEXT QUALE FILE USARE PER TRADURRE IL PROGRAMMA
# TELLING GETTEXT WHICH FILE TO USE FOR THE TRANSLATION OF THE APP
gettext.textdomain('davinci-toolbox')

# COMUNICO A GETTEXT IL SEGNALE DI TRADUZIONE
# TELLING GETTEXT THE TRANSLATE SIGNAL
_ = gettext.gettext

#-----------------------------------------------------------------------------------------------------



#
#
class build_about_window():

    #-----------------------------------------------------------------------------------------------------

    # IMPORTO GLI ATTRIBUTI E METODI DELLA CLASSE MADRE ADW.APPLICATION" UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA PRINCIPALE
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE MAIN WINDOW
        about_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        about_window_builder.set_translation_domain('davinci-toolbox')

		# IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA PRINCIPALE
		# IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        about_window_builder.add_from_file(f"{ui_path}/about_window.ui")

        # OTTENGO LA FINESTRA PRINCIPALE ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE MAIN WINDOW AND HER CHILD FROM THE UI FILE
        self.about_window = about_window_builder.get_object("about_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.about_window.set_transient_for(parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.icon = about_window_builder.get_object("about_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.title_text = about_window_builder.get_object("about_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.sub_title_text = about_window_builder.get_object("about_sub_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.sub_title_text_2 = about_window_builder.get_object("about_sub_title_text_2")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.sub_title_text_3 = about_window_builder.get_object("about_sub_title_text_3")

        #-----------------------------------------------------------------------------------------------------

        # CARICO IL FILE DELL'ICONA DI IN CASO ERRORE
        # LOADING THE ICON FILE IN CASE OF ERROR
        self.icon.set_from_file(f"{icon_path}/davinci-toolbox-icon.svg")

        # CARICO IL TESTO DEL TITOLO DI IN CASO ERRORE
        # LOADING TITLE TEXT IN CASE OF ERROR
        self.title_text.set_text(_("DaVinci Toolbox"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        self.sub_title_text.set_text(_("Version 1.0"))

        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        self.sub_title_text_2.set_text(_('''Developed with love by Lorenzo "Herzen" Maiuri\nTranslated with love by Camilla Fioretti'''))
        
        # CARICO IL TESTO DEL SOTTOTITOLO IN CASO DI ERRORE
        # LOADING THE SUBTITLE TEXT IN CASE OF ERROR
        paragraph_3 = '''This software is published under the <a href="https://github.com/H3rz3n/davinci-toolbox/blob/main/LICENSE">CC-BY-NC-SA license</a> and comes without any warranty.\nWe are not responsibile for any side effect or damage on your equipment.'''
        self.sub_title_text_3.set_markup(paragraph_3)

        #-----------------------------------------------------------------------------------------------------






    # MOSTRO LA FINESTRA DI INFO
    # SHOWING THE APP ABOUT WINDOW
    def show_about_window (self):

        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.about_window.present()

        #-----------------------------------------------------------------------------------------------------




























