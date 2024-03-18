import plugins
			
class Pluginsmf_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "copyright link", "text" : "<a href="http://www.simplemachines.org/about/copyright.php" title="Free Forum Software" target="_blank"'},
			{ "name" : "javascript", "text" : "document.getElementById("upshrink").src = smf_images_url + '},
			{ "name" : "smflogo gif", "regexp" : "/<img class="floatright" id="smflogo" src="[^"]*\/images\/smflogo.gif" alt="Simple Machines Forum" \/>},
			{ "version" : "/<a href="http:\/\/www.simplemachines.org\/" title="Simple Machines Forum" target="_blank"( class="new_win")?>Powered by SMF ([^<]+)/", "offset" : "1 },
			{ "version" : "/<a href=".*?" title="Simple Machines Forum" target="_blank" class="new_win">SMF ([^<]+)},
		]
		return(self.rules)
