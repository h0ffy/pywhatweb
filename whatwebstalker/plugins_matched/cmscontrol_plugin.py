import plugins
			
class Plugincmscontrol_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "+CMScontrol inurl:"index.php?id_menu="", "certainty" : "25 },
			{ "regexp" : "/<META name=[\"\']*formatter[\"\']* content=[\"\']*CMScontrol eContent[\"\']*>/i },
			{ "regexp" : "/<META name=[\"\']*abstract[\"\']* content=[\"\']*CMScontrol[\"\']*>/i },
			{ "text" : "document.write("<ME"+"TA ht"+"tp-eq"+"uiv=\"REF"+"RESH\" con"+"tent=\"1.00; u"+"rl="+"index"+"."+"ph"+"p\">");" },
			{ "regexp" : "/<META NAME=[\"\']*generator[\"\']* CONTENT=[\"\']*CMScontrol rel 3.x[\"\']*>/i", "version" : "'3.x" },
		]
			return(self.rules)
