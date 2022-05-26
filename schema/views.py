from material.frontend.views import ModelViewSet

from . import models


class ManufacturerViewSet(ModelViewSet):
   model = models.Manufacturer
   list_display = ('name', 'country')

class PaperstockViewSet(ModelViewSet):
   model = models.PaperStock
