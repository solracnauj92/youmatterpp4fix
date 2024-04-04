from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Comment

class CommentForm(forms.ModelForm):
    # Define a CloudinaryFileField for uploading files
    attachment = CloudinaryFileField(
        options={
            'folder': 'comment_attachments',  # Optional: Specify the folder in Cloudinary where files will be uploaded
            'resource_type': 'auto',           # Optional: Specify the type of resource (auto, image, raw, video)
            'format': 'jpg'                    # Optional: Specify the desired format of the uploaded file
        },
        required=False
    )

    class Meta:
        model = Comment
        fields = ('body', 'attachment')  # Include the 'attachment' field in the form
