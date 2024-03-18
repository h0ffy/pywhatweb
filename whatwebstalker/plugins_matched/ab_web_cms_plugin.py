import plugins
			
class Pluginab_web_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "inurl:ab_fct.php?fct=" },
			{ "text" : "<a href="#" onclick="maximize();" class="hdp_z01_z03_l" onmouseover="ShowIB(" },
			{ "text" : "<div style="text-align: center;"><br /><br /><a href="#" onclick="imprfct();" class="main_link">[Imprimer]</a></div>" },
			{ "version" : "/&nbsp;<a href="http:\/\/www.(ab-psi.com|aeline-informatique.com)" class="bdp_z01_z02_l">[^<]+ AB WEB v. ([\d\.]+)<\/a>/", "offset" : "1 },
		]
		return(self.rules)
