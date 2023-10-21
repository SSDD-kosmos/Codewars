from math import ceil


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return ceil(len(self.collection) / self.items_per_page)

    def page_item_count(self, page_index):
        if self.item_count() > 0 and 0 <= page_index < self.page_count():
            if page_index != 0:
                page_item = self.item_count() - page_index * self.items_per_page
                if page_item > self.items_per_page:
                    return self.items_per_page
                else:
                    return page_item
            elif self.item_count() < self.items_per_page:
                return self.item_count()
            else:
                return self.items_per_page
        else:
            return -1

    def page_index(self, item_index):
        if 0 <= item_index < self.item_count():
            return item_index // self.items_per_page
        else:
            return -1


# class PaginationHelper:
#
#     # The constructor takes in an array of items and a integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page
#
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
#
#     # returns the number of pages
#     def page_count(self):
#         return 1+(self.item_count() // self.items_per_page)
#
#     # returns the number of items on the current page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         # Covers all full pages
#         if page_index+1 < self.page_count():
#             return self.items_per_page
#         # The last page
#         elif page_index+1 == self.page_count():
#             return (self.item_count() % self.items_per_page)
#         else:
#             return -1
#
#     # determines what page an item is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         if item_index >= 0:
#             if self.item_count() >= (item_index+1):
#                 return (item_index+1) // self.items_per_page
#         return -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
helper.page_count()  # should == 2
helper.item_count()  # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1)  # last page - should == 2
helper.page_item_count(2)  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5)  # should == 1 (zero based index)
helper.page_index(2)  # should == 0
helper.page_index(20)  # should == -1
helper.page_index(-10)  # should == -1 because negative indexes are invalid
