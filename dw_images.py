from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {'keywords': 'woman selfies with covid mask, man selfies with covid mask,man selfies, woman selfies',
             'limit':70,
             'output_directory':'C:\\Users\\Ale\\Documents\\Code\\Python\\ProjetoYOLO\\data',
             'chromedriver':'C:\\Users\\Ale\\Documents\\Code\\chromedriver'

            }

absolute_image_paths = response.download(arguments)