import plugins


class Pluginsun_cobalt_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"model":
			    "/<TITLE>Login - Sun Cobalt (Qube [\\d]+|RaQ [\\d]+) - [^<^\\s]+[\n]?<\\/TITLE>/"},
			{"model": "/document.write\\("\\nThank you for using the Sun Cobalt (Qube [\d]+|RaQ [\d]+)\.\\n"\);/" },
			{ "certainty" : "25", "text" : "<META NAME="Copyright" VALUE="Copyright (C) 2000", "Cobalt Networks", "Inc.  All rights reserved.">" },
			{ "certainty" : "25", "text" : "var url = "/login.php?expired=true&target="+escape(pathname+top.location.search+top.location.hash);" },
			{ "certainty" : "25", "regexp" : "/<P ALIGN="CENTER"><FONT SIZE="5" COLOR="#000099" FACE="HELVETICA", "ARIAL"><B>Welcome to the Web Site of [^\s^<]+<\/B><\/FONT>/" },
			{ "certainty" : "75", "text" : "<HTML><BODY onLoad=\"location='/login.php'\"></BODY></HTML>" },
		]
	return(self.rules)
