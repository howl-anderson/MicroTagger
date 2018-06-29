"""
Can remove pinyin tag and remove sentence that don't match word/tag pattern
"""
from collections import Counter


class DataCleaner(object):
    def __init__(self, input_file, output_file):
        self.input_fd = open(input_file)
        self.output_fd = open(output_file, 'wt')

    def process(self):
        output_lines = []

        for raw_line in self.input_fd:
            # removing head and tail invisible char
            line = raw_line.strip()

            if not line:
                # skip empty line
                continue

            line_is_clean = self.line_is_clean(line)
            if not line_is_clean:
                # skip dirty line
                continue

            pinyin_free_line = self.remove_pinyin_tag(line)
            output_lines.append(pinyin_free_line)

            self.output_fd.write(pinyin_free_line + '\n')

        # self.output_fd.writelines(output_lines)

    def line_is_clean(self, line):
        for word_pinyin_tag in line.split():
            char_counter = Counter(word_pinyin_tag)
            if char_counter['/'] != 1:  # iff contains only one '/' is correct data item
                return False

        return True

    def remove_pinyin_tag(self, line):
        pinyin_free_data = []
        for word_pinyin_tag in line.split():
            # extract
            word_pinyin, tag = word_pinyin_tag.split('/')

            # if word_pinyin contains pinyin
            if '{' in word_pinyin:
                word, pinyin_with_tail = word_pinyin.split('{')

                # useless here
                pinyin = pinyin_with_tail[:-1]
            else:
                word = word_pinyin

            word_tag = "/".join([word, tag])
            pinyin_free_data.append(word_tag)

        return "  ".join(pinyin_free_data)  # using two space char for better visible for human just as origin does


if __name__ == "__main__":
    data_cleaner = DataCleaner('raw_data.txt', 'data.txt')
    data_cleaner.process()