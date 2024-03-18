import sys
import os
			
class justanswer_professional_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "text" : '<td align=center>Powered By <a href="http://guruscript.com">Guruscript.com</a></td></tr></table></div></body></html>' },
			{ "regexp" : '/<a href="register\.php\?typ=expert&que_id=[\d]+">Click here<\/a> to answer this question\./ },
			{ "text" : '<img src="images/settings.png" style="vertical-align:middle;" />&nbsp;<a href="logout.php" class="cpanel_a">Logout </a><br>' },
		]

