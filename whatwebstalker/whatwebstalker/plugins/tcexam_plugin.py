import plugins


class Plugintcexam_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<a name="topofdoc" id="topofdoc"></a>"},
			{"text": "<meta name="author" content="Nicola Asuni - Tecnick.com s.r.l." />"},
			{"regexp": "/<!-- TCExam \\(c\\) 2004-20[\\d]{2} Nicola Asuni - Tecnick.com s\\.r\\.l\\. - www\\.tcexam\\.com -->/"},
			{"text": "<!-- TCExam19730104 -->"},
			{"text": "<li><a href="tce_login.php" title="click on this link to access on this system">"},
			{"text": "<meta name="tcexam_level" content="0" />"},
			{"version": "/<span class="copyright"><a href="http: \/\/www\.tcexam\.(org|com)">TCExam<\/a> ver\. ([^\s]+) - Copyright &copy; 2004-20[\d]{2} Nicola Asuni - <a href="http:\/\/www\.tecnick\.com">Tecnick.com S\.r\.l\.<\/a><\/span>/", "offset" : "1 },
		]
	return(self.rules)
