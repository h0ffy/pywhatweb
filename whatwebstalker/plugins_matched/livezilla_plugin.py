import plugins
			
class Pluginlivezilla_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<td colspan="2" width="400" align="center" (class|id)="lz_index_light_text">LiveZilla is a registered trademark<br>of LiveZilla GmbH<br><br>Version ([\d\.]+)<\/td>/", "offset" : "1 },
			{ "text" : "<td><br><br><br><strong>Thank you for using LiveZilla!</strong></td>" },
			{ "text" : "<!-- http://www.LiveZilla.net Tracking Code --><div id="livezilla_tracking" style="display:none"></div>" },
			{ "text" : "<address><a href="http://www.livezilla.net" target="_blank">LiveZilla - Freeware Live Support</a></address>" },
			{ "certainty" : "25", "text" : "<meta name="author" content="LiveZilla GmbH">" },
			{ "text" : "<title>LiveZilla - Freeware Live Support - http://www.livezilla.net</title>" },
		]
		return(self.rules)
