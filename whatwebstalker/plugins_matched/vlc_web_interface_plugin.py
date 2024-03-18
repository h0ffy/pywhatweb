import sys
import os
			
class vlc_web_interface_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "text" : '<title>VLC media player - Web Interface</title>' }
			{ "certainty" : '75", "text" : '<title>VLC media player - Web Interface - Mosaic Wizard</title>' }
			{ "certainty" : '75", "text" : '<title>VLC media player - Web Interface with Flash Viewer</title>' }
			{ "certainty" : '75", "text" : '<title>VLC media player - Web Interface - VLM</title>' }
			{ "text" : '<!-- do we need to browse in order to setup a mosaic ? for the background image maybe ... -->' }
			{ "text" : '<input type="checkbox" id="vlm_schedule_repeat" onchange="toggle_schedule_repeat();update_vlm_add_schedule();" />' }
			{ "text" : '<input type="text" name="sout_mrl" id="sout_mrl" size="60" onkeypress="if( event.keyCode == 13 ) vlm_output_change();"/>' }
		]

