import plugins


class Pluginjagoanstore_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "CMS <a style="color:  # fff;font-size:11px;" href="http://www.jagoanstore.com/" target="_blank">Toko Online</a> by <a href="http://www.jagoanstore.com/" target="_blank"><img src="http://www.jagoanstore.com/jagstorecom-lil.png" border=0 align="absmiddle" /></a></div>\');" },
			{"string": / <div class = "copy" > Copyright (20[\d]{2}) Toko Online ini menggunakan JagoanStore CMS dari JagoanWeb Indonesia<\/div>/" },
		]
	return(self.rules)
