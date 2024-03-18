import plugins
			
class Pluginsitemajic_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td width=109 align='left'><input type='text' name='UserName' size='20' style='font-family: Arial; font-size: 8pt;' onKeyPress=\"if (event.keyCode == 13) { document.frm.Password.focus(); return false;	} else return true;\" ></td>" },
			{ "text" : "Website Powered by <a href='http://www.sitemajic.com' style='text-decoration:none'>SiteMajic</a>" },
		]
			return(self.rules)
