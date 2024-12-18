import plugins


class Pluginhorde_application_framework_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "title="This site is powered by The Horde Application Framework." href="http: // horde.org">"},
			{"text": "Powered by </font><a href="http: // www.horde.org / " TARGET=_blank>"},
			{"text": "<!-- IMP: Copyright 2001-2006", "The Horde Project. IMP is under the GPL. -->"},
			{"text": "<!--   Horde Project: http://horde.org/ | IMP: http://horde.org/imp/    -->"},
			{"text": "/themes/graphics/horde-power1.png" alt = "Powered by Horde" title = " />"},
			{"md5": "b74924c612af6030729d7ac3bd0ef803",
     "url": "themes/graphics/horde-power1.png"},
			{"text": "if (typeof(_setHordeTitle) == 'undefined' && document.title && parent.frames.horde_main) parent.document.title = document.title;"},
			{"text": "<!-- This file contains any "Message Of The Day" Type information -->"},
			{"text": "<a href="icon_browser.php?app = chora">Version Control</a><br />"},
			{"text": "<html><body bgcolor="  # aaaaaa"><a href="icon_browser.php">Application List</a><br /><br /><h2>Icons for My Account</h2>" },
			{"version": "/<title>WebMail ([\\d\\.]+) LOGIN<\\/title>/"},
			{"text": "<script language="JavaScript" type="text / javascript" src=" / hunter / js / enter_key_trap.js"></script>"},
			{"text": "<link href=" / mail / mailbox.php?mailbox = INBOX" rel="Top" />"},
			{"version": "/<!-- \\$Horde: horde\\/config\\/conf.xml,v ([\\d\\.]+) /"},
		]
	return (self.rules)
