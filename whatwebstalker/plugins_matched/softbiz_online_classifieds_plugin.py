import plugins
			
class Pluginsoftbiz_online_classifieds_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "                    Classifieds PLUS Script</strong> - ADMIN PANEL</font></p>" },
			{ "text" : "<!-- --><font style="font-family: Arial", "Helvetica", "sans-serif;font-size: 12px;font-style: normal;color: #009900;font-weight: bold;">Powered By <a href="http://www.softbizscripts.com/classified-ads-plus-script-features.php" style="font-family: Arial", "Helvetica", "sans-serif;font-size: 12px;font-style: normal;color: #0099FF;font-weight: normal;" title="Classified Ads Plus PHP Script" target="_blank" >Softbiz Scripts</a></font>" },
		]
		return(self.rules)
