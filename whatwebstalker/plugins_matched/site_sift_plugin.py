import plugins
			
class Pluginsite_sift_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "inurl: "index.php?go=detail id="" },
			{ "certainty" : "25", "ghdb" : "inurl: "index php go addpage"" },
			{ "certainty" : "25,"ghdb" : "powered by Site Sift"" },
			{ "regexp" : "/<div align="center" class="copyright">powered by <A class="bottomlink" href="http:\/\/[scripts|www]+.site-sift.com[\/]*">Site Sift[^<]*<\/A><\/div>/i },
			{ "text" : "				<!-- end of header.php -->" },
			{ "text" : "				<!-- begin of footer.php -->" },
		]
		return(self.rules)

