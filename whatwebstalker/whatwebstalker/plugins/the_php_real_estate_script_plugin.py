import plugins


class Pluginthe_php_real_estate_script_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "text": "<tr><td><h3>Administration Login<hr size=1/></h3><form action='login.php' method='post'><table border=0 cellpadding=2><tr><td>Username</td><td><input type='text' name='Username' required='yes' validate='text' message='Enter Admin Username.'></td></tr><tr><td>Password</td><td><input type='password' name='Password' required='yes' validate='text' message='Enter Admin Password.'></td></tr><td valign='top'>Image Verification</td>"
            },
            {
                "text": "<tr><td><h3>Administration Login<hr size=1/></h3><form action='login.php' method='post'><table border=0 cellpadding=2><tr><td>Username</td><td><input type='text' name='Username' required='yes' value='admin' validate='text' message='Enter Admin Username.'></td></tr><tr><td>Password</td><td><input type='password' name='Password' required='yes' validate='text' value='admin' message='Enter Admin Password.'></td></tr><td valign='top'>Image Verification</td>"
            },
        ]
        return self.rules
