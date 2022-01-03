# Letters!
# this will override it!
def mergefiles(files, openMergedFile):
    seen = set()
    for i in range(len(files)):
        file = files[i]
        line_list = [line.rstrip('\n') for line in file]
        postingStr = ""
        for line in line_list:
            #stringlst: ["Kelly", " (1,2)"]
            stringlst = line.split(":")
            token = stringlst[0]
            posting = stringlst[1]
            

            if token not in seen:
                if postingStr != "":
                    openMergedFile.write(postingStr + "\n")
                    postingStr = ""
                postingStr += f'{token}:{posting}'

            else:
                postingStr += posting

            #mark token as seen
            seen.add(token)


afile = open("partialindex/a.txt", "r")
bfile = open("partialindex/b.txt", "r")
cfile = open("partialindex/c.txt", "r")
dfile = open("partialindex/d.txt", "r")
efile = open("partialindex/e.txt", "r")
ffile = open("partialindex/f.txt", "r")
gfile = open("partialindex/g.txt", "r")
hfile = open("partialindex/h.txt", "r")
ifile = open("partialindex/i.txt", "r")
jfile = open("partialindex/j.txt", "r")
kfile = open("partialindex/k.txt", "r")
lfile = open("partialindex/l.txt", "r")
mfile = open("partialindex/m.txt", "r")
nfile = open("partialindex/n.txt", "r")
ofile = open("partialindex/o.txt", "r")
pfile = open("partialindex/p.txt", "r")
qfile = open("partialindex/q.txt", "r")
rfile = open("partialindex/r.txt", "r")
sfile = open("partialindex/s.txt", "r")
tfile = open("partialindex/t.txt", "r")
ufile = open("partialindex/u.txt", "r")
vfile = open("partialindex/v.txt", "r")
wfile = open("partialindex/w.txt", "r")
xfile = open("partialindex/x.txt", "r")
yfile = open("partialindex/y.txt", "r")
zfile = open("partialindex/z.txt", "r")
numberfile = open("partialindex/numbers.txt", "r")

# SORTED
sortedafile = open("sortedindex/a.txt", "w+")
sortedbfile = open("sortedindex/b.txt", "w+")
sortedcfile = open("sortedindex/c.txt", "w+")
sorteddfile = open("sortedindex/d.txt", "w+")
sortedefile = open("sortedindex/e.txt", "w+")
sortedffile = open("sortedindex/f.txt", "w+")
sortedgfile = open("sortedindex/g.txt", "w+")
sortedhfile = open("sortedindex/h.txt", "w+")
sortedifile = open("sortedindex/i.txt", "w+")
sortedjfile = open("sortedindex/j.txt", "w+")
sortedkfile = open("sortedindex/k.txt", "w+")
sortedlfile = open("sortedindex/l.txt", "w+")
sortedmfile = open("sortedindex/m.txt", "w+")
sortednfile = open("sortedindex/n.txt", "w+")
sortedofile = open("sortedindex/o.txt", "w+")
sortedpfile = open("sortedindex/p.txt", "w+")
sortedqfile = open("sortedindex/q.txt", "w+")
sortedrfile = open("sortedindex/r.txt", "w+")
sortedsfile = open("sortedindex/s.txt", "w+")
sortedtfile = open("sortedindex/t.txt", "w+")
sortedufile = open("sortedindex/u.txt", "w+")
sortedvfile = open("sortedindex/v.txt", "w+")
sortedwfile = open("sortedindex/w.txt", "w+")
sortedxfile = open("sortedindex/x.txt", "w+")
sortedyfile = open("sortedindex/y.txt", "w+")
sortedzfile = open("sortedindex/z.txt", "w+")
# Numbers
sortednumberfile = open("sortedindex/numbers.txt", "w+")

#open file for big merging
mergedfile = open("mergedfile.txt", "w+")


partialIndexFileList = [
    afile, bfile, cfile, dfile, efile, ffile, gfile, hfile, ifile, jfile,
    kfile, lfile, mfile, nfile, ofile, pfile, qfile, rfile, sfile, tfile,
    ufile, vfile, wfile, xfile, yfile, zfile, numberfile
]

sortedpartialIndexFileList = [
    sortedafile, sortedbfile, sortedcfile, sorteddfile, sortedefile,
    sortedffile, sortedgfile, sortedhfile, sortedifile, sortedjfile,
    sortedkfile, sortedlfile, sortedmfile, sortednfile, sortedofile,
    sortedpfile, sortedqfile, sortedrfile, sortedsfile, sortedtfile,
    sortedufile, sortedvfile, sortedwfile, sortedxfile, sortedyfile,
    sortedzfile, sortednumberfile
]

openedfiles = [
    open(f"sortedindex/{letter}.txt")
    for letter in "abcdefghijklmnopqrstuvwxyz"
]
openedfiles.append(open("sortedindex/numbers.txt"))

pointerMap = {}
for i in range(len(partialIndexFileList)):
    partialIndexFile = partialIndexFileList[i]
    sortedPartialIndexFile = sortedpartialIndexFileList[i]
    lines = sorted(partialIndexFile.readlines())
    for line in lines:
        sortedPartialIndexFile.write(line)

mergefiles(openedfiles, mergedfile)

# Letters!
afile.close()
bfile.close()
cfile.close()
dfile.close()
efile.close()
ffile.close()
gfile.close()
hfile.close()
ifile.close()
jfile.close()
kfile.close()
lfile.close()
mfile.close()
nfile.close()
ofile.close()
pfile.close()
qfile.close()
rfile.close()
sfile.close()
tfile.close()
ufile.close()
vfile.close()
wfile.close()
xfile.close()
yfile.close()
zfile.close()

# Numbers!
numberfile.close()

# Letters!
sortedafile.close()
sortedbfile.close()
sortedcfile.close()
sorteddfile.close()
sortedefile.close()
sortedffile.close()
sortedgfile.close()
sortedhfile.close()
sortedifile.close()
sortedjfile.close()
sortedkfile.close()
sortedlfile.close()
sortedmfile.close()
sortednfile.close()
sortedofile.close()
sortedpfile.close()
sortedqfile.close()
sortedrfile.close()
sortedsfile.close()
sortedtfile.close()
sortedufile.close()
sortedvfile.close()
sortedwfile.close()
sortedxfile.close()
sortedyfile.close()
sortedzfile.close()

# Numbers!
sortednumberfile.close()
mergedfile.close()
