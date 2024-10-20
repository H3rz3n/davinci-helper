#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale

# IMPORTING NOT STANDARD MODULES
from moviepy.editor import VideoFileClip
        

#-----------------------------------------------------------------------------------------------------

# DEFINING TRANSLATE FILES PATH
locale_path = os.path.join("/usr/share/davinci-helper/locale")

# DEFINING SETTINGS FILES PATH
home_dir = os.path.expanduser("~")
settings_path = os.path.join(f"{home_dir}/.config")

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







# FUNCTION THAT WILL CALCOLATE THE NECESSARY DISK SPACE TO COMPLETE THE CONVERSION
def calculate_disk_space (file_path_list, video_quality, audio_quality):

    #-----------------------------------------------------------------------------------------------------

    # RESETTING THE COUNTERS
    total_weight = 0
    unsupported_list = []
    video_settings = []
    audio_settings = []
    duration_list = []

    #-----------------------------------------------------------------------------------------------------

    # CALCULATING THE TOTAL FILE WEIGHT
    for file in file_path_list :

        # RESETTING THE COUNTERS
        file_weight = 0

        #-----------------------------------------------------------------------------------------------------

        # GETTING THE VIDEO INFO
        width, height, duration, fps = get_file_info(file)

        #-----------------------------------------------------------------------------------------------------
        
        # GETTING THE CORRECT ENCODER
        encoder = get_encoder(width, fps)

        #-----------------------------------------------------------------------------------------------------

        if encoder == "DNxHD" :

            # GETTING THE CORRECT VIDEO SETTINGS
            video_placeholder, video_bitrate = translate_video_settings_for_dnxhd(video_quality, width, height)

            # ADDING THE VIDEO CONVERSION SETTINGS TO THE LIST
            video_settings.append(video_placeholder)

            # GETTING THE CORRECT VIDEO SETTING
            audio_settings, audio_bitrate = translate_settings_for_audio(audio_quality, duration)

            # EXECUTING THE FILE WEIGHT CALCULATION
            file_weight = get_file_weight(video_bitrate, audio_bitrate, duration)

            # ADDING THE VIDEO DURATION TO THE DURATION LIST
            duration_list.append(duration)

        #-----------------------------------------------------------------------------------------------------

        elif encoder == "DNxHR" :

            # GETTING THE CORRECT VIDEO SETTING
            video_placeholder, video_bitrate = translate_video_settings_for_dnxhr(video_quality, width, fps)

            # ADDING THE VIDEO CONVERSION SETTINGS TO THE LIST
            video_settings.append(video_placeholder)

            # GETTING THE CORRECT VIDEO SETTING
            audio_settings, audio_bitrate = translate_settings_for_audio(audio_quality, duration)

            # EXECUTING THE FILE WEIGHT CALCULATION
            file_weight = get_file_weight(video_bitrate, audio_bitrate, duration)

            # ADDING THE VIDEO DURATION TO THE DURATION LIST
            duration_list.append(duration)

        #-----------------------------------------------------------------------------------------------------

        else :

            # ADDING THE FILE TO THE UNSUPPORTED FILE LIST
            unsupported_list.append(file)
            
        #-----------------------------------------------------------------------------------------------------

        # ADDING THE FILE WEIGHT TO THE TOTAL WEIGHT
        total_weight = total_weight + file_weight

        #-----------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------
    
    return video_settings, audio_settings, f"{total_weight} GB", unsupported_list, duration_list
    
    #-----------------------------------------------------------------------------------------------------




