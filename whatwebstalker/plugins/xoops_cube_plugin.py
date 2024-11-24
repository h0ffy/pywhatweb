import plugins


class Pluginxoops_cube_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "text": "<title>XOOPS Cube Site - Just Use it!</title>"},
			{"certainty": "75", "text": "<!-- RMV: added module header -->"},
			{"text": "<meta name="generator" content="XOOPS Cube" />"},
			{"text": "<meta name="author" content="XOOPS Cube" />"},
			{"version": "/Powered by XOOPS Cube ([^\\s^&]+)&copy; 200[01]-20[\\d]{2} (<a href="http: \/\/xoopscube\.sourceforge\.net\/" target="_blank">)?XOOPS Cube Project/" },
			{ "version" : "/Powered by <a href="http:\/\/xoopscube\.org\/" rel="external">XOOPS Cube<\/a> ([^\s]+) &copy; 200[01]-20[\d]{2} <a href="http:\/\/xoopscube\.sourceforge\.net\/" rel="external">XOOPS Cube Project<\/a><\/p>/" },
		]
	return(self.rules)
