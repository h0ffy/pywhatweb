import sys
import os
			
class mibew_messenger_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<p id="legal"><a href="http:\/\/mibew\.org\/" class="flink">Mibew Messenger<\/a> ([^\s]+) \| \(c\) 20[\d]{2} mibew\.org<\/p>/ },
			{ "certainty" : '75", "text" : '<div class="empty_inner" style=">&#160;</div>' },
		]

