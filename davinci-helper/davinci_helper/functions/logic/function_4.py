#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# ERROR TAB :
# EXIT 1 - IT WAS IMPOSSIBLE TO FIND A SUPPORTED GPU INSIDE THE SYSTEM
# EXIT 2 - IT WAS IMPOSSIBLE TO ADD THE RPM FUSION REPOSITORY
# EXIT 3 - IT WAS IMPOSSIBLE TO INSTALL THE GPU DRIVER

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, re

#-----------------------------------------------------------------------------------------------------

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale") 

# DEFINING THE SUPPORTED GPU LIST FILE 
gpu_database_path = os.path.join("//usr/share/davinci-helper/data/gpu_support")

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



# FUNCTION THAT FINDS THE GPU VENDOR
def find_gpu_vendor ():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING THE GPU VENDOR
    gpu_lspci = subprocess.run("lspci | grep -i vga", shell=True, capture_output=True, text=True )

    # MAKING LOWERCASE ALL THE STRING CHARACTER
    gpu_lspci = gpu_lspci.stdout.lower()

    # RESETTING THE COUNTER
    gpu_vendor = ""

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THE VENDOR IS NVIDIA
    if gpu_lspci.find("nvidia") != -1 :

        # SALVO IL PRODUTTORE DELLA GPU
        # SAVING THE GPU VENDOR
        gpu_vendor = " nvidia"
    
    # CHECKING IF THE VENDOR IS AMD
    if gpu_lspci.find("amd") != -1 :

        # SAVING THE GPU VENDOR
        gpu_vendor =  gpu_vendor + " amd"

    # CHECKING IF THE VENDOR IS INTEL
    if gpu_lspci.find("intel") != -1 :

        # SALVO IL PRODUTTORE DELLA GPU
        # SAVING THE GPU VENDOR
        gpu_vendor =  gpu_vendor + " intel"

    #-----------------------------------------------------------------------------------------------------

    # DELETING START AND END SPACES FROM THE STRING
    gpu_vendor = gpu_vendor.strip()

    # RETURNING TO THE APP THE VENDOR NAMES AND THE LSPCI OUTPUT
    return gpu_lspci, gpu_vendor

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT EXTRACTS GPU NAME FROM LSPCI
def extract_gpu_model_name(gpu_lspci):

    #-----------------------------------------------------------------------------------------------------

    # EXTRACTING THE GPU FROM THE [ ] BRACKETS
    gpu_model_name_list = re.findall(r'\[(.*?)\]', gpu_lspci)

    # RETURNING TO THE APP THE GPU MODEL NAME
    return gpu_model_name_list

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT EXTRACTS THE NUMERIC GPU NAME FROM LSPCI
def extract_gpu_model_number (gpu_lspci):

    #-----------------------------------------------------------------------------------------------------

    # EXTRACTING THE GPUS FROM THE [ ] BRACKETS
    square_brackets_output = re.findall(r'\[(.*?)\]', gpu_lspci)

    # RESETTING THE NUMERIC GPUS NAMES LIST
    gpu_model_number_list = []

    # EXTRACTING THE NUMERIC GPUS NAMES
    for item in square_brackets_output :

        gpu_model_number_list.extend(re.findall(r'\d+',item))

    # RETURNING TO THE APP THE GPU NUMERIC MODEL NAME
    return gpu_model_number_list

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT START THE RESERCH OF WHICH GPU MODEL IS IN USE
def start_gpu_support_search(gpu_vendor, gpu_model_name_list, gpu_model_number_list):

    #-----------------------------------------------------------------------------------------------------

    # RESETTING THE COUNTERS
    gpu_supported_nvidia = False
    gpu_supported_amd = False
    gpu_supported_intel = False

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THE VENDOR IS NVIDIA
    if gpu_vendor.find("nvidia") != -1 :

        # CHECKING IF THE GPU IS SUPPORTED
        gpu_supported_nvidia = check_nvidia_gpu_support(gpu_model_name_list, gpu_model_number_list)
    
    # CHECKING IF THE VENDOR IS AMD
    if gpu_vendor.find("amd") != -1 :

        # CHECKING IF THE GPU IS SUPPORTED
        gpu_supported_amd = check_amd_gpu_support(gpu_model_name_list, gpu_model_number_list)

    # CHECKING IF THE VENDOR IS INTEL
    if gpu_vendor.find("intel") != -1 :

        # CHECKING IF THE GPU IS SUPPORTED
        gpu_supported_intel = check_intel_gpu_support(gpu_model_name_list ,gpu_model_number_list)

    #-----------------------------------------------------------------------------------------------------

    # RETURNING TO THE APP IF THE GPUs ARE SUPPORTED  
    return gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel

    #-----------------------------------------------------------------------------------------------------

        



