import sys
import os
			
class Pluginphp_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "url" : "/?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000", "version" : "/<tr class="h"><th colspan="2">PHP (\d) Authors<\/th><\/tr>/" },
			{ "url" : "/?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000", "version" : "/<tr class="h"><th>PHP ([\d\.]+) Quality Assurance Team<\/th><\/tr>/" },
			{ "filepath" : "/<b>(Warning|Fatal error)<\/b>: .* in <b>([^<]+)<\/b> on line <b>[0-9]+<\/b><br \/>/", "offset" : "1 },
			{ "account" : "/<b>(Warning|Fatal error)<\/b>: .* in <b>\/home\/([^<^\/]+)\/[^<]*<\/b> on line <b>[0-9]+<\/b><br \/>/", "offset" : "1 },
			{ "account" : "/<b>(Warning|Fatal error)<\/b>: .* in <b>[A-Z]{1}:\\(Documents and Settings|Users)\\([^<^\\]+)\\[^<]*<\/b> on line <b>[0-9]+<\/b><br \/>/i", "offset" : "2 },
			{ "version" : "/[^\r^\n]*PHP\/([^\s^\r^\n]+)/", "search" : "headers[server]" },
			{ "module" : /[^\r^\n]*PHP\/[^\s^\r^\n]+ with (Hardening-Patch|Suhosin-Patch)/", "search" : "headers[server]" },
			{ "version" : "/[^\r^\n]*PHP\/([^\s^\r^\n]+)/", "search" : "headers[x-powered-by]" },
			{ "module" : /[^\r^\n]*PHP\/[^\s^\r^\n]+ with (Hardening-Patch|Suhosin-Patch)/", "search" : "headers[x-powered-by]" },
			{ "regexp" : "/^Error parsing (.+) on line [\d]+$/", "search" : "headers[php]" },
			{ "filepath" : "/^Error parsing (.+) on line [\d]+$/", "search" : "headers[php]" },
			{ "filepath" : "/^Error parsing \/home\/([^\/]+)\/.+ on line [\d]+$/", "search" : "headers[php]" },
			{ "name" : "PHP Warning Header", "regexp" : "//", "search" : "headers[php warning]" },
			{ "name" : "File extension", "regexp" : "/^(php|phtml|php3|php4|php5|phps)$/", "search" : "uri.extension" },
		]

