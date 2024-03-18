import plugins
			
class Pluginalstrasoft_askme_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Enter details about your question and press the button bellow. All fields are required." },
			{ "text" : "<font size="+2">AskMe Pro Admin</font></b>" },
			{ "text" : "<br> Powered by <a href='http://www.alstrasoft.com' targe='_blank'><font color=blue>AlstraSoft AskMe Pro</font></a><br><br>" },
			{ "text" : "<td colspan=2 align="center"><a href="pass_recover.php">Forgotten Password?</a></td>" },
			{ "text" : "Powered By <a href="http://www.alstrasoft.com">AlstraSoft AskMe Pro</td></tr></table></body></a></html>" },
		]
	return(self.rules)

