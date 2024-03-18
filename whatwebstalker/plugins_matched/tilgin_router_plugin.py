import plugins
			
class Plugintilgin_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<H1 id="title">Welcome to the Tilgin router</H1>" },
			{ "text" : "<TITLE>VOOD</TITLE>", "url" : "/" },
			{ "text" : "<A href="/wizard/" class=" title="Wizard">Run wizard</A> for a quick and simple initial configuration." },
			{ "text" : "<A href="/status/" class="menuitem" title="Status">Status</A><SPAN class="separator"> </SPAN><A href="/help/" class="last menuitem" title="Help">Help</A>" },
			{ "text" : "<LINK rel="stylesheet" type="text/css" href="/compressed-control.css">" },
		]
		return(self.rules)
