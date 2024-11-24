import plugins


class Pluginmyphp_forum_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/    <td width="50 % " class="copy" height="24">Powered by: MyPHP Forum v([\\d\\.]+)/"},
			{"version": "/    <td width="50 % " class="copy" height="24">Powered by: <a href="http: \/\/www.myphp.ws">MyPHP Forum v([\d\.]+)/" },
		]
	return(self.rules)
