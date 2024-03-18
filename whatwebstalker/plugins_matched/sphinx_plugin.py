import plugins
			
class Pluginsphinx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Created using <a href="http:\/\/sphinx\.pocoo\.org\/">Sphinx<\/a> ([^\s]+)\./" },
			{ "regexp" : "/<div class="sphinxsidebar">[\s]+<div class="sphinxsidebarwrapper">/" },
		]
		return(self.rules)
