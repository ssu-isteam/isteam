from django.contrib.auth.mixins import LoginRequiredMixin


class GroupwareView(LoginRequiredMixin):
    login_url = '/user/signin/'

    tabs = {
        'activities': '활동',
        'users': '회원명단',
        'accounts': '회계내역'
    }

    tab_items = tabs.items()

    tab_keys = tabs.keys()

    def select_tab(self, selected):
        if selected is not None and selected in self.tabs.keys():
            return selected
        else:
            return list(self.tab_keys)[0]