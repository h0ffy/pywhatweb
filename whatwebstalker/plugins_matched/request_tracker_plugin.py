import plugins
			
class Pluginrequest_tracker_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/NoAuth/images/favicon.png", "md5" : "1e35f1aa90c98ca2bab85c26ae3e1ba7" },
			{ "text" : "<link rel="stylesheet" href="/NoAuth/webrtfm.css" type="text/css" />", "module" : "FAQ Manager" },
			{ "text" : "<link rel="stylesheet" href="/RTIR/NoAuth/webrtir.css" type="text/css">", "module" : "Incident Response" },
			{ "text" : "<link rel="shortcut icon" href="/NoAuth/images//favicon.png" type="image/png" />", "module" : "Incident Response" },
			{ "text" : "<link rel="shortcut icon" href="/NoAuth/images/favicon.png" type="image/png" />" },
			{ "text" : "<link rel="stylesheet" href="/NoAuth/css/print.css" type="text/css" media="print" />" },
			{ "certainty" : "25", "text" : "<p id="bpscredits">" },
			{ "regexp" : "/<span class="rtname">RT for ([^<]+)<\/span>/" },
			{ "version" : "/<div class="titlebox-title">[\s]*<span class="left">[\s]*Login[\s]*<\/span>[\s]*<span class="right">[\s]*([^\s]+)[\s]*<\/span>[\s]*<\/div>/" },
			{ "version" : "/&#187;&#124;&#171; RT ([^\s]+) Copyright 1996-20[\d]{2} <a href="http:\/\/www\.bestpractical\.com\?rt=([^\s^"^>]+)">Best Practical Solutions", "LLC<\/a>\./" },
			{ "search" : "headers[set-cookie]", "regexp" : "/RT_SID_[^\s^=]+=[a-f\d]{32};/" },
		]
		return(self.rules)
