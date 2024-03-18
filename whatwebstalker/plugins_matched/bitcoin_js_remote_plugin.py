import plugins
			
class Pluginbitcoin_js_remote_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<span id="balance"</span>" },
			{ "text" : "<p><a href="http://tcatm.github.com/bitcoin-js-remote">bitcoin-js-remote</a> <span id="version"></span> by <a href="mailto:tcatm@gawab.com">tcatm</a></p>" },
		]
	return(self.rules)
