import plugins


class Plugintimelink_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"version": "/<p>Version ([\\d\\.]+)&nbsp;&copy; 2003 - 20[\\d]{2} Time ?Link International Corp\\. All Rights Reserved\\.<\\/p>/"},
            {"text": "<link rel="shortcut icon" type="image / png" href=" / timelink / images / favicon.ico"/>"},
            {"url": "images/login-panel-back.png", "md5": "37897a66217e910dd6c67f1d09c5e870", "version": "6.x", "string": "Enterprise"},
        ]
        return (self.rules)
