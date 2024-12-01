```python
import plugins

class Pluginfree_simple_software_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<tr><td><input type='submit' name ='submit' value ='Login'>&nbsp;</td></form><form action='/index.php?logout=logout' method='post'><td>&nbsp;<input type='submit' name ='submit' value ='Cancel'></td></tr></table></form><p>[<a href='/index.php?page=login&request=forgot_password&include=admin_login.inc'><font color='" },
            { "text" : "Powered by <a href='http://www.freesimplesoft.com'><font color='#FFFFFF'>Free Simple Software</font></a> (<a href='http://www.freesimplecms.com'><font color='#FFFFFF'>Free Simple CMS</font></a> / <a href='http://www.freesimpleshop.com'><font color='#FFFFFF'>Free Simple Shop</font></a> / <a href='http://www.freesimpleblog.com'><font color='#FFFFFF'>Free Simple Blog</font></a> / <a href='http://www.freesimplehost.com'><font color='#FFFFFF'>Free Simple Host</font></a>)" },
        ]
        return self.rules
```