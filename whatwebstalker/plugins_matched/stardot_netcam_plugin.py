import sys
import os
			
class stardot_netcam_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<title>NetCam Live Image[\ Popup]*<\/title>/ }
			{ "regexp" : '/<applet code="CaptureClient.class" width="[\d]+" height="[\d]+" alt="NetCam Live [Stream|Image]+">/ }
			{ "regexp" : '/<title>NetCamXL Live Image[\ Popup]*<\/title>/", "version" : 'XL" }
			{ "regexp" : '/<applet code="CaptureClient.class" width="[\d]+" height="[\d]+" alt="NetCamXL Live [Stream|Image]+">/", "version" : 'XL" }
	]

