import plugins


class Pluginkajona_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/<meta name="generator" content="Kajona.", "www\.kajona\.de" \/>/" },
			{ "regexp" : "/<!--\s+Website powered by Kajona. Open Source Content Management Framework/" },
			{ "regexp" : "/<script type="text\/javascript">KAJONA_(DEBUG|WEBPATH) = /" },
			{ "text" : "<div class="left">powered by Kajona</div>" },
			{ "text" : "<div id="footerContainer">powered by <a href="http://www.kajona.de" target="_blank" title="Kajona" },
			{ "string" : /<div class="copyright">&copy; (20[\d]{2}) <a href="http:\/\/www\.kajona\.de" target="_blank" title="Kajona/" },
		]
	return(self.rules)
