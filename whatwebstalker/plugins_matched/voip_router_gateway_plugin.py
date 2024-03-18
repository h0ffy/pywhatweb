import plugins
			
class Pluginvoip_router_gateway_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<area shape="poly" coords="152,237,152,180,194,180,260,215,293,214,293,236" href="enFrame.htm" alt="english version" onClick="form_submit(\'english\')">" },
		]
		return(self.rules)
