from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    # Define a CloudinaryFileField for uploading files
    attachment = CloudinaryFileField(
        options={
            'folder': 'collaborate_attachments',  # Optional: Specify the folder in Cloudinary where files will be uploaded
            'resource_type': 'auto',              # Optional: Specify the type of resource (auto, image, raw, video)
            'format': 'jpg'                       # Optional: Specify the desired format of the uploaded file
        },
        required=False
    )

    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message', 'attachment')  # Include the 'attachment' field in the form
