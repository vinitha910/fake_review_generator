class Vocabulary(object):
    def __init__(self, data_file):
        with open(data_file, 'rb') as data_file:
            dataset = pickle.load(data_file)
        self.ind2voc = dataset['ind2voc']
        self.voc2ind = dataset['voc2ind']
        self.unknown_token_idk = dataset['unknown_token_idx']

    # Returns a string representation of the tokens.
    def array_to_words(self, arr):
        return ' '.join([self.ind2voc[int(ind)] for ind in arr])

    # Returns a torch tensor representing each token in words.
    def words_to_array(self, words):
        words = re.findall(r"[\w]+|[.,!?;]|[\s]", words)
        arr = []
        for word in words:
            if word in self.voc2ind.keys():
                arr.append(self.voc2ind[word])
            else:
                arr.append(self.unknown_token_idx)
        return torch.LongTensor(arr)

    # Returns the size of the vocabulary.
    def __len__(self):
        return len(self.ind2voc)