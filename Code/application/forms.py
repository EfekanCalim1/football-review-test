from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Players, Review

class PlayersCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_players = Players.query.all()
        for players in all_players:
            if players.name == field.data:
                raise ValidationError(self.message)

class ReviewCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_reviews = Review.query.all()
        for review in all_reviews:
            if review.review == field.data:
                raise ValidationError(self.message)

class PlayersForm(FlaskForm):
    name = StringField('Player Name',
                validators=[
                    DataRequired(),
                    PlayersCheck(message= 'You have already added this player')
                ]
            )
    submit = SubmitField('Add Player')

class ReviewForm(FlaskForm):
    playerid = SelectField('Player',
                choices=[]
                )
    rating = SelectField('Rating',
                choices=[
                    ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')])
    review = StringField('Review',
                validators=[
                    DataRequired()])
    submit = SubmitField('Add Review')