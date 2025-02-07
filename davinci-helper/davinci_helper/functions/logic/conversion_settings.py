#
# Copyright 2024 Lorenzo Maiuri
# Pubblicato sotto licenza GPL-3.0
# Published under GPL-3.0 license
#   

#-----------------------------------------------------------------------------------------------------

# STANDARD MODULES IMPORT
import sys, os, subprocess, threading, gettext, locale, json

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

        # GETTING THE CORRECT VIDEO SETTING
        video_placeholder, video_bitrate = translate_video_settings_for_dnxhr(video_quality, width, height, fps)

        # CHECKING IF THE VIDEO IS COMPATIBLE WITH THE CODEC
        if video_bitrate == 0 :

            #-----------------------------------------------------------------------------------------------------

            # ADDING THE FILE TO THE UNSUPPORTED FILE LIST
            unsupported_list.append(file)

            #-----------------------------------------------------------------------------------------------------

        else :

            #-----------------------------------------------------------------------------------------------------

            # ADDING THE VIDEO CONVERSION SETTINGS TO THE LIST
            video_settings.append(video_placeholder)

            # GETTING THE CORRECT VIDEO SETTING
            audio_settings, audio_bitrate = translate_settings_for_audio(audio_quality, duration)

            # EXECUTING THE FILE WEIGHT CALCULATION
            file_weight = get_file_weight(video_bitrate, audio_bitrate, duration)

            # ADDING THE VIDEO DURATION TO THE DURATION LIST
            duration_list.append(duration)

            #-----------------------------------------------------------------------------------------------------

            # ADDING THE FILE WEIGHT TO THE TOTAL WEIGHT
            total_weight = total_weight + file_weight

            #-----------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------
    
    return video_settings, audio_settings, total_weight, unsupported_list, duration_list
    
    #-----------------------------------------------------------------------------------------------------





