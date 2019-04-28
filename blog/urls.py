from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name = "posts"),
    path("<pk>/", views.PostDetailView.as_view(), name = "detail"),
    #Note, the regex above does not even need the "int:" that is shows in the text.
    path("newPost", views.PostCreateView.as_view(), name = "post_new"),
    path("update/<pk>/", views.PostEditView.as_view(), name = "update_post"),
    path("delete/<pk>/", views.DeletePostView.as_view(), name = "delete_post")
#(?P<pk>\d+)
]

"""
All blog post entries will start with post/. Next is the primary key for our post entry
which will be represented as an integer <int:pk>.

Django automatically adds an auto-incrementing primary key to our
database models. So while we only declared the fields title, author, and body on our
Post model, under-the-hood Django also added another field called id, which is our
primary key. We can access it as either id or pk.
"""
