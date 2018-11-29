import json
import os

raw_data = [
    'reviews_Amazon_Instant_Video_5.json',
    'reviews_Apps_for_Android_5.json',
    'reviews_Automotive_5.json',
    'reviews_Baby_5.json',
    'reviews_Beauty_5.json',
    'reviews_Books_5.json',
    'reviews_CDs_and_Vinyl_5.json',
    'reviews_Cell_Phones_and_Accessories_5.json',
    'reviews_Clothing_Shoes_and_Jewelry_5.json',
    'reviews_Digital_Music_5.json',
    'reviews_Electronics_5.json',
    'reviews_Grocery_and_Gourmet_Food_5.json',
    'reviews_Health_and_Personal_Care_5.json',
    'reviews_Home_and_Kitchen_5.json',
    'reviews_Kindle_Store_5.json',
    'reviews_Movies_and_TV_5.json',
    'reviews_Musical_Instruments_5.json',
    'reviews_Office_Products_5.json',
    'reviews_Patio_Lawn_and_Garden_5.json',
    'reviews_Pet_Supplies_5.json',
    'reviews_Sports_and_Outdoors_5.json',
    'reviews_Tools_and_Home_Improvement_5.json',
    'reviews_Toys_and_Games_5.json',
    'reviews_Video_Games_5.json'
]

class ReviewDataCleaner:
    def __init__(self, raw_review):
        self.file_name = raw_review
        self.file = open('data/' + raw_review, 'r')
        self.line = self.file.readline()

    def hasNext(self):
        return self.line != ''

    def next(self):
        if self.hasNext():
            res = json.loads(self.line)
            self.line = self.file.readline()
            return res

    def close(self):
        self.file.close()
        self.line = ''

    def remove(self):
        os.remove('data/' + self.file_name)

def main():
    for raw_review in raw_data:
        cleaner = ReviewDataCleaner(raw_review)
        category = raw_review.replace('reviews_', '').replace('_5.json', '')
        outfile = open('processed_data/' + category + '.csv', 'w')
        while cleaner.hasNext():
            text = cleaner.next()['reviewText']
            outfile.write(text + '\n')
        outfile.close()
        cleaner.close()
        print('Done processing ' + raw_review + '. Removing file...')
        cleaner.remove()
        print('Done!')

if __name__ == '__main__':
    main()
