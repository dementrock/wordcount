import sys

IGNORE = ['a', 'the', 'are', 'were', 'is', 'am', 'as', 'to', 'than',
        'yes', 'no', 'and', 'was', 'that', 'of', 'be', 'will', 'in',
        'from', 'with', 'for', 'all', 'by', 'not', 'have', 'must',
        'this', 'there', 'it', 'which', 'at', 'an', 'would', 'had',
        'about', 'when', 'but', 'how', 'what', 'on', 'or', 'its',
        'into', 'through']

ITEM_PER_LINE = 3
ITEM_WIDTH = 15

def get_dict(filename):
    from collections import Counter 
    valid_words = [ word.lower() for word in open(filename, 'rU').read().split() if word.lower() not in IGNORE ]
    return Counter(valid_words)

def print_top(max_num, filename, outfilename):
    num = int(max_num)
    freq_list = get_dict(filename).most_common(num)
    freq_list = zip(freq_list, range(1, len(freq_list) + 1))
    item_wrapper = lambda x, index: x.ljust(ITEM_WIDTH) if index % ITEM_PER_LINE else x + '\n'
    output = ''.join([item_wrapper('%s %d' % (item[0], item[1]), index) for item, index in freq_list])
    if not output.endswith('\n'):
        output += '\n'
    output += '# of most frequent words: %s\nSource file: %s\n' % (max_num, filename)
    open(outfilename, 'w').write(output)

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        print 'usage: python wordcount.py NUMBER_OF_MOST_FREQUENT_WORDS INPUT_FILENAME OUTPUT_FILENAME'
    else:
        max_num, filename, outfilename = sys.argv[1:]
        print_top(max_num, filename, outfilename)

if __name__ == '__main__':
    main()
