def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    sorted_keys = environ.keys()
    sorted_keys.sort()
    result = ['<html><body><h1>TrivialWSGIApp in action</h1>'] + ['<p>Sample WSGI application. Just show your environment.</p><p><ul>'] + ['<li> %s => %s</li>' % (str(k), str(environ[k])) for k in sorted_keys]+['</ul></p></body></html>']
    return result