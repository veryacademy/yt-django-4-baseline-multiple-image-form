from django import forms

from .models import Image, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "slug",
            "description",
        ]


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = Image
        fields = ("image",)


# class ProjectForm(ProjectPartForm):
#     images = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True})
#     )

#     class Meta(ProjectPartForm.Meta):
#         fields = ProjectPartForm.Meta.fields + [
#             "images",
#         ]
