from modeltranslation.translator import register, TranslationOptions
from .models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    """ Класс, групипирующий свойства, подлежащие переводу в данном приложении """
    fields = ('title', 'about', 'content', 'author')
