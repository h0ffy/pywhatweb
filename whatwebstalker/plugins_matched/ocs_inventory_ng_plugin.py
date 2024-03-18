import plugins
			
class Pluginocs_inventory_ng_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<LINK REL='StyleSheet' TYPE='text/css' HREF='css/ocsreports.css'>" },
			{ "version" : "/<img src=image\/banner-ocs\.png><\/a><\/td><td width='33%' align='right'>[\s]+<b>Ver\. ([^&]+)&nbsp&nbsp&nbsp;<\/b>/" },
		]
	return(self.rules)
