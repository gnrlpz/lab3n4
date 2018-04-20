from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# used to keep code DRY
class BaseClass(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# to extend Django standard User model with a shipping address field
class Profile(BaseClass):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.TextField

# This hooks functions to User.save and User.create, so that profile is also updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Product(BaseClass):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    name = models.CharField(max_length=256)
    description = models.TextField

class Cart(BaseClass):
    cart_code = models.AutoField(primary_key=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField
    products = models.ManyToManyField(Product)

    def get_total_price(self):
        sum = 0
        for product in self.products:
            sum += product
        return sum