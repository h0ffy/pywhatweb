import plugins
			
class Pluginmagimagebank_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "</div></div><div id="SiteBottom" class="fun"></div><div id=\'SiteFooter\'>" },
			{ "regexp" : "/<link href="\/imagebank\/stylesheets\/fancybox\.css\?[\d]+" media="screen" rel="Stylesheet" type="text\/css" \/>/" },
			{ "text" : "Powered by MagImageBank | <a href="http://magimagebank.com/">magimagebank.com</a> | <a href="mailto:info@magimagebank.com">info@magimagebank.com</a>" },
		]
	return(self.rules)
