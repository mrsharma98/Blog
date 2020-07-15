from django import  forms
from blog.models import Post,Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        # above line connects the model we will use for this form class
        fields = ('author', 'title', 'text')
        # field that we want user to edit in this form.

        # adding the widgets
        # widgets is a dictionary.
        # by using widget we can design the style
        # the classes are the classes which we will define in CSS
        # and if there are more than there might be some pre-defined classess too.
        # eg of pre-defined are 'editable', 'medium-editor-textarea'

        widget = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # title -> the field name
            # TextInput -> widget name or we can say Input type is text.
            # attrs{} -> is a sub-dictionary
            # then the class with class name which is somewhat predefined.
            # this is the CSS class
            # we can define more than one classes
            # below we have defined 3 classes.
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
