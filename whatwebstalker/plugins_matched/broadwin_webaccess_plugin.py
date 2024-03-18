import plugins
			
class Pluginbroadwin_webaccess_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/favicon.ico", "md5" : "e852c819348eb49dcc549cd594e776ee" },
			{ "text" : "<frame marginheight="0" marginwidth="0" name="rightRunFrame" noresize src="bwRunRight.asp">" },
			{ "text" : "<html><!-- #BeginTemplate "/Templates/bw_templete1.dwt" -->" },
			{ "text" : "<form name="login" action="/broadweb/user/signin.asp" method="post" onSubmit="return validateUserName()">" },
			{ "version" : "/<div style="position:relative;top:15;width:870px; height:15px">[\s]+<font class=e5>[^:^<]+ : ([\d\.]+-[\d]{4}\.[\d]{2}\.[\d]{2})<\/font>[\s]+<\/div>/" },
			{ "search" : "headers[location]", "account" : "/^\.\/broadWeb\/bwRoot\.asp\?username=([^\s^&]+)$/" },
		]
	return(self.rules)
