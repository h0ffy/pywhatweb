import sys
import os
			
class the_php_real_estate_script_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<tr><td><h3>Administration Login<hr size=1/></h3><form action='login.php' method='post'><table border=0 cellpadding=2><tr><td>Username</td><td><input type='text' name='Username' required='yes' validate='text' message='Enter Admin Username.'></td></tr><tr><td>Password</td><td><input type='password' name='Password' required='yes' validate='text' message='Enter Admin Password.'></td></tr><td valign='top'>Image Verification</td>" },
			{ "text" : "<tr><td><h3>Administration Login<hr size=1/></h3><form action='login.php' method='post'><table border=0 cellpadding=2><tr><td>Username</td><td><input type='text' name='Username' required='yes' value='admin' validate='text' message='Enter Admin Username.'></td></tr><tr><td>Password</td><td><input type='password' name='Password' required='yes' validate='text' value='admin' message='Enter Admin Password.'></td></tr><td valign='top'>Image Verification</td>" },
		]

