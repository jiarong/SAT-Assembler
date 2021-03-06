#!/usr/bin/env python
import sys
import os

def output_hmm_file(content, file_name):
    with open(file_name, 'wb') as f:
        for line in content:
            f.write(line)

def main():
    if len(sys.argv) != 3:
        print >> sys.stderr, 'Usage: <input hmm file> <output folder>'
        sys.exit(2)
 
    hmm_file_name = sys.argv[1]
    dir = sys.argv[2]
    if not os.path.exists(dir):
        os.makedirs(dir)
    content = []
    acc = ''
    name = ''
    with open(hmm_file_name, 'Ur') as f:
        for line in f:
            content.append(line)
            items = line.strip().split()
            if items[0] == 'ACC':
                acc = items[1][:7] 
            if items[0] == 'NAME':
                name = items[1]
            elif items[0] == '//':
                if acc:
                    file_name = dir.rstrip('/') + '/' + acc + '.hmm' 
                elif name:
                    file_name = dir.rstrip('/') + '/' + name + '.hmm' 
                else:
                    sys.stderr.write('*** hmm file must have ACC or NAME lines..')
                    sys.exit(1)

                output_hmm_file(content, file_name)
                content = []
                acc = ''      
                name = ''

if __name__ == '__main__':
    main()
