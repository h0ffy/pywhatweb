import plugins
			
class Plugintele_data_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by Teledata<br>\n<center>Best viewed in IE6\.<\/center>/" },
			{ "text" : "<input name="txthomepassword" type="password"  size="22" id="txthomepassword" maxlength="200" />" },
			{ "text" : "align=center class="tdi-errormessage" style="height: 25px"><script type="text/javascript">showerror();</script></td>" },
			{ "text" : "<!--To reduce the gap between banner and content the below if condition is added-->" },
			{ "text" : "<iframe onload="postload(0);" scrolling="no" style="position:absolute;top:0;left:0;height:0;width:0;" id="fraLH" name="fraLH" src="default.aspx" frameborder="0" marginheight="0" marginwidth="0"></iframe>" },
		]
	return(self.rules)
