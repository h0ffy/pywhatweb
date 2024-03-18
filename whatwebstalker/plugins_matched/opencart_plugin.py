import plugins
			
class Pluginopencart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<!--\s+OpenCart is open source software and you are free to remove the powered by OpenCart if you want", "but its generally accepted practise to make a small donation\./" },
			{ "regexp" : "/<div id="powered">Powered By <a href="http:\/\/www\.opencart\.com"( title="OpenCart")?>OpenCart<\/a>/" },
			{ "version" : "/<div id="footer">\s*<a href="http:\/\/www\.opencart\.com">OpenCart<\/a> &copy; 2009(-20[\d]{2})? All Rights Reserved\.<br \/>Version ([^<]+)<\/div>/", "offset" : "1 },
			{ "version" : "/All Rights Reserved\.<br \/>OpenCart Version ([^<]+)\<\/div>/" },
			{ "text" : "/admin/index.php?route=common/login" method="post" enctype="multipart/form-data" id="form">" },
		]
		return(self.rules)
