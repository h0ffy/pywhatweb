import plugins


class Pluginerror_log_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "filepath": "/\\[[\\d]{2}\\-[A-Za-z]{3,4}\\-[\\d]{4} [\\d]{2}:[\\d]{2}:[\\d]{2}\\] PHP .{1,50}: .* in (.*) on line [0-9]+/"
            },
            {
                "account": "/\\[[\\d]{2}\\-[A-Za-z]{3,4}\\-[\\d]{4} [\\d]{2}:[\\d]{2}:[\\d]{2}\\] PHP .{1,50}: .* in \\/home\\/([^\\/]{1,32})\\/.* on line [0-9]+/"
            },
        ]
        return self.rules