# FUNCTION THAT WILL GET THE INFO FROM THE VIDEO FILE
def get_file_info (file):

    #-----------------------------------------------------------------------------------------------------

    # LOADING THE CLIP
    video = VideoFileClip(file)

    # GETTING THE VIDEO RESOLUTION
    width, height = video.size

    # GETTING THE DURATION
    duration = video.duration

    # GETTING THE FRAMERATE
    fps = video.fps

    #-----------------------------------------------------------------------------------------------------

    return width, height, duration, fps

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL GET THE CORRECT ENCODER FOR THE VIDEO
def get_encoder (width, fps):

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE CORRECT ENCODER USING THE WIDH PARAMETERS AS REFERENCE
    if width <= 1920 and fps <= 61:

        # RETURNING BACK THE CORRECT ENCODER
        return "DNxHD"

    elif fps > 61:

        # RETURNING BACK THE UNSUPPORTED VIDEO STATUS
        return "Unsupported"

    elif width > 4097 :

        # RETURNING BACK THE UNSUPPORTED VIDEO STATUS
        return "Unsupported"

    else :

        # RETURNING BACK THE CORRECT ENCODER
        return "DNxHR"

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL TRANSLATE VIDEO THE DROPDOWN SETTINGS IN FFMPEG SETTINGS
def translate_video_settings_for_dnxhd (video_quality, width, height):

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THE VIDEO IS 960X720
    if width == 960 and height == 720 :

        # GETTING THE VIDEO QUALITY SETTINGS
        if video_quality == 0 :
        
            # SETTING THE ORIGINAL QUALITY
            video_settings = "-b:v 115M"
            video_bitrate = 115

        elif video_quality == 1 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 75M"
            video_bitrate = 75

        elif video_quality == 2 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 60M"
            video_bitrate = 60

        elif video_quality == 3 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 42M"
            video_bitrate = 42

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THE VIDEO IS 1280X720
    if width == 1280 and height == 720 :

        # GETTING THE VIDEO QUALITY SETTINGS
        if video_quality == 0 :
        
            # SETTING THE ORIGINAL QUALITY
            video_settings = "-b:v 220M"
            video_bitrate = 220

        elif video_quality == 1 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 120M"
            video_bitrate = 120

        elif video_quality == 2 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 90M"
            video_bitrate = 90

        elif video_quality == 3 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 60M"
            video_bitrate = 60

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THE VIDEO IS 1440X1080
    if width == 1440 and height == 1080 :

        # GETTING THE VIDEO QUALITY SETTINGS
        if video_quality == 0 :
        
            # SETTING THE ORIGINAL QUALITY
            video_settings = "-b:v 110M"
            video_bitrate = 110

        elif video_quality == 1 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 100M"
            video_bitrate = 100

        elif video_quality == 2 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 84M"
            video_bitrate = 84

        elif video_quality == 3 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 63M"
            video_bitrate = 63

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate

    #-----------------------------------------------------------------------------------------------------

    # CHECKING IF THE VIDEO IS 1920X1080
    if width <= 1920 and height == 1080 :

        # GETTING THE VIDEO QUALITY SETTINGS
        if video_quality == 0 :
        
            # SETTING THE ORIGINAL QUALITY
            video_settings = "-b:v 440M"
            video_bitrate = 440

        elif video_quality == 1 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 220M"
            video_bitrate = 220

        elif video_quality == 2 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 120M"
            video_bitrate = 120

        elif video_quality == 3 :

            # SETTING THE HIGH QUALITY
            video_settings = "-b:v 75M"
            video_bitrate = 75

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate
    
    #-----------------------------------------------------------------------------------------------------
   



        
