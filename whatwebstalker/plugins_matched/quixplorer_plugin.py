import plugins
			
class Pluginquixplorer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>QuiXplorer ([^\s]+) - the QuiX project<\/title>/" },
			{ "version" : "/<A class="title" href="http:\/\/quixplorer\.sourceforge\.net" target="_blank">QuiXplorer ([^<]+)<\/A> - <A href="http:\/\/quix\.tk" target="_blank">the QuiX project<\/A><\/SMALL>/" },
			{ "text" : "<A class="title" href="http://quixplorer.sourceforge.net" target="_blank">QuiXplorer</A> - <A href="http://quix.tk" target="_blank">the QuiX project</A></SMALL>" },
		]
		return(self.rules)
