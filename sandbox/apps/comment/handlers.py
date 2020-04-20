from django.db.models.signals import post_save
from .models import ArticleComment, Notification


def notify_handler (sender, instance, created, ** kwargs):
    the_article = instance.belong
    create_p = instance.author
    # Determine whether it is the first time to generate a comment, and subsequent modification of the comment will not activate the signal again
    if created:
        if instance.rep_to:
            '''If the comment is a reply comment, notify both the author of the article and the commenter who responded, if the two are equal, only once'''
            if the_article.author == instance.rep_to.author:
                get_p = instance.rep_to.author
                if create_p != get_p:
                    new_notify = Notification (create_p = create_p, get_p = get_p, comment = instance)
                    new_notify.save ()
            else:
                get_p1 = the_article.author
                if create_p != get_p1:
                    new1 = Notification (create_p = create_p, get_p = get_p1, comment = instance)
                    new1.save ()
                get_p2 = instance.rep_to.author
                if create_p != get_p2:
                    new2 = Notification (create_p = create_p, get_p = get_p2, comment = instance)
                    new2.save ()
        else:
            '''If the comment is a first-level comment instead of responding to other comments and not the author's self-evaluation, notify the article author directly'''
            get_p = the_article.author
            if create_p != get_p:
                new_notify = Notification (create_p = create_p, get_p = get_p, comment = instance)
                new_notify.save ()

post_save.connect(notify_handler, sender = ArticleComment)