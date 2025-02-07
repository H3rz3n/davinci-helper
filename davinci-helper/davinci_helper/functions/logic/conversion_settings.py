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

    #-----------------------------------------------------------------------------------------------------

    # DEFINING THE DICTIONARY OF THE SUPPORTED RESOLUTIONS AND FRAMERATES
    bitrate_table = {

        # DICTIONARY OF MAX QUALITY
        "dnxhr_hq": {
            (1920, 1080, 30): 145, (1920, 1080, 60): 220, (1920, 1080, 120): 440, (1920, 1080, 240): 880,
            (1080, 1920, 30): 145, (1080, 1920, 60): 220, (1080, 1920, 120): 440, (1080, 1920, 240): 880,

            (2048, 1152, 30): 155, (2048, 1152, 60): 240, (2048, 1152, 120): 480, (2048, 1152, 240): 960,
            (1152, 2048, 30): 155, (1152, 2048, 60): 240, (1152, 2048, 120): 480, (1152, 2048, 240): 960,

            (2560, 1440, 30): 350, (2560, 1440, 60): 600, (2560, 1440, 120): 1200, (2560, 1440, 240): 2400,
            (1440, 2560, 30): 350, (1440, 2560, 60): 600, (1440, 2560, 120): 1200, (1440, 2560, 240): 2400,

            (3840, 2160, 30): 707, (3840, 2160, 60): 1170, (3840, 2160, 120): 2340, (3840, 2160, 240): 4680,
            (2160, 3840, 30): 707, (2160, 3840, 60): 1170, (2160, 3840, 120): 2340, (2160, 3840, 240): 4680,

            (7680, 4320, 30): 2000, (7680, 4320, 60): 4000, (7680, 4320, 120): 8000, (7680, 4320, 240): 16000,
            (4320, 7680, 30): 2000, (4320, 7680, 60): 4000, (4320, 7680, 120): 8000, (4320, 7680, 240): 16000
        },

        # DICTIONARY OF HIGH QUALITY
        "dnxhr_sq": {
            (1920, 1080, 30): 90, (1920, 1080, 60): 145, (1920, 1080, 120): 290, (1920, 1080, 240): 580,
            (1080, 1920, 30): 90, (1080, 1920, 60): 145, (1080, 1920, 120): 290, (1080, 1920, 240): 580,

            (2048, 1152, 30): 95, (2048, 1152, 60): 160, (2048, 1152, 120): 320, (2048, 1152, 240): 640,
            (1152, 2048, 30): 95, (1152, 2048, 60): 160, (1152, 2048, 120): 320, (1152, 2048, 240): 640,

            (2560, 1440, 30): 200, (2560, 1440, 60): 340, (2560, 1440, 120): 680, (2560, 1440, 240): 1360,
            (1440, 2560, 30): 200, (1440, 2560, 60): 340, (1440, 2560, 120): 680, (1440, 2560, 240): 1360,

            (3840, 2160, 30): 384, (3840, 2160, 60): 707, (3840, 2160, 120): 1414, (3840, 2160, 240): 2828,
            (2160, 3840, 30): 384, (2160, 3840, 60): 707, (2160, 3840, 120): 1414, (2160, 3840, 240): 2828,

            (7680, 4320, 30): 1200, (7680, 4320, 60): 2400, (7680, 4320, 120): 4800, (7680, 4320, 240): 9600,
            (4320, 7680, 30): 1200, (4320, 7680, 60): 2400, (4320, 7680, 120): 4800, (4320, 7680, 240): 9600
        },

        # DICTIONARY OF MID/LOW QUALITY
        "dnxhr_lb": {
            (1920, 1080, 30): 45, (1920, 1080, 60): 75, (1920, 1080, 120): 150, (1920, 1080, 240): 300,
            (1080, 1920, 30): 45, (1080, 1920, 60): 75, (1080, 1920, 120): 150, (1080, 1920, 240): 300,

            (2048, 1152, 30): 50, (2048, 1152, 60): 85, (2048, 1152, 120): 170, (2048, 1152, 240): 340,
            (1152, 2048, 30): 50, (1152, 2048, 60): 85, (1152, 2048, 120): 170, (1152, 2048, 240): 340,

            (2560, 1440, 30): 100, (2560, 1440, 60): 175, (2560, 1440, 120): 350, (2560, 1440, 240): 700,
            (1440, 2560, 30): 100, (1440, 2560, 60): 175, (1440, 2560, 120): 350, (1440, 2560, 240): 700,

            (3840, 2160, 30): 192, (3840, 2160, 60): 365, (3840, 2160, 120): 730, (3840, 2160, 240): 1460,
            (2160, 3840, 30): 192, (2160, 3840, 60): 365, (2160, 3840, 120): 730, (2160, 3840, 240): 1460,

            (7680, 4320, 30): 600, (7680, 4320, 60): 1200, (7680, 4320, 120): 2400, (7680, 4320, 240): 4800,
            (4320, 7680, 30): 600, (4320, 7680, 60): 1200, (4320, 7680, 120): 2400, (4320, 7680, 240): 4800
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