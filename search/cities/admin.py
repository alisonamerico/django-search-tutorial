from django.contrib import admin

from search.cities.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state',)


admin.site.register(City, CityAdmin)
