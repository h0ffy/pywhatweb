import plugins
			
class Pluginacti_web_configurator_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>Web Configurator - Version ([^\s]*\s?v[^<]+)<\/title>/" },
			{ "regexp" : "/<form name="frm(LOGIN|Config)" method="POST" enctype="multipart\/form-data" action="videoconfiguration\.cgi">/" },
			{ "string" : /<tr class="layout_footer_bgcolor">\s*<td width="776"[^>]*>\s+Copyright@2003-(20[\d]{2}) ACTi Corporation All Rights Reserved/" },
		]
	return(self.rules)
