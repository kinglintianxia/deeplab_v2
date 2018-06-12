import numpy as np
from PIL import Image

import caffe
import vis

# the demo image is "2007_000129" from PASCAL VOC
list_file = '/home/king/Documents/image/tum3_seg/kf_timestmp.txt'
indexlist = [line.rstrip('\n') for line in open(list_file)]
print "indexlist: " + str(indexlist[0])


# load net
net = caffe.Net('/home/king/Documents/deeplab_v2/exper/nyu/config/deeplab_largeFOV/deploy.prototxt','/home/king/Documents/deeplab_v2/exper/nyu/model/deeplab_largeFOV/train_iter_20000.caffemodel',caffe.TEST)

for i, name in enumerate(indexlist):
	# load image, switch to BGR, subtract mean, and make dims C x H x W for Caffe
	im = Image.open('/home/king/Documents/image/rgbd_dataset_freiburg3_long_office_household/rgb/'+name+'.png')
	in_ = np.array(im, dtype=np.float32)
	in_ = in_[:,:,::-1]
	in_ -= np.array((104.00698793,116.66876762,122.67891434))	# subtract mean
	in_ = in_.transpose((2,0,1))

	# shape for input (data blob is N x C x H x W), set data
	net.blobs['data'].reshape(1, *in_.shape)
	net.blobs['data'].data[...] = in_
	# run net and take argmax for prediction
	net.forward()
	out = net.blobs['score'].data[0].argmax(axis=0)

	# visualize segmentation in PASCAL VOC colors
	voc_palette = vis.make_palette(459)
	out_im = Image.fromarray(vis.color_seg(out, voc_palette))
	out_im.save('/home/king/Documents/image/tum3_seg/rgb/' + name + '.png')
	# masked_im = Image.fromarray(vis.vis_seg(im, out, voc_palette))
	# masked_im.save('/home/king/Documents/image/tum3_seg/rgb/' + name + 'merge.png')
