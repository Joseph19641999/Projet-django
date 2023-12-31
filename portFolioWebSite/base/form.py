from django.forms import ModelForm
from .models import  Project, Message, Skill, Endorsement, comment


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        # fields = ['title', 'body']
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'from-control'})
        self.fields['email'].widget.attrs.update({'class': 'from-control'})
        self.fields['subject'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})


class SkillForm(ModelForm):

    class Meta:
        model = Skill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})


class EndorsementForm(ModelForm):

    class Meta:
        model = Endorsement
        fields = '__all__'
        exclude = ['featured']

    def __init__(self, *args, **kwargs):
        super(EndorsementForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'class': 'form-control'})


class commentForm(ModelForm):

    class Meta:
        model = comment
        fields = '__all__'
        exclude = ['project']

    def __init__(self, *args, **kwargs):
        super(commentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'class': 'form-control'})
