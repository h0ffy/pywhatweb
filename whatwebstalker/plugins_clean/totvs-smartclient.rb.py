			{ "version" : "/<object\s+classid="clsid:[a-f\d\-]+"\s+codebase="TotvsSmartClientax\.cab#version=([^"]+)"/ }
			{ "string" : /<param name="StartProgram" value="([^"]+)"> <<= Programa/ }
			{ "string" : /<param name="Environment" value="([^"]+)"> <<= Ambiente/ }
			{ "search" : "headers[TotvsSmartClient]", "regexp" : "/^TotvsSmartClient$/ }
