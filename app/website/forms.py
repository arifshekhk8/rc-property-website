import re

from django import forms
from django.utils.translation import get_language
from projects.models import Project

from .copy import BN, EN


class InquiryForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    phone = forms.CharField(max_length=30)
    project = forms.ModelChoiceField(queryset=Project.objects.none(), empty_label=None)
    message = forms.CharField(
        required=False, max_length=600, widget=forms.Textarea(attrs={"rows": 4})
    )
    consent = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        copy = BN if get_language() == "bn" else EN
        self.fields["project"].queryset = Project.objects.published()
        for field in self.fields:
            self.fields[field].label = copy[field]
        self.fields["project"].label_from_instance = lambda obj: obj.title
        self.fields["phone"].widget.attrs.update(
            {"inputmode": "tel", "autocomplete": "tel", "placeholder": "01XXXXXXXXX"}
        )
        self.fields["name"].widget.attrs["autocomplete"] = "name"
        for name, field in self.fields.items():
            if name != "consent":
                field.widget.attrs["class"] = "form-control"
            if self.is_bound and name in self.errors:
                field.widget.attrs.update(
                    {"aria-invalid": "true", "aria-describedby": f"{name}-error"}
                )

    def clean_phone(self):
        value = self.cleaned_data["phone"].translate(str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789"))
        value = re.sub(r"[\s()-]", "", value)
        if value.startswith("+880"):
            value = "0" + value[4:]
        if not re.fullmatch(r"01[3-9][0-9]{8}", value):
            message = (
                "সঠিক বাংলাদেশি মোবাইল নম্বর লিখুন।"
                if get_language() == "bn"
                else "Enter a valid Bangladesh mobile number."
            )
            raise forms.ValidationError(message)
        return value
