```python
import plugins

class Pluginimageview_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r'/<td (width="160"|rowspan="2")><iframe allowtransparency="yes" frameborder="0" height="100%" width="100%" scrolling="auto" title="(frmcontent|frmlist)" name="(frmcontent|frmlist)" src="albumlist.php\?album=[^"]*"><\/iframe><\/td>/' },
            { "certainty" : "25", "text" : '<meta name="author" content="Jorge Schrauwen" />' },
            { "text" : '<frame src="preload.php" name="frImageview" id="frImageview" />' },
            { "text" : '<frame src="about:blank" name="iHistoryRecorder" id="iHistoryRecorder" />' },
            { "version" : r'/<meta name="description" content="Imageview ([\d]{1}) :: By Jorge Schrauwen \(http:\/\/www.backdot.be\)">/' },
            { "text" : '<link rel="Developer" href="http://www.blackdot.be" title="Blackdot.be" />' },
            { "version" : r'/<title>Imageview ([\d]{1}) :: Help:: (Administration|Installation|Miscellaneous|User|Welcome|Menu)<\/title>/' },
            { "version" : r'/<title>Imageview ([\d]{1}) :: (By Jorge Schrauwen|User Settings|Upload Image|Album View|Administration|RSS Feeds|Install)<\/title>/' },
        ]
        return self.rules
```