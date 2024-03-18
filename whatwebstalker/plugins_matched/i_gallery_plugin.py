import plugins
			
class Plugini_gallery_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>.:: i-Gallery ([\d\.]+) -[^:]+:.<\/title>/" },
			{ "version" : "/<font class="textsm">Powered By:&nbsp;<a class="linksm" href="http:\/\/www.b-cp.com\/igallery" target="_blank">i-Gallery ([\d\.]+)<\/a>/i },
			{ "text" : "var verify = confirm("Are you sure you want to permanently delete the selected \"Item\" from the i-Gallery database?  All information will be lost!");" },
			{ "text" : "<!-- ################ Begin Empty Root Folder Message ################ -->" },
			{ "regexp" : "/<img src="images\/igallery-logo.gif" width=[0-9]* height=[0-9]* border=[0-9]* alt="i-Gallery Home Page"><\/a><br>/" },
			{ "text" : "<title>.::  - Photo Viewer ::.</title>", "path" : "ViewPhoto.asp" },
		]
		return(self.rules)
