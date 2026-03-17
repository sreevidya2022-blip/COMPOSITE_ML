import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app_netlify import app

# Netlify requires this format for serverless functions
def handler(event, context):
    """
    Handler for Netlify Functions
    Converts API Gateway event to WSGI environ
    """
    try:
        # For local dev, if needed
        method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        
        # Create WSGI environ
        environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'QUERY_STRING': event.get('queryStringParameters') or '',
            'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
            'wsgi.url_scheme': 'https',
            'SERVER_NAME': 'netlify.app',
            'SERVER_PORT': '443',
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'wsgi.version': (1, 0),
            'wsgi.input': None,
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': True,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
        }
        
        # Add headers
        for header_name, header_value in event.get('headers', {}).items():
            header_name = header_name.upper().replace('-', '_')
            if header_name not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                header_name = f'HTTP_{header_name}'
            environ[header_name] = header_value
        
        # Call Flask app
        from werkzeug.wrappers import Response
        from werkzeug.serving import WSGIRequestHandler
        
        response = Response.from_app(app, environ)
        
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True),
            'isBase64Encoded': False
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
