from django import forms

from recruit.models import Question, Recruitment


class QuestionForm(forms.Form):
    def __init__(self, **kwargs):
        super(QuestionForm, self).__init__(**kwargs)

        recruitment = Recruitment.objects.order_by('year', 'semester').first()
        questions = Question.objects.filter(recruitment=recruitment.pk)
        questions = list(questions)

        for i, q in enumerate(questions):
            self.fields[f'{q.pk}'] = forms.CharField(
                label=q.question,
                widget=forms.Textarea(attrs={'size': '30'})
            )
