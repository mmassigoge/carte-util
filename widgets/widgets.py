import floppyforms as forms


class GMapPointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
    template_name = 'ara/gis/ara_google.html'
    map_options = '{}'
    mapa_attrs = ('map_options',)

    def __init__(self, *args, **kwargs):
        super(GMapLineStringWidget, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        for key in self.mapa_attrs:
            setattr(self, key, attrs.pop(key, getattr(self, key)))
            
    def get_context_data(self):
        ctx = super(GMapPointWidget, self).get_context_data()
        ctx['map_options'] = self.map_options
        return ctx

class GMapLineStringWidget(forms.gis.LineStringWidget, forms.gis.BaseGMapWidget):
    template_name = 'ara/gis/ara_google.html'
    map_options = '{}'
    mapa_attrs = ('map_options',)

    def __init__(self, *args, **kwargs):
        super(GMapLineStringWidget, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        for key in self.mapa_attrs:
            setattr(self, key, attrs.pop(key, getattr(self, key)))
    
    def get_context_data(self):
        ctx = super(GMapLineStringWidget, self).get_context_data()
        ctx['map_options'] = self.map_options
        return ctx
