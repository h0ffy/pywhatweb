import plugins
			
class Pluginspip_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div class="formulaire_spip formulaire_recherche"" },
			{ "version" : "/<meta name="generator" content="SPIP ([^\s]+) \[[\d]+\]"( \/)?>/" },
			{ "search" : "headers[composed-by]", "version" : "/SPIP ([^@]{1,10}) @ www\.spip\.net/" },
			{ "search" : "headers[composed-by]", "module" : /SPIP [^@]{1,10} @ www\.spip\.net \+ (.+)/" },
			{ "search" : "headers[composed-by]", "regexp" : "/SPIP @ www\.spip\.net/" },
			{ "search" : "headers[x-spip-cache]", "regexp" : "/^.+$/" },
			{ "text" : "<a href="spip.php" },
			{ "text" : "<img src=\'/spip" },
		]
			return(self.rules)
