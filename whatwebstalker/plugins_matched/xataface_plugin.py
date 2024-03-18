import plugins
			
class Pluginxataface_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- custom javascripts can go in slot "custom_javascripts" -->" },
			{ "text" : "<!-- Place any other items in the head of the document by filling the "head_slot" slot -->" },
			{ "string" : /<div class="fineprint">[\s]+Powered by Xataface<br\/>[\s]+\(c\) 2005-(20[\d]{2}) All rights reserved<\/div>/" },
		]
		return(self.rules)
