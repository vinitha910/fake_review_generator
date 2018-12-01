
processed_data = [
    'Amazon_Instant_Video.csv',
    'Apps_for_Android.csv',
    'Automotive.csv',
    'Baby.csv',
    'Beauty.csv',
    'Books.csv',
    'CDs_and_Vinyl.csv',
    'Cell_Phones_and_Accessories.csv',
    'Clothing_Shoes_and_Jewelry.csv',
    'Digital_Music.csv',
    'Electronics.csv',
    'Grocery_and_Gourmet_Food.csv',
    'Health_and_Personal_Care.csv',
    'Home_and_Kitchen.csv',
    'Kindle_Store.csv',
    'Movies_and_TV.csv',
    'Musical_Instruments.csv',
    'Office_Products.csv',
    'Patio_Lawn_and_Garden.csv',
    'Pet_Supplies.csv',
    'Sports_and_Outdoors.csv',
    'Tools_and_Home_Improvement.csv',
    'Toys_and_Games.csv',
    'Video_Games.csv'
]

class ReviewDataReader:
    def __init__(self, processed_review_file):
        self.file_name = processed_review_file
        self.file = open(processed_review_file, 'r')
        self.line = self.file.readline().strip()

    def hasNext(self):
        return self.line != ''

    def next(self):
        if self.hasNext():
            res = self.line
            self.line = self.file.readline().strip()
            return res

    def close(self):
        self.file.close()
        self.line = ''

def main():
    message_num = 3
    for file_name in processed_data:
        category = file_name.replace('.csv', '')
        reader = ReviewDataReader("processed_data/{:s}".format(file_name))
        count = 0
        print("Category: {:s}".format(category))
        while reader.hasNext() and count < message_num:
            review = reader.next()
            print("Review{:d}: {:s}".format(count, review))
            count += 1
        print('')

if __name__ == '__main__':
    main()
