import plugins


class Plugincanon_print_server_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<tr><td align="left"><A href="http: // www.niigata - canotec.co.jp" name="canon_group" target="new_win">"},
			{"url": "/ps_stat.htm",
     "firmware": "/<td>Hardware ID: [^<]{1,10}<br>Firmware Version: ([^<]{1,10})<br>Protocol ID: [^<]{1,10}<br>Default Name: [^<]{1,10}<br>Server Name: [^<]{1,10}<br>H\\/W Address: [^<]{12}<br>/"},
			{"url": "/ps_stat.htm", "string": / <td > Hardware ID: [ ^ <]{1, 10} < br > Firmware Version: [^<]{1, 10} < br > Protocol ID: [^<]{1, 10} < br > Default Name: [^<]{1, 10} < br > Server Name: [^<]{1, 10} < br > H\/W Address: ([^<]{12})<br>/" },
			{ "url" : "/canongrp.gif", "md5" : "894c5a7115790dc428592752baa20d13" },
			{ "url" : "/canoninc.gif", "md5" : "3f780904c5f8e650d0fb0df6b5e28d6b" },
			{ "model" : "Nethawk", "text" : "<a href="tcp_ip.htm">[TCP/IP]</a> <a href="netware.htm">[NetWare]</a> <a href="apple.htm">[AppleTalk]</a> <a href="smb.htm">[SMB]</a>" },
			{ "model" : "/<center>[\r\n]*<h1>[\r\n]*<b>(NetHawk N-111|NetHawk N500)<\/b><\/h1><\/center>/" },
			{ "text" : "<meta name="GENERATOR" content="Mozilla/4.7 [ja] (Win98; I) [Netscape]">", "model" : "NetHawk N-111", "certainty" : "25 },
			{ "certainty" : "25", "version" : "/^PRINT_SERVER WEB ([\d\.]+)$/", "search" : "headers[server]" },
		]
	return(self.rules)
