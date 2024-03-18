import plugins
			
class Pluginphpmyrealty_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Main Content table : stop -->" },
			{ "text" : "Powered by <a href="http://www.phpmyrealty.com" target="_blank" style="font-size: 12px; font-family: arial">phpMyRealty Professional</a>" },
			{ "text" : "<span class="table_header_text"> &nbsp;Administrator Control Panel</span>" },
		]
		return(self.rules)
