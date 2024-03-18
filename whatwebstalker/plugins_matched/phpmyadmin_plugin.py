import plugins
			
class Pluginphpmyadmin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "intitle:phpMyAdmin "Language: Afrikaans" "Welcome to phpMyAdmin"" },
			{ "version" : "/<title>phpMyAdmin ([^\s^<]+)[^<]*<\/title>/" },
			{ "version" : "/PMA_VERSION\:"([0-9\.]+)",auth_type},
			{ "version" : "/<h2>Welcome to  phpMyAdmin ([^<]+)<\/h2>/" },
			{ "text" : "<img src="./themes/original/img/logo_right.png" id="imLogo" name="imLogo" alt="phpMyAdmin" border="0" /></a>" },
			{ "md5" : "d037ef2f629a22ddadcf438e6be7a325", "url" : "favicon.ico" },
			{ "regexp" : "/<form method="post" action="index\.php" target="_(top|parent)"><input type="hidden" name="phpMyAdmin" value="/" },
		]
		return(self.rules)
