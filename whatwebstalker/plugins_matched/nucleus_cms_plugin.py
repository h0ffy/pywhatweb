import plugins
			
class Pluginnucleus_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Nucleus CMS v([^"^>]+)" \/>/" },
			{ "filepath" : "/<td>Admin-area <strong>path<\/strong>:<\/td>[\s]+<td><input name="AdminPath" size="60" value="([^"]+)" \/>/" },
			{ "text" : "<meta name="name" content="My Nucleus CMS" />" },
			{ "version" : "/<small>Copyright \| <a href="http:\/\/nucleuscms\.org">Nucleus CMS v([^\s^>]+)<\/a> \|/" },
		]
		return(self.rules)
