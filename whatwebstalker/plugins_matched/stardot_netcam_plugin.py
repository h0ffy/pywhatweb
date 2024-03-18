import plugins
			
class Pluginstardot_netcam_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>NetCam Live Image[\ Popup]*<\/title>/" },
			{ "regexp" : "/<applet code="CaptureClient.class" width="[\d]+" height="[\d]+" alt="NetCam Live [Stream|Image]+">/" },
			{ "regexp" : "/<title>NetCamXL Live Image[\ Popup]*<\/title>/", "version" : "XL" },
			{ "regexp" : "/<applet code="CaptureClient.class" width="[\d]+" height="[\d]+" alt="NetCamXL Live [Stream|Image]+">/", "version" : "XL" },
		]
		return(self.rules)

