import plugins
			
class Pluginhp_officejet_printer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "/<title>HP Officejet ([^<]+)<\/title>.*<body onLoad="window.top.location.href='.\/index.htm\?cat=info&page=printerInfo/m },
			{ "model" : "/<title>HP Officejet (Pro [A-Z0-9a-z ]+)<\/title>.*(home.htm\?cat=home&page=home|printerFrame.htm)/m},
			{ "text" : "index.htm?cat=info&page=printerInfo'},
			{ "certainty" : "25", "text" : "home.htm?cat=home&page=home'},
		]
		return(self.rules)
