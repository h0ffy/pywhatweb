{ "certainty" : "75", "regexp" : "/<TITLE>HP System Management Homepage Login<\/TITLE>/ }
{ "search" : "headers[set-cookie]", "regexp" : "/Compaq-HMMD=/ }
{ "search" : "headers[server]", "version" : "/CompaqHTTPServer\/[^\s]+ HP System Management Homepage\/([\d\.]+)$/ }