# FUNCTION THAT FINDS IF THE NVIDIA GPU IS COMPATIBLE
def check_nvidia_gpu_support (gpu_model_name_list, gpu_model_number_list):
    
    #-----------------------------------------------------------------------------------------------------

    # AZZERO I CONTATORI
    # RESETTING THE COUNTERS
    gpu_supported_nvidia = False

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF ANY OF THE FOUND GPU IN THE SYSTEM IS COMPATIBLE
    # FINDING THE GPU NAME ASSOCIETED TO THE COMPATIBLE GPU NUMERIC NAME
    # IT IS NECESSARY TO DO THIS CROSS CHECK BECAUSE FILTERING THE SQUARE BRACKETS [ ] MAY FIND INCORRECT STRINGS, THANK YOU AMD
  
    # SLIDING THE GPU NAME LIST
    for gpu_name in gpu_model_name_list :

        # SLIDING THE GPU NUMERIC NAME LIST
        for gpu_number in gpu_model_number_list :

            # REAGING ONE LINE AT TIME THE COMPATIBLE GPU LIST
            with open(f"{gpu_database_path}/nvidia_support.txt", 'r', encoding='utf-8') as file :
                for line in file:

                    # CHECKING IF THE GPU NAME IS PRESENT INSIDE THE SUPPORTED GPU LIST AND IF IT MATCHES THE GPU NUMERIC NAME FOUND AS COMPATIBLE
                    if ((re.search(r"\bgtx\b", gpu_name, re.IGNORECASE) or re.search(r"\brtx\b", gpu_name, re.IGNORECASE) or re.search(r"\bvquadro\b", gpu_name, re.IGNORECASE)) and (re.search(r"\bGTX\b", line, re.IGNORECASE) or re.search(r"\bRTX\b", line, re.IGNORECASE) or re.search(r"\bQUADRO\b", line, re.IGNORECASE)) and re.search(rf"\b{re.escape(gpu_number)}\b", line)):

                        # PRINTING THE GPU MODEL FOUND AS COMPATIBLE
                        gpu_name = gpu_name.upper()
                        print(_("A compatible Nvidia GPU was found : {gpu_name_placeholder}").format(gpu_name_placeholder = gpu_name))
                        print("")

                        # SETTING AD FOUND A SUPPORTED NVIDIA GPU
                        gpu_supported_nvidia = True

                        # EXTING THE CICLE IN A SECURE WAY
                        break

    #-----------------------------------------------------------------------------------------------------

    # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
    return gpu_supported_nvidia

    #-----------------------------------------------------------------------------------------------------           

        



