			{ "text" : '<meta name="generator" content="WeBid">' }
			{ "string" : /Powered by <a href="http:\/\/www\.webidsupport\.com\/">WeBid<\/a> &copy; 2008\s?[,-] ([\d]{4}) <a href="http:\/\/www\.webidsupport\.com\/">WeBid<\/a>/ }
			{ "search" : "headers[set-cookie]", "regexp" : "/WEBID_ONLINE=[a-f\d]{32};/ }
			{ "version" : "/<h1>WeBid Installer v([^\s^>]+)<\/h1>[\s]*<form name="form1" method="post" action="\?step=1">/ }
