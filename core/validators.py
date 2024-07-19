from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import imghdr

def validate_image_format(value):
    valid_image_formats = ['jpeg', 'png']
    image_format = imghdr.what(value)

    if image_format not in valid_image_formats:
        raise ValidationError(
            _('Unsupported image format. Please upload a JPEG or PNG image.')
        )
