import plugins


class Pluginbarracuda_waf_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<div style="border: 3px solid  # 4991C5; font:1.5em; font-family:tahoma,calibri,arial; font-weight:bold; color:#0A4369; padding:5px; margin:10px; text-align:center"> The requested service is temporarily unavailable. It is either overloaded or under maintenance. Please try later.</div><!--01234567890123456789" },
		]
	return (self.rules)
