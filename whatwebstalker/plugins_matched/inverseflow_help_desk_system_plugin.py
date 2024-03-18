import plugins
			
class Plugininverseflow_help_desk_system_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "text" : "<table width="100%" bgcolor="#FFAD4D" border="0"><tr><td><div class="infobar_01">" },
			{ "version" : "/<table width="100%" bgcolor="#FFAD4D" border="0"><tr><td><div class="infobar_01">InverseFlow Help Desk ([^<]+)<\/td><\/tr><\/table>/" },
			{ "text" : "<div class="normal">To view a ticket", "please enter your email address and ticket ID.  If you forgot your ticket ID", "you can use the <a href="ticket.php?cmd=lost">ticket lookup</a>.</div>" },
			{ "certainty" : "25", "regexp" : "/<div class="normal">[^<]+<a href="ticket\.php\?cmd=lost">/" },
			{ "certainty" : "25", "text" : "<form action="ticketview.php" method="get">" },
			{ "regexp" : "/<form action="ticket\.php" method="get">[\s]+<input type="hidden" name="cmd" value="lost" \/>/" },
		]
	return(self.rules)
