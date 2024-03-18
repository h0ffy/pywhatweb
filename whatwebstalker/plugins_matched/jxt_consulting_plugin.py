import plugins
			
class Pluginjxt_consulting_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="jxt-popup-wrapper">" },
			{ "text" : "<!-- Dynamic white label meta content -->" },
			{ "regexp" : "/Powered by <a href="http:\/\/(www\.)?jxt\.com\.au" target="_blank">JXT Consulting<\/a>/" },
			{ "text" : "<a href="http://www.jxt.com.au" target="_blank">Powered by JXT Consulting</a>" },
			{ "string" : /<link rel="shortcut icon" href="\/GetWhitelabelFile\.aspx\?whiteLabelFileID=(\d+)"\s?\/>/" },
		]
		return(self.rules)
