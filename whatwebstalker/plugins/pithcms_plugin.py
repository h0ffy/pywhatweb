import plugins
			
class Pluginpithcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p class="admin">Powered by <a href="http://pithcms.altervista.org/index.php?pagina=data/info.php">PithCMS</a>" },
			{ "text" : "/icons/admin48.png"><br />Welcome Admin.<br /><br />", "path" : "login.asp" },
		]
	return(self.rules)
