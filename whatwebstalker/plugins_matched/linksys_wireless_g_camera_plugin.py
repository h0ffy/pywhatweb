import plugins
			
class Pluginlinksys_wireless_g_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Linksys Wireless-G Internet-Videokamera</title>" },
			{ "text" : "<title>Linksys Wireless-G Internet Video Camera</title>" },
			{ "text" : "<body bgcolor="#ffffff" marginheight="0" marginwidth="0" leftmargin="0" topmargin="0" onload="parent.chkRefresh(\'vr\')"> </body>" },
		]
	return(self.rules)

