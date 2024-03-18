import plugins
			
class Pluginkonica_minolta_printer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "search" : "headers[server]", "version" : "/^LPC Http Server\/V([^\s]+)/" },
			{ "model" : "/<head><meta http-equiv=content-type content=text\/html; charset=[^\s^>]+><TITLE>KONICA MINOLTA .+ ([^<^\s]+)<\/TITLE>/" },
			{ "url" : "/wcd/js_error.xml", "text" : "<?xml-stylesheet href="js_error.xsl" type="text/xsl"?>" },
			{ "text" : "<meta http-equiv="refresh" content="0; URL=/wcd/js_error.xml">" },
		]
			return(self.rules)
