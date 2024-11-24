import plugins


class Pluginc99_shell_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "Dir: <input type="text" name="directory" method="get"> <input type="submit" value="List Directory"><br><br> eg: /etc/<br>"},
			{"text": "<center>Php Safe-Mode Bypass (List Directories):     <form action="" },
		]
	return(self.rules)
