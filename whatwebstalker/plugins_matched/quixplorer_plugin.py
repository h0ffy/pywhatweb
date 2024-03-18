import sys
import os
			
class quixplorer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<title>QuiXplorer ([^\s]+) - the QuiX project<\/title>/ }
			{ "version" : '/<A class="title" href="http:\/\/quixplorer\.sourceforge\.net" target="_blank">QuiXplorer ([^<]+)<\/A> - <A href="http:\/\/quix\.tk" target="_blank">the QuiX project<\/A><\/SMALL>/ }
			{ "text" : '<A class="title" href="http://quixplorer.sourceforge.net" target="_blank">QuiXplorer</A> - <A href="http://quix.tk" target="_blank">the QuiX project</A></SMALL>' }
	]

