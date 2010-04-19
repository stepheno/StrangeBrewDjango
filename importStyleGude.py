from xml.dom import minidom
from django.core.management import setup_environ
import settings
setup_environ(settings)

from StrangeBrew.SNB.models import Category

xmldoc = minidom.parse('styleguide.xml')

categories = xmldoc.getElementsByTagName('category')
for category in categories:
    subcategories = category.getElementsByTagName('subcategory')
    for subcategory in subcategories:
        comments = subcategory.getElementsByTagName('comments')
        if len(comments) > 0:
            comment = comments[0].firstChild.data
        id = subcategory.attributes["id"].value
        names = subcategory.getElementsByTagName('name')
        if len(names) > 0:
            cat_name = names[0].firstChild.data
        cat = Category(name=cat_name.lstrip('\n'),category=id.rstrip('\n'),description=comment.lstrip('\n'))
        print cat
        cat.save()
        #print cat.description
        #print "%s: %s" % (id,name)

