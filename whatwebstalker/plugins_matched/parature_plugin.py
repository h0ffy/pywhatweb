import plugins
			
class Pluginparature_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "This Website requires your browser to be JavaScript enabled. Please enable JavaScript  and click <a href="/ics/default.asp">here</a> to continue." },
			{ "string" : /<\!\-\- \*\*\*\*\*\* (PRODAPP[^\s]+) *\*\*\*\*\* \-\->/" },
			{ "version" : "/<!--<script src="\.\.\/ic1Browser\.js\?ver=([^"]+)"><\/script>-->/" },
			{ "certainty" : "75", "text" : "RedirectPortalURL('/ics/support/custhandler.asp?task=signOut&redirectURL=' + encodeURI('" },
			{ "text" : "<frame title="Left Navigation" name="cypLeft" src="KBFolder.asp?deptID=" },
			{ "md5" : "5b5120dc4f0bb058180da4361ac8fd70" },
		]
		return(self.rules)
