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
                    'placeholder': 'Enter Name',
                }
            ),
            'sn': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter SN'
                }
            ),
            'vc': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter VC'
                }
            ),
            'ac': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter AC'
                }
            ),
            'vkey': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Enter VKEY'
                }
            )
        }
        labels = {
            'device_name': 'Device Name',
            'sn': 'Device SN',
            'vc': 'Device VC',
            'ac': 'Device AC',
            'vkey': 'Device VKEY',
        }
