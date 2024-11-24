import plugins


class Pluginphpcow_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<b>Powered by</b>: <a href="http: // www.phpcow.com" target="_blank" style="color:  # 000000">PHPCow.com</a>" },
			{"text": "<b>Powered by</b>: <a href="http: // www.phpcow.com" target="_blank" style="color:  # 000000" title="PHPCow news publishing script", "content management system">PHPCow.com</a>" },
			{"text": "<meta name="Description" content="PHPCow news publishing content management system" />"},
			{"text": "<meta name="Keywords" content="phpcow", "news publishing", "article publishing", "cms" />"},
		]
	return (self.rules)
