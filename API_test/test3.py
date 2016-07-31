import requests

s = requests.session()
r = s.get("https://sso.youshang.com/loginServlet?entityId=assistant&assertHashType=3&needAuth=N&RelayState=http%3A%2F%2Fwww.youshang.com%2Fsso%2Fhandle.php&isYSLogin=1&name=kingdeetest_jinghui&password=kingdee331&authCode=")
id = s.get("http://vip2.youshang.com/default.jsp?dbid=79409803918")
data = s.get("http://vip2.youshang.com/basedata/invlocation.do?action=list&isDelete=2&_search=false&nd=1468567380270&rows=100&page=1&sidx=&sord=asc")

print r.text
print id.text
print data.text