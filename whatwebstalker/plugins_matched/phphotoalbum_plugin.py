import plugins
			
class Pluginphphotoalbum_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>My Picture Album</title>", "certainty" : "75 },
			{ "version" : "/<td align="right"><font style="font-face:Verdana; font-size:9; font-color:#000000;">Powered By: <a href="http:\/\/www.phphq.net\/\?script=phPhotoAlbum" target="_blank"><b>phPhotoAlbum v([\d\.]+)<\/b><\/a><\/font><\/td>/" },
		]
	return(self.rules)
