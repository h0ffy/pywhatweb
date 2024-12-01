```python
import plugins

class Pluginbm_classifieds_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<!-- // All source code on this site \xc3\x82\xc2\xa9 2007 BM Scripts unless otherwise stated - All Rights Reserved // -->" },
            { "text" : "<!-- // All source code on this site \xc3\x82\xc2\xa9 2007 BM Scripts unless otherwise noted - All Rights Reserved // -->" },
            { "text" : "\t\t<!-- START HEADER TABLE - HOLDS GRAPHIC AND SITE NAME -->" },
            { "text" : "\t\t<!-- START MAIN TABLE - HOLDS CATEGORIES, MENU, ETC. -->" },
            { "text" : "\t<p class='credits'><a href='http://www.bmscripts.com'>Powered by BM Classifieds</a><br /></p>" },
            { "text" : "\t<p class='credits'>Powered by BM Classifieds<br /></p>" },
        ]
        return self.rules
```