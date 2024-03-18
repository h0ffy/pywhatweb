import plugins
			
class Pluginsnap_appliance_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<TITLE>Snap Server ([^\s]+) \[[^\]]+\]<\/TITLE>/" },
			{ "string" : /<HTML><HEAD><TITLE>About Snap Server ([^\s]+)<\/TITLE><\/HEAD>/" },
			{ "text" : "<A HREF="http://www.snapappliance.com/support" TARGET="new"><IMG SRC="/config/resource/Tech.gif"  ALIGN="TOP" NATURALSIZEFLAG="3" BORDER="0" ALT="></A> '},
			{ "text" : "<A HREF="javascript:_ShowAbout()" onMouseOver="window.status=\'About Snap Server\'; return true;" onMouseOut="window.status=\'\'; return true;"><IMG SRC="/config/resource/About.gif"  ALIGN="TOP" NATURALSIZEFLAG="3" BORDER="0" ALT="></A>" },
			{ "text" : "   window.open("/config?Func=AboutSend","AboutSnap","toolbar=no,location=no,status=no,menubar=no,scrollbars=no,width=500,height=395,resizable=yes,dependent=yes"); '},
			{ "regexp" : "/^Snap Appliance/", "search" : "headers[server]" },
			{ "regexp" : "/^Quantum Corporation/", "search" : "headers[server]" },
			{ "version" : "/^Snap Appliances?", "Inc\.\/([\d\.]+)$/", "search" : "headers[server]" },
			{ "version" : "/^Quantum Corporation\.\/([\d\.]+)$/", "search" : "headers[server]" },
		]
		return(self.rules)
