import plugins
			
class Plugindvwa_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "		<title>Damn Vulnerable Web App (DVWA) - Login</title>" },
			{ "regexp" : "/		<link rel="stylesheet" type="text\/css" href="[^"]*dvwa\/css\/login.css" \/>/" },
			{ "text" : "			<p><label for="pass">Password</label><input type="password" AUTOCOMPLETE="off" size="20" name="password"></p><br />" },
		]
			return(self.rules)
