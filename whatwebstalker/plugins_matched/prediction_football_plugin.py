import plugins
			
class Pluginprediction_football_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Show the different leagues -->" },
			{ "text" : "<!-- Show the league ID if there is more than one. -->" },
			{ "regexp" : "/<!-- The display of powered by prediction football must not be removed without explicit permission\.[\s]+Unauthorized removal or modification of the powered by prediction football will require that[\s]+the associated payment is made\. -->/" },
			{ "version" : "/<small>Powered by <a target="_blank" class="VERSION" href="http:\/\/www\.predictionfootball\.com\/">[\s]+Prediction Football <\/a>([^\s^<]+)<\/small>/" },
		]
		return(self.rules)
