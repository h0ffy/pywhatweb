import plugins


class Pluginruby_on_rails_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"url": "/images/rails.png", "md5": "450fc241fab7867e96536903244087f4'},
			{ "url" : "/404.html", "text" : "<!-- This file lives in public/404.html -->'},
			{ "url" : "/422.html", "text" : "<!-- This file lives in public/422.html -->'},
			{ "url" : "/500.html", "text" : "<!-- This file lives in public/500.html -->'},
			{ "url" : "/404.html", "md5" : "adc851c2e0698b5d05ef0380ed69f6b9'},{ "url" : "/422.html", "md5" : "c6bd78379a0ad92caa6cbef7de676ce8'},
			{ "url" : "/javascripts/application.js", "text" : "// This file is automatically included by javascript_include_tag :defaults'},
			{ "url" : "/doesnotexist", "text" : "<title>The page you were looking for doesn't exist (404)</title>", "md5" : "adc851c2e0698b5d05ef0380ed69f6b9'},
			{ "url" : "/stylesheets/scaffold.css", "text" : "#errorExplanation h2 {'},
			{ "regexp" : "/<link[^>]*href="[^"]*\/assets\/application-?\w{32}?\.css"/" },
			{ "regexp" : "/<script[^>]*\/assets\/application-?\w{32}?\.js"/" },
			{ "regexp" : "/<meta content="authenticity_token" name="csrf-param"\s?\/>\s?<meta content="[^"]{44}" name="csrf-token"\s?\/>/" },
			{ "text" : "<h3><a href="rails/info/properties" onclick="about(); return false">About your application&rsquo;s environment</a></h3>", "string" : "default page'},
			{ "text" : "<p>Run <tt>rake db:migrate</tt> to create your database. If you're not using SQLite (the default)", "edit <tt>config/database.yml</tt> with your username and password.</p>", "string" : "default page'},
			{ "certainty" : "75", "text" : "<title>Action Controller: Exception caught</title>" },
			{ "filepath" : "/<p><code>RAILS_ROOT: ([^<]+)<\/code><\/p>/" },
			{ "text" : "<div id="session_dump" style="display:none"><pre class=\'debug_dump\'>---" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^request_method/", "name" : "request_method cookie" },
		]
	return(self.rules)
