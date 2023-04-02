import os
import requests

class DownloadManager:
    def __init__(self):
        self.download_list = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def add_download(self, url, filename):
        self.download_list.append({'url': url, 'filename': filename})

    def start_download(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

        for item in self.download_list:
            url = item['url']
            filename = item['filename']
            filepath = os.path.join(directory, filename)

            try:
                with requests.get(url, headers=self.headers, stream=True) as response:
                    response.raise_for_status()
                    with open(filepath, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                print(f"Downloaded {filename} from {url}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {filename} from {url}: {str(e)}")
