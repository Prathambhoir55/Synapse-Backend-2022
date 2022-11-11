from django.db import models

# Create your models here.
class Contact_info(models.Model):
    Phonenum = models.PositiveIntegerField(max_length=10,null =True)
    github = models.CharField(max_length=100,null =True)
    linkedin = models.CharField(max_length=100,null =True)
    insta = models.CharField(max_length=100,null =True)
    email = models.EmailField(max_length=100,null =True)

class CoreCommittee(models.Model):

    position_chocies = [
        ('The big three', (
            (1, 'Chair person'),
            (2, 'Co-chair person'),
            (3, 'Admin & secretary'),
            )),
        ('Tech', (
            (4,'ML Head'),
            (5,'Tech Head' )
            ))
        ('Non-Tech', (
            (6,'Creative Head'),
            (7,'Events & PR Head'),
            (8,'Marketing Head'),
            ))
    ]

    Fname = models.CharField(max_length=20,null=True)
    Lname = models.CharField(max_length=20,null=True)
    SapId = models.PositiveIntegerField(max_length=12,primary_key=True)
    Position = models.CharField(max_length=20, choices=position_chocies)
    testimonial = models.TextField(null=True)
    Profilepic = models.ImageField(upload_to="core_profile/",blank=True, null=True)
    fk_contactid = models.ForeignKey(Contact_info)

class Faculty(models.Model):

    Fname = models.CharField(max_length=20,null=True)
    Lname = models.CharField(max_length=20,null=True)
    #DJId = models.PositiveIntegerField(max_length=12,primary_key=True)
    Designation = models.CharField(max_length=20)
    testimonial = models.TextField(null=True)
    Profilepic = models.ImageField(upload_to="faculty_profile/",blank=True, null=True)
    fk_contactid = models.ForeignKey(Contact_info)
    Specialisation = models.CharField(max_length=20)

class Exmembers(models.Model):

    position_chocies = [
        ('The big three', (
            (1, 'Chair person'),
            (2, 'Co-chair person'),
            (3, 'Admin & secretary'),
            )),
        ('Tech', (
            (4,'ML Head'),
            (5,'Tech Head' )
            ))
        ('Non-Tech', (
            (6,'Creative Head'),
            (7,'Events & PR Head'),
            (8,'Marketing Head'),
            ))
        ('Founder', (
            (9,'Founder'),
            ))
    ]

    Fname = models.CharField(max_length=20,null=True)
    Lname = models.CharField(max_length=20,null=True)
    SapId = models.PositiveIntegerField(max_length=12,primary_key=True)
    Position = models.CharField(max_length=20, choices=position_chocies)
    testimonial = models.TextField(null=True)
    Profilepic = models.ImageField(upload_to="exmembers_profile/",blank=True, null=True)
    fk_contactid = models.ForeignKey(Contact_info)
