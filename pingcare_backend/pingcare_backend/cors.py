class CorsMiddleware(object):
	def process_response(self, req, resp):
		resp["Access-Control-Allow-Origin"] = "pingcare.biz"
		return resp
