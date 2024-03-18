import plugins
			
class Pluginhopftimeserver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/cgi-bin/main.cgi?ntp&0", "name" : "HTML Tag Pattern", "tagpattern" : "html,head,link,link,title,/title,style,/style,script,/script,meta,/head,body,table,tr,td,img,map,area,area,/map,/td,td,img,/td,/tr,tr,td,/td,td,/td,td,table,tr,td,img,/td,td,img,/td,td,a,/a,/td,td,img,/td,td,a,/a,/td,td,img,/td,td,a,/a,/td,td,img,/td,td,a,/a,/td,td,img,/td,td,a,/a,/td,td,img,/td,td,/td,td,table,tr,td,img,/td,td,img,/td,td,img,/td,td,img,/td,td,img,/td,/tr,/table,/td,td,img,/td,/tr,/table,/td,td,img,/td,/tr,tr,td,img,/td,td,/td,td,table,tr,td,table,tr,td,table,tr,td,table,tr,td,img,/td,td,div,/div,/td,td,img,/td,/tr,/table,/td,/tr,tr,td,table,tr,td,img,/td,td,/td,td,img,/td,/tr,tr,td,/td,td,div,table,tr,td,iframe,/iframe,/td,/tr,/table,/div,/td,td,/td,/tr,tr,td,img,/td,td,/td,td,img,/td,/tr,/table,/td,/tr,/table,/td,td,div,/div,/td,td,table,tr,td,table,tr,td,img,/td,td,div,/div,/td,td,img,/td,/tr,/table,/td,/tr,tr,td,table,tr,td,img,/td,td,/td,td,img,/td,/tr,tr,td,/td,td,div,table,tr,td,iframe,/iframe,/td,/tr,/table,/div,/td,td,/td,/tr,tr,td,img,/td,td,/td,td,img,/td,/tr,/table,/td,/tr,/table,/td,/tr,tr,td,table,tr,td,table,tr,td,img,/td,td,div,/div,/td,td,img,/td,/tr,/table,/td,/tr,tr,td,table,tr,td,img,/td,td,/td,td,img,/td,/tr,tr,td,/td,td,div,table,tr,td,form,table,tr,td,/td,/tr,tr,td,input,/td,/tr,tr,td,/td,/tr,tr,td,input,/td,/tr,tr,td,input,/td,/tr,tr,td,br,br,/td,/tr,/table,/form,/td,/tr,/table,/div,/td,td,/td,/tr,tr,td,img,/td,td,/td,td,img,/td,/tr,/table,/td,/tr,/table,/td,/tr,/table,/td,td,/td,/tr,/table,/td,td,img,/td,/tr,tr,td,/td,td,/td,td,div,/div,/td,td,img,/td,/tr,tr,td,/td,td,/td,td,/td,td,/td,/tr,/table,/body,/html'},
			{ "url" : "/cgi-bin/main.cgi?ntp&0", "version" : "/><title>Hopf ([^<]+) - System Info<\/title/" },
			{ "version" : "/><title>Hopf ([^<^\s]+) - (System Info|General|Peers|Server Configuration|Kernel Info)<\/title>/" },
			{ "version" : "/<head><title>HOPF ([^<^\s]+) Configuration<\/title>/" },
		]
		return(self.rules)

