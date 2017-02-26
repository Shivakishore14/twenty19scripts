#!/usr/bin/python
import urllib
import urllib2
import StringIO
import gzip

def getInputs():
	cid = raw_input("Enter the course id -->")
	strt = input("Enter the start vid no -->")
	end = input("Enter the end vid no -->")
	session = raw_input("Enter the Session -->")
	return cid,strt,end,session

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

	cid, strt, end, session = getInputs()
	headers = setHeader()

	headers["Cookie"] = "PHPSESSID="+session

	for i in range(strt, end+1):

		i1 = i if i > strt else strt
		headers['Referer'] = 'http://www.twenty19.com/courses/fetch/'+cid+'/'+str(i1-1) #just to make sure everything looks normal

		data = urllib.urlencode({'id' : str(i),'course_id'  : cid})
		req = urllib2.Request("http://www.twenty19.com/courses/track_progress", data, headers)
		req.get_method = lambda: "POST"
		res = urllib2.urlopen(req)

		buf = StringIO.StringIO(res.read())
		gzip_f = gzip.GzipFile(fileobj=buf)
		content = gzip_f.read()
		print content


if __name__ == '__main__':
	Main()
