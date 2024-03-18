import sys
import os
			
class Pluginefront_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<body  onkeypress = "if (window.eF_js_keypress) eF_js_keypress(event);" onbeforeunload = "if (window.getPeriodicData) getPeriodicData();">" },
			{ "text" : "<script>var BOOKMARKTRANSLATION = 'Bookmarks';var NODATAFOUND = 'No data found';</script>" },
			{ "text" : "</script><script>if (__shouldTriggerNextNotifications) { new Ajax.Request("send_notifications.php?ajax=1", "{method:\'get\", "asynchronous:true}); } </script>" },
			{ "version" : "/<div><a href = "http:\/\/www\.efrontlearning\.net">eFront<\/a> \(version ([^\)]+)\) &bull; Community Edition &bull; <a href = "index\.php\?ctg=contact">/" },
			{ "version" : "/<script type = "text\/javascript" src = "js\/scripts\.php\?(build=[\d]+)&load=[^"^>]+"> <\/script>/" },
		]

