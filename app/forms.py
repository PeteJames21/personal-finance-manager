import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired


class LoginForm(FlaskForm):
    '''Login fields etc'''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    '''Registration form'''
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class TransactionForm(FlaskForm):
    date = DateField('Date', default=datetime.date.today, validators=[DataRequired()])
    category = SelectField('Type of Transaction', choices=[('', 'Income, Expense or Transfer'), ('incomes', 'Income'), ('expenses', 'Expense'), ('transfers', 'Transfer')], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[InputRequired()])
    account_debited = StringField('Account Debited')
    account_credited = StringField('Account Credited')
    subcategory = StringField('Source/Destination of the money')
    description = StringField('Description')
    submit = SubmitField('Add Transaction')

class AddAccountForm(FlaskForm):
    account = StringField('Account Name', validators=[DataRequired()])
    balance = FloatField('Balance', validators=[InputRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Account')

class AddProfileForm(FlaskForm):
    profile = StringField('Profile Name', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Profile')
    set_as_default = BooleanField('Set as Default Profile?', default=False)