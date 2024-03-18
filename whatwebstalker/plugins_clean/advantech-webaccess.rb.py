			{ "text" : '<html><!-- #BeginTemplate "/Templates/bw_templete1.dwt" -->' }
			{ "text" : '<a href="/broadweb/WebAccessClientSetup.exe">' }
			{ "search" : "headers[location]", "regexp" : "/\.\/broadWeb\/bwviewpg\.asp\?proj=/ }
			{ "search" : "headers[location]", "account" : "/\.\/broadWeb\/bwRoot\.asp\?username=([^\s]+)/ }
			{ "version" : "/<div style="position:relative;top:15;width:870px; height:15px">\s+<font class=e5>[^:^<]+ : ([^\s]+)<\/font>/ }
