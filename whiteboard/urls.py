from django.urls import path, include
from django.views.generic import RedirectView
from  whiteboard import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='home'),
    path('registrate/', views.RegistrationUser.as_view(), name='registrate'),
    path( 'accounts/', include('django.contrib.auth.urls')),
    path( 'accounts/profile/',  RedirectView.as_view(url='/')),
    path('user-delete/<int:pk>', views.DeleteUser.as_view()),
]

urlpatterns += [
    path( 'post-update/<int:pk>', views.UpdatePost.as_view(),name='post-update'),
    path( 'post-create/', views.CreatePost.as_view(), name='post-create'),
    path( 'post-delete/<int:pk>', views.DeletePost.as_view(), name='post-delete'),
]

urlpatterns += [
    path( 'com-update/<int:pk>', views.UpdateComment.as_view(),name='com-update'),
    path( 'com-create/<int:pk>', views.CreateComment.as_view(),name='com-create'),
    path('com-delete/<int:pk>', views.DeleteComment.as_view(),name='com-delete'),

]

urlpatterns += [
    path( 'name-update/<int:pk>', views.UpdateName.as_view(),name='name-update'),
    path('avatar-update/<int:pk>', views.UpdateAvatar.as_view(),name='avatar-update'),
    path('info-update/<int:pk>', views.UpdateInfo.as_view(),name='info-update'),
    path('profile/<int:pk>', views.ProfileListView.as_view(),name='profile'),
    path('post/<int:pk>', views.post_detail,name='post'),

]
