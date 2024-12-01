```python
import plugins

class Pluginimpresspages_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "url" : "/favicon.ico", "md5" : "c92e16f66ec6069432c3be3d10bf5d1c" },
            { "text" : 'Powered by <a href="http://www.impresspages.org">ImpressPages CMS</a>' },
            { "text" : '<h1 class="ipWidgetTitleHeading">ImpressPages CMS successfully installed</h1>' },
            { "version" : '/<meta name="generator" content="ImpressPages CMS ([^\\s]+) under GNU GPL license"( \\/)?>/' },
            { "text" : '<!-- common functions used by various modules -->' },
            { "text" : '<script type="text/javascript">if(parent.header && parent.content)parent.window.top.location=\\\'admin.php\\\';</script>' },
            { "text" : '<span id="modCommunityNewsletterError" class="error">Incorrect e-mail address</span>' },
        ]
        return self.rules
```