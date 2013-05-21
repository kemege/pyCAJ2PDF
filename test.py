from __future__ import print_function
import os,sys
from struct import unpack,pack
f = open('test.caj','rb')

header = f.read(9*16)
pages_string = f.read(8)
pages = []
contents = []
[pages_count,unknown] = unpack('ii', pages_string)
print('pages: '+str(pages_count))
# extract content index
f.seek(12*16, os.SEEK_CUR)
[contents_count] = unpack('i', f.read(4))
print('contents items: '+str(contents_count))
for x in xrange(0,contents_count):
	contents_string = f.read(308)
	[contents_title, contents_index, contents_page, unknown, contentd_level] = unpack('256s24s12s12si', contents_string)
	contents.append([contents_title, contents_page, contentd_level])
	print('\t'*(contentd_level-1)+contents_title.replace('\x00','').decode('cp936').encode('utf-8'))
# extract page offsets
for x in xrange(0,pages_count):
	pageoffset_string = f.read(12)
	f.seek(8, os.SEEK_CUR)
	[page_offset, page_content_offset, rel_index, index] = unpack('IIhh', pageoffset_string)
	pages.append([page_offset, page_content_offset, rel_index, index])
	# print(str(index)+':'+str(page_offset))

for page in pages:
	f.seek(page[0])
	offset = 0
	while offset<=page[1]:
		char = f.read(4)
		[u1, u2, u3, u4] = unpack('bbbb', char)
		[word] = unpack('2s', pack('bb',u4,u3))
		print(word, end='')
		offset += 4

	print('\n')
f.close()
os.system('pause >nul')