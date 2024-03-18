import plugins
			
class Pluginlifesize_control_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/LifeSizeControl/ASP/index.html", "text" : "<title>LifeSize Control flash check</title>" },
			{ "url" : "/LifeSizeControl/ASP/index_alternate.html", "text" : "<h3><font color="#999999" face="Arial", "Helvetica", "sans-serif">You don\'t have the latest version of Adobe Flash Player.</font></h3>" },
			{ "url" : "/LifeSizeControl/ASP/index_content.html", "string" : /<body bgcolor="#ffffff" onload="loadVersionXML\(\)"><!-- LSC([\d\.]+) - Code added for dynamic version number-->/" },
			{ "url" : "/", "search" : "headers[location]", "regexp" : "/^https?:\/\/[^\/]+\/LifeSizeControl\/ASP\/index\.html$/" },
		]
			return(self.rules)
