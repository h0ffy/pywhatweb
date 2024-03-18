import plugins
			
class Pluginavantfax_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="description" content="Web 2.0 HylaFAX management" />" },
			{ "text" : "</label><br /><br /><input type="password" name="password" id="password" style="width: 12em" maxlength="15" /></p><br />" },
			{ "search" : "headers[set-cookie]", "regexp" : "/AvantFAX=[a-z\d]{26}; path=\//" },
			{ "version" : "/<p><a href="http:\/\/www\.avantfax\.com" target="_blank"><img src="images\/avantfax-big\.png" border="0" alt="AvantFAX" \/><\/a><\/p>[\s]+<p align="center">([^\s^<]+)<\/p>/" },
		]
		return(self.rules)

