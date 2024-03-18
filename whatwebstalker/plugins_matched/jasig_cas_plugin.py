import plugins
			
class Pluginjasig_cas_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<p>Powered by <a href="http:\/\/www\.ja-?sig\.org\/(products\/)?cas">Jasig Central Authentication Service ([^<^\s]+)<\/a><\/p>/", "offset" : "1 },
			{ "text" : "<title>CAS &#8211; Central Authentication Service</title>" },
			{ "text" : "<!-- Congratulations on bringing CAS online!  The default authentication handler authenticates where usernames equal passwords: go ahead", "try it out.  -->" },
			{ "text" : "<p>Powered by <a href="http://www.jasig.org/cas">Jasig Central Authentication Service</a></p>" },
		]
		return(self.rules)
