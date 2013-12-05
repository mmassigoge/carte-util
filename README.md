carte-util
==========


Libreria con elementos utiles

Para instalar: pip install [git+https://github.com/mmassigoge/carte-util.git](git+https://github.com/mmassigoge/carte-util.git)

wiggets
-------
Ejemplo de uso de Mapa con Geocodificador en admin.py

```python
from widgets.widgets import GMapPointWidget

class NodoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {'widget': GMapPointWidget }
    }
```
