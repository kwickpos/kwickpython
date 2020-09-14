#KwickPython [FREE TO USE, NO WARRANTY]
#link back to https://kwickpos.com
import cgi,os,sys,win32print,pywintypes
print("Access-Control-Allow-Origin: *")
print("Content-Type: text/plain\n")
form = cgi.FieldStorage()
p=form.getvalue('p')
if p:
  data=form.getvalue('data')
  if data:
    import base64
    raw_data=base64.b64decode(data)
    if raw_data:
      h = win32print.OpenPrinter(p)
      hJob = win32print.StartDocPrinter (h, 1, ("KwickPOS Ticket", None, "RAW"))
      win32print.StartPagePrinter (h)
      b=win32print.WritePrinter (h, raw_data)
      win32print.EndPagePrinter (h)
      win32print.EndDocPrinter (h)
      win32print.ClosePrinter (h)
      print(b)
      sys.exit()
  else:
    try:
      h = win32print.OpenPrinter(p)
      d = win32print.GetPrinter(h,2)
      win32print.ClosePrinter (h)
      a = d['Attributes']
      hex=hex(a)
      if ( hex[-3] == '6' ):
        print(p+' Offline')
        sys.exit()
      s = d['Status']
      if ( s == 1 ):
        print(p+' Paused')
        sys.exit()
      print(p+' Ready')
    except pywintypes.error:
      print(p+' No Such Printer')
else:
  import json
  p={}
  lst = win32print.EnumPrinters(2)
  for f,d,n,c in lst:
    p[n]={}
    p[n]['d']=d
    p[n]['c']=c
  print(json.dumps(p))
