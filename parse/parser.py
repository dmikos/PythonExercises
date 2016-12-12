from urllib.request import urlopen
from urllib.parse import urljoin
from lxml.html import fromstring
import xlsxwriter

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
TEACH_PATH = '#authors .author .m-l'



def parse_courses():
    f = urlopen(URL)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)
    courses = []

    for elem in list_doc.cssselect(ITEM_PATH):
        a = elem.cssselect('a.course-item__description__title')[0]
        href = a.get('href')
        name = a.text
        div = elem.cssselect('div.course-item__description__subtitle')[0]
        description = div.text
        url = urljoin(URL, href)

        course = {'name': name, 'lead': description, 'url': url}

        # details_html = urlopen(url).read().decode('utf-8')
        # details_doc = fromstring(details_html)

        # teaches = details_doc.cssselect(TEACH_PATH)
        # for teach_elems in details_doc.cssselect(TEACH_PATH):
        #    teaches = [teach_elems.text for teach_elem in teach_elems]
        #    print(teaches)
        courses.append(course)
    return courses

def export_excel(filename, courses):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    # worksheet.write(1, 2, 'Hello Excel')  #строка №1, колонка №2, текст в ячейке - "Hello Excel"

    bold = workbook.add_format({'bold': True})

    field_names = ('Название', 'Описание', 'url')
    for i, filed in enumerate(field_names):
        worksheet.write(0, i, filed, bold)

    fields = ('name', 'lead', 'url')
    for row, course in enumerate(courses, start=1):
        for col, field in enumerate(fields):
            #print(row, col, course[field])
            worksheet.write(row, col, course[field])

    workbook.close()

def main():
    courses = parse_courses()
    export_excel('courses.xlsx', courses)

if __name__ == '__main__':
    main()