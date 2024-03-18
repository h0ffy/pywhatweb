import plugins
			
class Pluginvbulletin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Powered by vBulletin" inurl:newreply.php'},
			{ "certainty" : "75", "regexp" : "/\* vBulletin [0-9a-z.]+ CSS},
			{ "name" : "vbulletin_global.js", "regexp" : "/<script type="text\/javascript" src="[a-z0-9.\/]*vbulletin_global.js},
			{ "regexp" : "/Powered by(:)? vBulletin(&reg;)? Version},
			{ "certainty" : "50", "regexp" : "/Copyright &copy;2000 - [0-9]+", "Jelsoft Enterprises Ltd.},
			{ "version" : "/Powered by(:)? vBulletin(&reg;)? Version ([0-9a-z.]+)/", "offset" : "2", "name" : "version" },
			{ "version" : "/<meta name="generator" content="vBulletin ([0-9a-z.]+)" \/>/", "name" : "version" },
			{ "version" : "/\* vBulletin ([0-9a-z.]+) CSS/", "name" : "version" },
			{ "version" : "/clientscript\/vbulletin_md5\.js,qv=(\d+)\.pagespeed\..*?js">/", "name" : "version" },
			{ "version" : "/clientscript\/vbulletin-core\.js\?v=(\d+)/", "name" : "version" },
			{ "version" : "/\/vbulletin\/clientscript\/guestforum\.js\?v=(\d+)/", "name" : "version" },
			{ "version" : "/clientscript\/vbulletin_global\.js\?v=(\d+)/", "name" : "version" },
			{ "version" : "/\/vbulletin_read_marker\.js\?v=(\d+)/", "name" : "version" },
			{ "search" : "headers[set-cookie]", "regexp" : "/bblastactivity/", "name" : "bblastactivity cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/bblastvisit/", "name" : "bblastvisit cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/bbsessionhash/", "name" : "bbsessionhash cookie" },
		]
	return(self.rules)

