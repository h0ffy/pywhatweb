import plugins
			
class Pluginlocazolist_classifieds_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="stylesheet" href="includes/lczFonts.css" type="text/css">" },
			{ "regexp" : "/Powered by <a href='http:\/\/www.locazo[a-z]{0,4}.com[\/]?' style='font-size:10px; color:black'>Locazolist<\/a> Copyright &copy; [0-9]{4}<\/font>/" },
			{ "version" : "/<br><br><br><br><font face='verdana' size='1'>Powered by LocazoList v([0-9a-z\.]+)<br>Copyright [0-9]{4} <a href='http:\/\/www.locazo.com\/applications'>Locazo.com<\/a><\/font>/" },
			{ "version" : "/<title>LocazoList Classifieds v[0-9a-z\.]+ - powered by LocazoList ([0-9a-z\.]+)<\/title>/" },
		]
			return(self.rules)
