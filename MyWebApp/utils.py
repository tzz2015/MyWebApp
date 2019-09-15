from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from MyWebApp.json_utils import result_handler, format_data


# 获取分页数据
def page_list(page, page_size, class_name, filter=None, exclude=None):
    if filter is not None and exclude is not None:
        class_list = class_name.objects.all().filter(**filter).exclude(**exclude)
    elif filter is not None:
        class_list = class_name.objects.all().filter(**filter)
    elif exclude is not None:
        class_list = class_name.objects.all().exclude(**exclude)
    else:
        class_list = class_name.objects.all()

    paginator = Paginator(class_list, page_size)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return PageInfo(class_list.__len__(), contacts.object_list).to_dict()


class PageInfo(object):
    def __init__(self, total, rs_list):
        self.total = total
        self.rs_list = rs_list

    def to_dict(self):
        return {
            'total': self.total,
            'list': format_data(self.rs_list)
        }