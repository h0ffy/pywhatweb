import plugins


class Pluginquest_password_manager_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<div class="text - color - error error - control" style="display: none" id="Account_NotFilled.Textbox">"},
			{"text": "<input type="submit" class="text - color - control button button - text" value="OK" name=" id = "button_Ok_control" / >" },
			{ "text" : "<head><link href="../../App_Themes/Default/Colors.css" type="text/css" rel="stylesheet" /><link href="../../App_Themes/Default/Controls/" },
			{ "text" : "<body id="ctl00_ctl00_ctl00_ctl00_Body" class="master master-base-main master-page-home">" },
			{ "text" : "<form name="aspnetForm" method="post" action="index.aspx" onsubmit="javascript:return WebForm_OnSubmit();" id="aspnetForm" enctype="multipart/form-data" autocomplate="off">" },
			{ "text" : "<div id="ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder_PleaseWait_content" class="progressbar"></div>" },
			{ "text" : "<div id='Control_ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder_ControlBrowserWarning_BrowserWarningPanel_ButtonPlaceHolder1_ButtonIgnore' class='enable hide  text-color-control button button-text'>" },
			{ "text" : "<input type="hidden" id="GINAPageExpiration" value="1200" />" },
			{ "md5" : "11a756ae488de6e3e31c675ab921e70f", "url" : "/QPM/App_Themes/Default/Images/Controls/Icons/32/icon_Warning.png" },
			{ "version" : "/<span id="ctl00_ctl00_ctl00_ContentPlaceHolder_ContentPlaceHolder_ContentPlaceHolder_AboutControl_LabelVersion">Full version number: ([^<]+)<\/span>/" },
		]
	return(self.rules)
