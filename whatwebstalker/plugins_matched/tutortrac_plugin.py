import plugins
			
class Plugintutortrac_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>TutorTrac Learning Center Tracking Software</TITLE>" },
			{ "text" : "<meta name="keywords" content="tutor,software,scheduling,learning,center,tutoring,assistant,assistance,education,accutrack,tutorial,community,college,university"><meta name="description" content="Web Based Tutor/Learning Center Management/Scheduling Software">" },
			{ "version" : "/<P ALIGN=right><FONT SIZE="-1" FACE="Verdana" COLOR="#CCCCCC">version[\s]+([\d\.]+)[\s]?&copy;Copyright 20[\d]{2}", "<\/FONT><A HREF="http:\/\/www\.go-redrock\.com"><FONT SIZE="-1" FACE="Verdana" COLOR="#CCCCCC">RedRock/" },
			{ "version" : "/<P ALIGN=right><FONT COLOR="#CCCCCC">version ([\d\.]+)[\s]+&copy;Copyright 2004-20[\d]{2}<br \/><\/FONT><A HREF="http:\/\/www\.go-redrock\.com"><FONT COLOR="#CCCCCC">RedRock/" },
			{ "url" : "/TutorTrac/favicon.ico", "md5" : "c56dda95e69b50c4b3802919aab0e950" },
			{ "url" : "/TracWeb40/favicon.ico", "md5" : "365ccabab0c04ec5c6a9721725b76c36" },
		]
	return(self.rules)
