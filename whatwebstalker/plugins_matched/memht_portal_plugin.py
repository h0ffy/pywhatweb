import plugins
			
class Pluginmemht_portal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name='author' content='MemHT Portal (www.memht.com) - Miltenovik Manojlo'>" },
			{ "text" : "// MemHT Portal is free", "released under a very permissive license as" },
			{ "text" : "<a href='http://www.memht.com' title='MemHT.com' target='_blank'><b>MemHT Portal</b></a> is a free software released under the GNU/GPL License by <a href='http://www.memht.com' title='MemHT.com' target='_blank'><b>Miltenovik Manojlo</b></a>" },
		]
		return(self.rules)
