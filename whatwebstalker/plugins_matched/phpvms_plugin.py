import plugins
			
class Pluginphpvms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<div class="jqmWindow" id="jqmdialog"></div>" },
			{ "version" : "/<a href="http:\/\/www\.phpvms\.net\/docs\/license">License & About<\/a> \|[\s]+Version ([^\s]+)[\s]+<\/div>/" },
			{ "regexp" : "/<!-- Please retain this!! It's part of the phpVMS license\. You must display a[\s]+"powered by phpVMS" somewhere on your page\. Thanks! -->/" },
			{ "text" : "<a href="http://www.phpvms.net" target="_blank">powered by phpVMS</a>" },
		]
		return(self.rules)
