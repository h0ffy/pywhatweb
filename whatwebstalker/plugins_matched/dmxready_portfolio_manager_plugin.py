import plugins
			
class Plugindmxready_portfolio_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link href="/css/PortfolioManager/styles_display_page.css" rel="stylesheet" type="text/css">" },
			{ "text" : "<a href=\"javascript:;\" class=\"menu_linkB\" onClick=\"window.open('/applications/PortfolioManager/components/inc_slideshowmanager.asp?index=0','send','toolbar=no,location=no,status=yes,menubar=no,copyhistory=yes,scrollbars=yes,width=700,height=520')\">" },
			{ "text" : "<input name="rememberme_portfoliomanager" type="checkbox"  id="rememberme_portfoliomanager"   value="yes">" },
			{ "regexp" : "/<form action="[^"]*\/applications\/PortfolioManager\/inc_portfoliomanager\.asp" method="POST" name="login" onSubmit="YY_checkform\('login','admin_username_portfoliomanager','#q','0','Please provide Username','admin_username_portfoliomanager','#q','0','Please provide Password'\);return document.MM_returnValue"/i },
		]
		return(self.rules)

