import plugins


class Pluginnopcommerce_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "ghdb": "powered by nopCommerce" "You have no items in your shopping cart."" },
			{ "text" : "<!--Powered by nopCommerce - http://www.nopCommerce.com-->" },
			{ "text" : "Powered by <a href="http://www.nopcommerce.com/">nopCommerce</a>" },
			{ "text" : "Powered by <a href="http://www.nopcommerce.com" target="_blank">nopCommerce</a>" },
			{ "text" : "<input type="submit" name="LoginForm$LoginButton" value="Log in" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;LoginForm$LoginButton&quot;", "&quot;&quot;", "true", "&quot;LoginForm&quot;", "&quot;&quot;", "false", "false))" id="LoginForm_LoginButton" class="adminButtonBlue" />" },
			{ "text" : "<input id="LoginForm_RememberMe" type="checkbox" name="LoginForm$RememberMe" checked="checked" /><label for="LoginForm_RememberMe">Remember me</label>" },
			{ "text" : "var LoginForm_UserNameOrEmailRequired = document.all ? document.all["LoginForm_UserNameOrEmailRequired"] : document.getElementById("LoginForm_UserNameOrEmailRequired");" },
		]
	return(self.rules)
