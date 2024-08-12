#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licensa CC-BY-NC-SA
# Published under CC-BY-NC-SA license
#   

#-----------------------------------------------------------------------------------------------------

# IMPORTAZIONE DEI MODULI STANDARD
# STANDARD MODULES IMPORT
from setuptools import setup, find_packages
import os

#-----------------------------------------------------------------------------------------------------

# FUNZIONE PER LEGGERE IL FILE README
# FUNCTION TO READ THE README FILE
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#-----------------------------------------------------------------------------------------------------

# INIZIO DELLE IMPOSTAZIONI DI SETUP
# SETUP SETTINGS START
setup(
    
    # NOME DEL PROGRAMMA
    # APP NAME
    name="davinci-toolbox",
    
    # VERSIONE DEL PROGRAMMA
    # APP VERSION
    version="1.0",

    # AUTORE DEL PROGRAMMA
    # APP AUTHOR
    author="Lorenzo Maiuri",

    # INDIRIZZO MAIL DELL'AUTORE
    # AUTHOR EMAIL ADDRESS
    author_email="lorenzo.maiuri@gmail.com",

    # DESCRIZIONE BREVE DEL PROGRAMMA
    # APP SHORT DESCRIPTION
    description=("A toolbox to help you install DaVinci Resolve."),

    # DESCRIZIONE LUNGA DEL PROGRAMMA
    # APP LONG DESCRIPTION
    long_description=read('README.md'),
    
    # TIPOLOGIA DI TESTO DELLA DESCRIZIONE LUNGA
    # LONG DESCRIPTION TEXT TYPE
    long_description_content_type='text/markdown',

    # LICENZA DI PUBBLICAZIONE
    # PUBBLICATION LICENSE
    license="CC-BY-NC-SA",

    # PAROLE CHIAVE
    # KEYWORDS
    keywords="davinci toolbox tool",

    # INDIRIZZO GITHUB DEL PROGETTO
    # PROJECT GITHUB ADDRESS
    url="https://github.com/H3rz3n/davinci-toolbox",

    # CLASSIFICAZIONE DEL PROGETTO
    # PROJECT CLASSIFICATION
    classifiers=[
        "Development Status :: 1.0 - Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: CC-BY-NC-SA-4.0 License",
    ],

    #-----------------------------------------------------------------------------------------------------

    # INCLUSIONE DEI FILE NON ESEGUIBILI
    # NOT EXECUTABLE FILES INCLUSION
    include_package_data=True,

    # POSIZIONE DEI FILE NON ESEGUIBILI
    # NOT EXECUTABLE FILES PATH
    data_files=[
        ('share/davinci-toolbox/data/css', ['data/css/style-dark.css']),
        ('share/davinci-toolbox/data/desktop', [
            'data/desktop/com.davinci.toolbox.app.desktop',
            'data/desktop/com.davinci.toolbox.app.metainfo.xml',
            'data/desktop/davinci-toolbox-icon.svg'
        ]),
        ('share/davinci-toolbox/data/icons/', [
        'data/icons/davinci-toolbox-icon.svg'
        ]),
        ('share/davinci-toolbox/data/icons/main_icons', [
            'data/icons/main_icons/F1.svg',
            'data/icons/main_icons/F2.svg',
            'data/icons/main_icons/F3.svg',
            'data/icons/main_icons/F4.svg'
        ]),
        ('share/davinci-toolbox/data/icons/function_icons', [
            'data/icons/function_icons/error.svg',
            'data/icons/function_icons/success.svg',
            'data/icons/function_icons/warning.svg',
            'data/icons/function_icons/file.svg'
        ]),
        ('share/davinci-toolbox/data/polkit', [
            'data/polkit/com.davinci.toolbox.app.rules',
            'data/polkit/com.davinci.toolbox.app.policy'
        ]),
        ('share/davinci-toolbox/data/ui', [
            'data/ui/about_window.ui',
            'data/ui/function_1.ui',
            'data/ui/function_2.ui',
            'data/ui/function_3.ui',
            'data/ui/function_4.ui',
            'data/ui/info_function_1.ui',
            'data/ui/info_function_2.ui',
            'data/ui/info_function_3.ui',
            'data/ui/info_function_4.ui',
            'data/ui/error_dialog.ui',
            'data/ui/welcome_messagge_splash_screen.ui',
            'data/ui/gpu_warning_splash_screen.ui',
            'data/ui/check_update.ui',
            'data/ui/reset_settings.ui',
            'data/ui/main_window.ui'
        ]),
        ('share/davinci-toolbox/data/gpu_support', [
            'data/gpu_support/amd_support.txt',
            'data/gpu_support/intel_support.txt',
            'data/gpu_support/nvidia_support.txt'
        ]),
        ('share/davinci-toolbox/data/settings', [
            'data/settings/davinci_toolbox_settings'
        ]),
        ('share/davinci-toolbox/locale', [
            
        ])
    ],

    #-----------------------------------------------------------------------------------------------------

    # VERSIONE MINIMA DI PYTHON RICHIESTA
    # MINUMUN REQUIRMENT PYTHON VERSION
    python_requires='>=3.0',

    # MODULI PYTHON ESEGUIBILI
    # EXECUTABLE PYTHON MODULES
    packages=['davinci_toolbox', 'davinci_toolbox/functions'],

    # AVVIO DEL PROGRAMMA
    # APP START
    entry_points={
        "console_scripts": [
            "davinci-toolbox=davinci_toolbox.main:main",
        ],
    },
)

#-----------------------------------------------------------------------------------------------------
