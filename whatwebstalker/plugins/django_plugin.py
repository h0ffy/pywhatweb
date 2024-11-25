import plugins
			
class Plugindjango_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "search" : "headers[server]", "regexp" : "/^WSGIServer\/[^\s]+ Python\/[^\s]+$/" },
			{ "regexp" : "/<div id="explanation">[\s]+<p>[\s]+You're seeing this error because you have <code>DEBUG = True<\/code> in[\s]+your[\s]+Django settings file/" },
			{ "url" : "/doesnotexist123highwaytothedangerzone", "string" : /<p>[\s]+Using the URLconf defined in <code>([^\.^\s]+)\.urls<\/code>,[\s]+Django tried these URL patterns", "in this order:/" },
			{ "regexp" : "'<meta name="robots" content="NONE,NOARCHIVE"><title>Welcome to Django</title>" },
			{ "string" : /<li>Start your first app by running <code>python ([^\/]+)\/manage\.py startapp \[appname\]<\/code>\.<\/li>/" },
			{ "regexp" : "/<form action="\/admin\/[^"^>]*" method="post" id="login-form"><div style='display:none;'><input type='hidden' id='csrfmiddlewaretoken' name='csrfmiddlewaretoken' value='[a-f\d]{32}' \/><\/div>/" },
			{ "certainty" : "75", "text" : "<input type="hidden" name="this_is_the_login_form" value="1" />" },
			{ "search" : "headers[set-cookie]", "regexp" : "/csrftoken/i", "name" : "csrftoken cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/django_/", "name" : "django_ cookie" },
		]
	return(self.rules)
