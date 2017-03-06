from django.db import models


class TagModel(models.Model):
    tag_name = models.CharField(max_length = 30, default = 'no name')
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    user_id = models.IntegerField(default = 0) # if it aint broke dont fix it

    class Meta:
        ordering = ["-created_at"]
        

class SchematicModel(models.Model):
    schematic_name = models.CharField(max_length = 30, default = 'no name')
    schematic_description = models.CharField(max_length = 250, default = 'no description')
    schematic_image = models.ImageField(upload_to = 'schematic_folder/', default = 'pic_folder/None/no-img.jpg')
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    user_id = models.IntegerField(default = 0) # if it aint broke dont fix it
    schematic_tags = models.ManyToManyField(TagModel)

    class Meta:
        ordering = ["-created_at"]
