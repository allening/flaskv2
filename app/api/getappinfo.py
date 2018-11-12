from flask import Blueprint,jsonify
import requests

getappinfo = Blueprint('getappinfo',__name__,url_prefix='/api')

ClusterUrl = 'http://yun.oa.com/cgi-bin/apd_report/cdb_cluster.cgi'

def getClusterInfo(ClusterUrl):
    req = requests.get(ClusterUrl)
    return req.text 

@getappinfo.route('/getappinfo',methods=['POST','GET'])
def getAppInfoFromCluster():

    return jsonify(getClusterInfo(ClusterUrl))
