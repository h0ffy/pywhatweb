import plugins


class Pluginsimsweb_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<title>SIMSWeb Loading.....</title>"},
			{"text": "index.html" > <font color = "black" face = "arial" > Loading SIMSWeb", "please wait..... < /font > < / a > < / h2 >" },
			{ "text" : "<script language="Javascript" src="/SIMSWeb/monitor.js"></script>" },
			{ "text" : "<form onSubmit="sendinfo(); return false;" name="LOGON">" },
		]
	return(self.rules)
