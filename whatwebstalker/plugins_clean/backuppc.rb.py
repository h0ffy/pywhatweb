{ "certainty" : "75", "ghdb" : 'inurl:"/cgi-bin/BackupPC_Admin"' }
{ "text" : '<input type="hidden" name="action" value="hostInfo"><input type="submit" value="Go" name="ignore">' }
{ "text" : '</head><body onLoad="document.getElementById(\'NavMenu\').style.height=document.body.scrollHeight">' }
{ "search" : "headers[www-authenticate]", "regexp" : "/Basic realm="(Backup Admin|BackupPC admin|backuppc)"/ }
{ "url" : "/", "search" : "headers[location]", "regexp" : "/\/cgi-bin\/BackupPC_Admin$/ }