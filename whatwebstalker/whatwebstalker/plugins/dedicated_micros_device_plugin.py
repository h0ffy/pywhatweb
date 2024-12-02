import plugins


class Plugindedicated_micros_device_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"url": "/gui/title.shtml",
     "model": "/^				var product = '([^']+)';[\\s]*$/"},
			{"url": "/common/script_variables.js.shtml", "model": "/^var SYSTEM_LOGO = "([ ^ "]+)"; [\s]*$/" },
			{ "url" : "/webpages/index.shtml", "text" : "	<title>DVIP</title>", "model" : "DVIP" },
			{ "search" : "headers[server]", "regexp" : "/^ADH-Web$/" },
		]
	return(self.rules)
