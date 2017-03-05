#!/usr/bin/python
#
#bricked version of script used in https://www.youtube.com/watch?v=wH_pMrTdGzk
#
import urllib
import urllib2

def getInputs():
    cid = raw_input("Enter the course id -->")
    pid = raw_input("Enter the project id -->")
    content = raw_input("Enter the content to be added -->")
    session = raw_input("Enter the Session -->")
    return cid,pid,content,session

def setHeader():
	headers = {}
	headers["Accept-Language"] = "en-US,en;q=0.5"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Connection"] = "close"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["User-Agent"] = "Mozilla/5.0 ( Windows; Vista 64; rv:50.0) Firefox/50.0"
	headers["Host"] = "www.twenty19.com"
	headers["Cache-Control"] = "max-age=0"
	headers["Upgrade-Insecure-Requests"] = "1"
	headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
	return headers

def Main():

    cid, pid,content,session = getInputs()
    headers = setHeader()

    headers["Cookie"] = "PHPSESSID="+session


    data = urllib.urlencode({'project_detail_image_uploaded_path':'', 'project_id' : pid,'course_id' : cid, 'project_add_detail_description':content})
    req = urllib2.Request("http://www.twenty19.com/courses/add_project_detail", data, headers)
    req.get_method = lambda: "POST"
    req.set_proxy("127.0.0.1:8080","http")
    res = urllib2.urlopen(req)
    print res.geturl()
    if (res.geturl()[-4:] == 'edit' or res.geturl()[-len(pid):] == pid):
        print "Done"
    else:
        print "Try Again"
    #print res.read();#result from the server

if __name__ == '__main__':
	Main()

