from wtforms import Form, TextAreaField, StringField, SubmitField
from wtforms import validators, ValidationError
from flask_wtf.file import FileField

def check_picture(form, field):
	form.count += 1
	if field.data: 
 		form.pictureStatus = True
	if (form.count >= 2 and not form.pictureStatus):
		raise ValidationError("Must upload a file or link a picture.")

class addPicture(Form):
	pictureStatus = False
	count = 0
	picture = FileField("File", [check_picture])
	link = StringField("Instagram Link", [check_picture])
	city = StringField("City",  [validators.Length(min=1, max=50, message=None), validators.Required()])
	caption = TextAreaField("Caption", [validators.Length(min=2, max=150, message=None), validators.Required()])
	email = StringField("E-mail", [validators.Email(message=u'Invalid email address.')])
	submit = SubmitField("Submit")




