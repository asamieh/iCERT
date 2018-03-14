import datetime
import urllib2
import json
cookies = '_ga=GA1.2.175691132.1512419993; NSC_TJMJDFSUXFC_443_MC=ffffffff09391c2d45525d5f4f58455e445a4a423660; _gid=GA1.2.982517699.1520871066; CFID=2063323; CFTOKEN=80846660; _gat=1'
delay=69
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
def dol_scan(base):
    processed = False
    url = 'https://icert.doleta.gov/index.cfm?event=ehRegister.caseStatusSearchGridData&page=1&rows=100&sidx=&sord=asc&caseNumberList='
    base += 1
    url += day_part + str(format(base, '06'))
    for j in xrange(99):
        base += 1
        url += '|' + day_part + str(format(base, '06'))
    req = urllib2.Request(url)
    req.add_header('Cookie', cookies)
    req.add_header('Referer', 'https://icert.doleta.gov/index.cfm?event=ehRegister.caseStatusSearch')
    resp = urllib2.urlopen(req)
    content = resp.read()
    obj = json.loads(content)
    if obj['ROWS'] != "":
        for case in obj['ROWS']:
            if case[3] == (datetime.datetime.now() - datetime.timedelta(days=delay)).date().strftime('%m/%d/%Y'):
                print case
            else:
                print str(case) + ' ---- '
    return processed
print datetime.datetime.now()
while (datetime.datetime.now() - datetime.timedelta(days=delay)).weekday() >= 5:
    delay += 1
print datetime.timedelta(days=delay)
print str((datetime.datetime.now() - datetime.timedelta(days=delay)).date().strftime('%m/%d/%Y')) + ' ' + weekdays[(datetime.datetime.now() - datetime.timedelta(days=delay)).weekday()]
day_part = 'P-100-' + str((datetime.datetime.now() - datetime.timedelta(days=delay)).date().timetuple().tm_year)[2:]+str(format((datetime.datetime.now() - datetime.timedelta(days=delay)).date().timetuple().tm_yday, '03')) + '-'
print day_part
for i in xrange(0, 1000000, 100):
    dol_scan(i)
