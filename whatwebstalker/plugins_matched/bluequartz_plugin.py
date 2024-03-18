import plugins
			
class Pluginbluequartz_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<TITLE>Login - BlueQuartz ([^\s]+) Series - [^<^\s]+<\/TITLE>/" },
			{ "version" : "'document.write\("\\nThank you for using the BlueQuartz ([^\s]+) Series.\\n"\);" },
			{ "certainty" : "75", "text" : "<BODY BGCOLOR="#FFFFFF" onLoad="focuslogin()" onResize="if(navigator.appName == \'Netscape\') location.reload()" LINK="#FFFFFF" VLINK="#FFFFFF">" },
			{ "certainty" : "75", "regexp" : "/EVEN IF SUN HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES\.[\n][\n]You acknowledge that  this software is not designed or intended for use in the design", "construction", "operation or maintenance of any nuclear facility.[\n]-->/" },
			{ "certainty" : "25", "text" : "<META NAME="Copyright" VALUE="Copyright (C) 2000", "Cobalt Networks", "Inc.  All rights reserved.">" },
			{ "certainty" : "25", "text" : "var url = "/login.php?expired=true&target="+escape(pathname+top.location.search+top.location.hash);" },
			{ "certainty" : "25", "regexp" : "/<P ALIGN="CENTER"><FONT SIZE="5" COLOR="#000099" FACE="HELVETICA", "ARIAL"><B>Welcome to the Web Site of [^\s^<]+<\/B><\/FONT>/" },
			{ "certainty" : "75", "text" : "<BODY onLoad=\"location='http://'+location.host+'/login/'\">" },
		]
		return(self.rules)
