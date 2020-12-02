from application.resources.recommender.feat_extraction import User
from application.resources.utils.user_input import user_fields
from application.resources.recommender import recommendation
from flask_restx import Resource
from application import api
from flask import request

recommendation_api = api.namespace('recommendation', description='Operations related to Recommendation')


@recommendation_api.route('/', endpoint='/recommendation')
class RecommendationController(Resource):

    def get(self):
        return 'Recommendation GET method Called'

    @api.expect(user_fields, validate=False)
    @api.doc(responses={
        200: 'Recommendation Given',
        400: 'Validation Error'
    })
    def post(self):
        json_data = request.get_json(force=True)
        out_value = recommendation.recommendations(words=json_data['word'])
        """        
        # Currently not prepossessing the json 
        user = User(json_data)
        data = user.pre_processing()
        """
        return out_value
