import plugins
			
class Plugincontrexx_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : " - powered by Contrexx   Web Content Management System</title>" },
			{ "text" : "<p id="powered"><a href="http://www.contrexx.com/" title="Powered by Contrexx&reg; Software">Powered by Contrexx&reg; Software</a>" },
			{ "text" : "<div class="footer_right">Powered by <a href="http://www.contrexx.com">Contrexx Software</a></div>" },
			{ "text" : "<meta name="generator" content="Contrexx   Web Content Management System"/>" },
			{ "text" : "<style type="text/css">@import url(core_modules/frontendEditing/css/style.css) all;</style>" },
			{ "text" : "<title>Contrexx Administration Console</title>" },
			{ "text" : "		<td><input type="submit" tabindex="4" name="submit_button" value="Anmelden" onclick="if(this.disabled || typeof(this.disabled)==\'boolean\') this.disabled=true ; form_submitted_test=form_submitted ; form_submitted=true ; form_submitted=(!form_submitted_test || confirm(\'Are you sure you want to submit this form again?\')) ; if(this.disabled || typeof(this.disabled)==\'boolean\') this.disabled=false ; sub_form=\'\' ; return true" /></td>" },
		]
	return(self.rules)
