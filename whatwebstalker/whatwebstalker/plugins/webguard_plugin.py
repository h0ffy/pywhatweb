import plugins


class Pluginwebguard_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "text": "<title>WebGuard Login</title>"},
			{"text": "<body leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" onLoad="GetInfo()" onResize="fit_center()">"},
			{"text": "<table id=loginback border="0" cellpadding="0" cellspacing="0" background="images / login_venus_back.gif" width=480 height=175 style=\'POSITION:absolute\'>"},
			{"text": "<td align="left" valign="middle"><input name="login_passwd" type="password" class="noborder" size="26"></td>"},
			{"url": "/UISelect.js", "version": "/var _VERSION = " < acronym title = '([^'] +)'><table border='0'/" },
			{ "url" : "/images/login_back.gif", "md5" : "4617667f3ec03b31a9971ff1c03da57e" },
			{ "md5" : "457dff12099372b8415b29e2e50c3910" },
		]
	return(self.rules)
