import plugins
			
class Pluginmailenable_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "</table><!-- loginPanel_shell_table -->" },
			{ "text" : "<td class="loginPanel_botLeft"><div class="loginPanel_botLeft_div"></div></td>" },
			{ "certainty" : "75", "text" : "<title>MailEnable - Webmail</title>" },
		]
		return(self.rules)
