from django.db import models


class CreditApplication(models.Model):
    """Кредитная заявка"""
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, related_name='contract',
                                    verbose_name='контракт')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'заявка номер {self.id}'


class Contract(models.Model):
    """Контракт"""
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

    def __str__(self):
        return f'контракт номер {self.id}'


class Product(models.Model):
    """Товар"""
    title = models.CharField(max_length=255, verbose_name='название')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='manufacturer',
                                     verbose_name='производитель')
    credit = models.ForeignKey(CreditApplication, on_delete=models.CASCADE, related_name='credit',
                                verbose_name='заявка')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    """Производитель"""
    title = models.CharField(max_length=200, verbose_name='название')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Производителя'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.title
