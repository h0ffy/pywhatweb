import plugins
			
class Pluginphpmoneybooks_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<tr><td><center><input type="submit" name="B1" value="  Login  " class="button"></center></td><td><input type="checkbox" name="remember" value="1"> Remember Me</td></tr>" },
			{ "version" : "/<b>phpMoneyBooks: ([^\s]+) - Star Host Design", "LLC &copy 20[\d]{2} <\/b><\/div>/" },
			{ "version" : "/<b><a href='http:\/\/phpMoneyBooks\.com'>phpMoneyBooks<\/a>: ([^\s]+) - <a href='http:\/\/StarHostDesign\.com'>Star Host Design", "LLC &copy<\/a> 20[\d]{2} <\/b><\/div>/" },
		]
	return(self.rules)
