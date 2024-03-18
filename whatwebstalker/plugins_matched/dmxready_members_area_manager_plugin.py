import plugins
			
class Plugindmxready_members_area_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<p align="center"><a href="[^"]*\/applications\/MembersAreaManager\/inc_membersareamanager\.asp\?show=sendpassword">Forget Password\?<\/a>/" },
			{ "regexp" : "/<form ACTION="[^"]*\/applications\/MembersAreaManager\/inc_membersareamanager\.asp" method="POST" name="login" onSubmit="YY_checkform\('login','entity_username','#q','0','Please provide username','entity_password','#q','0','Please provide password'\);return document.MM_returnValue" >/" },
		]
	return(self.rules)
