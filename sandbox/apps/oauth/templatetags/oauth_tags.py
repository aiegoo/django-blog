# Server must be restarted after creating new tags file

from django import template

register = template.Library ()

@ register.inclusion_tag ('oauth/tags/user_avatar.html')
def get_user_avatar_tag (user):
   '''Return the user's picture, it is an img tag'''
   return {'user': user}