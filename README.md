carte-util
==========


Toolbox useful for django admin

For use: pip install [git+https://github.com/mmassigoge/carte-util.git](git+https://github.com/mmassigoge/carte-util.git)

wiggets
-------
widget example including a geocoding field in a PointField

```python
from widgets.widgets import GMapPointWidget

class NodoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {'widget': GMapPointWidget }
    }
```
