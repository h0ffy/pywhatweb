import plugins
			
class Pluginpygopherd_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<BR>Generated by <A HREF="http://www.quux.org/devel/gopher/pygopherd">PyGopherd</A>" },
			{ "regexp" : "/<HTML><HEAD><TITLE>Selector Not Found<\/TITLE>[\s]+<H1>Selector Not Found<\/H1>/" },
		]
		return(self.rules)
