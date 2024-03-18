import plugins
			
class Pluginadcon_telemetry_gateway_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "string" : /^addUPI (Server [^\s]+)/" },
			{ "search" : "headers[server]", "module" : /^addUPI Server [^\s]+ \+(SSL)/" },
			{ "url" : "/mainpicture.jpeg", "md5" : "1e051ae64434f4092dc98774ff592406" },
			{ "text" : "<area href="http://www.adcon.at" coords="446,0,565,66" shape="rect" title="Adcon Telemetry" alt="Adcon Telemetry\'s web site">" },
			{ "version" : "/<font face="Verdana,Arial,Helvetica,Geneva" size="2">Release ([^\s^,]+)", "&copy;20[^\s]{2} Adcon Telemetry GmbH; all other trademarks mentioned here are registered with their owners\.<\/font>/" },
			{ "model" : "/<\/font> <font face="Verdana,Arial,Helvetica,Geneva" size="4"><b>Welcome to the ([^\s]+) Telemetry Gateway!<\/b><\/font>/" },
			{ "url" : "/images/background.gif", "md5" : "ba53de81edddae5e112c254d2ab182dc" },
			{ "text" : "<a name="configurator" href="/cgi-bin/configurator.jnlp">configure your Gateway</a>." },
			{ "version" : "/<hr>[\s]+<p>[\s]+Release ([^\s^,]+)", "&copy; 20[\d]{2} Adcon Telemetry GmbH<br>/" },
			{ "model" : "/<body onload="onLoadChangeConfiguratorLinks\(\)">[\s]+<h1 class="line1">([^\s]+) Telemetry Gateway<\/h1>/" },
		]
			return(self.rules)
