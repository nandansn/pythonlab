import requests

ocsURL = '''https://storage-den2.oraclecorp.com/auth/v1.0'''

ocsSrcDir = '''OCSDPTGT'''
ocsSrcFile = '''INSURANCE_TGT.txt'''

ocsTgtDir = '''OCSDPTGT'''
ocsTgtFile = '''OCS_OCS_TGT.txt'''

ocsContainer = '''DIPC'''

ocsStorageURL = '''https://storage-den2.oraclecorp.com/v1/Storage-bc2587c4d9fd43edbf020f0696e3f80e/'''

ocsTargetFileURL = ocsStorageURL + '/' + ocsContainer + '/' + ocsTgtDir + '/' + ocsTgtFile
headers = {
	'X-Storage-User': 'Storage-bc2587c4d9fd43edbf020f0696e3f80e:nandakumar.rangasamy@oracle.com',
	'X-Storage-Pass': 'dipcocs123'
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

