import plugins


class Pluginnetcomm_wireless_hotspot_gateway_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"model": "HS1100", "url": "/imgs_login/login_r3_c4.gif",
			    "md5": "c2ad9dc7eefb06f310782039011bd508"},
			{"certainty": "25", "url": "/", "regexp": "/if \\(now < 946685000 \\)[\\s]+\\{[\\s]+alert\\("Warning! The system time is wrong and may cause the inaccuracy of authentication and billing\. Please refer to the user manual to set up the correct system time\."\);/" },
			{ "certainty" : "25", "url" : "/", "text" : "<td colspan="8" align="center" background="imgs_login/login_r6_c7.gif"><font class="loginmsg"><strong>Welcome To Administrator Login Page<br> Please Enter Your User Name and Password To Sign In.</strong></font>&nbsp;</td>" },
		]
	return(self.rules)
