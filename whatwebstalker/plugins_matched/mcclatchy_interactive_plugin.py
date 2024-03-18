import plugins
			
class Pluginmcclatchy_interactive_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : " %r{<script type="text/javascript" src="http://media.\w+.com/mistats/mianalytics.js"></script>} },
			{ "text" :  'miAppControler contains master settings that can be used to quickly disable" },
		]
		return(self.rules)
