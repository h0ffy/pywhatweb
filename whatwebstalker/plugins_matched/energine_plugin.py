import plugins
			
class Pluginenergine_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script type="text\/javascript" src="[^"]*scripts\/Energine.js"><\/script>/" },
			{ "regexp" : "/<link rel="stylesheet" type="text\/css" href="[^"]*stylesheets\/energine.css" \/>/" },
			{ "text" : "<div id="footer"><span class="copyright">Powered by <a href="http://energine.org">Energine</a><br/>" },
			{ "text" : "<span class="copyright">Powered by <a href= "http://energine.org/">Energine</a></span>" },
			{ "certainty" : "75", "text" : "<div id="footer">Powered by Energine.</div>" },
			{ "text" : "<div id="footer">Powered by <a href="http://energine.org">Energine</a>" },
		]
			return(self.rules)
