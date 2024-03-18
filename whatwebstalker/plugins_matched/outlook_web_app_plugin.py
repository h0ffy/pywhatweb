import plugins
			
class Pluginoutlook_web_app_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<body class="owaLgnBdy">" },
			{ "version" : "/<link type="text\/css" rel="stylesheet" href="\/owa\/([^\s^\/]+)\/themes\/base\/logon\.css">/" },
			{ "version" : "/<td><img src="\/owa\/([^\s^\/]+)\/themes\/base\/warn\.png"><\/td>/" },
			{ "version" : "/<link rel="shortcut icon" href="\/owa\/([^\s^\/]+)\/themes\/base\/favicon\.ico" type="image\/x-icon">/" },
			{ "text" : "<!-- OwaPage = ASP.auth_logon_aspx -->" },
			{ "regexp" : "/<FORM action="(\/CookieAuth\.dll\?Logon|\/exchweb\/bin\/auth\/owaauth\.dll)" method="POST" name="logonForm"/i },
			{ "ghdb" : "inurl:/exchweb/bin/auth/owalogon.asp" },
			{ "name" : "html body", "url" : "/exchweb/bin/auth/owalogon.asp?url=https://1&reason=2',"text" : "<TR><TD><P style="color:red">You could not be logged on to'},
			{ "name" : "html body", "url" : "/CookieAuth.dll?GetLogon?url=/&reason=2',"text" : "<TR><TD><P style="color:red">You could not be logged on to'},
			{ "name" : "html title", "text" : "<TITLE>Microsoft Outlook Web Access</TITLE>" },
			{ "string" : /<IMG title="Microsoft Office Outlook Web Access provided by Microsoft Exchange Server ([\d]{4})" alt="Microsoft Office Outlook Web Access provided by Microsoft Exchange Server ([\d]{4})" height=62 src="\/exchweb\/img\/logon_logo\.gif" width=331 border=0 hspace=0>/" },
			{ "text" : "<td style="width:100%">To use Outlook Web App", "browser settings must allow scripts to run. For information about how to allow scripts", "consult the Help for your browser. If your browser doesn\'t support scripts", "you can download <a href="http://www.microsoft.com/windows/ie/downloads/default.mspx">Windows Internet Explorer</a> for access to Outlook Web App.</td>" },
		]
		return(self.rules)
