from io import BytesIO

from django.conf import settings
from django.core.files import File
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Category(models.Model):
    """
    Product category.
    """

    name = models.CharField(verbose_name=_("name"), max_length=128)
    slug = models.SlugField(verbose_name=_("slug"))

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Return URL for category detail view.
        """
        # We can't use traditional Django approach here (using `reverse()` to a Django view), because
        # these views are built in Vue frontend. So, we just return the "hard-coded" URL:
        return "/{slug}/".format(slug=self.slug)


class Product(models.Model):
    """
    Product for sale in the shop.
    """

    name = models.CharField(verbose_name=_("name"), max_length=128)
    category = models.ForeignKey(
        verbose_name=_("category"),
        to=Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    slug = models.SlugField(verbose_name=_("slug"))
    description = models.TextField(verbose_name=_("description"), blank=True, null=True)
    price = models.DecimalField(verbose_name=_("price"), max_digits=6, decimal_places=2)
    image = models.ImageField(
        verbose_name=_("image"), upload_to="products/", blank=True, null=True
    )
    thumbnail = models.ImageField(
        verbose_name=_("thumbnail"),
        upload_to="products/thumbnails/",
        blank=True,
        null=True,
    )
    created = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        ordering = [
            "-created",
        ]
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Return URL for product detail view.
        """
        # We can't use traditional Django approach here (using `reverse()` to a Django view), because
        # these views are built in Vue frontend. So, we just return the "hard-coded" URL:
        return "/{category_slug}/{slug}/".format(
            category_slug=self.category.slug,
            slug=self.slug,
        )

    @property
    def image_url(self) -> str:
        """
        Return image URL, or empty string if there's no image.
        """
        if self.image:
            # NB: do not put "/" between host and url here:
            return "{backend_host}{image_url}".format(
                backend_host=settings.BACKEND_URL,
                image_url=self.image.url,
            )
        return ""

    @property
    def thumbnail_url(self) -> str:
        """
        Return thumbnail image URL. Generate it when it's not created earlier.
        Return empty string if there's no image.
        """
        if not self.thumbnail:
            if self.image:
                self.thumbnail = self.create_thumbnail(self.image)
                self.save()
            else:
                return ""

        # NB: do not put "/" between host and url here:
        return "{backend_host}{thumbnail_url}".format(
            backend_host=settings.BACKEND_URL,
            thumbnail_url=self.thumbnail.url,
        )

    @staticmethod
    def create_thumbnail(image: Image, size=(300, 200)) -> File:
        """
        Create JPEG thumbnail file of specified size from `image`.
        """
        full_image = Image.open(image)
        full_image.convert("RGB")
        full_image.thumbnail(size=size)

        thumbnail_io = BytesIO()
        full_image.save(thumbnail_io, "JPEG", quality=85)

        print(image.name)
        thumbnail = File(thumbnail_io, name=image.name)

        return thumbnail
