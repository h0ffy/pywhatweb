import plugins
			
class Pluginfree_realty_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!--FreeRealty ([^\s]+) -->/" },
			{ "text" : "<font class="foot">This tool is Open Source and released under the <a href="http://www.gnu.org/copyleft/gpl.html">GPL</a></font>" },
			{ "text" : "<!-- THUS ENDETH THE MAIN CONTENT -->" },
			{ "text" : "<!-- HERE BEGINNETH THE FOOTER --><div class="foot">" },
		]
	return(self.rules)
