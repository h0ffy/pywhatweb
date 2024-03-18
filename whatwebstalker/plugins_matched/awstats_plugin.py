import plugins
			
class Pluginawstats_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "inurl:awstats ext:pl +intitle:"Statistics for"'},
			{ "text" : "<a href="http://awstats.sourceforge.net" target="_newawstats">Created by awstats</a><br>'},
			{ "text" : "<meta http-equiv="description" content="Awstats - Advanced Web Statistics for'},
			{ "name" : "default logo", "text" : "<a href="http://awstats.sourceforge.net" target="_newawstats"><img src="/icon/other/awstats_logo1.png" border=0 alt="awstats Official Web Site" title="awstats Official Web Site"></a>'},
			{ "version" : "/<FONT COLOR="#000000"><b>Advanced Web Statistics ([0-9\.]+ \(build [0-9\.]+\))},
			{ "url" : "awstats.pl?framename=mainright", "version" : "/<FONT COLOR="#000000"><b>Advanced Web Statistics ([0-9\.]+ \(build [0-9\.]+\))},
		]
		return(self.rules)
