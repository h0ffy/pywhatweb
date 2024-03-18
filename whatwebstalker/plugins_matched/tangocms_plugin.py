import plugins
			
class Plugintangocms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by <a href="http:\/\/(www\.)?tangocms\.org" title="(Open Source CMS|TangoCMS)">TangoCMS<\/a>\./" },
			{ "text" : "<input type="checkbox" id="sessionRemember" name="session[remember]" value="1" checked="checked"> <label class="horizontal" for="sessionRemember">Remember me?</label>" },
		]
	return(self.rules)
