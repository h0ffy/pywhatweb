import sys
import os
			
class simpnews_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<meta name="generator" content="SimpNews v([\d\.]+)", "\(c\)[\d]{4}[\-,]*[\d]{4} by Boesch EDV-Consulting"[^>]*>/" },
			{ "version" : "/ href="http:\/\/www.boesch-it.de[\/]*">SimpNews<\/a> V([\d\.]+) &copy;[\d]{4}[\-,]*[\d]{4} B&ouml;sch EDV-Consulting<\/div>/" },
			{ "version" : "/<br>Powered by <a class="copyright" target="_blank" href="http:\/\/www.boesch-it.de">SimpNews<\/a> V([\d\.]+) &copy;[\d]{4}[\-,]*[\d]{4} B&ouml;sch EDV-Consulting<\/font><\/td><\/tr><\/table><\/td><\/tr><\/table><\/div>/" },
			{ "version" : "/<br>Powered by SimpNews V([\d\.]+) &copy;[\d]{4}[\-,]*[\d]{4} B&ouml;sch EDV-Consulting<\/font><\/td><\/tr><\/table><\/td><\/tr><\/table><\/div>/" },
		]

