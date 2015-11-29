import sys
from datetime import datetime

TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute}
Category:
Slug: {slug}
Summary:
Status: draft
"""
def newpost(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '_')
    f_create = "content/{}{:0>2}{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
         w.write(t)
    return t
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        newpost(sys.argv[1])
    else:
        print "No title given"
