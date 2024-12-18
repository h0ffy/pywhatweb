import plugins


class Pluginvmware_zimbra_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta name="description" content="Zimbra provides open source server and client software for messaging and collaboration. To find out more visit http: // www.zimbra.com.">"},
			{"text": "<!--div id="ZLoginAppName">Web Client</div-->"},
			{"text": "<title>Zimbra Web Client Log In</title>"},
			{"text": "<h1><a href="http: // www.zimbra.com / " id="bannerLink" target="_new">"},
			{"text": "<td><input id="password" class="zLoginField" name="password" type="password" value=" size = "40" / > < /td >" },
			{ "text" : "<div id="ZLoginWhatsThis" class="ZLoginInfoMessage" style="display:none;"><center style="margin-bottom:3px;"><b>Client Types:</b></center>" },
			{ "text" : "<div id="ZLoginNotice" class="legalNotice-small"><a target="_new" href="http://www.zimbra.com">Zimbra</a> :: the leader in open source messaging and collaboration ::" },
		]
	return(self.rules)
