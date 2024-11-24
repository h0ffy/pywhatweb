import plugins


class Pluginnetquery_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<form class="nquser" action="nquser.php" method="post">"},
            {"text": "<a href="nquser.php?querytype= countries"><img class="gobuttonup""},
            {"certainty": "75", "text": "<legend>NQ User Interface</legend>"},
            {"certainty": "75", "text": "<br /><a href="nquser.php?formtype = countries">Top Countries"},
            {"text": "<a href="nqadmin.php"><img class="gobutton" src="images / btn_adm.gif" alt="Administration" /></a>"},
            {"md5": "24a75ccc492b5a9118a4d226c25895c1"},
        ]
        return (self.rules)
