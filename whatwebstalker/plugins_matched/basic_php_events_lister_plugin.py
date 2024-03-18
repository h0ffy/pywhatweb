import plugins
			
class Pluginbasic_php_events_lister_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by: <a href="http://www.mevin.com/">mevin productions</a>" },
			{ "text" : "<br /><center><input class="text" type="submit" name="submitBtn" value="Login" /></center>" },
			{ "text" : "<center><br> <a href=recover.php>Lost your password?</a></center>" },
		]
		return(self.rules)

