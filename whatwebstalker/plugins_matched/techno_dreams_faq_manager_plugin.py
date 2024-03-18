import plugins
			
class Plugintechno_dreams_faq_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "		<a href="admin/">Admin Area</a></td></tr></table></body></html>" },
			{ "text" : "		<td><font size="-1">&nbsp;</font><p><b><font size="-1">FAQ ADMIN AREA</font></b></td>" },
		]
		return(self.rules)

