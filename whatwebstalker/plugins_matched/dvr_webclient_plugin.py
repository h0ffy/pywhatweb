import plugins
			
class Plugindvr_webclient_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "md5" : "8cf9f140f2ec4f5d3e533b5bc2b221ea'},
			{ "text" : "259F9FDF-97EA-4C59-B957-5160CAB6884E'},
		]
		return(self.rules)
