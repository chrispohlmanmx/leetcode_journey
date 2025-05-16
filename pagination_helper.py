class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return self.item_count() // self.items_per_page + 1
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.page_count() - 1:
            return -1
        else:
            total_pages = self.page_count()
            final_page = total_pages - total_pages // self.item_count()
            if page_index + 1 == final_page:
                return self.item_count() % self.items_per_page
            else:
                return self.items_per_page
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > self.item_count() -1:
            return -1
        else:
            total_items = 0
            for i in range(0, self.page_count()):
                total_items += self.page_item_count(i)
                print(total_items, i)
                if item_index <= total_items:
                    return i
            

def main():
    collection = [1,2,3,4]
    helper = PaginationHelper(collection, 1)

    print(f'{helper.item_count():.2f}')
    print(f'{helper.page_count():.2f}')
    print(f'number of items on page 1 {helper.page_item_count(0)} and number of items on page 2 {helper.page_item_count(1)}')
    print(f'item number 2 is on page {helper.page_index(2)} and item number 7 should be -1 and is actually: {helper.page_index(7)}')
    helper.page_index(2)

if __name__ == "__main__":
    main()
