from django import forms

from apps.device.models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'device_name',
            'sn',
            'vc',
            'ac',
            'vkey',
        ]
        widgets = {
            'device_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Device Name',
                }
            ),
            'sn': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Device SN'
                }
            ),
            'vc': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Device VC'
                }
            ),
            'ac': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Device AC'
                }
            ),
            'vkey': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Device VKEY'
                }
            )
        }
