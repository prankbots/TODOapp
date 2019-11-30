import lineX
from lineX import *
from akad.ttypes import *
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
_session = requests.session()
botStart = time.time()
TODOapp = codecs.open("TODOapp.json","r","utf-8")
todo_start = json.load(TODOapp)
me = LINE("YOUR TOKEN")
oepoll = OEPoll(me)
meProfile = me.getProfile()
meSettings = me.getSettings()
# BATAS MID
meM = me.getProfile().mid
tz = pytz.timezone("Asia/Jakarta") #YOUR AREA
timeNow = datetime.now(tz=tz)
jam = "『 " + timeNow.strftime('%H:%M:%S') + " 』"
def bot(op):
  global threading
  try:
    if op.type == 0:
      return
    if op.type == 25 or op.type == 26:
      msg = op.message
      text = msg.text
      to = msg.to
      if text.lower() == "todo":
        data = {
          "type": "flex",
          "altText": "{} membagikan flex todoapp".format(meProfile.displayName),
          "contents": str(todo_start["todoapp"])
        }
        me.sendFlex(to,data)
      if text.lower() == "sp":
        start = time.time()
        me.sendMessage(to, "Testing..")
        sp = time.time() - start
        took = time.time() - start
        tek = time.time() - start
        me.sendMessage(to,"program: %.3fms\nrespon: %.8f" % (took,tek))
  except Exception as e:
    print(e)
    if op.type == 59:
      print(op)
while True:
  try:
    ops=oepoll.singleTrace(count=50)
    if ops != None:
      for op in ops: 
        bot(op)
        oepoll.setRevision(op.revision)
  except Exception as e:
    print(e)