# FUNCTION THAT FINDS IF THE AMD GPU IS COMPATIBLE
def check_amd_gpu_support (gpu_model_name_list, gpu_model_number_list):

    #-----------------------------------------------------------------------------------------------------

    # AZZERO I CONTATORI
    # RESETTING THE COUNTERS
    gpu_supported_amd = False
    
    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF ANY OF THE FOUND GPU IN THE SYSTEM IS COMPATIBLE
    # FINDING THE GPU NAME ASSOCIETED TO THE COMPATIBLE GPU NUMERIC NAME
    # IT IS NECESSARY TO DO THIS CROSS CHECK BECAUSE FILTERING THE SQUARE BRACKETS [ ] MAY FIND INCORRECT STRINGS, THANK YOU AMD
    
    # SLIDING THE GPU NAME LIST
    for gpu_name in gpu_model_name_list :

        # SLIDING THE GPU NUMERIC NAME LIST
        for gpu_number in gpu_model_number_list :
            
            # REAGING ONE LINE AT TIME THE COMPATIBLE GPU LIST
            with open(f"{gpu_database_path}/amd_support.txt", 'r', encoding='utf-8') as file :
            
                for line in file:
                    
                    # CHECKING IF THE GPU NAME IS PRESENT INSIDE THE SUPPORTED GPU LIST AND IF IT MATCHES THE GPU NUMERIC NAME FOUND AS COMPATIBLE
                    if ((re.search(r"\brx\b", gpu_name, re.IGNORECASE) or re.search(r"\bvega\b", gpu_name, re.IGNORECASE)) and (re.search(r"\bRX\b", line, re.IGNORECASE) or re.search(r"\bVEGA\b", line, re.IGNORECASE)) and re.search(rf"\b{re.escape(gpu_number)}\b", line)):

                        # PRINTING THE GPU MODEL FOUND AS COMPATIBLE
                        gpu_name = gpu_name.upper()
                        print(_("A compatible AMD GPU was found : {gpu_name_placeholder}").format(gpu_name_placeholder = gpu_name))
                        print("")

                        # SETTING AD FOUND A SUPPORTED AMD GPU
                        gpu_supported_amd = True

                        # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
                        return gpu_supported_amd

                        # EXTING THE CICLE IN A SECURE WAY
                        break
                    
            
    #-----------------------------------------------------------------------------------------------------
    
    # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
    return gpu_supported_amd

    #-----------------------------------------------------------------------------------------------------
    




# FUNCTION THAT FINDS IF THE INTEL GPU IS COMPATIBLE
def check_intel_gpu_support (gpu_model_name_list, gpu_model_number_list):
    
    #-----------------------------------------------------------------------------------------------------

    # RESETTING THE COUNTERS
    gpu_supported_intel = False

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF ANY OF THE FOUND GPU IN THE SYSTEM IS COMPATIBLE
    # FINDING THE GPU NAME ASSOCIETED TO THE COMPATIBLE GPU NUMERIC NAME
    # IT IS NECESSARY TO DO THIS CROSS CHECK BECAUSE FILTERING THE SQUARE BRACKETS [ ] MAY FIND INCORRECT STRINGS, THANK YOU AMD

    # SLIDING THE GPU NAME LIST
    for gpu_name in gpu_model_name_list :

        # SLIDING THE GPU NUMERIC NAME LIST
        for gpu_number in gpu_model_number_list :

            # REAGING ONE LINE AT TIME THE COMPATIBLE GPU LIST
            with open(f"{gpu_database_path}/intel_support.txt", 'r', encoding='utf-8') as file :
                for line in file:

                    # CHECKING IF THE GPU NAME IS PRESENT INSIDE THE SUPPORTED GPU LIST AND IF IT MATCHES THE GPU NUMERIC NAME FOUND AS COMPATIBLE
                    if ((re.search(r"\barc\b", gpu_name, re.IGNORECASE)) and (re.search(r"\bARC\b", line, re.IGNORECASE)) and re.search(rf"\b{re.escape(gpu_number)}\b", line)):

                        # PRINTING THE GPU MODEL FOUND AS COMPATIBLE
                        gpu_name = gpu_name.upper()
                        print(_("A compatible Intel GPU was found : {gpu_name_placeholder}").format(gpu_name_placeholder = gpu_name))
                        print("")

                        # SETTING AD FOUND A SUPPORTED INTEL GPU
                        gpu_supported_intel = True

                        # EXTING THE CICLE IN A SECURE WAY
                        break

    #-----------------------------------------------------------------------------------------------------

    # RETURNING TO THE APP IF THERE ARE SUPPORTED GPUs 
    return gpu_supported_intel

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT PRINTS THE ERROR MESSAGE IF THE APP HAS NOT FOUND A COMPATIBLE GPU
def check_supported_gpu_presence(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel):

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THERE ISN'T A COMPATIBLE GPU
    if gpu_supported_nvidia == False and gpu_supported_amd == False and gpu_supported_intel == False :

        # STAMPO IL MESSAGGIO DI ERRORE
        # PRINTING THE ERROR MESSAGE
        print(_("DEBUG : No supported GPU has been found inside your system."))
        print(_("If you know that you have a DaVinci Resolve compatible GPU,"))
        print(_("please open an issue and paste this error code on the project GitHub page :"))
        print("")
        print("https://github.com/H3rz3n/davinci-helper/issues")
        print("")
        exit(1)
    
    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT ADDS THE RPM FUSION REPOSITORY
