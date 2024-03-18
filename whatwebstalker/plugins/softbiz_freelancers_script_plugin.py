import plugins
			
class Pluginsoftbiz_freelancers_script_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "                  <div align="center"><font size="3"><strong>Softbiz SEO Freelancers Script</strong><br>" },
			{ "text" : "<div align="right"><!-- --><font style="font-family: Arial", "Helvetica", "sans-serif;font-size: 12px;font-style: normal;color: #009900;font-weight: bold;">Powered By <a href="http://www.softbizscripts.com/freelancers-script-features.php" style="font-family: Arial", "Helvetica", "sans-serif;font-size: 12px;font-style: normal;color: #0099FF;font-weight: normal;" title="Softbiz Freelancers Script" target="_blank" >Freelancers script</a></font></div>" },
		]
	return(self.rules)
