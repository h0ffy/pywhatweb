import plugins
			
class Pluginqr_code_panel_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<tr><td width='100%' align='center' class='small'>QR-Code Panel<a title='V[^\s^<]+ \([\d]{2}\/[\d]{2}\/[\d]{4}\)'> V([^\s^<]+)<\/a><br \/>/" },
			{ "certainty" : "75", "regexp" : "/&copy; [\d]{4} by <a href='http:\/\/www\.g0lgs\.co\.uk\/downloads\.php'>G0LGS<\/a><\/td><\/tr>/" },
		]
		return(self.rules)
