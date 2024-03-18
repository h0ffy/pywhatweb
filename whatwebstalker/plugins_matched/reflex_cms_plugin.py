import plugins
			
class Pluginreflex_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<link id="ctl00_hlnk[^"]+" rel="stylesheet" type="text\/css"[^>]+href="[^"]*\/Site\/Resources\/css\/(layout|styles).css" \/>/" },
			{ "text" : "var Page_Validators =  new Array(document.getElementById("ctl00_cphMain_rfvUserName")", "document.getElementById("ctl00_cphMain_rfvUserPassword"));" },
			{ "text" : "<img src="Resources/images/reflex.png" alt="ReFlex Administration" />" },
			{ "text" : "<script defer type="text/javascript" src="Resources/js/pngfix.js"></script>" },
			{ "url" : "/Admin/Resources/images/reflex.png", "md5" : "982a1eb449c954d214307a20dc2301ea" },
		]
		return(self.rules)