# FUNCTION THAT WILL TRANSLATE THE VIDEO DROPDOWN SETTINGS IN FFMPEG SETTINGS
def translate_video_settings_for_dnxhr (video_quality, width, fps):

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE VIDEO QUALITY SETTINGS
    if video_quality == 0 :
    
        # SETTING THE ORIGINAL QUALITY
        video_settings = "-profile:v dnxhr_hq"
        
        if width <= 1920 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 145

        elif width <= 1920 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 220

        elif width <= 2048 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 155

        elif width <= 2048 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 240

        elif width <= 4096 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 707

        elif width <= 4096 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 1170

        else:

            # SETTING THE BITRATE
            print (width, fps)

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate

    #-----------------------------------------------------------------------------------------------------
    
    if video_quality == 1 :

        # SETTING THE ORIGINAL QUALITY
        video_settings = "-profile:v dnxhr_sq"
        
        if width <= 1920 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 90

        elif width <= 1920 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 145

        elif width <= 2048 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 95

        elif width <= 2048 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 160

        elif width <= 4096 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 384

        elif width <= 4096 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 707
        
        else:

            # SETTING THE BITRATE
            print (width, fps)

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate

    #-----------------------------------------------------------------------------------------------------

    if video_quality == 2 or video_quality == 3 :

        # SETTING THE ORIGINAL QUALITY
        video_settings = "-profile:v dnxhr_lb"
        
        if width <= 1920 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 45

        elif width <= 1920 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 75

        elif width <= 2048 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 50

        elif width <= 2048 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 85

        elif width <= 4096 and fps <= 30 :

            # SETTING THE BITRATE
            video_bitrate = 192

        elif width <= 4096 and fps <= 60 :

            # SETTING THE BITRATE
            video_bitrate = 365

        else:

            # SETTING THE BITRATE
            print (width, fps)

        # GIVING BACK THE VALUES
        return video_settings, video_bitrate

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL TRANSLATE THE AUDIO DROPDOWN SETTINGS IN FFMPEG SETTINGS
def translate_settings_for_audio (audio_quality, duration):

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE VIDEO QUALITY SETTINGS
    if audio_quality == 0 :
    
        # SETTING THE ORIGINAL QUALITY
        audio_settings = "pcm_s16le"
        audio_bitrate = 1.536

        # GIVING BACK THE VALUES
        return audio_settings, audio_bitrate

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE VIDEO QUALITY SETTINGS
    if audio_quality == 1 :
    
        # SETTING THE ORIGINAL QUALITY
        audio_settings = "libmp3lame -b:a 320k"
        audio_bitrate = 0.32

        # GIVING BACK THE VALUES
        return audio_settings, audio_bitrate

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE VIDEO QUALITY SETTINGS
    if audio_quality == 2 :
    
        # SETTING THE ORIGINAL QUALITY
        audio_settings = "libmp3lame -b:a 256k"
        audio_bitrate = 0.256

        # GIVING BACK THE VALUES
        return audio_settings, audio_bitrate

    #-----------------------------------------------------------------------------------------------------

    # GETTING THE VIDEO QUALITY SETTINGS
    if audio_quality == 3 :
    
        # SETTING THE ORIGINAL QUALITY
        audio_settings = "libmp3lame -b:a 192k"
        audio_bitrate = 0.192

        # GIVING BACK THE VALUES
        return audio_settings, audio_bitrate

    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL CALC THE FILE WEIGHT
def get_file_weight (video_bitrate, audio_bitrate, duration):

    #-----------------------------------------------------------------------------------------------------

    # CALCULATING THE VIDEO WEIGHT IN GB
    video_weight = (video_bitrate*duration*1000000)/(8*1073741824)

    # CALCULATING THE AUDIO WEIGHT IN GB
    audio_weight = (audio_bitrate*duration*1000000)/(8*1073741824)

    #-----------------------------------------------------------------------------------------------------

    # CALCULATING THE FILE WEIGHT
    file_weight = video_weight + audio_weight

    # TRIM TO THE FIRST TWO DECIMALS
    file_weight = round(file_weight,2)

    # RETURNING THE VALUE
    return file_weight

    #-----------------------------------------------------------------------------------------------------









'''


f" ffmpeg -i {input_file} -c:v dnxhd {video_settings} -c:a {audio_settings} {output_path}/{file_name}_converted.mov"




"ffmpeg -i input.mp4 -c:v dnxhd -b:v 36M -c:a pcm_s16le output.mov"

"ffmpeg -i input.mp4 -c:v dnxhd -profile:v dnxhr_hq -c:a pcm_s16le output.mov"
'''