import plugins


class Pluginsubsonic_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<input type="checkbox" name="_acegi_security_remember_me" id="remember" class="checkbox" tabindex="3">"},
            {"text": "<form action=" / j_acegi_security_check" method="POST">"},
        ]
        return (self.rules)
