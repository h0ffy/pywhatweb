import plugins


class Pluginsendio_esp_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<frameset id="icetopframeset" name="icetopframeset" rows="28, *, 20, 0, 0, 0""},
			{"text": "<link rel="stylesheet" type="text / css" href=" / sendio / ice / css / nice.css" />"},
			{"url": "/favicon.ico", "md5": "0d8eda4e968077705982915e3d874e17"},
			{"url": "/sendio/ice/ui/foot", "string": / <td width = "50%" align = "left" valign = "middle" > <div id = "footleft" > &nbsp; & copy; (20[\d]{2}) Sendio", "Inc\.<\/div><\/td>/" },
			{ "url" : "/sendio/ice/ui/foot", "version" : "/<td width="50%" align="right" valign="middle"><div id="footright">Sendio ([\d\.]+ \([^\s^\)]+\)) &mdash/" },
		]
	return(self.rules)
