```python
import plugins

class Pluginibm_cognos_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<meta name="Trademark" content="Licensed Material - Property of IBM Corp. IBM, the IBM logo, and Cognos are trademarks of IBM Corp., registered in many jurisdictions worldwide." />' },
            { "ghdb" : 'inurl:"cognos/cgi-bin/cognos.cgi"' },
            { "ghdb" : 'inurl:"cognos8/cgi-bin/cognos.cgi"' },
            { "text" : '<td nowrap class="copyright" id="loginLegalContainer">Licensed Material - Property of IBM Corp.<br>(C) Copyright IBM Corporation and its licensors 2005, 2009.<br>IBM, the IBM logo, and Cognos are trademarks of IBM Corp., registered in many jurisdictions worldwide.</td>' },
        ]
        return self.rules
```