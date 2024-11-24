import plugins


class Pluginacidcat_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {
                "text": "<!-- Start Acidcat CMS footer information. Note: this code is not to be edited or removed in the free version. -->"
            },
            {
                "text": '<tr><td colspan="2" valign="top" class="ac_menuleftbg" ><table width="100%" cellspacing="0" border="0"><tr>'
            },
            {
                "text": '<tr><td colspan="2" valign="top" class="ac_menuleftbg" ><table cellspacing="0" border="0"><tr>'
            },
            {
                "text": '<td class="ac_footer_menu">&nbsp;<br /><br /></td></tr></table></td>'
            },
            {"text": '<td class="ac_footer_menu">&nbsp;<br /></td></tr></table></td>'},
            {
                "certainty": "75",
                "text": '<table cellspacing="0" class="ac_admin_main">',
            },
            {
                "text": '<link href="admin/css/admin_import.css" rel="stylesheet" type="text/css" />'
            },
            {
                "text": "<br><center><table border=1 class=errorTable><tr><td class='login_view'><img src=images/acidcat_logo.gif><td colspan=1 class='login_view'><b>Acidcat CMS Error"
            },
            {
                "version": '/<a href="http:\\/\\/www.acidcat.com">Powered by Acidcat CMS v ([\\d\\.a-z]+)<\\/a>/'
            },
        ]
        return self.rules
