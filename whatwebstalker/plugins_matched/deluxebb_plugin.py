import plugins
			
class Plugindeluxebb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<!-- \|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|[\r\n\s]+\| This forum is coded by and          \|[\r\n\s]+\| copyrighted to Frank Nissel         \|/" },
			{ "text" : "<meta name="description" content="powered by DeluxeBB - www.deluxebb.com" />" },
			{ "version" : "/<p><a href="http:\/\/www.deluxebb.com" target="_blank">DeluxeBB ([\d\.]+)<\/a> is copyrighted to the DeluxeBB team '05/" },
		]
		return(self.rules)
