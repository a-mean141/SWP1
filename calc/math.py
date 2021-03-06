from cgi import parse_qs
from mathplate import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if a.isdigit() and b.isdigit():
	a, b = int(a), int(b)
    else:
	a, b = 0, 0
    response_body = html%{
	'sum':a + b,
	'mul':a * b,
    }
    start_response('200 OK', [
	('Content-Type', 'text/html'),
	('Content-Length', str(len(response_body)))
    ])
    return [response_body]
