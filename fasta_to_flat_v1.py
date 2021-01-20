from string import *

print 'The script and input fasta file should be in the same folder. Output will be created at the same location as that of the script.\n'
fname = raw_input('Please enter the name of the fasta file: ')
ifile = open(fname, 'r')
itext = ifile.read().split('>')
ifile.close()
while '' in itext:
	itext.remove('')

outfile = open('flat_' + fname, 'w')
icount = 0
for i in itext:
	icount += 1
	i1 = i.split('\n')
	acc = i1[0]
	iseq = ''.join(i1[1:])
	outfile.write('>' + acc + '\n' + iseq + '\n')
outfile.close()

print 'Output file:', ('flat_' + fname), 'created successfully with', icount, 'entries.'
