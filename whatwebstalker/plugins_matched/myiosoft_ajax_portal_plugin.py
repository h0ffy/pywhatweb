import plugins
			
class Pluginmyiosoft_ajax_portal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/      <td align="right"  style="padding:5px; background-color: #EDF2FB;" nowrap> Powered by <a href="http:\/\/myiosoft.com\/\?[\d\.]+">Ajax Portal ([\d\.]+)<\/a><\/td>/" },
		]
	return(self.rules)

