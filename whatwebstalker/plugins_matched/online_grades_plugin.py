import plugins
			
class Pluginonline_grades_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<small><br /><em>Disclaimer</em>:  If you handed in an assignment or took a test today", "don't expect the grade to be online immediately.  Teachers only update their grade books as needed.</small><ul><li>" },
			{ "certainty" : "75", "version" : "/<meta name="keywords" content="Online Grades Version ([^\s^"]+)" \/>/" },
			{ "version" : "/      <div class="center">[\r\n]      Online Grades Version:[\r\n]      ([^\s]+)      <\/div>/" },
			{ "text" : "<meta name="author" content="Online Grade Posting System -- http://www.onlinegrades.org" />" },
			{ "text" : "<!-- YOU CAN SAFELY REMOVE OR CHANGE ANYTHING BETWEEN THIS SECTION OF COMENTED CODE -->" },
			{ "text" : "<!-- STOP REMOVING LINES HERE IF REMOVING/CHANGING THE FOOTER -->" },
			{ "regexp" : "/<a href="http:\/\/www.onlinegrades.org"><img src="[^"^>]+\/images\/og.png"[^>]+alt="Powered by Online Grades"[^>]*><\/a>/" },
		]
			return(self.rules)
