import plugins
			
class Pluginsabnzbd_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/    <form action="\/sabnzbd\/[^"]*" method="POST">/" },
		]
	return(self.rules)

