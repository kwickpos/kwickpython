# kwickpython
Direct print to local printers from web browsers

# Requirement
1. MS windows 
2. python and pywin32 required.

# Steps to run the agent
```
Open cmd console by Winkey-R, type "cmd" and Enter
Make KwickPython cgi-bin directory: C:\KwickPython\htbin
Save KwickPython script as: C:\KwickPython\htbin\kp.py
Start the KwickPython: C:\KwickPython>python -m http.server --cgi 9100
```

# AJAX inside your web page
```
Get List of Printers from the Local Client
	$.ajax({url:'http://127.0.0.1:9100/htbin/kp.py',
		success:function(list_printers){
			console.log(list_printers)
		}
	});
Check Printer *printer name required
	$.ajax({url:'http://127.0.0.1:9100/htbin/kp.py',
		data:{p:'printer_name'},
		success:function(status){
			console.log(status)
		}
	});
Printing *printer name & data required
	$.ajax({url:'http://127.0.0.1:9100/htbin/kp.py',
		data:{p:'printer_name',d:'base64_encoded_data'},
		success:function(bytes){
			console.log(bytes)
		}
	});
```
