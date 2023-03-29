from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Order(models.Model):
    """
    Represents an Order in eshop.
    """

    user = models.ForeignKey(
        verbose_name=_("customer"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    first_name = models.CharField(verbose_name=_("first name"), max_length=32)
    last_name = models.CharField(verbose_name=_("last name"), max_length=32)
    email = models.CharField(verbose_name=_("e-mail"), max_length=32)
    address = models.CharField(verbose_name=_("address"), max_length=128)
    place = models.CharField(verbose_name=_("place"), max_length=32)
    phone = models.CharField(verbose_name=_("phone"), max_length=32)
    paid_amount = models.DecimalField(
        verbose_name=_("paid amount"),
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )
    created = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        ordering = [
            "-created",
        ]
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return _("Order #{id}").format(
            id=self.id,
        )


class OrderItem(models.Model):
    """
    Represents an Item in the Order, which includes some quantity of one Product.
    """

    order = models.ForeignKey(
        verbose_name=_("order item"),
        to=Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        verbose_name=_("product"),
        to=Product,
        on_delete=models.CASCADE,
        related_name="items",
    )
    price = models.DecimalField(
        verbose_name=_("price"),
        max_digits=8,
        decimal_places=2,
    )
    quantity = models.IntegerField(
        verbose_name=_("quantity"),
        default=1,
    )
    created = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        ordering = [
            "-created",
        ]
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def __str__(self):
        return _("Order item #{id} (from {order}").format(
            id=self.id,
            order=str(self.order),
        )
