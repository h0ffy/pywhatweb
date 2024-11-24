import plugins


class Pluginauxilium_petratepro_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<form method="post" name="myform2" action="index.php?cmd = 11">"},
            {"text": "<p class="text"><b>Leader Of The Pack (Top 10 Pets)</b><br><br>"},
        ]
        return (self.rules)
