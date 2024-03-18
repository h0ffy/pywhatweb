import plugins
			
class Pluginphpmyfaq_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="phpMyFAQ ([\d\.]+)" \/>/" },
			{ "version" : "/<p id="copyrightnote">powered by <a href="http:\/\/www.phpmyfaq.de[\/]*" target="_blank">phpMyFAQ<\/a> ([\d\.]+)/" },
			{ "md5" : "8390bf2d1fe24799bbd381d1b7d6d00b", "url" : "template/favicon.ico" },
			{ "md5" : "8390bf2d1fe24799bbd381d1b7d6d00b", "url" : "template/default/favicon.ico" },
		]
	return(self.rules)

