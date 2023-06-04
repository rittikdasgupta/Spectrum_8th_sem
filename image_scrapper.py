import requests
import os
import sys


if len(sys.argv) < 2:
    print('Please provide an argument.')
else:
    obj = sys.argv[1]
    print(f'The argument you provided is: {obj}')

    # define the API endpoint and parameters
    api_endpoint = 'https://serpapi.com/search'
    params = {
        'engine': 'google',
        'q': obj,
        'tbm': 'isch',
        'ijn': '0',
        'api_key': 'd487e4a21432f8a47981599b1c1ccb9b4f28a109a52a9ba9f848be67d42b6127'
    }

    # make the API request and parse the response JSON
    response = requests.get(api_endpoint, params=params).json()

    # download the first 10 images to a directory called "stairs_images"
    os.makedirs(f'{obj}_images', exist_ok=True)
    for i in range(10):
        img_url = response['images_results'][i]['original']
        img_name = f'{obj}_{i}.jpg'
        img_path = os.path.join(f'{obj}_images', img_name)
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as f:
            f.write(img_data)
            print(f'Saved image {img_path}')
