import plugins


class Pluginioncube_loader_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "ghdb": "inurl:"loader - wizard.php" filetype:php intitle:"ionCube Loader Wizard""},
			{"text": "<img src="?page = logo" alt="ionCube logo">"},
			{"text": "<h2>ionCube Loader Wizard</h2><p class="alert">An updated version of this Wizard script is available <a href="http: // loaders.ioncube.com / ">here</a>.</p>"},
			{"version": "/<p>The ionCube Loader ([^\\s]+) is already installed but it is an old version\\. It is recommended that the Loader be updated to the latest version/"},
			{"version": "/<p>The ionCube Loader ([^\\s]+) is already installed and encoded files should run without problems.<\\/p>/"},
			{"module": / <div id = "footer" > Copyright ionCube Ltd\. 2002-20[\d]{2} \| (Loader Wizard version [^\s]+) /" },
			{ "text" : "<div id="loading"><script type="text/javascript">document.write(\'<p>Initialising<br>ionCube Loader Wizard<br><span id="status"></span></p>\');</script>" },
		]
	return(self.rules)
