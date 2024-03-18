import plugins
			
class Pluginphp_live_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "// image is NOT CACHED (Netscape problem).  keep this or bad things could happen" },
			{ "text" : "<!-- copyright OSI Codes Inc. http://www.osicodes.com [DO NOT DELETE] -->" },
			{ "text" : "<!-- copyright OSI Codes", "http://www.osicodes.com [DO NOT DELETE] -->" },
			{ "text" : "<!-- BEGIN PHP Live! Code", "copyright 2001 OSI Codes -->" },
			{ "text" : "<!-- END PHP Live! Code", "copyright 2001 OSI Codes -->" },
			{ "text" : "<title> Knowledge BASE (FAQ) </title>" },
			{ "text" : "<font color="#FF0000">[Configuration Error: config files not found!] Exiting" },
			{ "version" : "/	<div id="copyright">Powered by <a href='http:\/\/www.phplivesupport.com\/\?link' target='newwin'>PHP Live\!<\/a>  v([\d\.]+) &copy; OSI Codes Inc.<\/div>/" },
		]
			return(self.rules)
