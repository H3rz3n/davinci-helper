#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
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

# DEFINISCO I PERCORSI DEI FILE IMMAGINE
# DEFINING IMAGES FILES PATH
icon_path = os.path.join("/usr/share/davinci-helper/data/icons")

# DEFINISCO I PERCORSI DEI FILE UI
# DEFINING UI FILES PATH
ui_path = os.path.join("/usr/share/davinci-helper/data/ui")

# DEFINISCO I PERCORSI DEI FILE DI TRADUZIONE
# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

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



# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA DELLA FUNZIONE 2
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE FUNCTION 2 WINDOW
class build_function_2 ():

    # IMPORTO GLI ATTRIBUTI E METODI DALLA CLASSE MADRE UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE PARENT CLASS USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI 
        # STARTING THE BUILDER FUNCTION TO READ THE UI
        function_2_window_builder = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        function_2_window_builder.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA
		# IMPORTING THE UI FILE THAT REPRESENT THE WINDOW
        function_2_window_builder.add_from_file(f"{ui_path}/function_2.ui")
        
        # OTTENGO LA FINESTRA ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE WINDOW AND HER CHILD FROM THE UI FILE
        self.function_2_window = function_2_window_builder.get_object("function_2_window")

        # IMPOSTO LA FINESTRA COME FIGLIA DELLA FINESTRA GENITORE
        # SETTING THE WINDOW AS CHILD OF THE PARENT WINDOW
        self.function_2_window.set_transient_for(parent)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.icon = function_2_window_builder.get_object("function_2_icon")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.title_text = function_2_window_builder.get_object("function_2_title_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.file_path_entry = function_2_window_builder.get_object("function_2_file_path_entry")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.functions_button_box = function_2_window_builder.get_object("function_2_functions_buttons_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.open_file_button = function_2_window_builder.get_object("function_2_open_file_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.start_installation_button = function_2_window_builder.get_object("function_2_start_installation")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.exit_button_box = function_2_window_builder.get_object("function_2_exit_button_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.exit_button = function_2_window_builder.get_object("function_2_exit_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.waiting_text = function_2_window_builder.get_object("function_2_waiting_text")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.spinner_box = function_2_window_builder.get_object("function_2_spinner_box")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.spinner = function_2_window_builder.get_object("function_2_spinner")

        #-----------------------------------------------------------------------------------------------------

        # APRO LA FINESTRA DI SELEZIONE FILE ALLA PRESSIONE DEL BOTTONE
        # OPENING THE FILE CHOOSER WINDOW DIALOG WHEN THE BUTTON IS PRESSED
        self.open_file_button.connect('clicked',self.open_file)
        
        # AVVIO LA FUNZIONE DI CONTROLLO DEL FILE ALLA PRESSIONE DEL BOTTONE
        # STARTING THE FILE CHECK FUNCTION WHEN THE BUTTON IS PRESSED
        self.start_installation_button.connect('clicked',self.installation_security_check)

        # CHIUDO LA FINESTRA DELLA FUNZIONE 2 ALLA PRESSIONE DEL BOTONE
        # CLOSE THE FUNCTION 2 WINDOW WHEN THE BUTTON IS PRESSED
        self.exit_button.connect('clicked', lambda button: self.function_2_window.destroy())

        # DICHIARAZIONE PERCORSO FILE DELL'ICONA DI PRESENTAZIONE
        # DECLARING THE FILE PATH OF THE PRESENTATION ICON 
        self.icon.set_from_file(f"{icon_path}/function_icons/file.svg")

        # IMPOSTO IL TESTO ATTESA
        # SETTING THE WAITING TEXT
        self.waiting_text.set_text(_("The time needed to complete the operation will vary\ndepending on on your computer and network performance"))

        # IMPOSTO IL TESTO DEL TITOLO
        # SETTING THE TITLE TEXT
        self.title_text.set_text(_("Select the DaVinci Resolve installer file"))

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE MANDA A SCHERMO LA FINESTRA 
    # FUNCTION THAT DISPLAYS THE WINDOW
    def print_window (self):

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN THE WINDOW AND HER CHILDS
        self.function_2_window.present()





    # FUNZIONE CHE MANDA A SCHERMO IL POP-UP DI ERRORE
    # FUNCTION THAT DISPLAYS THE ERROR POP-UP
    def print_error_dialog (self, error_type, error_log):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE
        error_dialog_window = Gtk.Builder()

        # COMUNICO ALLA FUNZIONE BUILDER QUALE DIZIONARIO USARE PER TRADURRE L'INTERFACCIA
        # TELLING THE BUILDER FUNCTION THE DICTIONARY NAME TO USE FOR THE INTERFACE TRANSLATION
        error_dialog_window.set_translation_domain('davinci-helper')
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA DI ERRORE PER LA SCELTA DEL FILE
        # IMPORTING THE UI FILE THAT REPRESENT THE FILE ERROR DIALOG WINDOW
        error_dialog_window.add_from_file(f"{ui_path}/error_dialog.ui")
        
        # OTTENGO LA FINESTRA DI ERRORE PER LA SCELTA DEL FILE ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE FILE ERROR DIALOG WINDOW AND HER CHILD FROM THE UI FILE
        self.error_dialog_window = error_dialog_window.get_object("error_dialog")

        # IMPOSTO LA FINESTRA DI ERRORE PER LA SCELTA DEL FILE COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE FILE ERROR DIALOG WINDOW AS CHILD OF THE MAIN WINDOW
        self.error_dialog_window.set_transient_for(self.function_2_window)

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.exit_button = error_dialog_window.get_object("error_exit_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_button = error_dialog_window.get_object("error_log_button")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILEE
        self.error_label = error_dialog_window.get_object("error_label")

        # OTTENGO L'OGGETTO ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE OBJECT AND HIS CHILD FROM THE UI FILE
        self.log_scrolled = error_dialog_window.get_object("error_log_scrolled")

        # OTTENGO IL IL CAMPO DI TESTO DEI LOG ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE LOGS TEXT FIELD AND HER CHILD FROM THE UI FILE
        self.log_texview = error_dialog_window.get_object("error_log_text")

        # OTTENGO IL IL CAMPO DI TESTO DEI LOG ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE LOGS TEXT FIELD AND HER CHILD FROM THE UI FILE
        self.error_icon = error_dialog_window.get_object("error_icon")

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO IL BUFFER DI TESTO DAL CAMPO DI TESTO DEI LOG
        # OBATINING THE LOGS TEXT BUFFER FROM THE TEXT FIELD
        self.log_textbuffer = self.log_texview.get_buffer()

        # AVVIO LA FUNZIONE CHE MOSTRA I LOG
        # STARTING THE FUNCTION THAT SHOWS THE LOGS
        self.log_button.connect('clicked', self.show_logs, error_log)

        # CHIUDO LA FINESTRA DI ERRORE ALLA PRESSIONE DEL BOTONE
        # CLOSE THE ERROR WINDOW WHEN THE BUTTON IS PRESSED
        self.exit_button.connect('clicked', lambda button: self.error_dialog_window.destroy())

        #-----------------------------------------------------------------------------------------------------

        # CONTROLLO PER QUALE TIPOLOGIA DI ERRORE È STATO INVOCATO IL POP-UP
        # CHECK FOR WHICH TYPE OF ERROR THE POP-UP WAS INVOKED
        if error_type == "Missing":

            # CARICO IL FILE DELL'ICONA DI AVVISO
            # LOADING THE WARNING ICON FILE
            self.error_icon.set_from_file(f"{icon_path}/function_icons/warning.svg")

            # STAMPO IL MESSAGGIO DI ERRORE PER FILE MANCANTE
            # PRINTING MISSING FILE ERROR MESSAGE
            self.error_label.set_text(_("No file has been found on this path, please select a file to continue with the installation"))

        elif error_type == "Unsuitable" :

            # CARICO IL FILE DELL'ICONA DI AVVISO
            # LOADING THE WARNING ICON FILE 
            self.error_icon.set_from_file(f"{icon_path}/function_icons/warning.svg")

            # STAMPO IL MESSAGGIO DI ERRORE PER FILE NON IDONEO
            # PRINTING THE ERROR MESSAGE FOR INSUITABLE FILE
            self.error_label.set_text(_("The file you chose is not a DaVinci Resolve installation zip file. If you have renamed the file please make sure that the file name containes the words 'DaVinci', 'Resolve', 'Linux' like the original one. Please select an appropriate file to continue."))

        elif error_type == "Extraction" :

            # CARICO IL FILE DELL'ICONA DI ERRORE
            # LOADING THE ERROR ICON FILE 
            self.error_icon.set_from_file(f"{icon_path}/function_icons/error.svg")

            # STAMPO IL MESSAGGIO DI ERRORE PER ERRORE NELL'ESTRAZIONE DELL'INSTALLER
            # PRINTING THE ERROR MESSAGE FOR AN ERROR DURING THE INSTALLER EXTRACTION
            self.error_label.set_text(_("There was an error extracting the 'Name.zip' installer file. Please check the logs to have more details."))

            # MOSTRO IL PULSANTE PER APRIRE I LOG
            # SHOWING THE BUTTON TO READ THE LOGS
            self.log_button = error_dialog_window.get_object("log_button")
            self.log_button.set_visible(True)
        
        elif error_type == "Install" :

            # CARICO IL FILE DELL'ICONA DI ERRORE
            # LOADING THE ERROR ICON FILE 
            self.error_icon.set_from_file(f"{icon_path}/function_icons/error.svg")

            # STAMPO IL MESSAGGIO DI ERRORE PER ERRORE DURANTE L'AVVIO DELL'INSTALLER
            # PRINTING THE ERROR MESSAGE FOR AN ERROR DURING THE INSTALLER LAUNCH
            self.error_label.set_text(_("There was an error during the installer startup. Please check the logs to have more details."))

            # MOSTRO IL PULSANTE PER APRIRE I LOG
            # SHOWING THE BUTTON TO READ THE LOGS
            self.log_button = error_dialog_window.get_object("log_button")
            self.log_button.set_visible(True)

        else :

             # CARICO IL FILE DELL'ICONA DI ERRORE
            # LOADING THE ERROR ICON FILE
            self.error_icon.set_from_file(f"{icon_path}/function_icons/error.svg")

            # STAMPO IL MESSAGGIO DI ERRORE PER GLI ERRORI SCONOSCIUTI
            # PRINTING THE ERROR MESSAGE FOR UNKNOWN ERRORS
            self.error_label.set_text(_("There was an unknown error. Please check the logs to have more details."))
            
            # MOSTRO IL PULSANTE PER APRIRE I LOG
            # SHOWING THE BUTTON TO READ THE LOGS
            self.log_button = error_dialog_window.get_object("log_button")
            self.log_button.set_visible(True)

        #-----------------------------------------------------------------------------------------------------

        # MANDO A SCHERMO LA FINESTRA ED I SUOI CHILD
        # PRINTING TO SCREEN WINDOW AND HER CHILDS
        self.error_dialog_window.present()

        #-----------------------------------------------------------------------------------------------------

        



    # FUNZIONE CHE RENDE VISIBILE IL LOG DI ERRORE
    # FUNCTION THAT SHOWS THE ERROR LOGS
    def show_logs (self, widget, error_log):

        #-----------------------------------------------------------------------------------------------------

        # ACQUISISCO LO STATO DI VILIBILITÀ DEL CONTENITORE DEI LOG
        # ACQUIRING VIBILITY STATUS OF THE LOG CONTAINER
        current_log_visibility = self.log_scrolled.get_visible()

        #-----------------------------------------------------------------------------------------------------

        # ACQUISISCO SE LA FUNZIONE LOG È STATA GIÀ AVVIATA IN PRECEDENZA
        # ACQUIRING IF THE LOG FUNCTION WAS ALREADY STARTED
        if current_log_visibility == True :

            # NASCONDO IL CAMPO DI TESTO DEI LOG
            # HIDING THE LOGS TEXT FIELD
            self.log_scrolled.set_visible(False)

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_textbuffer.get_end_iter()
            start_iter = self.log_textbuffer.get_start_iter()

            # SVUOTO IL TEXT BUFFER DEI LOG
            # EMPTYING THE LOG TEXT BUFFER
            self.log_textbuffer.delete(start_iter, end_iter)

        else :

            # RENDO VISIBILE IL CAMPO DI TESTO DEI LOG
            # SHOWING THE LOGS TEXT FIELD
            self.log_scrolled.set_visible(True)

            # OTTENGO CIÒ CHE È STATO PRECEDENTEMENTE CARICATO NEL BUFFER DEL TESTO
            # OBTAINING WHAT WAS PREVIOUSLY ADDED TO THE TEXT BUFFER
            end_iter = self.log_textbuffer.get_end_iter()

            # AGGIUNGO IL NUOVO TESTO AL BUFER DEL TESTO DEI LOG
            # ADDING NEW TEXT TO THE LOG TEXT BUFFER
            self.log_textbuffer.insert(end_iter, error_log)

        #-----------------------------------------------------------------------------------------------------
        




    # FUNZIONE CHE APRE LA FINESTRA DI DIALOGO PER LA SELEZIONE DEL FILE
    # FUNCTION THAT OPEN THE FILE CHOOSER DIALOG WINDOW
    def open_file(self,widget):

        #-----------------------------------------------------------------------------------------------------

        # CREAZIONE DELLA FINESTRA DI DIALOGO PER LA SEZIONE DEL FILE
        # CREATING THE FILE CHOOSER DIALOG WINDOW
        file_dialog = Gtk.FileDialog.new()

        # ACQUISISCO L'OPZIONE PER FILTRARE LA TIPOLOGIA DI FILE SELEZIONABILE
        # ACQUIRING THE OPTION TO FILTER THE FILE TYPE THAT THE USER CAN CHOSE
        zip_filter = Gtk.FileFilter()

        # IMPOSTO IL NOME DELLA TIPOLOGIA DI FILE SELEZIONABILE
        # SETTING THE SELECTABLE FILE TYPE NAME
        zip_filter.set_name("Zip Files")

        # IMPOSTO L'ESTENSIONE DEL FILE SELEZIONABILE
        # SETTING THE SELECTABLE FILE TYPE EXTENSION
        zip_filter.add_pattern("*.zip")
        
        # IMPOSTO IL FILTRO NELLA FINESTRA DI SELEZIONE FILE
        # SETTING THE FILTER IN THE FILE CHOOSER DIALOG WINDOW
        file_dialog.set_default_filter(zip_filter)
        
        # MANDO A SCHERMO LA FINESTRA DI DIALOGO PER LA SELEZIONE DEL FILE,
        # PASSANDO COME LA PARAMETRI LA FINESTRA DELLA FUNZIONE DUE IN MODO CHE SIA TRANSIENTE, IL PARAMETRO NONE E LA FUNZIONE DA ESEGUIRE UNA VOLTA SELEZIONATO IL FILE
        # PRINTING TO SCREEN THE FILE CHOOSER DIALOG WINDOW, USING AS PARAMETERS
        # THE FUNCTION WINDOW (SO IT'S SETTED AS PARENT), NONE AND THE FUNCTION TO EXECUTE AFTER THE USER SELECT THE FILE
        file_dialog.open(self.function_2_window, None, self.on_file_opened)

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE VIENE ESEGUITA ALLA SCELTA DI UN FILE 
    # FUNCTION THAT IS EXECUTED WHEN A FILE IS CHOOSED
    def on_file_opened(self, file_dialog, result):

        #-----------------------------------------------------------------------------------------------------
        
        # ESEGUE SEMPRE TRANNE IN CASO DI ERRORI
        # ALWAYS EXECUTE THIS EXCEPT IF THERE ARE ERROS
        try:

            # ACQUISIZIONE DELL'OGGETTO DEL FILE SELEZIONATO
            # ACQUIRING THE OBJECT OF THE FILE SELECTED
            file = file_dialog.open_finish(result)

            # OTTENGO IL PERCORSO DEL FILE SELEZIONATO
            # ACQUIRING THE PATH OF FILE SELECTED
            file_path = file.get_path()

            # STAMPO IL PERCORSO DEL FILE SELEZIONATO NEL CAMPO DI TESTO DEL PERCORSO FILE
            # PRINTING THE FILE PATH OF THE SELECTED FILE IN THE FILE PATH TEXT FIELD
            self.file_path_entry.set_text(file_path)

        # ESEGUE QUESTO SE CI SONO DEGLI ERRORI
        # EXECUTE THIS IF THERE ARE ERRORS
        except GLib.Error as e:

            # STAMPA NEL TERMINALE IL MESSAGGIO DI ERRORE
            # PRINTING IN THE TERMINAL THE ERROR MESSAGE
            print(f"Error: {e.message}")

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE IL CONTROLLO DI IDONEITÀ DEL FILE SELEZIONATO
    # FUNCTION THAT STARTS THE ELIGIBILITY CHECK OF THE CHOOSED FILE
    def installation_security_check (self, widget):

        #-----------------------------------------------------------------------------------------------------

        # OTTENGO IL PERCORSO DEL FILE DI INSTALLAZIONE DAL CAMPO DI TESTO
        # OBTAINING THE FILE PATH FROM THE TEXT FIELD
        file_path = self.file_path_entry.get_text()

        #-----------------------------------------------------------------------------------------------------

        # CONTROLLO SE IL PERCORSO INDICATO È VUOTO
        # CHECKING IF THE FILE PATH IS EMPTY
        if len(file_path) >= 2 :

            #-----------------------------------------------------------------------------------------------------
            
            # STABILISCO I PARAMETRI CHE DEVE AVERE IL NOME DEL FILE DI INSTALLAZIONE
            # ESTABLISHING THE PARAMETERS THAT THE INSTALLATION FILE MUST HAVE
            name_check = ["DaVinci", "Resolve", "Linux", ".zip"]

            # AZZERAMENTO DELLA VARIABILE DI CONTROLLO E DEL CONTATORE
            # RESETTING THE CONTROL TRIGGER AND THE COUNTER
            check_passed = False
            counter = 0

            # CONTROLLO SE LE PAROLE DI RIFERIMENTO SONO CONTENUTE NEL NOME DEL FILE
            # CHECKING IF THE REFERENCE WORDS ARE CONTAINED IN THE FILE NAME
            for word in name_check:
                if word in file_path:
                    counter += 1
                if counter >= 4:
                    check_passed=True

            #-----------------------------------------------------------------------------------------------------

            # CONTROLLO SE LA CONDIZIONE DEL NOME È RISPETTATA
            # CHECKING IF THE NAME CONDITION IS RESPECTED
            if  check_passed == True:

                # AVVIO DELLA FUNZIONE CHE MOSTRA LA ROTELLA DI CARICAMENTO
                # STARTING THE FUNCTION THAT SHOWS THE LOADING WHEEL
                self.show_spinner()

                # AVVIO DELLA FUNZIONE CHE AVVIA L'INSTALLAZIONE DI DAVINCI RESOLVE
                # STARTING THE FUNCTION THAT STARTS THE DAVINCI RESOLVE INSTALLATION WIZARD
                threading.Thread(target=self.start_installation, args=(file_path,) ).start()

            else :
                
                # IMPOSTO L'ERRORE DI USCITA COME "FILE NON IDONEO"
                # SETTING THE EXIT ERROR AS "UNSUITABLE FILE"
                error_type = "Unsuitable"
                error_log = "Nothing to see here, all clear"

                # MANDO A SCHERMO IL POP-UP DI ERRORE 
                # PRINTING TO SCREEN THE ERROR POP-UP
                self.print_error_dialog(error_type, error_log)

            #-----------------------------------------------------------------------------------------------------

        else :

            # IMPOSTO L'ERRORE DI USCITA COME "FILE MANCANTE"
            # SETTING THE EXIT ERROR AS "MISSING FILE"
            error_type = "Missing"
            error_log = "Nothing to see here, all clear"

            # MANDO A SCHERMO IL POP-UP DI ERRORE 
            # PRINTING TO SCREEN THE ERROR POP-UP
            self.print_error_dialog(error_type, error_log)

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE DI AVVIO DELLO SCRIPT DI INSTALLAZIONE DI DAVINCI RESOLVE DAL MODULO PYTHON
    # FUNCTION THAT LAUNCH THE INSTALLATION SCRIPT OF DAVINCI RESOLVE INSTALLATION FUNCTION FROM PYTHON MODULE
    def start_installation(self, file_path):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO LA FUNZIONE DI INSTALLAZIONE
        # STARTING THE INSTALLATION FUNCTION
        error_type, error_log = installation_script(file_path)

        # AL COMPLETAMENTO DEL PROCESSO AGGIORNO LA GUI
        # ON PROCESS END UPDATE THE GUI
        GLib.idle_add(self.on_task_complete, error_type, error_log )

        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE RIPRISTINA LA FINESTRA DELLA FUNZIONE 2 UNA VOLTA CHIUSO IL WIZARD DI INSTALLAZIONE ED AVVIA IL POP-UP PER EVENTUALI ERRORI
    # FUNCTION THAT RESTORE THE FUNCTION 2 WINDOW ONCE THE INSTALLATION WIZARD IS CLOSED AND STARTS THE ERROR POP-UP IF IS NEED
    def on_task_complete(self, error_type, error_log):

        #-----------------------------------------------------------------------------------------------------

        # AVVIO DELLA FUNZIONE CHE NASCONDE LA ROTELLA DI CARICAMENTO
        # STARTING THE FUNCTION THAT HIDES THE LOADING WHEEL
        self.hide_spinner()

        # CONTROLLO SE LO SCRIPT HA RIPORTATO ERRORI
        # CHECKING IF THE SCRIPT HAS REPORTED ERRORS
        if error_type != "No":
            
            # AVVIO DELLA FUNZIONE CHE STAMPA IL POP-UP DI ERRORE
            # STARTING THE FUNCTION THAT PRINTS THE ERROR POP-UP
            self.print_error_dialog(error_type, error_log)
        
        #-----------------------------------------------------------------------------------------------------





    # FUNZIONE CHE NASCONDE GLI ELEMENTI DELL'INTERFACCIA LASCIANDO SOLO LA ROTELLA DI CARICAMENTO
    # FUNCTION THAT HIDES ALL THE UI ELEMENTS AND SHOWS ONLY THE LOADING WHEEL
    def show_spinner (self):

        #-----------------------------------------------------------------------------------------------------

        # NASCONDO L'ICONA
        # HIDING THE ICON
        self.icon.set_visible(False)

        # NASCONDO IL TESTO DI TITOLO
        # HIDING THE TITLE TEXT
        self.title_text.set_visible(False)

        # NASCONDO IL CAMPO DI TESTO
        # HIDING THE TEXT FIELD
        self.file_path_entry.set_visible(False)

        # NASCONDO IL BOX DEI BOTTONI FUNZIONE
        # HIDIG THE FUNCTIONS BUTTONS BOX
        self.functions_button_box.set_visible(False)

        # NASCONDO IL BOX DEL BOTTONE DI USCITA
        # HIDING THE EXIT BUTTON BOX
        self.exit_button_box.set_visible(False)

        #-----------------------------------------------------------------------------------------------------

        # MOSTRO IL BOX DELLO SPINNER
        # SHOWING THE SPINNER BOX
        self.spinner_box.set_visible(True)

        # AVVIO LO SPINNER
        # STARTING THE SPINNER
        self.spinner.start()

        #-----------------------------------------------------------------------------------------------------




    
    # FUNZIONE CHE NASCONDE LA ROTELLA DI CARICAMENTO E MOSTRA TUTTI GLI ALTRI ELEMENTI DELL'INTERFACCIA
    # FUNCTION THAT HIDES THE LOADING WHEEL AND SHOW ALL THE UI ITEMS
    def hide_spinner(self):
        #-----------------------------------------------------------------------------------------------------
        
        # MOSTRO L'ICONA
        # SHOWING THE ICON
        self.icon.set_visible(True)

        # MOSTRO IL TESTO DI TITOLO
        # SHOWING THE TITLE TEXT
        self.title_text.set_visible(True)

        # MOSTRO IL CAMPO DI TESTO
        # SHOWING THE TEXT FIELD
        self.file_path_entry.set_visible(True)

        # MOSTRO IL BOX DEI BOTTONI FUNZIONE
        # SHOWING THE FUNCTIONS BUTTONS BOX
        self.functions_button_box.set_visible(True)

        # MOSTRO IL BOX DEL BOTTONE DI USCITA
        # SHOWING THE EXIT BUTTON BOX
        self.exit_button_box.set_visible(True)

        #-----------------------------------------------------------------------------------------------------

        # NASCONDO IL BOX DELLO SPINNER
        # HIDING THE SPINNER BOX
        self.spinner_box.set_visible(False)

        # FERMO LO SPINNER
        # STOPPING THE SPINNER
        self.spinner.stop()

        #-----------------------------------------------------------------------------------------------------
        