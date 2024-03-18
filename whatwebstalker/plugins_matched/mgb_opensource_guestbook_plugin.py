import sys
import os
			
class mgb_opensource_guestbook_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<meta name="copyright" content="MGB OpenSource Guestbook \(C\) Copyright 2004-(20[\d]{2}) by http:\/\/www\.m\-gb\.org\/">/" },
			{ "text" : "<!-- If you want to remove this copyright you can do so. But it took and already takes a lot of time to code all this stuff." },
			{ "text" : "<td class="entry_info" colspan="3"><a href="email.php?id=denied">" },
			{ "string" : /<span class="copyright"><a href="http:\/\/www\.m\-gb\.org\/" title="MGB Homepage" target="_blank">MGB OpenSource Guestbook<\/a> &copy; 2004-(20[\d]{2})<br>/" },
		]

