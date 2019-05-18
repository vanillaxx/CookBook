import os
import django

def populate():
    add_tag('agrest')
    add_tag('truskawki')
    add_tag('maliny')
    add_tag('porzeczki')
    add_tag('poziomki')
    add_tag('jablka')
    add_tag('gruszki')
    add_tag('jajka')
    add_tag('rzodkiewka')
    add_tag('ziemniaki')
    add_tag('szpinak')
    add_tag('cukier')
    add_tag('kapusta')
    add_tag('kasza')
    add_tag('maka')
    add_tag('pomidory')
    add_tag('mleko')
    add_tag('kokos')
    add_tag('banany')
    add_tag('liczi')
    add_tag('cynamon')


def add_tag(name):
    t = Tag.objects.get_or_create(name=name)
    return t


if __name__ == '__main__':
    print('Populating...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CookBook.settings')
    django.setup()
    from blog.models import Tag
    populate()
