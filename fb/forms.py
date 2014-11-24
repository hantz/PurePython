from django.forms import Form, CharField, Textarea, HiddenInput


class UserPostForm(Form):
	text = CharField(widget=Textarea(
							attrs={"rows": 5, "cols": 100}))

class UserCommentForm(Form):
	text = CharField(widget=Textarea(
							attrs={"rows": 3, "cols": 50}))
	