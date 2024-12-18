import plugins


class Pluginqnap_nas_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"ghdb": "inurl:"Qmultimedia / cgi - bin / thumb_index.cgi" filetype:cgi", "module": "Multimedia Station"},
			{"text": "<title>QNAP Photo Station</title>", "module": "Photo Station"},
			{"text": "<title>QNAP Download Station</title>", "module": "Download Station"},
			{"text": "<TITLE>QNAP Multimedia Station (Photo Album)</TITLE>",
			                                          "module": "Multimedia Station"},
			{"text": "<TITLE>Multimedia Station</TITLE>", "module": "Multimedia Station", "certainty": "75 },
			{ "certainty" : "75", "text" : "NavPage("http://"+ location_hostname_for_ipv6(location.hostname) +":"+ qweb_port +"/", "0);" },
			{ "certainty" : "75", "text" : "location.href=pr+"://["+location.hostname+"]"+pt+redirect_suffix;" },
			{ "regexp" : "/^\/\/window.location = '\/indexnas\.cgi\?counter=' \+ Math\.floor\(\(diff1-diff2\)\/1000\);[\r\n]^window.location.replace\('\/indexnas\.cgi\?counter=' \+ Math\.floor\(\(diff1-diff2\)\/1000\)\);$/" },
			{ "text" : "<a href="http://www.qnap.com"><img src="/ajax_obj/images/qnap_logo_w.gif" alt="QNAP Turbo NAS" title="QNAP Turbo NAS"" },
			{ "text" : "<td class="header_tb_logo"><img id=\'qlogo\' src="/ajax_obj/images/qnap_logo_dark.gif" width="158" height="75"></td>" },
			{ "text" : "<table width="100%" border="0" background="/v3_menu/images/admin_header.jpg" cellpadding="0" cellspacing="0" class="12-blue">", "model" : "Unknown Model (not TS Series)" },
			{ "text" : "<img id="img_webserver" src="/ajax_obj/images/login_main_2.jpg" longdesc="javascript:onQuickLinkChange(2);" alt="Web Server" />", "module" : "QWeb Server" },
			{ "text" : "<img id="img_multimedia" src="/ajax_obj/images/login_main_3.jpg" longdesc="javascript:onQuickLinkChange(3);" alt="Multimedia Station" />", "module" : "Multimedia Station" },
			{ "text" : "<img id="img_download" src="/ajax_obj/images/login_main_4.jpg" longdesc="javascript:onQuickLinkChange(4);" alt="Download Station" />", "module" : "Download Station" },
			{ "text" : "<img id="img_webfile" src="/ajax_obj/images/login_main_5.jpg" longdesc="javascript:onQuickLinkChange(5);" alt="Web File Manager" />", "module" : "Web File Manager" },
			{ "text" : "<img id="img_surveillance" src="/ajax_obj/images/login_main_6.jpg" longdesc="javascript:onQuickLinkChange(6);" alt="Surveillance Station" />", "module" : "Surveillance Station" },
			{ "text" : "<title>Welcome to QNAP Turbo NAS</title>" },
			{ "url" : "/ajax_obj/images/favicon.ico", "md5" : "9afa5d60e5ef15dc75d7662e418cac72" },
		]
	return(self.rules)
