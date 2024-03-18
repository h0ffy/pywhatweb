import plugins
			
class Pluginmoodle_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a title="Moodle[^"]+" href="http:\/\/moodle\.org\/">/" },
			{ "version" : "/<a title="Moodle ([\d\.]+[^"]+)" href="http:\/\/moodle\.org\/">/" },
			{ "name" : "moodle logo.gif", "certainty" : "75", "regexp" : "/<img style="width:100px;height:30px" src="[^"]+\/moodlelogo\.gif" alt="moodlelogo" \/>/" },
			{ "name" : "MoodleSession Cookie", "search" : "headers[set-cookie]", "regexp" : "/MoodleSession=/" },
			{ "name" : "MOODLEID_ Cookie", "search" : "headers[set-cookie]", "regexp" : "/MOODLEID_[^\s^=]*=/" },
		]
		return(self.rules)
