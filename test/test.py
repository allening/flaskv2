import requests

ClusterUrl = 'http://yun.oa.com/cgi-bin/apd_report/cdb_cluster.cgi'

def getClusterInfo(ClusterUrl):
    req = requests.get(ClusterUrl)
    return req.text

print getClusterInfo(ClusterUrl)