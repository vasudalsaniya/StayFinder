from django.contrib import admin
from django.utils.html import format_html
from .models import User, Country, State, City, HotelCategory, Hotel, Room, RoomImages, Review, FavoriteHotel, Booking, Payment

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'profile_image')

    def profile_image(self, obj):
        if obj.profile_pic:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_pic.url)
        return 'No Image'
    profile_image.short_description = 'Profile Image'

class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ('room', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 100px;" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

admin.site.register(User, UserAdmin)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(HotelCategory)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomImages, RoomImagesAdmin)
admin.site.register(Review)
admin.site.register(FavoriteHotel)
admin.site.register(Booking)
admin.site.register(Payment)
