import plugins
			
class Pluginalstrasoft_epay_enterprise_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a class=copy href="http://www.alstrasoft.com/" target="_blank">Powered by EPay Enterprise.</a>&nbsp;" },
			{ "search" : "headers[set-cookie]", "regexp" : "/ln=English/", "certainty" : "25 },
			{ "text" : " <tr><td align=center><input class=submit type=submit name=send value="LOGIN NOW!"></td></tr>" },
			{ "text" : "<tr><td class=capl><a href='/shop.htm?action=view'>TOP CATEGORIES</a>&nbsp;&nbsp;&gt;&gt;&nbsp;" },
		]
	return(self.rules)

