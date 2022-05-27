from django.urls import path, include
from django.views import generic

from . import views


urlpatterns = [
    path('', generic.TemplateView.as_view(template_name="schema/index.html"), name="index"),
    # path('', generic.RedirectView.as_view(url='./mymodel/'), name="index"),
    path('manufacturer/', include(views.ManufacturerViewSet().urls)),
    path('paperstock/', include(views.PaperstockViewSet().urls)),

    path('paperstock/', include(views.PaperstockViewSet().urls)),
    path('archive/', include(views.ArchiveViewSet().urls)),
    path('battery/', include(views.BatteryViewSet().urls)),
    path('condition/', include(views.ConditionViewSet().urls)),
    path('filter/', include(views.FilterViewSet().urls)),
    path('negativesize/', include(views.NegativeSizeViewSet().urls)),
    path('format/', include(views.FormatViewSet().urls)),
    path('flashmodel/', include(views.FlashModelViewSet().urls)),
    path('flash/', include(views.FlashViewSet().urls)),
    path('enlargermodel/', include(views.EnlargerModelViewSet().urls)),
    path('enlarger/', include(views.EnlargerViewSet().urls)),
    path('mount/', include(views.MountViewSet().urls)),
    path('person/', include(views.PersonViewSet().urls)),
    path('process/', include(views.ProcessViewSet().urls)),
    path('teleconvertermodel/', include(views.TeleconverterModelViewSet().urls)),
    path('teleconverter/', include(views.TeleconverterViewSet().urls)),
    path('toner/', include(views.TonerViewSet().urls)),
    path('filmstock/', include(views.FilmStockViewSet().urls)),
    path('bulkfilm/', include(views.BulkFilmViewSet().urls)),
    path('mount/', include(views.MountAdapterViewSet().urls)),
    path('shutterspeed/', include(views.ShutterSpeedViewSet().urls)),
    path('developer/', include(views.DeveloperViewSet().urls)),
    path('lensmodel/', include(views.LensModelViewSet().urls)),
    path('cameramodel/', include(views.CameraModelViewSet().urls)),
    path('accessory/', include(views.AccessoryViewSet().urls)),
    path('lens/', include(views.LensViewSet().urls)),
    path('camera/', include(views.CameraViewSet().urls)),
    path('film/', include(views.FilmViewSet().urls)),
    path('negative/', include(views.NegativeViewSet().urls)),
    path('print/', include(views.PrintViewSet().urls)),
    path('scan/', include(views.ScanViewSet().urls)),
    path('order/', include(views.OrderViewSet().urls)),
]
