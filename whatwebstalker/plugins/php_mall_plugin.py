import plugins


class Pluginphp_mall_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "Powered by <a href="http: // www.netartmedia.net / mall">iBoutique.MALL</a>"},
            {"text": "<td align="right"><input type=password class="login_form_text_field" name="Password"></td>"},
            {"text": "Powered by <a href="http: // www.netartmedia.net / mall" target="_blank">PHP Mall</a>"},
            {"text": "<span class="price_style"><span class=price_style>"},
        ]
        return (self.rules)
