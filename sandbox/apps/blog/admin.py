from django.contrib import admin
from .models import Article, Tag, Category, Timeline, Carousel, Silian, Keyword, FriendLink


@ admin.register (Article)
class ArticleAdmin (admin.ModelAdmin):
    # The purpose of this is to give a screening mechanism, which is generally better by time
    date_hierarchy = 'create_date'

    exclude = ('views',)

    # When viewing the modified attributes, the first field is tagged with <a>, so it is best to put the title
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')

    # Set the fields to which the <a> tag needs to be added
    list_display_links = ('title',)

    # Activate the filter, this is useful
    list_filter = ('create_date', 'category')

    list_per_page = 50 # control the number of objects displayed per page, the default is 100

    filter_horizontal = ('tags', 'keywords') # add a box to the left and right for multiple selection

    # Restrict user permissions and only see articles edited by you
    def get_queryset (self, request):
        qs = super (ArticleAdmin, self) .get_queryset (request)
        if request.user.is_superuser:
            return qs
        return qs.filter (author = request.user)


@ admin.register (Tag)
class TagAdmin (admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


@ admin.register (Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


# Customize the name and URL title of the management site
admin.site.site_header = 'Site Administration'
admin.site.site_title = 'Blog background management'


@ admin.register (Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('title', 'side', 'update_date', 'icon', 'icon_color',)
    fieldsets = (
        ('Icon information', {'fields': (('icon', 'icon_color'),)}),
        ('Time Position', {'fields': (('side', 'update_date', 'star_num'),)}),
        ('Main content', {'fields': ('title', 'content')}),
    )
    date_hierarchy = 'update_date'
    list_filter=('star_num', 'update_date')


@ admin.register (Carousel)
class CarouselAdmin (admin.ModelAdmin):
    list_display = ('number', 'title', 'content', 'img_url', 'url')


@ admin.register (Silian)
class SilianAdmin (admin.ModelAdmin):
    list_display = ('id', 'remark', 'badurl', 'add_date')


@ admin.register (Keyword)
class KeywordAdmin (admin.ModelAdmin):
    list_display = ('name', 'id')


@ admin.register (FriendLink)
class FriendLinkAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'link', 'create_date', 'is_active', 'is_show')
    date_hierarchy = 'create_date'
    list_filter = ('is_active', 'is_show')