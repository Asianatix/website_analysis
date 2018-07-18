import Image
import argparse

def split(image_path):
    im=Image.open(image_path)
    w=im.size[0]
    h=im.size[1]

    if h == min(w,h):
    	print('You don\'t need to split your image.' )
    else:
    	subregion = list()
    	n_split = int(h/200)
    	ds = float(h)/n_split

    	for i in range(n_split):
    		hmin = int(ds*i)
    		hmax = int(ds*(i+1))

    		box = (0,hmin,w,hmax)
    		subregion.append(im.crop(box))

    	for num in range(len(subregion)):
    		subregion[num].save(str(num)+'.png',"PNG")
        print('The image is splitted successfully.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    split(args.image_file)