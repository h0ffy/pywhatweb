import plugins
			
class Pluginnewscoop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/newscoop\.sourcefabric\.org\/" target="_blank">\s+Newscoop<\/a>&nbsp;([\d\.]+)[^,]*,\s+the open content management system for professional journalists\./" },
			{ "text" : "Powered by Newscoop", "the open content management system for professional journalists.<br />" },
			{ "text" : "Powered by <a href="http://newscoop.sourcefabric.org/" target="_blank">Newscoop</a>", "the open content management system for professional journalists." },
			{ "text" : "<meta name="generator" content="Newscoop" />" },
		]
		return(self.rules)
