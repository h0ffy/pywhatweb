import plugins
			
class Pluginiscripts_socialware_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "var loginWindow=window.open('http://www.meebo.com','ChatRoom','top=5 ,left=5,toolbars=no,maximize=no,resize=no,width=500,height=478,location=no,directories=no,scrollbars=yes,border=thin,caption=no');" },
			{ "text" : "          <td align="right">Powered by <a href="http://www.iscripts.com/socialware/" target="_blank">iScripts SocialWare</a> . A premium product from <a href="http://www.iscripts.com" target="_blank">iScripts.com</a></td>" },
		]
		return(self.rules)

