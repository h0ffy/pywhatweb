import plugins


class Pluginluci_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<a style="color: white; text - decoration: none" href=" / cgi - bin / luci">LuCI - Lua Configuration Interface</a>"},
			{"text": "<link rel="stylesheet" type="text / css" media="screen" href=" / luci - static / openwrt.org / cascade.css" />"},
			{"text": "<li><a href=" / cgi - bin / luci / admin / ">Administration</a></li>"},
			{"url": "/luci-static/openwrt.org/header.png",
			    "md5": "aba24739c2534a161fab2485e605a960"},
			{"version": "/<p class="luci"><a href="\/cgi-bin\/luci\/about">Powered by LuCI [^<]+ \(v([^\)]+)\)<\/a><\/p>/", "offset" : "0 },
			{ "version" : "/<p class="luci"><a href="\/cgi-bin\/luci\/about">Powered by LuCI ([\d\.]+)<\/a><\/p>/" },
			{ "firmware" : "/<div id="header">[\r\n]*<h1>OpenWrt Firmware<\/h1>[\r\n]*<p>[\r\n]*([^<]+)<br \/>[\r\n]*Load: [^<]{10,15}<br \/>[\r\n]*Hostname: ([^\r\n<]+)[\s]*<\/p>[\r\n]*<\/div>/", "offset" : "0 },
			{ "string" : /<div id="header">[\r\n]*<h1>OpenWrt Firmware<\/h1>[\r\n]*<p>[\r\n]*([^<]+)<br \/>[\r\n]*Load: [^<]{10,15}<br \/>[\r\n]*Hostname: ([^\r\n<]+)[\s]*<\/p>[\r\n]*<\/div>/", "offset" : "1 },
		]
	return(self.rules)
