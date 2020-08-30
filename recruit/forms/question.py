from django import forms

from recruit.models import Question, Recruitment


class QuestionForm(forms.Form):
    def __init__(self, **kwargs):
        super(QuestionForm, self).__init__(**kwargs)

        recruitment = Recruitment.objects.get(year=2020, semester=1)
        questions = Question.objects.filter(recruitment=recruitment.pk)
        questions = list(questions)

        for i, q in enumerate(questions):
            self.fields[f'question_{i}'] = forms.CharField(
                label=q.question,
                widget=forms.Textarea(attrs={'size': '30'})
            )
