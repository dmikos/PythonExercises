from urllib.request import urlopen
from urllib.parse import urljoin
from lxml.html import fromstring

# url = https://geekbrains.ru/courses#cour
# class="gb__main-wrapper"
# class="container footer-stick"
# class="row"
# id="courses"
# class="course-item col-md-6 col-xs-12 v-top m-b-lg tag-2 tag-3free" data-id="2"
# class="course-item col-md-6 col-xs-12 v-top m-b-lg tag-2 tag-3 tag-1 tag-48 tag-47free" data-id="110"


URL = 'https://geekbrains.ru/courses#cour'
ITEM_PATH = '.row .course-item .course-item__description'
DESCR_PATH1 = '.gb__main-wrapper .div padder-v m-r m-l .row m-t-lg .col-md-6 .author .pull-left'
DESCR_PATH = '.col-md-6 .author .pull-left'
TEACH_PATH = '#authors .author .m-l m-b-xs m-t-xs m-r-xs'



def parse_courses():
    f = urlopen(URL)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)

    for elem in list_doc.cssselect(ITEM_PATH):
        a = elem.cssselect('a.course-item__description__title')[0]
        href = a.get('href')
        name = a.text
        div = elem.cssselect('div.course-item__description__subtitle')[0]
        description = div.text
        url = urljoin(URL, href)

        course = {'name': name, 'lead': description, 'url': url}

        details_html = urlopen(url).read().decode('utf-8')
        details_doc = fromstring(details_html)

        for teach_elems in details_doc.cssselect(TEACH_PATH):
            teaches = [teach_elems.text for teach_elem in teach_elems]
            print(teaches)
        # teach_elems = details_doc.cssselect(TEACH_PATH)
        # teaches = [teach_elems.text for teach_elem in teach_elems]




def main():
    parse_courses()

if __name__ == '__main__':
    main()