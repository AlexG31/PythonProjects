# -*- coding=utf-8 -*-
import os
import sys
import codecs
def get_leadingSpacesNum(str):
		cnt=0
		for ch in str:
				if ch!=' ':
						break
				cnt+=1
		return cnt

def unTabfy(filename,Tabweight=4):
	''' format the py file'''

	fp=codecs.open(filename,'r','utf-8')
	fout=codecs.open(filename.split('.')[0]+'_noTab.py','w','utf-8')
	content=list()
	for line in fp:
		str=line.replace(chr(9),' '*Tabweight)
		content.append(str)
	## replace tab:
	## gain 4 spaces at most
	spacecnt=0
	for line_ind,line in enumerate(content):
		## reduce spaces
		if len(line.strip(' \r\n'))==0:
				fout.write(line)
				continue
		cspacecnt=get_leadingSpacesNum(line)
		print '==='*3
		print line
		print cspacecnt,' spaces'
		print '---'*3

		if cspacecnt>spacecnt:
				if cspacecnt-spacecnt!=4:
						line=' '*(spacecnt+4)+line[cspacecnt:]
						t_ind=line_ind+1
						while t_ind<len(content):
								if len(content[t_ind].strip(' \r\n'))==0:
										t_ind+=1
										continue
								tmp=get_leadingSpacesNum(content[t_ind])
								if tmp==cspacecnt:
										## process:reduce space
										print '--',content[t_ind]
										content[t_ind]=' '*(spacecnt+4)+content[t_ind][cspacecnt:]

										pass
								elif tmp<=spacecnt:
										print 'tmp %d <spacecnt %d'%(tmp,spacecnt)
										print 'content[%d]:'%t_ind,content[t_ind]
										print '*'*10
										break
								t_ind+=1
				spacecnt=spacecnt+4
		else:
			spacecnt=cspacecnt
		fout.write(line)
	fp.close()
	fout.close()
flist=os.listdir('.')
for f in flist:
		if f.endswith('.py') and not f.endswith('_noTab.py'):
				print '>>untabfy:',f
				unTabfy(f)
print '---End---'