def add_repository():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF RPM FUSION REPO IS ALREADY INSTALLED
    rpm_fusion_repo_check = subprocess.run("dnf repolist", shell=True, capture_output=True, text=True )

    # CHECKING IF RPM FUSION REPO IS ALREADY INSTALLED
    if rpm_fusion_repo_check.stdout.find("rpmfusion-free") != -1 and rpm_fusion_repo_check.stdout.find("rpmfusion-nonfree"):

        # PRINTING THE MESSAGE
        print(_("The RPM Fusion repository had already been added to the system, there was no need to add it."))
        print("")

    else :
    
        # ADDING THE RPM FUSION REPOSITORY
        adding_repo = subprocess.run("dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if adding_repo.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to add the RPM Fusion Free and Non-Free repository."))
            print(_("Check your network connection and try again or add it by yourself."))
            print("")
            print(adding_repo.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("")
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")
            exit(2)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The RPM Fusion Free and Non-Free repository have been successfully added."))
            print("")

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT STARTS THE CORRECT GPU DRIVER INSTALLATION
def start_driver_install(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel):

    #-----------------------------------------------------------------------------------------------------

    # CHECKING WHICH DRIVER NEEDS TO BE INSTALLED AND STARTING THE CORRECT INSTALLATION FUNCTION
    if gpu_supported_nvidia == True :

        # STARTING THE DRIVER INSTALLATION
        install_nvidia_driver()

    if gpu_supported_amd == True :

        # STARTING THE DRIVER INSTALLATION
        install_amd_driver()

    if gpu_supported_intel == True :

        # STARTING THE DRIVER INSTALLATION
        install_intel_driver()
    
    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT STARTS THE NVIDIA DRIVER INSTALLATION
def install_nvidia_driver():

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    nvidia_driver_check_1 = subprocess.run("dnf list --installed | grep akmod-nvidia", shell=True, capture_output=True, text=True )
    nvidia_driver_check_2 = subprocess.run("dnf list --installed | grep xorg-x11-drv-nvidia-cuda", shell=True, capture_output=True, text=True )
    nvidia_driver_check = nvidia_driver_check_1.stdout + nvidia_driver_check_2.stdout

    # CHECKING IF IS ALREADY INSTALLED THE PROPRIETARY NVIDIA DRIVER
    if nvidia_driver_check.find("akmod-nvidia") != -1 and ((nvidia_driver_check.find("xorg-x11-drv-nvidia-cuda") != -1) and not (nvidia_driver_check.find("xorg-x11-drv-nvidia-cuda-"))) :

        # PRINTING THE MESSAGE
        print(_("The proprietary Nvidia GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLING THE NVIDIA PROPRIETARY DRIVER  
        nvidia_driver_install = subprocess.run("dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if nvidia_driver_install.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the proprietary Nvidia GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(nvidia_driver_install.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The proprietary Nvidia GPU driver has been successfully installed."))
            print("")

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT STARTS THE AMD GPU DRIVER INSTALLATION
def install_amd_driver():

    #-----------------------------------------------------------------------------------------------------
    
    # ACQUIRING IF IS ALREADY INSTALLED THE AMD DRIVER
    amd_driver_check = subprocess.run("dnf list --installed | grep rocm && dnf list --installed | grep freeworld", shell=True, capture_output=True, text=True ).stdout

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF IS ALREADY INSTALLED THE AMD DRIVER         
    if (amd_driver_check.find("rocm-opencl") != -1) and (amd_driver_check.find("rocm-smi") != -1) and (amd_driver_check.find("rocm-core") != -1) and (amd_driver_check.find("rocm-hip") != -1) :

        # PRINTING THE MESSAGE
        print(_("The open source AMD GPU driver was already installed on the system, there was no need to install it."))
        print("")

    else :

        # INSTALLING THE AMD DRIVER  
        amd_driver_install = subprocess.run("dnf install -y rocm-opencl rocm-smi rocm-core rocm-hip", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if amd_driver_install.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the open source AMD GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(amd_driver_install.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

    #-----------------------------------------------------------------------------------------------------
        
    # CHECKING IF IS ALREADY INSTALLED THE MESA FREEWORLD DRIVER         
    if (amd_driver_check.find("mesa-va-drivers-freeworld") != -1) and (amd_driver_check.find("mesa-vdpau-drivers-freeworld") != -1):

        # PRINTING THE MESSAGE
        print(_("The MESA Freeworld drivers were already installed on the system, there was no need to install it."))
        print("")

    else :

        # SWAPPING THE MESA TO THE COMPLETE VERSION
        amd_driver_swap = subprocess.run("dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld && dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld", shell=True, capture_output=True, text=True )

        # CHECKING IF THERE WERE ERRORS
        if amd_driver_swap.returncode != 0 :

            # PRINTING THE ERROR MESSAGE
            print(_("DEBUG : It was impossible to install the open source AMD GPU driver."))
            print(_("Check your network connection and try again or install it by yourself."))
            print("")
            print(amd_driver_swap.stdout)
            print("")
            print(_("Please open an issue report and paste this error code on the project GitHub page :"))
            print("https://github.com/H3rz3n/davinci-helper/issues")
            print("")            
            exit(3)

        else :

            # PRINTING THE SUCCESSFUL STATE
            print(_("The open source AMD GPU driver has been successfully installed."))
            print("")

    #-----------------------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------------------






# FUNCTION THAT STARTS THE INTEL GPU DRIVER INSTALLATION
def install_intel_driver():

   #-----------------------------------------------------------------------------------------------------
    
    print(_("DEBUG : It was impossible to install the drivers for your GPU because it is currently not supported by this app. "))
    print("")
    print(_("If you know that your GPU is supported by DaVinci Resolve please open an issue report on the project GitHub page :"))
    print("")
    print("https://github.com/H3rz3n/davinci-helper/issues")
    print("")
    exit(1)
    
    #-----------------------------------------------------------------------------------------------------












# STARTING THE FUNCTION THAT FINDS THE GPU VENDOR
gpu_lspci, gpu_vendor = find_gpu_vendor()

# ACQUIRING GPU MODEL NAME
gpu_model_name_list = extract_gpu_model_name(gpu_lspci)

# ACQUIRING GPU MODEL NAME
gpu_model_number_list = extract_gpu_model_number(gpu_lspci)

# STARTING THE FUNCTION THAT FINDS THE GPU MODEL
gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel = start_gpu_support_search(gpu_vendor, gpu_model_name_list, gpu_model_number_list)

# STARTING THE FUNCTION THAT CHECKS IF THERE ARE NOT BEEN FOUND COMPATIBLE GPUs
check_supported_gpu_presence(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel)

# STARTING THE FUNCTION THAT ADDS THE RPM FUSION REPOSITORY
add_repository()

# STARTING THE FUNCTION THAT INSTALLS THE NECESSARY GPU DRIVERS
start_driver_install(gpu_supported_nvidia, gpu_supported_amd, gpu_supported_intel)










