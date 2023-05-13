from django.db import models

# Create your models here.


from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    start_date = models.DateTimeField(auto_now=True, blank=True)
    end_date = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        abstract = True



class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    
    class Meta:
        ordering = ['created']
    
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

        
class HeroSection(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    paragraph = models.TextField()
    cta_text = models.CharField(max_length=50, blank=False, default='')



class Studies(BaseModel):
    school_name = models.CharField(max_length=100, blank=False, default='')
    education_level = models.CharField(max_length=100, blank=False, default='')
    specialization = models.CharField(max_length=100, blank=False, default='')

class AboutSection(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    sentence = models.TextField()
    images = models.ImageField(upload_to='images/')
    studies = models.ForeignKey(Studies, on_delete=models.CASCADE)

class WorkExperience(BaseModel):
    company =  models.CharField(max_length=100, blank=False, default='')
    company_descr = models.TextField()
    job_title =  models.CharField(max_length=100, blank=False, default='')
    duty = models.TextField()




class Technologies(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')

class Projects(models.Model):
    project_name =  models.CharField(max_length=100, blank=False, default='')
    project_image = models.ImageField(upload_to='images/')
    project_url = models.URLField(max_length=200)
    technologies = models.ForeignKey(Technologies, on_delete=models.PROTECT)

class SocialAccountLinks(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    account_link = models.URLField(max_length=200)
    link_icon = models.CharField(max_length=100, blank=False, default='')