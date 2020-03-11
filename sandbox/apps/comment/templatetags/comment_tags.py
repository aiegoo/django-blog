# Server must be restarted after creating new tags file

from django import template

register = template.Library ()

@ register.simple_tag
def get_comment_count (entry):
    '' 'Get the total number of comments for an article' ''
    lis = entry.article_comments.all ()
    return lis.count ()

@ register.simple_tag
def get_parent_comments (entry):
    '' 'Get a list of parent comments for an article' ''
    lis = entry.article_comments.filter (parent = None)
    return lis

@ register.simple_tag
def get_child_comments (com):
    '' 'Get a list of child level paths for a parent comment' ''
    lis = com.articlecomment_child_comments.all ()
    return lis

@ register.simple_tag
def get_comment_user_count (entry):
    '' 'Get total number of reviewers' ''
    p = []
    lis = entry.article_comments.all ()
    for each in lis:
        if each.author not in p:
            p.append (each.author)
    return len (p)

@ register.simple_tag
def get_notifications (user, f = None):
    '''Get prompt information for a user\'s corresponding conditions'''
    if f == 'true':
        lis = user.notification_get.filter (is_read = True)
    elif f == 'false':
        lis = user.notification_get.filter (is_read = False)
    else:
        lis = user.notification_get.all ()
    return lis

@ register.simple_tag
def get_notifications_count (user, f = None):
    '' 'Get the total number of prompts under the corresponding conditions of a user' ''
    if f == 'true':
        lis = user.notification_get.filter (is_read = True)
    elif f == 'false':
        lis = user.notification_get.filter (is_read = False)
    else:
        lis = user.notification_get.all ()
    return lis.count ()