import plugins
			
class Pluginmahara_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- This site is powered by Mahara", "an Open Source" },
			{ "text" : "<!-- there is a div id="performance-info" wrapping this -->" },
			{ "text" : "<div id="powered-by"><a href="http://mahara.org/"><img src="" },
			{ "text" : "<script type="text/javascript">var strings = {"namedfieldempty":"The required field \"%s\" is empty","processing":"Processing","requiredfieldempty":"A required field is empty","unknownerror":"An unknown error occurred (0x20f91a0)"," },
		]
	return(self.rules)
