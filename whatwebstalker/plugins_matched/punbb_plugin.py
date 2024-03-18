import plugins
			
class Pluginpunbb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<!-- forum_debug -->" },
			{ "text" : "<div id="brd-index" class="brd-page basic-page">" },
			{ "text" : "<p id="copyright">Powered by <strong><a href="http://punbb.informer.com/">PunBB</a></strong>", "supported by <strong><a href="http://www.informer.com/">Informer Technologies", "Inc</a></strong>.</p>" },
			{ "module" : /<p style="clear: both; ">Currently installed <span id="extensions-used" title="([^"]+)\.">[\d]+ official extensions<\/span>\. Copyright &copy; 2003&ndash;/" },
		]
		return(self.rules)

