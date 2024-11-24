import plugins


class Plugincontrolstar_scada_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<APPLET archive="scada.jar", "toolbox.jar", "batik.jar", "crimson - parser.jar" code="Scada" style="position: absolute
             left: 0
             top: 0
             width: expression(document.body.clientWidth)
             height: expression(document.body.clientHeight)
             " >"},
        ]
        return (self.rules)
