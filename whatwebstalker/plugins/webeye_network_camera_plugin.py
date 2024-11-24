import plugins


class Pluginwebeye_network_camera_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<title>WebEye User Login</title>"},
            {"text": "<title>WebEye Java Applet Page</title>"},
            {"text": "<title>WebEye Index Page</title>"},
            {"text": "<meta name="Author" content="WebGateInc">"},
            {"text": "<meta name="generator" content="WebGateInc">"},
            {"text": "<p>Click <a href=". / login.ml?FORM_METHOD = get">here</a> if you have a problem to login ..."},
            {"text": "			  <applet archive=" / wg_jwebeye.jar" code=WebEyeApplet.class codebase=. width=720 height=773> \\"},
        ]
        return (self.rules)
