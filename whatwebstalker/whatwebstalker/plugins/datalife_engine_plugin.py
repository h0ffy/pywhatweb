import plugins


class Plugindatalife_engine_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta name="generator" content="DataLife Engine(http: // dle - news.ru)" />"},
			{"text": "<meta name="generator" content="DataLife Engine" />"},
			{"text": "<meta name="generator" content="DataLife Engine Nulled by M.I.D - Team(http: // www.mid - team.ws)" />", "string": "Nulled by M.I.D-Team"},
			{"regexp": "/<script language="javascript" type="text\/javascript">[\s]+<!--[\s]+var dle_root       = '[^']+';[\s]+var dle_admin      = '[^']*';[\s]+var dle_login_hash = '[^']*';[\s]+(var dle_group      = [\d]+;[\s]+)?var dle_skin       = '[^']*';[\s]+var dle_wysiwyg    = '[^']*';[\s]+var quick_wysiwyg  = '[^']*';[\s]+/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/dle_hash=[^;]+;/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/dle_password=[^;]+;/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/dle_user_id=[^;]+;/" },
		]
	return(self.rules)
