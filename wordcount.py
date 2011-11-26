import sys

IGNORE = ['a', 'the', 'are', 'were', 'is', 'am', 'as', 'to', 'than',\
        'yes', 'no', 'and', 'was', 'that', 'of', 'be', 'will', 'in',\
        'from', 'with', 'for', 'all', 'by', 'not', 'have', 'must',\
        'this', 'there', 'it', 'which', 'at', 'an', 'would', 'had',\
        'about', 'when', 'but', 'how', 'what', 'on', 'or', 'its',\
        'into', 'through']

def get_dict(filename):
    f = open(filename, 'rU')
    words = f.read().split()
    dict = {}
    for word in words:
        if word.lower() in IGNORE:
            continue
        if word.lower() not in dict:
            dict[word.lower()] = 1
        else:
            dict[word.lower()] += 1
    f.close()
    return dict

def print_top(max_num, filename, outfilename):
    num = int(max_num)
    dict = get_dict(filename)
    f = open(outfilename, 'w')
    cnt = 0
    tmp = 0
    for a, b in sorted(dict.items(), key=lambda x: x[1], reverse=True):
        tmp += 1
        st = a + ' ' + str(b)
        if tmp != 3:
            f.write(st.ljust(15))
        else:
            f.write(st + '\n')
            tmp = 0
        print a, b
        cnt += 1
        if cnt == num: break
    f.write('\n')
    f.write('# of most frequent words: ' + max_num + '\n')
    f.write('Source file: ' + filename + '\n')
    f.close()

def main():
    #print 'usage: python wordcount.py NUMBER_OF_MOST_FREQUENT_WORDS INPUT_FILENAME OUTPUT_FILENAME'
    max_num = sys.argv[1]
    filename = sys.argv[2]
    outfilename = sys.argv[3]
    print_top(max_num, filename, outfilename)

if __name__ == '__main__':
  main()
