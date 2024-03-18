{ "version" : "/<div id=footer>[\s]+<a href="http:\/\/www\.rejetto\.com\/hfs\/">HttpFileServer ([^<]+)<\/a>[\s]+<br \/>Servertime/ }
{ "version" : "/^HFS (\d\.\d.+)$/", "search" : "headers[server]" }
{ "regexp" : "/^HFS /", "search" : "headers[server]" }
