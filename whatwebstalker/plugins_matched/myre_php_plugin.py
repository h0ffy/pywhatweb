import plugins
			
class Pluginmyre_php_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td align=right><a href='links_view.php'><font class='menu_top'><b><u>My Last Viewed</u></b></font></a>&nbsp;&nbsp;<a href='alert.php?action=register'><font class='menu_top'><b><u>Get e-mail alerts</u></b></font></a>&nbsp;&nbsp;" },
			{ "text" : "<!-- BEGIN: MENU FOOTER don't change anything -->" },
		]
		return(self.rules)
