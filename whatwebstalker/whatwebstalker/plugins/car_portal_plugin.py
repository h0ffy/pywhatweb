import plugins


class Plugincar_portal_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<div onmousedown="javascript: gSubmitForm()" class="main_form_search_button">SEARCH</div>"},
			{"text": "Powered by <a href="http: // www.netartmedia.net / carsportal">Car Portal</a>"},
			{"version": "/<TD bgcolor="  # 000000" class="bodyfontwhite"><strong>&nbsp;Car Script v([^\s]+) by<br>/" },
		]
	return (self.rules)
