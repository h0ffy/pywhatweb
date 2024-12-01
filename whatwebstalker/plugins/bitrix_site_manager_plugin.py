```python
import plugins

class Pluginbitrix_site_manager_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "search" : "headers[p3p]", "name" : "P3P Header", "regexp" : r"^policyref=\"/bitrix/p3p\.xml\", \"CP=\"NON DSP COR CUR ADM DEV PSA PSD OUR UNR BUS UNI COM NAV INT DEM STA\"$" },
            { "search" : "headers[set-cookie]", "name" : "BITRIX_SM_SALE_UID Cookie", "regexp" : r"BITRIX_SM_SALE_UID=[\d]+;" },
            { "search" : "headers[set-cookie]", "name" : "BITRIX_SM_GUEST_ID Cookie", "regexp" : r"BITRIX_SM_GUEST_ID=[\d]+;" },
            { "search" : "headers[set-cookie]", "name" : "BITRIX_SM_LAST_VISIT Cookie", "regexp" : r"BITRIX_SM_LAST_VISIT=" },
            { "search" : "headers[set-cookie]", "name" : "BITRIX_SM_BANNERS Cookie", "regexp" : r"BITRIX_SM_BANNERS=" },
            { "search" : "headers[x-powered-cms]", "name" : "X-Powered-CMS Header", "regexp" : r"^Bitrix Site Manager \(" },
            { "search" : "headers[b-powered-by]", "name" : "B-Powered-By Header", "regexp" : r"^Bitrix SM \(" },
            { "search" : "headers[b-powered-by]", "name" : "B-Powered-By Header", "version" : r"^Bitrix SM/([\d\.]+) \(" },
        ]
        return self.rules
```