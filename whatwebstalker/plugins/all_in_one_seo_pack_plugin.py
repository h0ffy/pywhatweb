import plugins
			
class Pluginall_in_one_seo_pack_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- /all in one seo pack -->" },
			{ "version" : "/<!-- All in One SEO Pack ([\d\.]+) by Michael Torbert of Semper Fi Web Design/" },
		]
<<<<<<< HEAD
	return(self.rules)
=======
        return(self.rules)
>>>>>>> parent of c1541b4c (Merge branch 'main' of https://github.com/h0ffy/pywhatweb)