# FUNCTION THAT WILL GET THE INFO FROM THE VIDEO FILE
def get_file_info (file):

    #-----------------------------------------------------------------------------------------------------
    
    # GETTING VIDEO AVERAGE FRAMERATE, DURATION, WIDTH AND HEIGHT
    if not os.path.isfile(file):

        raise FileNotFoundError(f"The file {file} does not exist or is inaccessible.")
        exit(1)

    else :

        try:
            # EXECUTING FFPROBE AND GET METADATA AS JSON
            result = subprocess.run(f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,avg_frame_rate -of json "{file}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            if result.returncode != 0:
                raise ValueError(f"ffprobe error: {result.stderr.strip()}")

            # PARSING THE JSON OUTPUT
            metadata = json.loads(result.stdout)
            stream_info = metadata.get("streams", [])[0]

            # EXTRACTING VALUES WITH EXPLICIT TYPE CONVERSIONS AND FALLBACK DEFAULTS
            width = int(stream_info.get("width") or 0)                                                              # CONVERT TO INTEGER OR DEFAULT TO 0
            height = int(stream_info.get("height") or 0)                                                            # CONVERT TO INTEGER OR DEFAULT TO 0
            duration = float(stream_info.get("duration") or 0.0)                                                    # CONVERT TO FLOAT OR DEFAULT TO 0.0

            # PARSING THE AVERAGE FRAME RATE
            avg_frame_rate = stream_info.get("avg_frame_rate", "0/1")                                               # DEFAULT TO "0/1" IF NOT FOUND
            num, denom = (int(n) for n in avg_frame_rate.split('/')) if '/' in avg_frame_rate else (0, 1)
            fps = num / denom if denom != 0 else 0.0                                                                # ENSURE FRAME RATE IS A FLOAT

            return width, height, duration, fps

        except Exception as e:
            raise RuntimeError(f"Failed to get video info: {e}")

    #-----------------------------------------------------------------------------------------------------





        
# FUNCTION THAT WILL TRANSLATE THE VIDEO DROPDOWN SETTINGS IN FFMPEG SETTINGS
def translate_video_settings_for_dnxhr (video_quality, width, height, fps):

    #-----------------------------------------------------------------------------------------------------

    # DEFINING THE QUALITY DICTIONARY
    profiles = {
        0: "dnxhr_hq",  # HIGH QUALITY
        1: "dnxhr_sq",  # STANDARD QUALITY
        2: "dnxhr_lb",  # LOW BANDWIDTH
        3: "dnxhr_lb"   # LOW BANDWIDTH
    }

    print("Dati del file : ", width, "-", height)

    #-----------------------------------------------------------------------------------------------------

    # DEFINING THE DICTIONARY OF THE SUPPORTED RESOLUTIONS AND FRAMERATES
    bitrate_table = {

        # HIGH QUALITY (dnxhr_hq)
        "dnxhr_hq": {

            # 144p
            (256, 144, 30): 10, (256, 144, 60): 15,  
            (144, 256, 30): 10, (144, 256, 60): 15,  

            # 240p
            (426, 240, 30): 20, (426, 240, 60): 30,  
            (240, 426, 30): 20, (240, 426, 60): 30,  

            # 360p
            (640, 360, 30): 35, (640, 360, 60): 50,  
            (360, 640, 30): 35, (360, 640, 60): 50,  

            # 480p
            (854, 480, 30): 50, (854, 480, 60): 75,  
            (480, 854, 30): 50, (480, 854, 60): 75,  

            # 720p
            (1280, 720, 30): 75, (1280, 720, 60): 110,  
            (720, 1280, 30): 75, (720, 1280, 60): 110,  

            # 1080p
            (1920, 1080, 30): 145, (1920, 1080, 60): 220,  
            (1080, 1920, 30): 145, (1080, 1920, 60): 220,  

            # 2K
            (2560, 1440, 30): 350, (2560, 1440, 60): 600,  
            (1440, 2560, 30): 350, (1440, 2560, 60): 600,  

            # 4K
            (3840, 2160, 30): 707, (3840, 2160, 60): 1170,  
            (2160, 3840, 30): 707, (2160, 3840, 60): 1170,  

            # 8K
            (7680, 4320, 30): 2000, (7680, 4320, 60): 4000,  
            (4320, 7680, 30): 2000, (4320, 7680, 60): 4000,  
        },

        # STANDARD QUALITY (dnxhr_sq)
        "dnxhr_sq": {

            # 144p
            (256, 144, 30): 5, (256, 144, 60): 8,  
            (144, 256, 30): 5, (144, 256, 60): 8,  

            # 240p
            (426, 240, 30): 12, (426, 240, 60): 18,  
            (240, 426, 30): 12, (240, 426, 60): 18,  

            # 360p
            (640, 360, 30): 22, (640, 360, 60): 35,  
            (360, 640, 30): 22, (360, 640, 60): 35,  

            # 480p
            (854, 480, 30): 35, (854, 480, 60): 55,  
            (480, 854, 30): 35, (480, 854, 60): 55,  

            # 720p
            (1280, 720, 30): 55, (1280, 720, 60): 90,  
            (720, 1280, 30): 55, (720, 1280, 60): 90,  

            # 1080p
            (1920, 1080, 30): 90, (1920, 1080, 60): 145,  
            (1080, 1920, 30): 90, (1080, 1920, 60): 145,  

            # 2K
            (2560, 1440, 30): 200, (2560, 1440, 60): 340,  
            (1440, 2560, 30): 200, (1440, 2560, 60): 340,  

            # 4K
            (3840, 2160, 30): 384, (3840, 2160, 60): 707,  
            (2160, 3840, 30): 384, (2160, 3840, 60): 707,  

            # 8K
            (7680, 4320, 30): 1200, (7680, 4320, 60): 2400,  
            (4320, 7680, 30): 1200, (4320, 7680, 60): 2400,  
        },

        # LOW BANDWIDTH (dnxhr_lb)
        "dnxhr_lb": {

            # 144p
            (256, 144, 30): 2, (256, 144, 60): 4,  
            (144, 256, 30): 2, (144, 256, 60): 4,  

            # 240p
            (426, 240, 30): 6, (426, 240, 60): 10,  
            (240, 426, 30): 6, (240, 426, 60): 10,  

            # 360p
            (640, 360, 30): 12, (640, 360, 60): 20,  
            (360, 640, 30): 12, (360, 640, 60): 20,  

            # 480p
            (854, 480, 30): 20, (854, 480, 60): 35,  
            (480, 854, 30): 20, (480, 854, 60): 35,  

            # 720p
            (1280, 720, 30): 35, (1280, 720, 60): 55,  
            (720, 1280, 30): 35, (720, 1280, 60): 55,  

            # 1080p
            (1920, 1080, 30): 45, (1920, 1080, 60): 75,  
            (1080, 1920, 30): 45, (1080, 1920, 60): 75,  

            # 2K
            (2560, 1440, 30): 100, (2560, 1440, 60): 175,  
            (1440, 2560, 30): 100, (1440, 2560, 60): 175,  

            # 4K
            (3840, 2160, 30): 192, (3840, 2160, 60): 365,  
            (2160, 3840, 30): 192, (2160, 3840, 60): 365,  

            # 8K
            (7680, 4320, 30): 600, (7680, 4320, 60): 1200,  
            (4320, 7680, 30): 600, (4320, 7680, 60): 1200,  
        }
    }

    #-----------------------------------------------------------------------------------------------------

    # ACQUIRING THE QUALITY PROFILE
    profile = profiles[video_quality]

    # CHECKING IF THE VIDEO FILE IS COMPATIBLE WITH THE CODEC
    if (width, height, fps) not in bitrate_table[profile]:

        # SETTING THE ERROR
        video_settings = "not"
        video_bitrate = 0
        
        # RETURNING THE VALUES
        return video_settings, video_bitrate

    # SETTING THE VIDEO SETTINGS
    video_settings = f"-profile:v {profile}"

    # SETTING THE VIDEO BITRATE
    video_bitrate = bitrate_table[profile][(width, height, fps)]

    # RETURNING THE VALUES
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