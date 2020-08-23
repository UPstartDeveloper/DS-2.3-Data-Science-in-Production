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
    """
    pass


# run the app in debug mode locally
if __name__ == '__main__':
    app.run(debug=True)
    