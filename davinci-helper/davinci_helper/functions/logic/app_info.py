#
# Copyright 2024 Lorenzo Maiuri
# Published under GPL-3.0 license
# GitHub : https://github.com/H3rz3n/davinci-helper
#

#-----------------------------------------------------------------------------------------------------


# APP NAME
app_name = "DaVinci Helper"

# APP VERSION
app_version = "v2.0.3"

# APP ICON
app_icon = "davinci_helper_icon"

# APP WEBSITE
app_website = "https://github.com/H3rz3n/davinci-helper"

# APP DEVELOPERS
app_developers = "Lorenzo Maiuri"

# APP CONTRIBUTORS
app_contributors = ""

# APP TRANSLATOR
app_translator = "Lorenzo Maiuri (ITA)\nCamilla Fioretti (ENG)"

# APP LICENSE
app_license = "gpl-3.0"

# APP ISSUE URL
app_issue_url = "https://github.com/H3rz3n/davinci-helper/issues"

# APP COPYRIGHT
with open(f"/usr/share/davinci-helper/data/LICENSE", 'r', encoding='utf-8') as file :

    # READING THE COPYRIGHT FILE
    app_copyright = file.read()
