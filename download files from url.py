#Using wget
import wget
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


file_Path = 'research_Paper_3.pdf'
wget.download(url, file_Path)
print('downloaded')

#Using urllb.request
  import urllib.request
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


file_Path = 'research_Paper_2.pdf'
urllib.request.urlretrieve(url, file_Path)


#Using Requests
  import requests
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


response = requests.get(url)
file_Path = 'research_Paper_1.pdf'

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
else:
    print('Failed to download file')

