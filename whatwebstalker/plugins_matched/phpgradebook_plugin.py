import plugins
			
class Pluginphpgradebook_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<title>phpGradeBook</title> " },
			{ "version" : "/<a href='http:\/\/phpGradeBook\.com'>PHP_GradeBook<\/a> ([^C^\n]+) Created by Robert/" },
			{ "version" : "/<small>PHP_GradeBook ([^C^\n]+) Created by Robert/" },
			{ "md5" : "9761e989848ed31a7d7a5a5411197281" },
		]
		return(self.rules)
