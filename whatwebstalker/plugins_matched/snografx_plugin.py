import plugins
			
class Pluginsnografx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<!-- Website designed[\ and powered]* by [^\|]+\|\| Visit: http:\/\/snografx.com\/ -->/" },
			{ "text" : "var snoOff = new Image();snoOff.src = "xfx/snografx0.gif";var snoOn = new Image();snoOn.src = "xfx/snografx2.gif";" },
			{ "text" : "var snoOff = new Image();snoOff.src = "4fx/00sno.png";var snoOn = new Image();snoOn.src = "4fx/02sno.png";" },
			{ "text" : "Website powered by: <a href='http://snografx.com/' target='_blank'>Snöfx</a>" },
		]
	return(self.rules)
