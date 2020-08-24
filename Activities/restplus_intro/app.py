import werkzeug
# This next lime Prevents ImportErrors - flask-restplus currently gets broken by 
# Werkzeug 1.0.0. Alternatively, you could also downgrade werkzeug 
# (the package Python uses to interface with an HTTP web server)
# Note: line 6 must happen BEFORE you import Flask to be able to work!
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api, fields, Resource


# instantiate Flask app and API - in same file for now
app = Flask(__name__)
api = Api(app)

# languages for the HTTP responses
python = {'language': 'Python'}
languages = [python]


# Outlining a model - Swagger will make docs for this
language_model = api.model('Language', {
    'language': fields.String('human-readable description')
    }  # key value pair passed in above 
)

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
        return languages  # jsonify not required like in vanilla Flask

    # route where users can add new languages
    @api.expect(language_model)  # has to be in form of model above
    def post(self):
        '''Data is sent with multiple methods. One is shown below'''
        languages.append(api.payload)  # param for model field above
        return {'result': 'Language added'}, 201  # HTTP 201 = "something created" 


# run the app in debug mode locally
if __name__ == '__main__':
    app.run(debug=True)
    