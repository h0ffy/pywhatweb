import plugins
			
class Pluginemc_documentum_webtop_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<body  marginwidth='0' topmargin='40' bottommargin='0' class='contentBackground' leftmargin='0' rightmargin='0' marginheight='40'>" },
			{ "text" : "<select name='Login_docbase_0' id='DocbaseName' title=\"Repository\" size='0' class=defaultDropdownListStyle onchange='setKeys(event);" },
			{ "text" : "<td scope="row" align=\'right\' class="fieldlabel" height="30"><span  class=\'defaultLabelStyle\'>Repository</span></td><td class="defaultcolumnspacer">:&nbsp;</td>" },
			{ "text" : "<td nowrap class="logintitletext" height="23" valign="top"><span  class=\'dialogTitle\'>Webtop Login" },
			{ "text" : "<script type="text/javascript">var g_virtualRoot = "/webtop";</script>" },
			{ "text" : "<td><input type='text' name='MyLogin_username_0' id='LoginUsername' title=\"Login Name\" size='40' onkeypress=\"handleKeyPress(event)\"></td>" },
			{ "regexp" : "/<script type="text\/javascript" src='\/webtop\/index\.js'><\/script>[\s]+<\/head>[\s]+<body onload='doRedirect\("\/component\/main"\)'>[\s]+<\/body>[\s]+<\/html>/" },
			{ "version" : "/<div id="logo"><span  class='defaultLabelStyle'>Webtop<\/span>[\s]?&nbsp;<span  class='dialogTitleVersion'>([^<]+)<\/span>/" },
		]
	return(self.rules)
