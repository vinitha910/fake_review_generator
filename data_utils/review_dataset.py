import numpy as np
from vocabulary import Vocabulary

class ReviewDataset(torch.utils.data.Dataset):
    def __init__(self, data_file, sequence_length, batch_size):
        super(ReviewDataset, self).__init__()

        self.sequence_length = sequence_length
        self.batch_size = batch_size
        self.vocab = Vocabulary(data_file)

        with open(data_file, 'rb') as data_pkl:
            dataset = pickle.load(data_pkl)

        self.tokens = dataset['tokens']
        remainder = len(self.tokens) % self.batch_size
        num_tokens = len(self.tokens) - remainder
        self.tokens = self.tokens[:num_tokens]

        assert len(self.tokens) % batch_size == 0

        incr = len(self.tokens)/self.batch_size
        index_range = len(self.tokens)/self.batch_size
        data_start_idx = 0
        label_start_idx = 1
        data_end_idx = data_start_idx + self.sequence_length
        label_end_idx = label_start_idx + self.sequence_length
        batch = 0 
        data = [[]]
        labels = [[]]

        while label_start_idx < len(self.tokens):
            data[batch].append(self.tokens[int(data_start_idx):int(data_end_idx)])
            labels[batch].append(self.tokens[int(label_start_idx):int(label_end_idx)])

            if label_end_idx == index_range:
                data.append([])
                labels.append([])
                data_start_idx = data_end_idx + 1
                label_start_idx = label_end_idx + 1
                data_end_idx = data_start_idx + self.sequence_length
                label_end_idx = label_start_idx + self.sequence_length
                index_range += incr
                batch += 1

            else:
                data_start_idx += self.sequence_length
                label_start_idx += self.sequence_length

                data_end_idx += self.sequence_length
                if data_end_idx > index_range - 1:
                    data_end_idx = index_range - 1;

                label_end_idx += self.sequence_length
                if label_end_idx > index_range:
                    label_end_idx = index_range
        
        self.data = []
        self.labels = []
        for b in range(len(data[0])):
            self.data.append([])
            self.labels.append([])
            for d in range(len(data)):
                if b < len(data[d]):
                    self.data[-1].append(data[d][b])
                    self.labels[-1].append(labels[d][b])

    def __len__(self):
        return len(np.unique(self.data))
        
    def __getitem__(self, idx):
        # Return the data and label for a character sequence as described above.
        # The data and labels should be torch long tensors.
        # You should return a single entry for the batch using the idx to decide which chunk you are 
        # in and how far down in the chunk you are.
        col = int(idx % len(self.data[0]))
        row = int(idx / len(self.data[0]))

        if row >= len(self.data) or col >= len(self.data[row]):
            print("ReviewDataset index out of bounds")
            
        item_data = torch.LongTensor(self.data[row][col])
        item_label = torch.LongTensor(self.labels[row][col])
        
        return item_data, item_label

    def vocab_size(self):
        return len(self.vocab)