import mailbox
import dateutil.parser
from datetime import datetime
import os
import re


mbox = mailbox.mbox('./Takeout/Mail/NIMBUS 2021 Reflections-not done.mbox')
path = os.getcwd()
print(path)
def extractattachements(message):
    if message.get_content_maintype() == 'multipart':
        for part in message.walk():
            if part.get_content_maintype() == 'multipart': continue
            if part.get('Content-Disposition') is None: continue
            fn = part.get_filename()
            frm = message['From']
            frm = re.sub(r"[^a-zA-Z0-9]+", ' ', frm)
            frm = frm.strip()
            if fn is None: fn = "untitled"
            #d = dateutil.parser.parse(message['Date'])
            #pre = d.strftime("%Y-%m-%d-%H-%M-%S")
            filename = fn
            
            if not os.path.exists('./data/'+frm+'/'):
                os.mkdir('./data/'+frm+'/')
            #fb = open(path+'\\data\\'+frm+'\\'+filename,'wb')
            while os.path.exists('./data/'+frm+'/'+filename):
                filename = filename+' new'
            print(filename)
            fb = open('./data/'+frm+'/'+filename,'wb')
            pl = part.get_payload(decode=True)
            if pl is None: break
            fb.write(pl)
            fb.close()

for message in mbox:
    extractattachements(message)
    #  pre + "--" + frm + "--" + 