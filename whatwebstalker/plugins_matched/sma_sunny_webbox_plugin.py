import plugins
			
class Pluginsma_sunny_webbox_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/culture/index.dml", "account" : "["User","Installer"]", "version" : "/<UserLevels><Items><XmlItem name="[^"^\s]*"><Items \/><Value>User<\/Value><\/XmlItem><XmlItem name="[^"^\s]*"><Items \/><Value>Installer<\/Value><\/XmlItem><\/Items><\/UserLevels><\/Element><\/Content><StatusBar deviceKey="[^"^\s]*" hideDataTransfer="[^"^\s]*" hidePasswordSafety="[^"^\s]*" hidePlantTime="[^"^\s]*" hideUserLevel="[^"^\s]*" hideUpdateState="[^"^\s]*" noRefresh="[^"^\s]*" serialNumber="[\d]*" version="([^"^\s]+)" \/><\/Page>/" },
			{ "url" : "/", "regexp" : "/<title>Sunny WebBox<\/title>[\s]+<\/head>[\s]+<frameset rows="75,\*,22" frameborder="no" border="2" framespacing="0">/" },
			{ "url" : "/", "regexp" : "/<meta http-equiv="refresh" content="0; URL=\/culture\/index\.dml">[\s]+<meta http-equiv="Content-Type" content="text\/html; charset=utf-8">[\s]+<title>SMA Sunny Webbox<\/title>[\s]+<link rel="SHORTCUT ICON" href="\.\.\/img\/favicon\.ico">/" },
			{ "search" : "headers[server]", "regexp" : "/^(WebBox-20|Sunny WebBox)$/" },
		]
	return(self.rules)

