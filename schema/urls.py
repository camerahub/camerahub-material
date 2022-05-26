from django.urls import path, include
from django.views import generic

from . import views


urlpatterns = [
    path('', generic.TemplateView.as_view(template_name="schema/index.html"), name="index"),
    # path('', generic.RedirectView.as_view(url='./mymodel/'), name="index"),
    path('manufacturer/', include(views.ManufacturerViewSet().urls)),
]
