import requests

ocsURL = '''https://storage-den2.oraclecorp.com/auth/v1.0'''

ocsSrcDir = '''OCSDPTGT'''
ocsSrcFile = '''INSURANCE_TGT.txt'''

ocsTgtDir = '''OCSDPTGT'''
ocsTgtFile = '''OCS_FILE_USER_DATA.txt'''

ocsContainer = '''DIPC'''

ocsStorageURL = '''https://storage-den2.oraclecorp.com/v1/Storage-911cde94e9a749e380b658e7febb1c85/'''

ocsTargetFileURL = ocsStorageURL + '/' + ocsContainer + '/' + ocsTgtDir + '/' + ocsTgtFile
headers = {
	'X-Storage-User': 'Storage-911cde94e9a749e380b658e7febb1c85:basavaraja.allundi@oracle.com',
	'X-Storage-Pass': 'welcome1'
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

