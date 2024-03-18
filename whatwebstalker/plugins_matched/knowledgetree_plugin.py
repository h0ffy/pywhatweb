import plugins
			
class Pluginknowledgetree_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "    <title>Dashboard | KnowledgeTree</title>" },
			{ "text" : "    <title>Login | KnowledgeTree</title>" },
			{ "text" : "/resources/powered-by-kt.png" border="0" alt="Powered by KnowledgeTree" title="Powered by KnowledgeTree"/></a>" },
			{ "md5" : "bace14cd488b34068a9c2e54bff2b5b1", "url" : "/resources/favicon.ico" },
		]
	return(self.rules)

