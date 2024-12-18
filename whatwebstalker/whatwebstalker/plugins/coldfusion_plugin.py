import plugins


class Plugincoldfusion_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "	<title>ColdFusion Administrator Login</title>"},
			{"regexp": "/<meta name="Author" content="Copyright(\(c\)\ )?[0-9]{4}-[0-9]{4} Macromedia( Corp|", "Inc)\. All rights reserved\.">/" },
			{ "text" : "	{   document.write(\"<link rel='STYLESHEET' type='text/css' href='./cfadmin_ns.css'>\");}" },
			{ "text" : "<form name="loginform" action="./enter.cfm" method="POST" onSubmit="cfadminPassword.value = hex_hmac_sha1(salt.value", "hex_sha1(cfadminPassword.value));" >" },
			{ "text" : "<input name="cfadminPassword" type="Password" size="15" style="width:15em;" class="label" maxlength="100" id="admin_login">" },
			{ "text" : "	Macromedia", "the Macromedia logo", "Macromedia ColdFusion and ColdFusion are<br />" },
			{ "text" : "	<tr><td><img src="./images/mx_copyrframe.gif" width="2" height="57" border="0" alt="ColdFusion MX" hspace="10"></td>" },
			{ "url" : "/CFIDE/administrator/images/loginbackground.jpg", "md5" : "596b3fc4f1a0b818979db1cf94a82220", "version" : "9.x" },
			{ "url" : "/CFIDE/administrator/images/AdminColdFusionLogo.gif", "md5" : "620b2523e4680bf031ee4b1538733349", "version" : "7.x" },
			{ "search" : "headers[page-completion-status]", "certainty" : "75", "regexp" : "/(Abnormal|Normal)/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/CFAUTHORIZATION_cfadmin=/" },
			{ "name" : "File extension", "regexp" : "/^(cfm|cfc)$/", "search" : "uri.extension" },
		]
	return(self.rules)
