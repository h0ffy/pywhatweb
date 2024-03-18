import plugins
			
class Pluginsnort_report_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<br><br><br><br>Snort Report Version ([^<]+)<br>Copyright 2000-20[\d]{2}", "<a href="http:\/\/www\.symmetrixtech\.com">Symmetrix Technologies", "LLC\.<\/a><\/td>/" },
			{ "text" : "<title>SNORT Report - Signature Detail ()</title>" },
		]
		return(self.rules)
