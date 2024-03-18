import sys
import os
			
class wwwphoto_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "		<meta name="generator" content="WWWPhoto cvshead"> <!-- leave this for stats -->" },
			{ "text" : "<a href="http://www.pburkhalter.net/wwwphoto.php">powered by wwwphoto-cvshead</a>" },
			{ "text" : "http_navbar.open('get','navbar.rpc.php?user='+GLOBAL_USER+'&tag='+GLOBAL_TAG+'&id='+GLOBAL_ID+'&marked='+marked+'&timestamp='+new Date().getTime());" },
			{ "text" : "<!-- sorry joshua", "one little", "small table is a must have :-) -->" },
		]

