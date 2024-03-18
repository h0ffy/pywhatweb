import plugins
			
class Pluginmibew_messenger_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<p id="legal"><a href="http:\/\/mibew\.org\/" class="flink">Mibew Messenger<\/a> ([^\s]+) \| \(c\) 20[\d]{2} mibew\.org<\/p>/" },
			{ "certainty" : "75", "text" : "<div class="empty_inner" style=">&#160;</div>" },
		]
		return(self.rules)
