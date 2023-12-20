import pydirbuster
import urllib.request
import re
class web():
  def __init__(self):
    self.website = "https://www.redstone-cg.com"
    self.ext = ['html','css','js','php','py','xml','json']
    self.wordlist = "common.txt"
    self.filename = "test.txt"
    self.twofile = "test2.txt"
  def runScan(self):
    scanning = pydirbuster.Pybuster(url=self.website, wordfile=self.wordlist, exts=self.ext,logfile=self.filename)
    scanning.Run()
  def ReadingLines(self):
    dirUrl = ''
    WriteToFile = open(self.twofile, "w")
    ReadFromFile = open(self.filename, "r")
    readlin = ReadFromFile.readlines()
    for lines in readlin:
      if "200" in lines:
        dirUrl = lines[0:-15]
        newurl= self.website + dirUrl
        print(newurl)
        webUrl = urllib.request.urlopen(newurl)
        data = webUrl.read()
        data = str(data)
        Comment = re.findall('<!--(.*?)-->', data)
        #I need to add a for loop to make it not a list.
        WriteToFile.write(str(Comment))
        WriteToFile.write("/n")
    WriteToFile.close()
    ReadFromFile.close()
test=web()
test.runScan()
test.ReadingLines()
