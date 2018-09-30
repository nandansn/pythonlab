import requests

ocsURL = '''https://gse00003349.storage.oraclecloud.com/auth/v1.0'''

ocsSrcDir = '''OCSDPTGT'''
ocsSrcFile = '''INSURANCE_TGT.txt'''

ocsTgtDir = '''SRC_DIR'''
ocsTgtFile = '''test_data_usr_null_fill.txt'''

ocsContainer = '''DIPC_METADATA_EXPORT'''

ocsStorageURL = '''https://gse00003349.storage.oraclecloud.com/v1/Storage-gse00003349/'''

ocsTargetFileURL = ocsStorageURL + '/' + ocsContainer + '/' + ocsTgtDir + '/' + ocsTgtFile
headers = {
	'X-Storage-User': 'Storage-gse00003349:cloud.admin',
	'X-Storage-Pass': 'inbornFeature@4'
}

response = requests.get(ocsURL, headers=headers)
xAuthToken = response.headers.get('X-Auth-Token')
print(response.headers.get('X-Auth-Token'))

# get file list
xAuthTokenHeader = {
    'X-Auth-Token':xAuthToken
}

print("Token:",xAuthTokenHeader)
print("OCS File URL:",ocsTargetFileURL)
print('')
response = requests.get(ocsTargetFileURL, headers=xAuthTokenHeader)
print('File Content')
print(response.text)

