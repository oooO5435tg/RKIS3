from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from whiteboard.form import RegisterForm
from whiteboard.models import MyUser, Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexListView(ListView):
    model = Post
    pagination_by = 1
    context_object_name = 'post_list'
    template_name = "index.html"



class RegistrationUser(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = "registration/user_create.html"



class UpdateName(LoginRequiredMixin,UpdateView):
    model = MyUser
    fields = ['username']
    template_name = "update_form.html"
    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                return super().form_valid(form)
            else:
                raise Exception
        except Exception as e:
            return HttpResponseRedirect(
                reverse(" UpdateName", kwargs={"pk": self.object.pk})
            )


class UpdateAvatar(LoginRequiredMixin,UpdateView):
    model = MyUser
    fields = ['avatar']
    template_name = "update_form.html"
    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                return super().form_valid(form)
            else:
                raise Exception
        except Exception as e:
            return HttpResponseRedirect(
                reverse(" UpdateAvatar", kwargs={"pk": self.object.pk})
            )


class UpdateInfo(LoginRequiredMixin,UpdateView):
    model = MyUser
    fields = ['description']
    template_name = "update_form.html"
    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                return super().form_valid(form)
            else:
                raise Exception
        except Exception as e:
            return HttpResponseRedirect(
                reverse(" UpdateInfo", kwargs={"pk": self.object.pk})
            )


class DeleteUser(LoginRequiredMixin,DeleteView):
    model = MyUser
    template_name = "delete_form.html"


class ProfileListView(ListView):
    model = Post
    template_name = "profile.html"

    def get_context_data(self, **kwargs, ):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["user_p"] = MyUser.objects.get(pk=self.kwargs["pk"])
        context["post_list"] = Post.objects.filter(user=self.kwargs["pk"])
        return context


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['text', 'pict']
    template_name = "create_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "delete_form.html"

    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                self.object.delete()
                return HttpResponseRedirect(
                    reverse("IndexListView")
                )
            else:
                raise Exception
        except Exception as e:
            return HttpResponseRedirect(
                reverse("DeletePost", kwargs={"pk": self.object.pk})
            )



class UpdatePost(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['text', 'pict']
    template_name = "update_form.html"


class CreateComment(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['text', 'pict']
    template_name = "create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post =  Post.objects.get(pk=self.kwargs["pk"])

        return super().form_valid(form)


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "delete_form.html"

    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                self.object.delete()
                return HttpResponseRedirect(
                    reverse("post_detail", kwargs={"pk": self.object.pk})
                )
            else:
                raise Exception
        except Exception as e:
            return HttpResponseRedirect(
                reverse("DeleteComment", kwargs={"pk": self.object.pk})
            )



class UpdateComment(LoginRequiredMixin,UpdateView):
    model = Comment
    fields = ['text', 'pict']
    template_name = "update_form.html"

    def form_valid(self, form):
        try:
            if self.object.user_id == self.request.user:
                return super().form_valid(form)
            else:
                raise Exception
        except Exception as e:
            return HttpResponseRedirect(
                reverse(" UpdateComment", kwargs={"pk": self.object.pk})
            )
