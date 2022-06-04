from gc import get_objects
from django.shortcuts import render
from villageapp.models import Notification, Complaints

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(req):

    return render(req, 'villageapp/index.html', {'complaints': complaints})

### HANDLING NOTIFICATION PART ######


class NotificationListView(ListView):
    model = Notification
    template_name = 'villageapp/notification.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'villageapp/notif_detail.html'
    context_object_name = 'item'


class NotificationCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    fields = ['title', 'content']
    template_name = 'villageapp/add_new_notify.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotificationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notification
    fields = ['title', 'content']
    template_name = 'villageapp/add_new_notify.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NotificationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notification
    template_name = 'villageapp/notify_confirm_delete.html'
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


### HANDLING Complaints PART ######


class ComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/complaints.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class SolvedComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/solved_complaints.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class UnSolvedComplaintsListView(ListView):
    model = Complaints
    template_name = 'villageapp/unsolved_complaints.html'
    context_object_name = 'data'
    ordering = ['-date_posted']


class ComplaintsDetailView(DetailView):
    model = Complaints
    template_name = 'villageapp/comp_detail.html'
    context_object_name = 'item'


class ComplaintsCreateView(LoginRequiredMixin, CreateView):
    model = Complaints
    fields = ['title', 'category', 'descritrion', 'image']
    template_name = 'villageapp/add_new_comp.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ComplaintsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complaints
    fields = ['title', 'category', 'descritrion', 'image']
    template_name = 'villageapp/add_new_comp.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ComplaintsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Complaints
    template_name = 'villageapp/comp_confirm_delete.html'
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(req):
    return render(req, 'villageapp/about.html')


def jobs(req):
    return render(req, 'villageapp/jobs.html')


def complaints(req):
    return render(req, 'villageapp/complaints.html')
