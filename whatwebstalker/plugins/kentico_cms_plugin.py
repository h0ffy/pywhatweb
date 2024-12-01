```python
import plugins

class Pluginkentico_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<\/title><meta name="generator" content="Kentico CMS [^\\(^>]{1,5} \(build ([\d\.]{1,10})\) [^"^>]*" \/>/' },
            { "regexp" : r'/2fCMSAdministration.aspx" id="form1" class="logon-page"/', "name" : "Admin-Login-Page", "certainty" : "100"},
            { "search" : "headers[set-cookie]", "regexp" : r'/CMSCsrfCookie/', "name" : "CMSCsrfCookie cookie" },
            { "search" : "headers[set-cookie]", "regexp" : r'/CMSCurrentTheme/', "name" : "CMSCurrentTheme cookie" },
            { "search" : "headers[set-cookie]", "regexp" : r'/CMSPreferredCulture/', "name" : "CMSPreferredCulture cookie" },
            { "search" : "headers[set-cookie]", "regexp" : r'/CMSCsrfCookie/', "name" : "CMSCsrfCookie cookie" },
        ]
        return self.rules
```