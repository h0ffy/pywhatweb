import plugins
			
class Pluginjive_sbs_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<link rel="stylesheet" href="\/([\d\.]+)\/styles\/jive-global\.css" type="text\/css" media="all" \/>/" },
			{ "version" : "/<link rel="stylesheet" href="\/([\d\.]+)\/styles\/jive-icons\.css" type="text\/css" media="all" \/>/" },
			{ "text" : "<a href="#jive-body-full" class="jive-skip-nav">Skip navigation</a>" },
			{ "text" : "<body class="jive-body-formpage jive-body-formpage-login" >" },
			{ "version" : "/<a class="font-color-meta" href="http:\/\/www\.jivesoftware\.com\/poweredby\/" target="_blank" alt="Jive Software Version: [\d]+">[^<]+powered by Jive SBS &reg; ([^\s]+)  community software[\s]+<\/a>[\s]+<div class="jiveVersion" style="display: none;">/" },
			{ "module" : /jive\.rte\.defaultStyles\.push\("\/plugins\/([^\/]+)\/resources\/styles\/[^\.]+\.css"\);/" },
			{ "version" : "/<div id="jive-loginVersion">[\s]+Jive SBS[\s]+([^\s]+)[\s]+<\/div>/" },
			{ "url" : "/community/admin/images/jive-logo.png", "md5" : "8badf8cdaaa8e9adf2e552bc3ab77f49" },
			{ "url" : "/admin/images/jive-logo.png", "md5" : "8badf8cdaaa8e9adf2e552bc3ab77f49" },
			{ "url" : "/___sbsstatic___/logo-jive-darkgloss.jpg", "md5" : "70c76564f1c22c6d9a66854fdc721fd9" },
			{ "text" : " * This software is the proprietary information of Jive Software. Use is subject to license terms.", "url" : "/0.0.0/styles/jive-global.css" },
			{ "search" : "headers[set-cookie]", "string" : /jive\.server\.info="?serverName=[^:]+:serverPort=[\d]+:contextPath=[^:]*:(localName=[^:]+:localPort=[\d]+):localAddr=/" },
			{ "search" : "headers[x-jsl]", "regexp" : "/^D=[\d]+ t=[\d]+$/" },
			{ "search" : "headers[x-jal]", "regexp" : "/^[\d]+$/" },
		]
		return(self.rules)
