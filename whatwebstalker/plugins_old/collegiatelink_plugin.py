import plugins
			
class Plugincollegiatelink_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/www\.collegiatelink\.net">CollegiateLink<\/a> Version ([\d\.]+)<\/p><div id="links">CollegiateLink uses /" },
			{ "text" : "</div></div></div><div class="salink"><span class="shadow"><!----></span></div></div><span class="clearDiv"><!----></span></div></div><span class="clearDiv"><!----></span><script type="text/javascript">" },
		]
	return(self.rules)
