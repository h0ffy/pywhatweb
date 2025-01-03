import plugins


class Pluginmywebftp_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "text": "<TITLE>MyWebFTP</TITLE>"},
			{"text": "<FORM METHOD=post NAME="mwForm" ENCTYPE="multipart / form - data" ACTION="" },
			{ "version" : "/^<P><B>MyWebFTP (Hoster|Free)<\/B> Version ([\d\.]+)/", "offset" : "1 },
			{ "string" : /<BR>Copyright &copy 2000-(20[\d]{2}) <A HREF="http:\/\/www\.mywebftp\.com\/">MyWebFTP<\/A>/" },
			{ "text" : "<LINK REL="stylesheet" TYPE="text/css" HREF=\'mwftp/common/mwftp.css\'>" },
			{ "text" : "<SCRIPT LANGUAGE=JAVASCRIPT SRC=\'mwftp/common/mwftp.js\'></SCRIPT>" },
		]
	return(self.rules)
