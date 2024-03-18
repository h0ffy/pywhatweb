import plugins
			
class Plugindd_wrt_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/images/favicon.ico", "md5" : "9c003f40e63df95a2b844c6b61448310" },
			{ "url" : "/style/logo.png", "md5" : "4ec5945774160eb5db079e509a67a20e" },
			{ "text" : "<link type="text/css" rel="stylesheet" href="style/pwc/ddwrt.css" />" },
			{ "certainty" : "75", "version" : "/<title>DD-WRT \((build [^<^\)]+)\) - Info<\/title>/" },
			{ "model" : "/<div class="setting">[\s]+<div class="label"><script type="text\/javascript">Capture\(status_router\.sys_model\)<\/script><\/div>[\s]+([^&]+)&nbsp;[\s]+<\/div>[\s]+<div class="setting">/" },
			{ "text" : "<a href="http://www.dd-wrt.com/">DD-WRT</a><br /><form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank"><input type="hidden" name="cmd" value="_xclick" /><input type="hidden" name="business" value="paypal@dd-wrt.com" /><input type="hidden" name="item_name" value="DD-WRT Development Support" />" },
			{ "string" : /<script type="text\/javascript">[\s]+\/\/<!\[CDATA\[[\s]+document\.write\("<span id=\\"(lan|wc|wl)_mac\\" style=\\"cursor:pointer; text-decoration:underline;\\" title=\\" \+ share\.oui \+ "\\" onclick=\\"getOUIFromMAC\('([A-F\d:]{17})'\)\\" >"\);/", "offset" : "1 },
		]
	return(self.rules)
