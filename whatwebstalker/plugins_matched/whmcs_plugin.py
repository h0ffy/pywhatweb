import sys
import os
			
class whmcs_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<p align="center">Powered by <a href="http://www.whmcs.com/" target="_blank">WHMCompleteSolution</a></p>' }
			{ "text" : '<td align="right" valign="middle">Powered by <a href="http://www.whmcs.com/" target="_blank">WHMCS</a></td>' }
			{ "text" : '<div id="welcome_box">Please <a href="clientarea.php" title="Login"><strong>Login</strong></a> or <a href="register.php" title="Register"><strong>Register</strong></a></div>' }
			{ "version" : '/<tr><td bgcolor="#efefef" height="20" align="center"><a href="index\.php">Home<\/a> \| <a href="clients\.php">Clients<\/a> \| <a href="supporttickets\.php">Tickets<\/a> \| <a href="orders\.php">Orders<\/a> \| <a href="activitylog\.php">Activity<\/a> \| <a href="logout\.php">Logout<\/a><\/td><\/tr>[\s]+<tr><td align="center">[^,^\s]+", "[^<]+<br \/>Version: ([^<^\s]+)<\/td><\/tr>/ }
			{ "text" : '<p>Got a new license key?  <a href="licenseerror.php?licenseerror=change">Click here to enter it</a></p>' }
		]

