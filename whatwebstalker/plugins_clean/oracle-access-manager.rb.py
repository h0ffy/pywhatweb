			{ "version" : "/<p id="footerVersion">Oracle Access Manager Version: ([^\s]+)<\/p>/ }
			{ "search" : "headers[set-cookie]", "regexp" : "/ObSSOCookie=[^;]+;/", "certainty" : "75 }
			{ "search" : "headers[location]", "regexp" : "/obrareq\.cgi/", "certainty" : "75 }
