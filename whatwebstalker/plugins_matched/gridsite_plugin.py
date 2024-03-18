import plugins
			
class Plugingridsite_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="gridsite-admin.cgi?cmd=history&amp;file=index.html">View&nbsp;page&nbsp;history</a>" },
			{ "text" : "<a href="gridsite-admin.cgi?cmd=print&amp;file=index.html">Print&nbsp;View</a>" },
			{ "version" : "/Built with <a href="http:\/\/www.gridsite.org\/">GridSite<\/a>&nbsp;([\d\.]+)/" },
			{ "version" : "/Built with <a href="http:\/\/www.gridsite.org\/">GridSite<\/a> ([\d\.]+)/" },
			{ "text" : "<!-- start of gridsitefoot.txt -->" },
		]
		return(self.rules)
