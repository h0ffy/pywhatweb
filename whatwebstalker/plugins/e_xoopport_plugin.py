import plugins
			
class Plugine_xoopport_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div align='center'>Powered by E-Xoopport ([^&]+)&copy; 2004[\-0-9]{0,5} <a href='http:\/\/www.e-xoopport.it\/' target='_blank'>The E-Xoopport Project<\/a><\/div>/" },
			{ "version" : "/<meta name="generator" content="E-Xoopport ([^"]+)">/" },
		]
	return(self.rules)
