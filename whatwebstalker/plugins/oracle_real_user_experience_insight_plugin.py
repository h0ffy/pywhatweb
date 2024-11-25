import plugins
			
class Pluginoracle_real_user_experience_insight_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<title>Oracle Real User Experience Insight \-\[ ([^\s]+@[^\s]+) \]\-<\/title>/" },
			{ "version" : "/<title>Oracle Real User Experience Insight \-\[ ([\d\.a-z]+) \]\-<\/title>/" },
			{ "version" : "/<div class="windowWatermark">Version: ([^\s]+)/" },
			{ "url" : "/ruei/rpc.php", "text" : "{"retval":false,"error_" },
		]
	return(self.rules)
