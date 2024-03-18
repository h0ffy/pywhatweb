import plugins
			
class Pluginusp_secure_login_service_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Optional: If browser does not support Javascript", "load URL xyz -->" },
			{ "text" : "<!-- SLS JavaScripts -->" },
			{ "text" : "<form action="auth" method="post" name="LoginForm" onsubmit="return checkFormSubmit();" >" },
			{ "certainty" : "75", "regexp" : "/<input name="currentRequestedPage" type="hidden" value="[^"]+" \/><\/form>/" },
			{ "search" : "headers[slsstatus]", "string" : /^([\d]+)$/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/SLSLanguage=([a-z]{2,3});/" },
			{ "search" : "headers[set-cookie]", "module" : "zzzzzz", "regexp" : "/SCDID_S=[^;\s\$]{54}\$\$;/" },
		]
	return(self.rules)

