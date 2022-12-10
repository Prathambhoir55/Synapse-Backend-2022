from django.db import models

class Contact_info(models.Model):
    Phonenum = models.PositiveIntegerField(null =True)
    github = models.CharField(max_length=100,null =True)
    linkedin = models.CharField(max_length=100,null =True)
    insta = models.CharField(max_length=100,null =True)
    email = models.EmailField(max_length=100,null =True)

    def __str__(self):
        return self.email

class CoreCommittee(models.Model):

    position_chocies = [
        ('The big three', (
            (1, 'Chair person'),
            (2, 'Co-chair person'),
            (3, 'Admin & secretary')
            )),
        ('Tech', (
            (4,'ML Head'),
            (5,'Tech Head' )
            )),
        ('Non-Tech', (
            (6,'Creative Head'),
            (7,'Events & PR Head'),
            (8,'Marketing Head')
            ))
    ]

    Fname = models.CharField(max_length=20,null=True)
    Lname = models.CharField(max_length=20,null=True)
    SapId = models.PositiveIntegerField(primary_key=True)
    Position = models.IntegerField(choices=position_chocies)
    testimonial = models.TextField(null=True)
    Profilepic = models.ImageField(upload_to="core_profile/",blank=True, null=True)
    fk_contactid = models.ForeignKey(Contact_info, on_delete=models.PROTECT)

    def __str__(self):
        return (str(self.SapId)+" "+self.Fname +" "+self.Lname)

class Faculty(models.Model):

    Fname = models.CharField(max_length=20,null=True)
    Lname = models.CharField(max_length=20,null=True)
    #DJId = models.PositiveIntegerField(primary_key=True)
    Designation = models.CharField(max_length=20)
    testimonial = models.TextField(null=True)
    Profilepic = models.ImageField(upload_to="faculty_profile/",blank=True, null=True)
    fk_contactid = models.ForeignKey(Contact_info, on_delete=models.PROTECT)
    Specialisation = models.CharField(max_length=20)
    def __str__(self):
        return (self.Fname +" "+self.Lname)

class Exmembers(models.Model):

    position_chocies = [
        ('The big three', (
            (1, 'Chair person'),
            (2, 'Co-chair person'),
            (3, 'Admin & secretary')
            )),
        ('Tech', (
            (4,'ML Head'),
            (5,'Tech Head' )
            )),
        ('Non-Tech', (
            (6,'Creative Head'),
            (7,'Events & PR Head'),
            (8,'Marketing Head')
            )),
        ('Founder', (
            (9,'Founder'),
            ))
    ]

    Fname = models.CharField(max_length=20,null=True)
    Lname = models.CharField(max_length=20,null=True)
    SapId = models.PositiveIntegerField(primary_key=True)
    Position = models.IntegerField(choices=position_chocies)
    testimonial = models.TextField(null=True)
    Profilepic = models.ImageField(upload_to="exmembers_profile/",blank=True, null=True)
    fk_contactid = models.ForeignKey(Contact_info, on_delete=models.PROTECT)

    def __str__(self):
        return (str(self.SapId)+" "+self.Fname +" "+self.Lname)

class Event(models.Model):
    title = models.CharField(max_length=100, null =True)
    description = models.TextField(null =True)
    date = models.DateField(null =True)
    sponsors = models.TextField(null =True)
    budget = models.IntegerField(null =True)
    status = models.BooleanField()

class multi_image(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/",blank=True, null=True)

class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    project_no = models.IntegerField(null=True)
    field = models.TextField(null=True)

    core = models.ManyToManyField(CoreCommittee, blank=True, related_name='core_projects')
    fk_faculty = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE)
    Exmembers = models.ManyToManyField(CoreCommittee, blank=True)
    
class Projects_image(models.Model):
    Project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Projects/",blank=True, null=True)

# class Resources(models.model):
#     title = models.CharField(max_length=100, null =True)
#     description = models.TextField(null =True)

# class Resources_image(models.Model):
#     resources = models.ForeignKey(Resources,default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="resources/",blank=True, null=True)
