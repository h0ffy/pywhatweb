import plugins


class Pluginvivotek_network_camera_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"url": "/main.html", "text": "<div id="logo_icon"><a href="http: // www.vivotek.com / " target="_blank"><img alt="logo" src="pic / logo.gif"></a></div>"},
			{"certainty": "25", "regexp": "/<frameset rows="2000, 0" border="0" frameborder="no" framespacing="0">[\\s]+<frame name="mainframe" src="main\.html" marginheight="0" marginwidth="0">/" },
			{ "certainty" : "25", "search" : "headers[server]", "regexp" : "/^(Network Camera|Network Dome Camera|Network Camera with Pan\/Tilt|Wireless Network Camera)$/" },
			{ "url" : "/cgi-bin/admin/getparamjs.cgi", "model" : "/system_modelname="([^"]+)"/" },
			{ "url" : "/cgi-bin/admin/getparamjs.cgi", "version" : "/system_supportscriptversion="([^"]+)"/" },
			{ "url" : "/cgi-bin/admin/getparamjs.cgi", "firmware" : "/system_firmwareversion="([^"]+)"/" },
			{ "url" : "/cgi-bin/admin/getparamjs.cgi", "string" : /system_hostname="([^"]+)"/" },
			{ "url" : "/cgi-bin/admin/getparamjs.cgi", "account" : "/security_user(pass|name)\.[\d]{1,2}="([^"]+)"/", "offset" : "1 },
			{ "url" : "/setup/system.html", "text" : "<script type="text/javascript" 	src="/cgi-bin/admin/getparamjs.cgi?system">" },
		]
	return(self.rules)
