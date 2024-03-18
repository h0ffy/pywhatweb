import plugins
			
class Pluginjustanswer_professional_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<td align=center>Powered By <a href="http://guruscript.com">Guruscript.com</a></td></tr></table></div></body></html>" },
			{ "regexp" : "/<a href="register\.php\?typ=expert&que_id=[\d]+">Click here<\/a> to answer this question\./" },
			{ "text" : "<img src="images/settings.png" style="vertical-align:middle;" />&nbsp;<a href="logout.php" class="cpanel_a">Logout </a><br>" },
		]
			return(self.rules)
