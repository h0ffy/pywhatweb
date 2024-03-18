import sys
import os
			
class sqlitemanager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- SQLiteFunctionProperties.class.php : propView() -->' }
			{ "text" : '<!-- common.lib.php : displayMenuTitle() -->' }
			{ "text" : '<td style="white-space: nowrap">	<form name="database" action="main.php" enctype="multipart/form-data" method="POST" onSubmit="checkPath();" target="main">' }
			{ "text" : '<h2 class="sqlmVersion">Database : <a href="main.php?dbsel=' }
			{ "string" : /<title>(SQLite version [\d\.\s-]+)(undefined)?<\/title>/ }
			{ "version" : '/<h2 class="sqlmVersion">Welcome to <a href="http:\/\/www\.sqlitemanager\.org" target="_blank">SQLiteManager<\/a> version ([^\s^>]+)<\/h2>/ }
			{ "string" : /<h4 class="serverInfo">(SQLite version [\d\.\s-]+)(undefined)? \/ PHP version 5.2.17<\/h4>/ }
			{ "string" : /<h4 class="serverInfo">SQLite version [\d\.\s-]+(undefined)? \/ (PHP version [^\s^<]+)<\/h4>/", "offset" : '1 }
	]

