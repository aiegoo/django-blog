from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
import markdown
import emoji
import re


# Create your models here.

# Article keywords, used as keywords in SEO
class Keyword(models.Model):
    name = models.CharField('Article Keywords', max_length=20)

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


# Post tags
class Tag(models.Model):
    name = models.CharField('Article Tag', max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField('Description', max_length=240, default=settings.SITE_DESCRIPTION,
                                   help_text='Used as a description in SEO, the length refers to the SEO standard')

    class Meta:
        verbose_name = 'Label'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})

    def get_article_list(self):
        '' 'Return a list of all articles published under the current label' ''
        return Article.objects.filter(tags=self)


# Article categories
class Category(models.Model):
    name = models.CharField('Article classification', max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField('Description', max_length=240, default=settings.SITE_DESCRIPTION,
                                   help_text='Used as a description in SEO, the length refers to the SEO standard')

    class Meta:
        verbose_name = 'Classification'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def get_article_list(self):
        return Article.objects.filter(category=self)


# Article
class Article(models.Model):
    IMG_LINK = '/static/blog/img/summary.png'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Article Title')
    summary = models.TextField('Article summary', max_length=230,
                               default='Article summary is equivalent to the description content of the webpage, '
                                       'please fill in ...')
    body = RichTextUploadingField(verbose_name='BlogContent',null=True,blank=True)
    img_link = models.CharField('Image address', default=IMG_LINK, max_length=255)
    create_date = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Modified time', auto_now=True)
    views = models.IntegerField('Views', default=0)
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category, verbose_name='Article Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='Tag')
    keywords = models.ManyToManyField(Keyword, verbose_name='Article Keywords',
                                      help_text='Article keywords, used as keywords in SEO, it is best to use long tail words, 3-4 are enough')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[: 20]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def update_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_pre(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()


# timeline
class Timeline(models.Model):
    COLOR_CHOICE = (
        ('primary', 'Basic-Blue'),
        ('success', 'Success-Green'),
        ('info', 'Info-Sky Blue'),
        ('warning', 'Warning-orange'),
        ('danger', 'Danger-Red')
    )
    SIDE_CHOICE = (
        ('L', 'Left'),
        ('R', 'Right'),
    )
    STAR_NUM = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )
    side = models.CharField('Position', max_length=1, choices=SIDE_CHOICE, default='L')
    star_num = models.IntegerField('Number of stars', choices=STAR_NUM, default=3)
    icon = models.CharField('icon', max_length=50, default='fa fa-pencil')
    icon_color = models.CharField('Icon Color', max_length=20, choices=COLOR_CHOICE, default='info')
    title = models.CharField('Title', max_length=100)
    update_date = models.DateTimeField('Update time')
    content = models.TextField('main content')

    class Meta:
        verbose_name = 'Timeline'
        verbose_name_plural = verbose_name
        ordering = ['update_date']

    def __str__(self):
        return self.title[: 20]

    def title_to_emoji(self):
        return emoji.emojize(self.title, use_aliases=True)

    def content_to_markdown(self):
        # First converted to emoji and then to markdown
        to_emoji_content = emoji.emojize(self.content, use_aliases=True)
        return markdown.markdown(to_emoji_content, extensions=['markdown.extensions.extra', ])


# Slideshow
class Carousel(models.Model):
    number = models.IntegerField('Number',
                                 help_text='Number determines the order in which pictures are played, not more than 5 pictures')
    title = models.CharField('Title', max_length=20, blank=True, null=True, help_text='Title can be empty')
    content = models.CharField('Description', max_length=80)
    img_url = models.CharField('Image address', max_length=200)
    url = models.CharField('Jump link', max_length=200, default='#',
                           help_text='Hyperlink for image jump, default # means no jump')

    class Meta:
        verbose_name = 'Picture Carousel'
        verbose_name_plural = verbose_name
        # The smaller the number is, the earlier it is, and the time will be added later.
        ordering = ['number', '-id']

    def __str__(self):
        return self.content[: 25]


# Dead chain
class Silian(models.Model):
    badurl = models.CharField('Dead chain address', max_length=200,
                              help_text='Note: The address is in the full link format starting with http')
    remark = models.CharField('Dead chain description', max_length=50, blank=True, null=True)
    add_date = models.DateTimeField('Date of submission', auto_now_add=True)

    class Meta:
        verbose_name = 'Dead Link'
        verbose_name_plural = verbose_name
        ordering = ['-add_date']

    def __str__(self):
        return self.badurl


class FriendLink(models.Model):
    name = models.CharField('Site name', max_length=50)
    description = models.CharField('Site description', max_length=100, blank=True)
    link = models.URLField('Friendly chain address',
                           help_text='Please fill in the full form address starting with http or https')
    logo = models.URLField('Website Logo', help_text='Please fill in the full form address starting with http or https',
                           blank=True)
    create_date = models.DateTimeField('Creation time', auto_now_add=True)
    is_active = models.BooleanField('Whether active', default=True)
    is_show = models.BooleanField('Whether the homepage is displayed', default=False)

    class Meta:
        verbose_name = 'Friendly Link'
        verbose_name_plural = verbose_name
        ordering = ['create_date']

    def __str__(self):
        return self.name

    def get_home_url(self):
        '' 'Extract the homepage of YouChain' ''
        u = re.findall(r'(http | https: //.*?) /.*?', self.link)
        home_url = u[0] if u else self.link
        return home_url

    def active_to_false(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def show_to_false(self):
        self.is_show = True
        self.save(update_fields=['is_show'])
