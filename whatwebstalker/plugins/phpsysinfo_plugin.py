import plugins
			
class Pluginphpsysinfo_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Created by phpSysInfo"", "certainty" : "25 },
			{ "text" : "var sTargetURL = "index.php?disp=dynamic";" },
			{ "version" : "/Generated by[\s&nbsp;]*<a href="http:\/\/phpsysinfo.sourceforge.net[^>]*>[\s&nbsp;]*phpSysInfo[\s&nbsp;]*-[\s&nbsp;]*([^<]+)<\/a>/" },
			{ "version" : "/Created by[\s&nbsp;]*<a href="http:\/\/phpsysinfo.sourceforge.net[^>]*>[\s&nbsp;]*phpSysInfo[\s&nbsp;]*-[\s&nbsp;]*([^<]+)<\/a>/" },
			{ "version" : "/<span>Created by <\/span><a href="http:\/\/phpsysinfo.sourceforge.net\/"><span>phpSysInfo - <\/span><span>([^<]+)<\/span>/" },
			{ "os" : "/<td style="width:160px; "><span>Kernel Version<\/span><\/td><td>([^<]+)<\/td><\/tr>/" },
			{ "os" : "/<td valign="top"><font size="-1">Distro Name<\/font><\/td>[\r\n\s]*<td><img[^>]+>[\s&nbsp;]*<font size="-1">([^<]+)<\/font><\/td>/" },
			{ "os" : "/<td valign="top"><font size="-1">Kernel Version<\/font><\/td>[\r\n\s]*<td><font size="-1">([^<]+)<\/font><\/td>/" },
		]
	return(self.rules)
