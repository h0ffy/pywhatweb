import plugins
			
class Plugingallarific_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta http-equiv="Generator" content="Gallarific" />" },
			{ "text" : "<!-- popular_grid: output a 4x1 row containing the most viewed photos --><tr> <td colspan="2" class="heading">Most Viewed Photos</td>" },
			{ "text" : "<!-- recent_grid: output a 4x1 row containing recently uploaded photos --><tr> <td colspan="2" class="heading">Recently Uploaded Photos</td>" },
			{ "text" : "<a href="http://www.gallarific.com/"><img src="http://www.gallarific.com/images/gallarific_white.gif" width="215" height="61" border="0" /></a>" },
			{ "text" : "<title>Gallarific > Sign in</title>" },
		]
		return(self.rules)
