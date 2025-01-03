import plugins


class Plugineasy_site_edit_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/Powered by <a href="http: \/\/www\.easysiteedit\.com" class="link(tahoma11)?[^"]*" target="_blank">Easy Site-Edit<\/a>/" },
			{ "account" : "/<TD bgcolor=#(F7FDFF|FFFFFF)>FTP User Name<\/TD>[\s]+<TD bgcolor=#(F7FDFF|FFFFFF)><INPUT TYPE="text" NAME="user_name" value="([^"]+)" class="textboxset(enlarge)?">(<p>\[&nbsp;Note:&nbsp;Ftp user name to login into the server&nbsp;\]<\/p>|&nbsp;&nbsp;&nbsp;\(Ftp user name to login into the server\))<\/TD>/", "offset" : "2 },
			{ "account" : "/<TD bgcolor=#(F7FDFF|FFFFFF)>FTP User Password<\/TD>[\s]+<TD bgcolor=#(F7FDFF|FFFFFF)><INPUT TYPE="password" NAME="user_pass" value="([^"]+)" class="textboxset(enlarge)?">(&nbsp;&nbsp;&nbsp;\(Ftp password to login into the server\)|<p>[&nbsp;Note:&nbsp;Ftp password to login into the server&nbsp;]<\/p>)<\/TD>/", "offset" : "2 },
			{ "filepath" : "/<TD bgcolor=#(F7FDFF|FFFFFF)>FTP Directory of CMS<\/TD>[\s]+<TD bgcolor=#(F7FDFF|FFFFFF)><INPUT TYPE="text" NAME="dir_cms" value="([^"]+)" class="textboxset(enlarge)?">(&nbsp;&nbsp;&nbsp;\(Directory path of cms in the remote server.\)|<p>\[&nbsp;Note:&nbsp;Directory path of cms in the remote server&nbsp;\]<\/p>)<\/TD>/", "offset" : "2 },
		]
	return(self.rules)
