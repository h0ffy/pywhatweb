import plugins
			
class Pluginsonicwall_gms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<TITLE>SonicWALL Global Management System Version ([^\s^<])[\s]?<\/TITLE>/" },
			{ "version" : "/<P><B>SonicWALL Global Management System v([^\s^<]+)/" },
			{ "version" : "/<TITLE>SonicWALL Universal Management Suite v([^\s^<]+)<\/TITLE>/" },
			{ "version" : "/<P><B>SonicWALL Universal Management Suite v([^\s^<]+)<\/B>/" },
			{ "url" : "/sgms/login", "text" : "<title>SonicWALL GMS Login</title>" },
			{ "url" : "/sgms/login", "text" : "<title>SonicWALL GMS Login Screen</title>" },
			{ "text" : "<body background="images/gray_waves.back.gif" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="onLoadFunc()">" },
		]
		return(self.rules)
