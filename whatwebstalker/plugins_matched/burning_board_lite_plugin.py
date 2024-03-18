import plugins
			
class Pluginburning_board_lite_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by <a href="http:\/\/www.woltlab.de[^>]*>Burning Board[\s]*<\/a>/" },
			{ "version" : "/Powered by <b><a href="http:\/\/www.woltlab.de" target="_blank">Burning Board ([^<]+)<\/a><\/b>/" },
			{ "version" : "/Powered by <b>Burning Board ([\d\.]+)<\/b>/" },
			{ "version" : "/<p class="copyright"><a href="http:\/\/www.woltlab.com">Forum Software: <strong>Burning Board&reg; ([\d\.]*)<\/strong>", "developed by <strong>WoltLab&reg; GmbH<\/strong><\/a><\/p>/" },
		]
		return(self.rules)

