import plugins
			
class Pluginconexant_emweb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<table border="1" cellpadding="0" cellspacing="0" scrolling="no" style="border-collapse: collapse"bordercolor="#FFFFFF" width="80%">", "status" : "401 },
			{ "text" : "<title>Flexor 151 Home</title>", "model" : "Flexor 151" },
			{ "text" : "<td><b>Flexor 151</b> is connected and working properly", "for more information", "model" : "Flexor 151" },
			{ "text" : "Advanced configuration: <a style="font-size: 90%" href="voice.html">Voice Settings</a>&nbsp;&nbsp;&nbsp;<a style="font-size: 90%" href="network.html">Network Settings</a>&nbsp;&nbsp;&nbsp;<a style="font-size: 90%" href="qos.html">QoS Settings</a>", "model" : "Flexor 151" },
			{ "text" : "<h2><a class="lg" href="status.html">Flexor 151</a></h2>", "model" : "Flexor 151" },
			{ "text" : "<tr valign="middle"><td class="tmainhead"><img src="/webconfig/images/blank.gif" width="49" height="10" alt=" hspace="0" vspace="0" align="top" id="logospacer">e-con TDL-3424M Ethernet Router</td></tr>", "model" : "e-con TDL-3424M" },
			{ "text" : "<TITLE>AT-iMG634WA</TITLE>", "model" : "Allied Telesyn-iMG634WA" },
			{ "text" : "<TITLE>AT-iMG606BD</TITLE>", "model" : "Allied Telesyn-iMG606BD" },
			{ "text" : "<TITLE>AT-iMG646BD</TITLE>", "model" : "Allied Telesyn-iMG646BD" },
			{ "md5" : "1ddf1d795d6576316495844f824dc84f", "url" : "/images/banner2.gif", "model" : "Allied Telesyn-iMG634WA" },
			{ "md5" : "27bc3ddd5ca0799f0a9e1035f76b390c", "url" : "/images/banner2.gif", "model" : "AT-iMG646BD / AT-iMG606BD" },
			{ "text" : "<p class="help_data"><b>Note:</b> If "Checking Firmware Upgrades Automatically" or "Image Upgrade" fails then please contact your service provider.</p>", "url" : "/help.html", "model" : "Allied Telesyn-iMG634A-R2" },
			{ "version" : "/Conexant-EmWeb\/([^\r^\n]+)/", "search" : "headers[server]"},
			{ "version" : "/Virata-EmWeb\/([^\r^\n]+)/", "search" : "headers[server]"},
		]
			return(self.rules)
