import plugins
			
class Pluginvsp_stats_processor_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/powered by <A HREF="http:\/\/www.(scivox.net|clanavl.com)\/vsp\/">vsp stats processor<\/A>/" },
			{ "text" : "&nbsp;theme:bismarck by <A HREF="#" TITLE="myrddin8 <AT> gmail <DOT> com">myrddin</A>&nbsp;", "string" : "bismarck" },
			{ "certainty" : "25", "regexp" : "/<TITLE>vsp \((map|award|game|player) stats\)<\/TITLE>/" },
			{ "certainty" : "25", "text" : "<BODY>error: cannot establish database connection or database database_name does not exist", "string" : "Error" },
			{ "version" : "/<A HREF="http:\/\/www.clanavl.com\/vsp\/">vsp<\/A> v([\d\.]+),/" },
		]
		return(self.rules)
