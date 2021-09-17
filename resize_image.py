from PIL import Image
import os
import PIL
import glob
import socketio

sio = socketio.Client()
sio.connect('https://api-koibid.diligentsoftinter.com')

path = 'images'

files = os.listdir(path)

@sio.on('postbid')
def on_message():
	for f in files:
		print(f)
		image = Image.open(path + '/' + f)
		if image.width < image.height:
			if image.width > 800:
				new_image = image.resize((int(image.width * 0.25), int(image.height * 0.25)))
				new_image.save('images/'+f)
				print(str(new_image.width) + ' ' + str(new_image.height))

		if image.width > image.height:
			if image.width > 800:
				new_image = image.resize((int(image.width * 0.25), int(image.height * 0.25)))
				new_image.save('images/' + f)
				print(str(new_image.width) + ' ' + str(new_image.height))





