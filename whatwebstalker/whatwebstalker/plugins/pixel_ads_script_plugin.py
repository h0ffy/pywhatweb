import plugins


class Pluginpixel_ads_script_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<a href="index.php?magnify = 1">Magnifier On</a></div>"},
			{"text": "<a href="index.php?magnify = 1">Zoom On</a></div>"},
			{"text": "  <title>Pixel Ads Script</title>"},
			{"text": "  <title>Scrap Pixels - Pixel List</title>"},
			{"text": "  <title>Pixel Ads Script Administration - Administrator Login</title>"},
			{"text": "          <td width="850" class="sitetitle">Pixel Ads Script"},
			{"regexp": "/          <td width="150" class="statsbox" bgcolor="  # FFFFFF"><strong>Pixels Sold:<\/strong> [\d\,]+<br>/" },
			{"text": " href="http: // www.pixel - ads - script.com">Powered by: Pixel-Ads-Script.Com</a></div>"},
		]
	return (self.rules)
