import plugins
			
class Pluginhunt_electronics_cctv_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" OnLoad="preload_img(false", "\'images/btn_login_red.gif\", "\'images/btn_reset_red.gif\'); placeFocus();na_preload_img(false", "\'img/login_btn2.gif\", "\'img/login_btn4.gif\'); LoadSavedID();">" },
			{ "text" : "   //login.action = "./webviewer.php" ;" },
			{ "text" : "                        <!--<p>If ActiveX control can\'t be loaded", "please download and install Webviewer ActiveX Control.<br>&gt;&gt; <a href="./WebviewerInstaller.exe">Download Webviewer Installer v.1.0.2.4</a>-->", "version" : "HVRM-T1600L" },
			{ "text" : "                        <!--<p>If ActiveX control can\'t be loaded", "please download and install Webviewer ActiveX Control.<br>&gt;&gt; <a href="./WebviewerInstaller.exe">Download Webviewer Installer v.1.0.2.5</a>-->", "version" : "HVRM-H1600L / HVRM-T1600M" },
			{ "text" : "                        <!--<p>If ActiveX control can\'t be loaded", "please download and install Webviewer ActiveX Control.<br>&gt;&gt; <a href="./WebviewerInstaller.exe">Download Webviewer Installer v.1.0.3.0</a>-->", "version" : "HNVS-04" },
		]
		return(self.rules)
