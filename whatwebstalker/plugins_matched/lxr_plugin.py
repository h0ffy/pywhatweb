import plugins
			
class Pluginlxr_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<hr>\nThis page was automatically generated by the \n<a href="http:blurb\.html">LXR engine<\/a>\.\n<br>\nVisit the <a href="http:\/\/lxr\.linux\.no\/">LXR main site<\/a> for more\ninformation\./" },
			{ "text" : "<b>[</b>&nbsp;<a href="ident">identifier search</a>&nbsp;<b>]</b>" },
			{ "text" : "[&nbsp;<a href="ident">identifier search</a>&nbsp;]" },
		]
		return(self.rules)

