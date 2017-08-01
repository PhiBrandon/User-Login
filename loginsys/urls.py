from django.conf.urls import url
from .views import loginView, registerView

urlpatterns = [
	url(r'^$', loginView.as_view(), name="login"),
	url(r'^register/', registerView.as_view(), name="register" )
]