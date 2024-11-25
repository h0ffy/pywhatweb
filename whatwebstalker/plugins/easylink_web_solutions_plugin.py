import plugins
			
class Plugineasylink_web_solutions_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Dieser Abschnitt darf nur mit Genehmigung des Entwicklers entfernt werden und bedarf einer" },
			{ "version" : "/<meta name="generator" content="easyLink v([\d\.]+)" \/>/" },
			{ "version" : "/[P|p]?owered by easyLink v([\d\.]+)/" },
		]
	return(self.rules)
