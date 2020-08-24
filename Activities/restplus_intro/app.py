import werkzeug
# This next lime Prevents ImportErrors - flask-restplus currently gets broken by 
# Werkzeug 1.0.0. Alternatively, you could also downgrade werkzeug 
# (the package Python uses to interface with an HTTP web server)
# Note: line 6 must happen BEFORE you import Flask to be able to work!
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api, Resource


# instantiate Flask app and API - in same file for now
app = Flask(__name__)
api = Api(app)

# routes for the API
@api.route('/language')
class Language(Resource):
    """
    This is a class for the API route, we use these rather than functions 
    (which is more like vanilla Flask).

    For now, the base route will be created automatically using
    a really sleek Swagger documentation - will help us document 
    information about our API, and try out the endpoints in the browser.
    """
    def get(self):
        '''Method for the Language class to handle GET requests.'''
        return {'hey': 'there'}  # jsonify not required like in vanilla Flask


# run the app in debug mode locally
if __name__ == '__main__':
    app.run(debug=True)
    