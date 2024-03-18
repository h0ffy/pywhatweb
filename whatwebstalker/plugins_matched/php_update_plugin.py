import plugins
			
class Pluginphp_update_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.php-update.co.uk" target="_blank">PHP-Update</a>" },
			{ "regexp" : "/Powered by <a href=[^>]*http:\/\/www.php-update.co.uk[^>]*>PHP[\ \-]*Update<\/a>/" },
			{ "regexp" : "/>Powered by PHP-Update<\/a>/i },
			{ "text" : "<a href="http://www.php-update.co.uk">Powered by PHP-Update </a>" },
		]
	return(self.rules)

