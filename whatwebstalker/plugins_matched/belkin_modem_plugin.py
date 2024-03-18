import plugins
			
class Pluginbelkin_modem_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "html comments", "regexp" : "/\/\/ when proto = Bridge or ipExt = 1", "DHCP should show disabled/" },
			{ "text" : "href=\"main_router.css\" src=\"showMenu.js\" },
			{ "version" : "2307 wireless router", "text" : "<meta name=\"description\" content=\"Belkin 2307"},
			{ "version" : "F5D7230-4P", "text" : "<td bgcolor=\"#94CAE4\" width=\"50%\" height=\"18\">F5D7230-4P</td>"},
			{ "name" : "inline javascript", "text" : "var isPPPoE", "isStatic", "isDynamic", "isnat", "isdialup", "isbigpond", "ispptp", "isfirewall;"},
		]
	return(self.rules)
