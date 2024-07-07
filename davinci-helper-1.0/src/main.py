# main.py
#
# Copyright 2024 Lorenzo Maiuri
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

#-------------------------------------------------------------------------------
#                 INIZIO DEL PROGRAMMA / THE SOFTWARE STARTS HERE
#-------------------------------------------------------------------------------



# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, time, subprocess, fcntl

# IMPORTAZIONE DEI MODULI PER LE FUNZIONI DI INFO
# INFO FUNCTION MODULES IMPORT
from functions.function_1_GUI import build_function_1

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib



'''
# Funzione per stampare il contenuto delle directory
def list_directory_contents(directory_path):
    try:
        with os.scandir(directory_path) as entries:
            print(f"Contenuto della directory {directory_path}:")
            for entry in entries:
                if entry.is_file():
                    print(f"  File: {entry.name}")
                elif entry.is_dir():
                    print(f"  Directory: {entry.name}")
    except FileNotFoundError:
        print(f"Errore: la directory {directory_path} non esiste.")
    except PermissionError:
        print(f"Errore: permesso negato per la directory {directory_path}.")

# Ottieni il percorso assoluto del file corrente
current_file_path = os.path.abspath(__file__)

# Ottieni la directory del file corrente
current_dir_path = os.path.dirname(current_file_path)

# Stampa i percorsi
print(f"Percorso del file corrente: {current_file_path}")
print(f"Directory del file corrente: {current_dir_path}")

# Stampa il contenuto della directory corrente e della directory data
list_directory_contents(current_dir_path)
'''



#
#
current_directory = os.path.dirname(os.path.abspath(__file__))

#
#
css_path = os.path.join(current_directory, '..', 'data', 'css')

#
#
ui_path = os.path.join(current_directory, '..', 'data', 'ui')

#
#
icon_path = os.path.join(current_directory, '..', 'data', 'icons')

#
#
po_path = os.path.join(current_directory, '..', 'po')





