from __future__ import print_function
import os,sys
from struct import unpack
f = open('test2.caj','rb')

header = f.read(9*16)
pages = f.read(8)
[pages,unknown] = unpack('ii', pages)
print(pages)
# extract content index
f.seek(12*16, os.SEEK_CUR)
[contents_count] = unpack('i', f.read(4))
print(contents_count)
for x in xrange(1,contents_count):
	contents_string = f.read(308)
	[contents_title, contents_index, contents_page, unknown] = unpack('256s24s12s16s', contents_string)
	print(contents_title.decode('cp936').replace('\x00',''))
# extract pages
f.close()

os.system('pause >nul')