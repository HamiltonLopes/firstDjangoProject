from django.conf.urls import url
from . import views
import portfolios.views
urlpatterns = [
    url(r'^$', views.portfolio_exibir),
]