import plugins
			
class Plugincushy_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Content Management Powered by <a href="http://www.cushycms.com">CushyCMS</a>'},
			{ "text" : "<li id="poweredBy"><img alt="Powered by CushyCMS" src="/images/cushy_badge.gif'},
			{ "text" : "<span id="cushycms-footer">Powered by CushyCMS</span>'},
			{ "regexp" : "/<[^>]+class="cushycms"},
		]
	return(self.rules)

