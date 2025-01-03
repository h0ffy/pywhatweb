import plugins


class Plugincouchpotato_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<html><body><h1>Error 401 Unauthorized</h1>Something unexpected has happened.</body></html>", "certainty": "25 },
			{ "version" : "/<a href="\/cron\/force\/">Force check<\/a> \)[\s]+<\/div>[\s]+<div id="version">[\s]+Version: <em>([^\s^<]+)<\/em>/" },
			{ "md5" : "a59c6fead5d55050674f327955df3acb", "url" : "/static/images/favicon.ico" },
			{ "md5" : "4814f0d48b2944e48d474325fc4a0f86", "url" : "/static/images/homescreen.png" },
		]
	return(self.rules)
