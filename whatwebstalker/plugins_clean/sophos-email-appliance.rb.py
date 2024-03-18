			{ "search" : "headers[server]", "regexp" : "/^Sophos Email Appliance$/ }
			{ "search" : "headers", "string" : /[Ss]erver: Sophos Email Appliance\r?\n.+Location: https?:\/\/([^\/]+)/m }
			{ "text" : '<td class="logincontent" valign="top"><a href="http://www.sophos.com"><img src="images/logo_sophos.gif" border="0" alt="Email Appliance"></a></td>' }
			{ "text" : '<title>Sophos Email Appliance</title>", "certainty" : "75 }
			{ "text" : '<!-- end main content -->", "certainty" : "25 }
