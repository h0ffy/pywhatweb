import plugins
			
class Pluginwarcraft_3_frozen_throne_config_file_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "// Radius to give XP to teammates near where the special objective is completed (rescued hosties", "bomb planted", "killed vip", "vip escaped", "default is 750)" },
		]
		return(self.rules)
