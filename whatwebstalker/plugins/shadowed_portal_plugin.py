import plugins
			
class Pluginshadowed_portal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by <a href="http:\/\/www.shad0wed.com\/"[^>]*>Shadowed Portal ([^<]+)<\/a>.<br \/>These script's code is Copyright &copy; 2003-20[\d]{2} by <a href="http:\/\/www.shadowedworks.com\/"[^>]*>Shadowed Works<\/a>.<br \/>Please be sure to read the <a href="http:\/\/www.shad0wed.com\/load.php\?mod=pages(&|&amp;)page=Terms_and_Conditions"[^>]*>Terms and Conditions<\/a> required for the use of these scripts./" },
		]
	return(self.rules)
