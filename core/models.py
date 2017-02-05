from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('criado em'), auto_now_add=True)
    updated = models.DateTimeField(_('atualizado em'), auto_now=True)

    class Meta:
        abstract = True


class BaseRegister(models.Model):
    name = models.CharField(_('nome'), max_length=75)
    phone = models.CharField(_('telefone'), max_length=15, help_text='(85) 99999-9999')
    email = models.EmailField(_('email'))

    class Meta:
        abstract = True


class Customer(TimeStampedModel, BaseRegister):
    dob = models.DateField(_('data de aniversário'))

    class Meta:
        verbose_name = _('Cliente')

    def __str__(self):
        return self.name


class Staff(TimeStampedModel, BaseRegister):
    class Meta:
        verbose_name = _('Funcionário')

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(_('nome'), max_length=75)
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _('Produto')

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    staff = models.ForeignKey(Staff, verbose_name=_('funcionário'))
    customer = models.ForeignKey(Customer, verbose_name=_('cliente'))
    product = models.ForeignKey(Product, verbose_name=_('produto'))

    class Meta:
        verbose_name = _('Serviço')

    def __str__(self):
        return '{} - {} - {}'.format(self.staff.name, self.customer.name, self.product.name)


class Expense(TimeStampedModel):
    description = models.TextField(_('descrição'))
    value = models.DecimalField('valor', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _('Despesa')

    def __str__(self):
        return self.description
