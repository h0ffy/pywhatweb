import plugins
			
class Pluginab_web_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : '<a href="#" onclick="maximize();" class="hdp_z01_z03_l" onmouseover="ShowIB(\\"' },
			{ "text" : '<div style="text-align: center;"><br /><br /><a href="#" onclick="imprfct();" class="main_link">[Imprimer]</a></div>' },
			{ "version" : r"/&nbsp;<a href=\"http:\/\/www.(ab-psi.com|aeline-informatique.com)\" class=\"bdp_z01_z02_l\">[^<]+ AB WEB v. ([\d\.]+)<\/a>/", "offset" : "1" },
		]
        return(self.rules)