from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Customer(models.Model):
    email = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Order(models.Model):
    robot_serial = models.CharField(max_length=5, blank=False, null=False, verbose_name='серийный номер робота')
    model = models.CharField(max_length=2, blank=False, null=True, verbose_name='модель')
    version = models.CharField(max_length=2, blank=False, null=True, verbose_name='версия')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, verbose_name='Заказчик')

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False, verbose_name='серия')
    model = models.CharField(max_length=2, blank=False, null=False, verbose_name='модель')
    version = models.CharField(max_length=2, blank=False, null=False, verbose_name='версия')
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name='время создания')
    stock = models.IntegerField(default=1, verbose_name='Наличие на складе')
    out_of_stock = models.BooleanField(default=False, verbose_name='Нет в наличии')

    orders = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказ')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказчик')

    def __str__(self):
        return f'{self.serial} {self.model} {self.version}'

    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'


class NotificationManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def all(self, recipient):
        return self.get_queryset().filter(
            recipient=recipient,
            read=False
        )


class Notification(models.Model):
    """Уведомления"""
    text = models.TextField()
    read = models.BooleanField(default=False)
    recipient = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Получатель')
    objects = NotificationManager()

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'






