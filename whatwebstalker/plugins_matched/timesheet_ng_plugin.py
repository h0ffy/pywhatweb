import plugins
			
class Plugintimesheet_ng_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "md5" : "df3e567d6f16d040326c7a0ea29a4f41", "url" : "images/spacer.gif" },
			{ "text" : "<!-- include the timesheet face up until the heading start section -->" },
			{ "text" : "<td><img class="login_image" src="images/spacer.gif"></td>" },
			{ "text" : "<META name="description" content="Timesheet Next Gen">" },
		]
		return(self.rules)
