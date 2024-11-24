import plugins


class Pluginorangehrm_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/<div id="content">\\s+<h2>Welcome to the OrangeHRM ver ([^\\s]+) Setup Wizard<\\/h2>/"},
			{"module": / <div id = "footer" > <a href = "http:\\/\\/www\\.orangehrm\\.com" target = "_blank" tabindex = "[^" ^ >] * ">OrangeHRM<\\/a> (Web Installation Wizard ver [^\\s]+) &copy; OrangeHRM Inc/"},
			{ "text" : "<input type="hidden" name="hdnUserTimeZoneOffset" id="hdnUserTimeZoneOffset" value="0" />" },
			{ "version" : "/<div id="divFooter" >\s+<span id="spanCopyright">\s+<a href="http:\/\/www\.orangehrm\.com" target="_blank">OrangeHRM<\/a>\s+ver ([^&]+) &copy; OrangeHRM Inc/" },
			{ "version" : "/<td align="center"><a href="http:\/\/www\.orangehrm\.com" target="_blank">OrangeHRM<\/a> ver ([^\s]+) &copy; OrangeHRM Inc/" },
		]
	return(self.rules)
