import re
from django import forms


class CreateOrderForm(forms.Form):
    # этот вариант, если хранить frontenf в backend, не лучший вариант
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    # requires_delivery = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("0", False), ("1", True)], initial=0)
    # delivery_address = forms.CharField(widget=forms.Textarea(
    #     attrs={'class': 'form-control', 'id': 'delivery-address', 'rows': 2, 'placeholder': 'Delivery Address'}))
    # payment_on_get = forms.ChoiceField(widget=forms.RadioSelect(), choices=[("0", False), ("1", True)], initial='card')

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )

    # дополнительная валидация будет проверятья после основной(базовой) валидации
    def create_phone_number(self):
        data = self.cleaned_data["phone_number"]

        if not data.isdigit():
            raise forms.ValidationError("Please enter a valid phone number")

        pattern = re.compile(r"^\+\d{3}$")
        if not pattern.match(data):
            raise forms.ValidationError("Please enter a valid phone number")

        return data
