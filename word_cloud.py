import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_frequencies(filename):
    '''
    Function that will produce a word cloud based on the frequency of the word
    '''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    words, freq = [], {}
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip().split()
            line = list(map(lambda x: x.translate(str.maketrans('', '', string.punctuation)), line))
            words += line

    for word in words:
        if word not in uninteresting_words:
            if word in words:
                freq[word] = 1
            else:
                freq[word] += 1

    cloud = WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()


filename = 'book.txt'
word_cloud = generate_frequencies(filename)
plt.imshow(word_cloud, interpolation = 'nearest')
plt.axis('off')
plt.show()