from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    text=models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField('Tag', related_name='notes')

    def __str__(self):
        return self.text

class Tag(models.Model):
    tag_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.tag_name



# # Assuming you have a Note instance with an id of 1
# note = Note.objects.get(id=1)

# # To get all tags related to the note, you can use the `tags` attribute
# tags = note.tags.all()

# # You can then iterate through the tags and print their names
# for tag in tags:
#     print(tag.tag_name)