import plugins
			
class Pluginnoticeboardpro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<td align="center" colspan="4" height="38" width="572" bgcolor="#f5f5dc"><p class="copy">Version ([\d\.]+) -/" },
			{ "text" : "<A HREF="registerOutline.php" CLASS="Xref" style="margin-right:10">[Register]</A>" },
			{ "text" : "<A HREF="loginOutline.php" CLASS="Xref" style="margin-left:165; margin-right:10">[Sign In]</A>" },
		]
		return(self.rules)

