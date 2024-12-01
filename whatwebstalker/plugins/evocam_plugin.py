```python
import plugins

class Pluginevocam_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/<title>EvoCam( \d)*<\/title>/" },
            { "regexp" : r"/<TITLE>EvoCam( Java| JavaScript)? Example Page<\/TITLE>/" },
            { "text" : r'Powered by <A HREF="http://www.evological.com/evocam.html">EvoCam</A>' },
            { "regexp" : r'/<applet archive="evocam.jar" code="com.evological.evocam.class"/' },
            { "regexp" : r'/<param name="archive" value="evocam.jar">/i' },
        ]
        return self.rules
```