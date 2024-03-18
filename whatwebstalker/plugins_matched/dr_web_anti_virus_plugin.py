import plugins
			
class Plugindr_web_anti_virus_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/DRWEB_PERSONAL_OFFICE=[^;]*;/" },
			{ "md5" : "b3465a1bb7fa5ca9e63d2924f4f7a865", "url" : "/avdesk/includes/system/templates/images/logo_en.png" },
			{ "md5" : "2ef77c5015f2a5aee1633d58a32037ef", "url" : "/avdesk/includes/system/templates/images/logo_ru.png" },
			{ "filepath" : "/var _globalVars = \{\s+'mailSystem': "\d*',\s+'sessionTmout': "\d*',\s+'rootDir': "[^']+',\s+'https': "\d',\s+'currentPage': "([^']+)',/" },
			{ "text" : "<div id="logo" class="logo"><img src="/avdesk/includes/system/templates/images/logo_en.png" alt=" /></div>" },
		]
		return(self.rules)
