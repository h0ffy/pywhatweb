import plugins
			
class Pluginpivotx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- PivotX -->" },
			{ "text" : "<script src="includes/js/pivotx.js" type="text/javascript"></script>" },
			{ "text" : "<img src="templates_internal/assets/pivotx.png" alt="PivotX" /></a>" },
			{ "version" : "/<em>PivotX - ([^<]+)<\/em> &nbsp; - &nbsp; &copy; 20[\d]{2}/" },
			{ "text" : "<meta name="generator" content="PivotX" />" },
			{ "version" : "/<meta name="generator" content="PivotX" \/><!-- version: PivotX - ([^\s]+) -->/" },
		]
	return(self.rules)
