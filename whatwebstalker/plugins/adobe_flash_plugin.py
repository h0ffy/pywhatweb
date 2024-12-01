import re
import plugins
			
class Pluginadobe_flash_plugin(plugins.Base):
    def __init__(self):
        super().__init__()
        
    def start(self):
        self.rules = [
            { "regexp" : re.compile("<object[^>]+application\/x-shockwave-flash[^>]+>", re.I) },
            { "regexp" : re.compile("<embed[^>]+src[\s]*=[\s]*[\"']?[^\s^'^\"^>]+", re.I) },
            { "regexp" : re.compile("new[\s]+FlashObject[\s]*\([\s]*['\"]?[^'^\"]+", re.I) },
            { "regexp" : re.compile("new[\s]+SWFObject[\s]*\([\s]*['\"]?[^'^\"]+", re.I) },
            { "regexp" : re.compile("\.embedSWF[\s]*\([\s]*[\"']?[^'^\"]+", re.I) },
            { "name" : "File extension", "regexp" : re.compile("^(fla|flv|swf|swt|swc)$", re.I), "search" : "uri.extension" },
        ]
        return self.rules