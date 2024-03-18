import plugins
			
class Pluginlandshop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a class="white" href="http:\/\/www\.landshop\.gr" target="_blank" (alte="Samedia LandShop")? title="Samedia Landshop">Land[Ss]hop<sup>&reg;<\/sup><\/a><br>/" },
			{ "text" : "<div class="more CAT" style="height:20px;margin:5px 0px 10px 0px;text-align:right"><a class="item fat"  href="ls.php?" },
			{ "text" : "<!--<A href="<#G_ADMIN_URL#>/action/contacts.php?action=list"><#list_contacts#></a>-->" },
		]
		return(self.rules)

