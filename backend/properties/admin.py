from django.contrib import admin

from .models import Property, Reservation


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "price_per_night",
        "bedrooms",
    ]
    list_filter = ["category"]


class PropertyReservationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "start_date",
        "end_date",
    ]
    list_filter = ["number_of_nights"]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation, PropertyReservationAdmin)
