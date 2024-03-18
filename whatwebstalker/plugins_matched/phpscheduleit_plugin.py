import plugins
			
class Pluginphpscheduleit_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div align="left"><img src="img/phpScheduleIt.png" alt="logo" vspace="5"/></div>" },
			{ "text" : "<p align="center">Powered by <a href="http://phpscheduleit.sourceforge.net">phpScheduleIt</a></p>" },
			{ "text" : "<p align="right"><a href="http://phpscheduleit.sourceforge.net">Powered By phpScheduleIt" },
			{ "text" : "<br>Powered By: phpScheduleIt</p>", "certainty" : "75 },
			{ "version" : "/<p align="center">[<!\-]*<a href="http:\/\/phpscheduleit.sourceforge.net">[\->]*Powered By phpScheduleIt v([\d\.]+)[<!\-]*<\/a>[\->]*<\/p>/" },
			{ "version" : "/<p align="center"><a href="http:\/\/phpscheduleit.sourceforge.net">phpScheduleIt v([\d\.]+)<\/a><\/p>/" },
			{ "version" : "/<p align="center">Powered by <a href="http:\/\/phpscheduleit.sourceforge.net">phpScheduleIt v([\d\.]+)<\/a><\/p>/" },
			{ "version" : "/[P|p]?owered by <a href="http:\/\/phpscheduleit.sourceforge.net"[^>]*>phpScheduleIt v([\d\.]+)<\/a>/" },
		]
	return(self.rules)

