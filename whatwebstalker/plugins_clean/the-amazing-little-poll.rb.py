			{ "version" : "/<h1>The Amazing Little Poll Admin Center v([^<]+)<\/h1>/ }
			{ "text" : '<form action="lp_admin.php" method="post" name="form0">Admin Password:<input type="hidden" name="adminstep" value="1"><input type="Password" name="pwd" size="20"><br><input type="Submit" value="OK"></form>' }
			{ "url" : "lp_settings.inc", "string" : /\/\/ Change this password so no one else can access the lp_admin\.php via the web\s+\$pwd="([^"]+)";/ }
			{ "search" : "headers[set-cookie]", "regexp" : "/pollidcookie=/ }
