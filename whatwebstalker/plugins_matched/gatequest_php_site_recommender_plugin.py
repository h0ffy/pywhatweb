import plugins
			
class Plugingatequest_php_site_recommender_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>GateQuest php Site Recommender - Include Method</title>" },
			{ "certainty" : "25", "text" : "<link rel="stylesheet" href="recommend.css" type="text/css">" },
			{ "name" : "HTML Tag Pattern", "tagpattern" : "!doctype,html,head,title,/title,link,/head,body,table,tr,td,a,img,/a,/td,/tr,tr,td,table,form,tr,td,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,span,/span,br,br,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,span,/span,br,textarea,/textarea,/td,/tr,tr,td,table,tr,td,input,/td,td,/td,td,input,/td,/tr,/table,/td,/tr,/form,/table,/td,/tr,/table,/body,/html'},
			{ "name" : "HTML Tag Pattern", "tagpattern" : "!doctype,html,head,title,/title,link,/head,body,table,tr,td,a,/a,/td,/tr,tr,td,table,form,tr,td,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,span,/span,br,br,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,span,/span,br,textarea,/textarea,/td,/tr,tr,td,table,tr,td,input,/td,td,/td,td,input,/td,/tr,/table,/td,/tr,/form,/table,/td,/tr,/table,/body,/html'},
			{ "name" : "HTML Tag Pattern", "tagpattern" : "!doctype,html,head,title,/title,link,/head,body,table,tr,td,a,,/a,/td,/tr,tr,td,table,form,tr,td,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,span,/span,br,br,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,/td,td,input,/td,/tr,tr,td,span,/span,br,textarea,/textarea,/td,/tr,tr,td,table,tr,td,input,/td,td,/td,td,input,/td,/tr,/table,/td,/tr,/form,/table,/td,/tr,/table,/body,/html'},
		]
			return(self.rules)
