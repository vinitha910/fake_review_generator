import json

class ReviewDataReader:
    def __init__(self, category):
        self.file = open('data/reviews_' + category + '_5.json', 'r')
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

def main():
    category = 'Amazon_Instant_Video'
    reader = ReviewDataReader(category)
    print(reader.next()['reviewText'])

if __name__ == '__main__':
    main()
