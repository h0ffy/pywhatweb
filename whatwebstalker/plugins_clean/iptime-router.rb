{ "model" : "/<head><title>EFM Networks ipTIME ([A-Z0-9]+)<\/title>/ }
{ "model" : "/<head><title>EFM networks - ipTIME ([A-Z0-9]+)<\/title>/ }
{ "url" : "/login/login.cgi", "string" : /([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})<\/span><br>[\s]*<span class=item_text><b>Version [\d\.]+<\/b><\/span>/ }
{ "url" : "/login/login.cgi", "firmware" : "/(No IP|[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})<\/span><br>[\s]*<span class=item_text><b>(F\/W )?Version ([\d\.]+)<\/b><\/span>/", "offset" : "2 }
