from django.core.validators import ValidationError

def validar_telefono(numero):
    if not numero.isdigit():
        raise ValidationError(
            ('%(value)s no es un número de teléfono válido'),
            params={'value': numero},
        )
