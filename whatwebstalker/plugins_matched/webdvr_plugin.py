import plugins
			
class Pluginwebdvr_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>WebDVR</title>" },
			{ "text" : "<TITLE>WEBDVR</TITLE>" },
			{ "text" : "		alert("Direct Draw Overlay Mode: It is faster than GDI but only available on ATI Video Card and requires Direct 7 or above.\nIf you have other video cards than ATI", "you shouldn\'t use this mode.");" },
			{ "text" : "		alert("DirectDraw Video acceleration will be enabled if your VGA card supports Microsoft DirectX 8.1 or later.");" },
			{ "text" : "		window.location="webdvr.html";" },
		]
		return(self.rules)
