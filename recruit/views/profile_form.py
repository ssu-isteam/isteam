from django.views.generic import FormView

from recruit.forms.profile import ProfileForm


class ProfileFormView(FormView):
    form_class = ProfileForm

    template_name = 'recruit/profile.html'
