# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULE IMPORT
import sys, gi, os, subprocess, time, threading

# RICHIESTA DELLE VERSIONI DI GTK ED ADWAITA
# REQUESTING THE CHOOSEN VERSION OF GTK AND ADWAITA
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# IMPORTO I MODULI NECESSARI
# IMPORTING THE NECESSARY MODULES
from gi.repository import Gtk, Adw, Gdk, Pango, Gio, GLib





# DEFINISCO LA CLASSE CHE PERMETTE LA CREAZIONE E MESSA SCHERMO DELLA FINESTRA DELLA FUNZIONE 1
# DEFINING THE CLASS WHO CREATES AND DISPLAYS THE FUNCTION 1 WINDOW
class build_function_1 ():

    # IMPORTO GLI ATTRIBUTI E METODI DELLA CLASSE MADRE A"DW.APPLICATION" UTILIZZANDO LA FUNZIONE INIT E LA SUPERCLASSE
    # IMPORTING ATTRIBUTE AND METHODS FROM THE MAIN CLASS "ADW.APPLICATION" USING THE INIT FUNCTION AND THE SUPERCLASS
    def __init__(self, parent):

        # AVVIO LA FUNZIONE BUILDER PER LEGGERE IL FILE UI DELLA FINESTRA INFO 1
        # STARTING THE BUILDER FUNCTION TO READ THE UI FILE OF THE INFO WINDOW 1
        function_1_window_builder = Gtk.Builder()
        
        # IMPORTO IL FILE UI CHE RAPPRESENTA LA FINESTRA INFO 1
		# IMPORTING THE UI FILE THAT REPRESENT THE INFO WINDOW 1
        function_1_window_builder.add_from_file("../data/ui/function_1.ui")
        
        # OTTENGO LA FINESTRA DI INFO 1 ED I SUOI CHILD DAL FILE UI
        # OBTAINING THE INFO WINDOW 1 AND HER CHILD FROM THE UI FILE
        self.function_window_1 = function_1_window_builder.get_object("function_1_window")

        # IMPOSTO LA FINESTRA DI INFO 1 COME FIGLIA DELLA FINESTRA PRINCIPALE
        # SETTING THE INFO WINDOW 1 AD CHILD OF THE MAIN WINDOW
        self.function_window_1.set_transient_for(parent)

        

        # OTTENGO IL CAMPO DI TESTO DEL TERMINALE DAL FILE UI
        # OBTAINING THE TERMINAL TEXT FIELD FROM THE UI FILE
        self.terminal_textview_1 = function_1_window_builder.get_object("terminal_text_1")
        
        #
        #
        self.terminal_textbuffer_1 = self.terminal_textview_1.get_buffer()
        


    #
    #
    def print_window (self):

        # MANDO A SCHERMO LA FINESTRA PRINCIPALE ED I SUOI CHILD
        # PRINTING TO SCREEN THE MAIN WINDOW AND HER CHILDS
        self.function_window_1.present()

    







    #
    #
    def add_text(self, text):

        GLib.idle_add(self._add_text, text)


    #
    #
    def _add_text(self, text):

        #
        #
        end_iter = self.terminal_textbuffer_1.get_end_iter()

        #
        #
        self.terminal_textbuffer_1.insert(end_iter, text)









    #
    #
    def function_1 (self):

        
        
        #
        #
        def search_libs_38_39_40 (fedora_version):

             # LETTURA DELLA LISTA DELLE LIBRERIE INSTALLATE
            # READING INSTALLED LIBRARY LIST
            library_list_output = subprocess.Popen("pkexec dnf list installed | grep lib", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            library_list, library_list_err = library_list_output.communicate()
            


            

















           
            
            # AGGIUNGO ALLA LISTA DI STAMPA LA VERSIONE DI FEDORA UTILIZZATA
            # ADDING TO THE PRINTING LIST THE FEDORA VERSION USED BY THE USER
            print_fedora = "You are using " + fedora_version + "\n"

            # STAMPA IL TESTO DELLA VARIABIE DUMMY NELLA GUI
            # PRINTING "DUMMY" TEXT INSIDE THE GUI TEXTVIEW 
            self.add_text(print_fedora)


            
            
            # CONTROLLO SE LE LIBRERIE NECESSARIE SONO INSTALLATE
            # CHECKING IF ALL THE LIBRARIES NEEDED ARE INSTALLED
            lib_to_install = ""
            
            # CERCO libxcrypt-compat
            # SEARCHING FOR libxcrypt-compat
            if library_list.find('libxcrypt-compat') == -1 :
                lib_to_install = lib_to_install + " libxcrypt-compat"
            
            # CERCO libcurl
            # SEARCHING FOR libcurl
            if library_list.find('libcurl') == -1 :
                lib_to_install = lib_to_install + " libcurl"
            
            # CERCO libcurl-devel
            # SEARCHING FOR libcurl-devel
            if library_list.find('libcurl-devel') == -1 :
                lib_to_install = lib_to_install + " libcurl-devel"
            
            # CERCO mesa-libGLU
            # SEARCHING FOR mesa-libGLU
            if library_list.find('mesa-libGLU') == -1 :
                lib_to_install = lib_to_install + " mesa-libGLU"
            
            # CERCO zlib-ng-compat
            # SEARCHING FOR zlib-ng-compat
            if library_list.find('zlib') == -1 :
                lib_to_install = lib_to_install + " zlib"
            
            

            # CONTROLLO SE CI SONO DELLE LIBRERIE MANCANTI
            # CHEKING IF THERE ARE MISSING LIBRARIES
            if lib_to_install != "" :
                
                # AGGIUNGO ALLA LISTA DI STAMPA LE LIBRERIE CHE VERRANNO INSTALLATE
                # ADDING TO THE PRINTING LIST THE LIBRARIES THAT WILL BE INSTALLED
                output_before_install = "The following packages will be installed" + lib_to_install + "\n"
                print("ciao")
                
                # STAMPA IL TESTO DELLA VARIABIE DUMMY NELLA GUI
                # PRINTING "DUMMY" TEXT INSIDE THE GUI LABEL
                self.add_text(output_before_install)
                print(output_before_install)

                
                # INSTALLAZIONE DELLE LIBRERIE MANCANTI
                # INSTALLING MISSING LIBRARIES
                subprocess.Popen(f"pkexec dnf update", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                lib_installation_output = subprocess.Popen(f"pkexec dnf install -y {lib_to_install}", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                lib_installation, lib_installation_err = lib_installation_output.communicate()

                
                self.add_text("\n" + lib_installation)



                #
                #
                exit_message = "\n\nCongratulation, you have successfully completed the pre-installation phase.\nAll the needed dependencies have been installed.\nNow you can proceed to install Davinci Resolve."
                

                # STAMPA IL TESTO DELLA VARIABIE DUMMY NELLA GUI
                # PRINTING "DUMMY" TEXT INSIDE THE GUI LABEL
                self.add_text(exit_message)

                
            else :
                
                no_install = "\n\nCongratulation, you have successfully completed the pre-installation phase.\nThere was nothing to install or update on your system.\nNow you can proceed to install Davinci Resolve."
                self.add_text(no_install)
            


                   
        

       #------------------------------------------------------------------------------------------------------------------------------------------------

        

        # LETTURA DELLA VERSIONE DI FEDORA INSTALLATA
        # READING WHICH VERSION OF FEDORA IS INSTALLED
        fedora_version_output = subprocess.Popen("cat /etc/fedora-release", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        

        #
        #
        fedora_version = fedora_version_output.stdout.readline()
        print(fedora_version)

        

 



        # CONTROLLO SE È INSTALLATO FEDORA 38
        # CHECKING IF IS INSTALLED FEDORA 38
        if fedora_version.find("38") != -1 :
            
            #
            #
            #lib_output = search_libs_38_39_40(library_list, fedora_version)
            # Create and start a new thread to run the target function
            thread = threading.Thread(target=search_libs_38_39_40(fedora_version))
            thread.start()

            


        # CONTROLLO SE È INSTALLATO FEDORA 39
        # CHECKING IF IS INSTALLED FEDORA 39
        elif fedora_version.find("39") != -1 :

            #
            #
            #lib_output = search_libs_38_39_40(library_list, fedora_version)
            thread = threading.Thread(target=search_libs_38_39_40(fedora_version))
            thread.start()



        # CONTROLLO SE È INSTALLATO FEDORA 40
        # CHECKING IF IS INSTALLED FEDORA 40
        elif fedora_version.find("40") != -1 :

            #
            #
            #lib_output = search_libs_38_39_40(library_list, fedora_version)
            thread = threading.Thread(target=search_libs_38_39_40(fedora_version))
            thread.start()

            

        

        

        