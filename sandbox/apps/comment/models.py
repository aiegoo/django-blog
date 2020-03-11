from django.db import models
from django.conf import settings
from apps.blog.models import Article

import markdown
import emoji


class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class) s_related', verbose_name='reviewer', on_delete=models.CASCADE)
    create_date=models.DateTimeField('Creation time', auto_now_add=True)
    content=models.TextField('Comment Content')
    parent=models.ForeignKey('self', verbose_name='parent comment', related_name='%(class) s_child_comments', blank=True,
                               null=True, on_delete=models.CASCADE)
    rep_to=models.ForeignKey('self', verbose_name='Reply', related_name='%(class) s_rep_comments', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        '' 'This is a metaclass for inheritance' ''
        abstract=True

    def __str__(self):
        return self.content [:20]

    def content_to_markdown(self):
        # First converted to emoji and then to markdown, 'escape': all original HTML will be escaped and included in the document
        to_emoji_content=emoji.emojize(self.content, use_aliases=True)
        to_md=markdown.markdown(to_emoji_content,
                                  safe_mode='escape',
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                  ])
        return to_md

class ArticleComment(Comment):
    belong=models.ForeignKey(Article, related_name='article_comments', verbose_name='belonging articles', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Post Comment'
        verbose_name_plural=verbose_name
        ordering=['create_date']

class Notification(models.Model):
    create_p=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Prompt creator', related_name='notification_create', on_delete=models.CASCADE)
    get_p=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Prompt Recipient', related_name='notification_get', on_delete=models.CASCADE)
    comment=models.ForeignKey(ArticleComment, verbose_name='Owned Comment', related_name='the_comment', on_delete=models.CASCADE)
    create_date=models.DateTimeField('Hint time', auto_now_add=True)
    is_read=models.BooleanField('Whether read', default=False)

    def mark_to_read(self):
        self.is_read=True
        self.save(update_fields=['is_read'])

    class Meta:
        verbose_name='Prompt Message'
        verbose_name_plural=verbose_name
        ordering=['-create_date']

    def __str__(self):
        return '() @ 了 {}'. format(self.create_p, self.get_p)