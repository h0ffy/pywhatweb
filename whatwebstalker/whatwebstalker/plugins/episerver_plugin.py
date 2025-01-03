import plugins


class Pluginepiserver_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"name": "meta generator tag with EPiServer",
     "text": "<meta name=\"GENERATOR\" content=\"EPiServer\" />"},
			{"name": "EPiServer comment", "text": "<!-- EPiServer -->"},
			{"text": "src=" / Util / javascript / episerverscriptmanager.js"'},
			{ "url" : "/App_Themes/Default/Images/General/LoginBackground.gif", "md5" : "5a530899177854181da891894554478a", "version" : "4.x"},
			{ "url" : "/App_Themes/Default/Images/General/LoginBackground.gif", "md5" : "7dea9dcf92792b1bf2bddfe71549dd19", "version" : "5.x-6.x"},
			{ "url" : "/util/images/loginbackground.gif", "md5" : "5a530899177854181da891894554478a", "version" : "4.x"},
			{ "url" : "/util/images/loginbackground.gif", "md5" : "7dea9dcf92792b1bf2bddfe71549dd19", "version" : "5.x-6.x"},
			{ "url" : "/Util/images/EPiServerCMSLogo.png", "md5" : "066ab2c653211887d01e52bcc30293ba", "version" : "6.x"},
			{ "url" : "/util/login.aspx", "text" : "<h1>Log in to EPiServer CMS 6", "version" : "6.x"},
		]
	return(self.rules)
