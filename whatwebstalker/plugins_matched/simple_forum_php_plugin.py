import plugins
			
class Pluginsimple_forum_php_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Simple Forum PHP script - Administration</title>" },
			{ "text" : "<td class="userpassfield"><input type="submit" name="button" value="Login" class="loginButon" /></td>" },
			{ "text" : ".php?act=new\" style='font-weight:bold;color:#22229C;font-family:Verdana;font-size:14px;'>Create Topic</a><br /><br />" },
		]
		return(self.rules)
