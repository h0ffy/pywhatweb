```python
import plugins

class Pluginapache_archiva_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "certainty" : "25", "text" : "<title>Apache Archiva \\\\" },
            { "text" : 'No context on this server matched or handled this request.<BR>Contexts known to this server are: <ul><li><a href="/archiva">/archiva&nbsp;--->&nbsp;org.mortbay.jetty.webapp.WebAppContext' },
            { "text" : '<form namespace="/" id="quickSearch" name="quickSearch" onsubmit="customOnsubmit_quickSearch(); return validateForm_quickSearch();" action=""' },
            { "text" : '<form namespace="/" id="quickSearch" name="quickSearch" onsubmit="return validateForm_quickSearch();" action=""' },
            { "version" : r'/<div class="xleft">\s+<a target="_blank" href="http:\/\/archiva\.apache\.org\/">Apache Archiva ([\d\.]+)<\/a>\s+<\/div>\s+<div class="xright">/' },
            { "version" : r'/<div class="xleft">\s+Apache Archiva ([\d\.]+)\s+<\/div>\s+<div class="xright">/' },
        ]
        return self.rules
```