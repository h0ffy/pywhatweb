import plugins
			
class Pluginmotorito_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- end META_TAGS subst -->" },
			{ "text" : "<!-- CAL POSAR UN DISCRIMINADOR DE NAVEGADORS PER CARREGAR ELS ESTILS ADEQUATS -->" },
		]
		return(self.rules)
