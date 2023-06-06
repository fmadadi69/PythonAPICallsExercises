import docx
import re

filename = '/Users/apple/Documents/intro.docx'
new_filename= '/Users/apple/Documents/new_intro.docx'


def getText(text_file):
    doc = docx.Document(text_file)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)


text = getText(filename)

all_nums = re.findall('\d+', text)
all_reversed_nums = []
for nums in all_nums:
    all_reversed_nums.append(nums[::-1])

print(all_nums)
print(all_reversed_nums)

new_text = text

# for item1 in all_nums:
#     new_text = new_text.replace(item1, all_reversed_nums.pop(0))

zipped_nums = zip(all_nums, all_reversed_nums)
for items in zipped_nums:
    new_text = new_text.replace(items[0],items[1])

print(new_text)
my_doc = docx.Document()
my_doc.add_paragraph(new_text)
my_doc.save(new_filename)

