from material.frontend.views import ModelViewSet

from . import models


class ManufacturerViewSet(ModelViewSet):
   model = models.Manufacturer
   list_display = ('name', 'country')

class PaperstockViewSet(ModelViewSet):
   model = models.PaperStock

class ArchiveViewSet(ModelViewSet):
   model = models.Archive

class BatteryViewSet(ModelViewSet):
   model = models.Battery

class ConditionViewSet(ModelViewSet):
   model = models.Condition

class FilterViewSet(ModelViewSet):
   model = models.Filter

class NegativeSizeViewSet(ModelViewSet):
   model = models.NegativeSize

class FormatViewSet(ModelViewSet):
   model = models.Format

class FlashModelViewSet(ModelViewSet):
   model = models.FlashModel

class FlashViewSet(ModelViewSet):
   model = models.Flash

class EnlargerModelViewSet(ModelViewSet):
   model = models.EnlargerModel

class EnlargerViewSet(ModelViewSet):
   model = models.Enlarger

class MountViewSet(ModelViewSet):
   model = models.Mount

class PersonViewSet(ModelViewSet):
   model = models.Person

class ProcessViewSet(ModelViewSet):
   model = models.Process

class TeleconverterModelViewSet(ModelViewSet):
   model = models.TeleconverterModel

class TeleconverterViewSet(ModelViewSet):
   model = models.Teleconverter

class TonerViewSet(ModelViewSet):
   model = models.Toner

class FilmStockViewSet(ModelViewSet):
   model = models.FilmStock

class BulkFilmViewSet(ModelViewSet):
   model = models.BulkFilm

class MountAdapterViewSet(ModelViewSet):
   model = models.MountAdapter

class ShutterSpeedViewSet(ModelViewSet):
   model = models.ShutterSpeed

class DeveloperViewSet(ModelViewSet):
   model = models.Developer

class LensModelViewSet(ModelViewSet):
   model = models.LensModel

class CameraModelViewSet(ModelViewSet):
   model = models.CameraModel

class AccessoryViewSet(ModelViewSet):
   model = models.Accessory

class LensViewSet(ModelViewSet):
   model = models.Lens

class CameraViewSet(ModelViewSet):
   model = models.Camera

class FilmViewSet(ModelViewSet):
   model = models.Film

class NegativeViewSet(ModelViewSet):
   model = models.Negative

class PrintViewSet(ModelViewSet):
   model = models.Print

class ScanViewSet(ModelViewSet):
   model = models.Scan

class OrderViewSet(ModelViewSet):
   model = models.Order
