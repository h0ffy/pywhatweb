			{ "status" : "403", "text" : "<html><body>Sorry", "invalid request</body></html>" }
			{ "search" : "headers[server]", "regexp" : "/^CloudFront/ }
			{ "search" : "headers[x-cache]", "regexp" : "/^Error from cloudfront/ }
