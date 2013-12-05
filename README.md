carte-util
==========


Libreria con elementos utiles

Para instalar: pip install git+https://github.com/mmassigoge/carte-util.git

==wiggets==
Ejempl de uso de Mapa con geocodificador en admin.py

from widgets.widgets import GMapPointWidget

class NodoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {'widget': GMapPointWidget }
    }
