```
import plugins

class Pluginbluequartz_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r"/<TITLE>Login - BlueQuartz ([^\s]+) Series - [^<^\s]+<\/TITLE>/" },
            { "version" : r"'document.write\\nThank you for using the BlueQuartz ([^\s]+) Series.\\n');" },
            { "certainty" : "75", "text" : r'<BODY BGCOLOR="#FFFFFF" onLoad="focuslogin()" onResize="if(navigator.appName == \'Netscape\') location.reload()" LINK="#FFFFFF" VLINK="#FFFFFF">' },
            { "certainty" : "75", "regexp" : r"/EVEN IF SUN HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES\.\n\nYou acknowledge that  this software is not designed or intended for use in the design, construction, operation or maintenance of any nuclear facility.\n-->/" },
            { "certainty" : "25", "text" : r'<META NAME="Copyright" VALUE="Copyright (C) 2000, Cobalt Networks, Inc.  All rights reserved.">' },
            { "certainty" : "25", "text" : r'var url = "/login.php?expired=true&target="+escape(pathname+top.location.search+top.location.hash);' },
            { "certainty" : "25", "regexp" : r'/<P ALIGN="CENTER"><FONT SIZE="5" COLOR="#000099" FACE="HELVETICA", "ARIAL"><B>Welcome to the Web Site of [^\s^<]+<\/B><\/FONT>/' },
            { "certainty" : "75", "text" : r'<BODY onLoad="location=\'http://\'+location.host+\'/login/\'">' },
        ]
        return self.rules
```