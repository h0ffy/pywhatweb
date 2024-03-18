import plugins
			
class Pluginphp_easy_data_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id='phpeasydata_container'  >" },
			{ "text" : "  <head><title>PhpEasyData login page</title>" },
			{ "version" : "/<a[^>]*href="http:\/\/www.(phpeasydata.com|freewebmaster-scripts.com\/phpeasydata)[^>]*>PHPEasyData[\s]*([^<]+)<\/a>/" },
			{ "version" : "/n main de pages dynamiques. " target="_blank"[\s]*>PhpEasyData[\s]*([^<]+)<\/a><\/b>/" },
		]
	return(self.rules)
