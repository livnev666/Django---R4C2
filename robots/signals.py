from django.db.models import signals
from django.dispatch import receiver
from .models import Robot


@receiver(signals.pre_save, sender=Robot)
def check_robot_model(sender, instance, **kwargs):
    if not instance.model:
        instance.model = 'Нет модели'


@receiver(signals.post_save, sender=Robot)
def create_robot(sender, instance, created, **kwargs):
    if created:
        if instance.stock >= 1 and instance.model == 'TT':
            print(f'Добрый день! Недавно вы интересовались нашим роботом модели {instance.model}  '
                  f'версии {instance.version} Этот робот теперь в наличии в количестве {instance.stock} шт. '
                  f'Если вам подходит этот вариант - пожалуйста, свяжитесь с нами')

    if created:
        print(f'Был создан {instance.model}')
    else:
        print(f'Обновления для модели {instance.model}')
        if instance.stock >= 1 and instance.model == 'TT':
            print(f'Робот {instance.model} появился в наличии в количестве {instance.stock} шт.')