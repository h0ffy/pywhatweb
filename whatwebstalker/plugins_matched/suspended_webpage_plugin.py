import sys
import os
			
class Pluginsuspended_webpage_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- InstanceBegin template=rwh.dwt codeOutsideHTMLIsLocked=false --><!--Copyright &copy; 2002-2010 by Flux Services", "Inc.--><html><head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><title>Website Unavailable - UltraWebsiteHosting.com</title><META NAME=ROBOTS CONTENT=NOINDEX,NOFOLLOW><LINK REL="SHORTCUT ICON" HREF=favicon.ico><style type="text/css">", "version" : "'ultrawebsitehosting.com" },
			{ "text" : "background-image: url(http://www.ultrawebsitehosting.com/suspended/body-bg.gif);", "version" : "'ultrawebsitehosting.com" },
		]
		return(self.rules)

