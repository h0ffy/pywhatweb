import plugins
			
class Plugineasyfeeds_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="feedslist" align="left" class="divTableCell">" },
			{ "text" : "<div style="float: left; height: 35px; width: 300px; margin: 45px 0px 0px 40px;"></div>" },
			{ "version" : "/<td colspan="3" style="font-size: 10px; text-align: left;"><CENTER>Powered By:<br>EasyFeeds-([^<]+)<br \/>Ktools.net LLC-<a href="http:\/\/www.ktools.net" target="_blank">http:\/\/www.ktools.net<\/a><\/CENTER><\/td>/" },
			{ "version" : "/<CENTER>Powered By:<br>EasyFeeds-([^<]+)<br \/>Ktools.net LLC-<a href="http:\/\/www.ktools.net" target="_blank">http:\/\/www.ktools.net<\/a><\/CENTER><\/div>/" },
		]
		return(self.rules)
