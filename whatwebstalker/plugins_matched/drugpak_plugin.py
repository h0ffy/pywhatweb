import plugins
			
class Plugindrugpak_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<LINK REL=StyleSheet HREF="<#imagepath>/<#_style1 default=dpstyle.css>" TYPE="text/css" MEDIA=screen>" },
			{ "certainty" : "25", "text" : "<!--Assist making SSL connection-->" },
			{ "text" : "<hr>Powered by DrugPak</body>" },
			{ "text" : "<LINK REL=StyleSheet HREF="/dplimg/DPSTYLE.CSS" TYPE="text/css" media="all">" },
			{ "regexp" : "/<!--Request processed in [\d]{2} min", "[\d]{2} sec", "[\d]{3} ms--><\/BODY>/" },
		]
		return(self.rules)
