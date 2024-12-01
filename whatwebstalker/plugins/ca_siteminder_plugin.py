```python
import plugins

class Pluginca_siteminder_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/<td><img alt=\"Logo\" src=\"(\\/)?(siteminderagent\\/)?(pw\\/|pwcgi\\/|pwserv\\/)?siteminder_logo\\.gif\" height=\"44\"><\\/td><\\/tr><\\/table>/" },
            { "text" : "<!-- SiteMinder Encoding=UTF-8; -->" },
            { "text" : "<!-- SiteMinder Encoding=ISO-8859-1; -->" },
            { "text" : "<tr><td></td></tr></table></td></tr></table></center></div><!--</form> --></body></html>" },
            { "regexp" : r"/\\/\\* SiteMinder Login Form CGI\\s+Copyright \\(C\\) 1999,2000 Netegrity", "Inc\\. All rights reserved\\./" },
            { "url" : "/siteminderagent/forms/login.fcc", "text" : "<title>SiteMinder Password Services</title>" },
        ]
        return self.rules
```