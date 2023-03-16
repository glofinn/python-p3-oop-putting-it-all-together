#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count=0,):
        self.title = title
        self.page_count = page_count
        # self.author = author

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        pass

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if (type(page_count)) in (int,):
            self._page_count = page_count

        else:
            print('page_count must be an integer')

    page_count = property(get_page_count, set_page_count)
        
    def turn_page(self):
        print('Flipping the page...wow, you read fast!')




    # def set_author(self):
    #     return self.author
    
    # def get_author(self, author):
    #     pass

    # def set_page_count(self):
    #     return self.page_count
    
    # def get_page_count(self, page_count):
    #     if (type(page_count) != (int,)):
    #         print('page_count must bean integer')
            
    # property(set_page_count, get_page_count)