# IMPORTO IL FILE CSS PER LA DEFINIZIONE DEGLI STILI
# IMPORTING THE CSS FILE FOR STYLES DEFINITION
css_provider = Gtk.CssProvider()
css_provider.load_from_path(f'{css_path}/style-dark.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)






# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA PRINCIPALE
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE MAIN WINDOW
class build_main_window(Adw.Application):

    # IMPORTO GLI ATTRIBUTI E METODI DELLA CLASSE MADRE A"DW.APPLICATION" UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # RICHIAMO LA FUNZIONE "CONNECT" UTILIZZANDO COME PARAMETRI "ACTIVATE" E LA FUNZIONE DI GENERAZIONE DELLA FINESTRA PRINCIPALE
        # CALLING THE CONNECT FUNCTION USING AS PARAMETERS "ACTIVATE" AND THE MAIN WINDOW CREATOR FUNCTION
        self.connect('activate', self.main_window_activation)




    # AVVIO DELLA FUNZIONE CHE GENERA LA FINESTRA PRINCIPALE E LA MANDA A SCHERMO
    # STARTING THE FUNCTION THAT CREATES THE MAIN WINDOW AND DIPLAYS IT
    def main_window_activation (self, app):


        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA PRINCIPALE
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE MAIN WINDOW
        main_window_builder = Gtk.Builder()

		# IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA PRINCIPALE
		# IMPORTING THE UI FILE THAT REPRESENT THE MAIN WINDOW
        main_window_builder.add_from_file(f"{ui_path}/main_window.ui")

        # OTTENGO LA FINESTRA PRINCIPALE ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE MAIN WINDOW AND HER CHILD FROM THE UI FILE
        self.main_window = main_window_builder.get_object("main_window")

        # DICHIARAZIONE PERCORSO FILE DELL'ICONA 1
        # DECLARING THE FILE PATH OF ICON 1 
        self.icon_1 = main_window_builder.get_object("icon_1")
        self.icon_1.set_from_file(f"{icon_path}/icons_main/F1.png")

        # DICHIARAZIONE PERCORSO FILE DELL'ICONA 2
        # DECLARING THE FILE PATH OF ICON 2 
        self.icon_2 = main_window_builder.get_object("icon_2")
        self.icon_2.set_from_file(f"{icon_path}/icons_main/F2.png")

        # DICHIARAZIONE PERCORSO FILE DELL'ICONA 3
        # DECLARING THE FILE PATH OF ICON 3 
        self.icon_3 = main_window_builder.get_object("icon_3")
        self.icon_3.set_from_file(f"{icon_path}/icons_main/F3.png")

        # DICHIARAZIONE PERCORSO FILE DELL'ICONA 4
        # DECLARING THE FILE PATH OF ICON 4 
        self.icon_4 = main_window_builder.get_object("icon_4")
        self.icon_4.set_from_file(f"{icon_path}/icons_main/F4.png")

        # IMPOSTO LA FINESTRA PRINCIPALE PER FAR CHIUDERE IL PROGRAMMA ALLA CHIUSURA DELLA FINESTRA
        # SETTING THE MAIN WINDOW TO CLOSE THE APP AFTER ALL APP WINDOWS ARE CLOSED
        self.main_window.set_application(self)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.main_window.present()










        # OTTENGO IL BOTTONE INFO 1 DAL FILE UI
        # OBTAINING THE INFO BUTTON 1 FROM THE UI FILE
        self.function_button_1 = main_window_builder.get_object("function_button_1")

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 1
        # OPEN THE INFO WINDOW OF FUNCTION 1
        self.function_button_1.connect('clicked', self.function_1_window_activation)










    




        # OTTENGO IL BOTTONE INFO 1 DAL FILE UI
        # OBTAINING THE INFO BUTTON 1 FROM THE UI FILE
        self.info_button_1 = main_window_builder.get_object("info_button_1")

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 1
        # OPEN THE INFO WINDOW OF FUNCTION 1
        self.info_button_1.connect('clicked', self.info_window_1_activation)

        # OTTENGO IL BOTTONE INFO 2 DAL FILE UI
        # OBTAINING THE INFO BUTTON 2 FROM THE UI FILE
        self.info_button_2 = main_window_builder.get_object("info_button_2")

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 2
        # OPEN THE INFO WINDOW OF FUNCTION 2
        self.info_button_2.connect('clicked', self.info_window_2_activation)

        # OTTENGO IL BOTTONE INFO 3 DAL FILE UI
        # OBTAINING THE INFO BUTTON 3 FROM THE UI FILE
        self.info_button_3 = main_window_builder.get_object("info_button_3")

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 3
        # OPEN THE INFO WINDOW OF FUNCTION 3
        self.info_button_3.connect('clicked', self.info_window_3_activation)

        # OTTENGO IL BOTTONE INFO 4 DAL FILE UI
        # OBTAINING THE INFO BUTTON 4 FROM THE UI FILE
        self.info_button_4 = main_window_builder.get_object("info_button_4")

        # APRI LA FINESTRA DI INFO DELLA FUNZIONE 4
        # OPEN THE INFO WINDOW OF FUNCTION 4
        self.info_button_4.connect('clicked', self.info_window_4_activation)

        



        








    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 1
    # FUNCTION THAT SHOWS THE FUNCTION 1 WINDOW
    def function_1_window_activation (self, widget):
        
        # GENERO LA FINESTRA FUNZIONE 1 USANDO LA CLASSE APPOSITA E PASSANDO LA FINESTRA PRINCIPALE COME RIFERIMENTO
        # CREATING THE FUNCTION 1 WINDOW USING HER CLASS AND GIVING THE MAIN WINDOW AS REFERENCE
        function_window_1 = build_function_1(self.main_window)
        
        # MANDO A SCHERMO LA FINESTRA DELLA FUNZIONE 1 ED I SUOI CHILD
        # PRINTING TO SCREEN THE FUNCTION 1 WINDOW AND HER CHILDS
        function_window_1.print_window()
        function_window_1.function_1()

















    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DELLA FUNZIONE 1
    # FUNCTION THAT SHOW THE WINDOW OF THE FUNCTION 1
    def info_window_1_activation (self, widget):

        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA INFO 1
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE INFO WINDOW 1
        info_1_window_builder = Gtk.Builder()
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA INFO 1
		# IMPORTING THE UI FILE THAT REPRESENT THE INFO WINDOW 1
        info_1_window_builder.add_from_file(f"{ui_path}/info_function_1.ui")
        
        # OTTENGO LA FINESTRA DI INFO 1 ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE INFO WINDOW 1 AND HER CHILD FROM THE UI FILE
        info_window_1 = info_1_window_builder.get_object("info_window_1")

        # IMPOSTO LA FINESTRA DI INFO 1 COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE INFO WINDOW 1 AD CHILD OF THE MAIN WINDOW
        info_window_1.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        info_window_1.present()

        # OTTENGO IL BOTTONE OK 1 DAL FILE UI
        # OBTAINING THE OK BUTTON 1 FROM THE UI FILE
        self.ok_button_1 = info_1_window_builder.get_object("ok_button_1")

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.ok_button_1.connect('clicked', lambda button: info_window_1.destroy())


    
    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DI INFO DELLA FUNZIONE 2
    # FUNCTION THAT SHOW THE INFO WINDOW OF THE FUNCTION 2
    def info_window_2_activation (self, widget):

        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA INFO 2
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE INFO WINDOW 2
        info_2_window_builder = Gtk.Builder()
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA INFO 2
		# IMPORTING THE UI FILE THAT REPRESENT THE INFO WINDOW 2
        info_2_window_builder.add_from_file(f"{ui_path}/info_function_2.ui")
        
        # OTTENGO LA FINESTRA DI INFO 2 ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE INFO WINDOW 2 AND HER CHILD FROM THE UI FILE
        info_window_2 = info_2_window_builder.get_object("info_window_2")

        # IMPOSTO LA FINESTRA DI INFO 2 COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE INFO WINDOW 2 AD CHILD OF THE MAIN WINDOW
        info_window_2.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        info_window_2.present()

        # OTTENGO IL BOTTONE OK 2 DAL FILE UI
        # OBTAINING THE OK BUTTON 2 FROM THE UI FILE
        self.ok_button_2 = info_2_window_builder.get_object("ok_button_2")

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.ok_button_2.connect('clicked', lambda button: info_window_2.destroy())



    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DI INFO DELLA FUNZIONE 3
    # FUNCTION THAT SHOW THE INFO WINDOW OF THE FUNCTION 3
    def info_window_3_activation (self, widget):

        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA INFO 3
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE INFO WINDOW 3
        info_3_window_builder = Gtk.Builder()
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA INFO 3
		# IMPORTING THE UI FILE THAT REPRESENT THE INFO WINDOW 3
        info_3_window_builder.add_from_file(f"{ui_path}/info_function_3.ui")
        
        # OTTENGO LA FINESTRA DI INFO 3 ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE INFO WINDOW 3 AND HER CHILD FROM THE UI FILE
        info_window_3 = info_3_window_builder.get_object("info_window_3")

        # IMPOSTO LA FINESTRA DI INFO 3 COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE INFO WINDOW 3 AD CHILD OF THE MAIN WINDOW
        info_window_3.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        info_window_3.present()

        # OTTENGO IL BOTTONE OK 3 DAL FILE UI
        # OBTAINING THE OK BUTTON 3 FROM THE UI FILE
        self.ok_button_3 = info_3_window_builder.get_object("ok_button_3")

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED%py3_install
        self.ok_button_3.connect('clicked', lambda button: info_window_3.destroy())



    # FUNZIONE CHE MOSTRA SCHERMO LA FINESTRA DI INFO DELLA FUNZIONE 4
    # FUNCTION THAT SHOW THE INFO WINDOW OF THE FUNCTION 4
    def info_window_4_activation (self, widget):

        
        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA INFO 4
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE INFO WINDOW 4
        info_4_window_builder = Gtk.Builder()
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA INFO 4
		# IMPORTING THE UI FILE THAT REPRESENT THE INFO WINDOW 4
        info_4_window_builder.add_from_file(f"{ui_path}/info_function_4.ui")
        
        # OTTENGO LA FINESTRA DI INFO 4 ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE INFO WINDOW 4 AND HER CHILD FROM THE UI FILE
        info_window_4 = info_4_window_builder.get_object("info_window_4")

        # IMPOSTO LA FINESTRA DI INFO 4 COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE INFO WINDOW 4 AD CHILD OF THE MAIN WINDOW
        info_window_4.set_transient_for(self.main_window)

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        info_window_4.present()

        # OTTENGO IL BOTTONE OK 4 DAL FILE UI
        # OBTAINING THE OK BUTTON 4 FROM THE UI FILE
        self.ok_button_4 = info_4_window_builder.get_object("ok_button_4")

        # CHIUDO LA FINESTRA DI INFO ALLA PRESSIONE DEL BOTONE
        # CLOSE THE INFO WINDOW WHEN THE BUTTON IS PRESSED
        self.ok_button_4.connect('clicked', lambda button: info_window_4.destroy())





#
#
def main():


    # ASSEGNANAZIONE DELL'ID DEL PROGRAMMA E COPIA DELLA CLASSE DELLA FINESTRA PRINCIPALE NELLA VARIABILE CHE RAPPRESENTA LA FINESTRA DEL PROGRAMMA
    # ASSIGNING THE APP ID AND COPY OF THE MAIN WINDOW CLASS IN A VARIABLE
    app_gui = build_main_window(application_id="com.davinci.helper.app")

    # AVVIO DELLA FINESTRA PRINCIPALE
    # STARTING THE MAIN WINDOW
    app_gui.run(sys.argv)





#------------------------------------------------------

if __name__ == '__main__':
    
    main()

    #input("inserisci qualcosa per andare avanti")