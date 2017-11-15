from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
import os
import time

def equal(im1, im2):
  return ImageChops.difference(im1, im2).getbbox() is None

#width = 1288
#height = 725
#x_point = 269
#y_point = 123

# The new parameters are full screen mode in shwde7518 with Ctrl+above arrow
width = 1521
height = 854
x_point = 279
y_point = 105

print "-------------------------------------------------------------------------------"
current_path = os.getcwd()
print "The current path containing this python file is: " + current_path

#captured_folder_path = 'C:/Chong_dxxz_Projects/3D_Reconstruction/data/meeting_room_BUM06_5/Captured_Images'
captured_folder_path = current_path + os.sep + "Captured_Images" + os.sep + time.strftime( '%Y%m%d_%H%M%S' )
if os.path.exists( captured_folder_path ):
	print "The path of images capture folder with time stamp is: " + captured_folder_path
else:
	print "The images capture folder doesn't exist! I will create it now!"
	os.makedirs( captured_folder_path )
	print "The path of images capture folder with time stamp is: " + captured_folder_path
print "-------------------------------------------------------------------------------"

full_screen_image = ImageGrab.grab()
print 'Image size of full screen is: ' + str(full_screen_image.size)
print 'Image mode of full screen is: ' + str(full_screen_image.mode)
#full_screen_image.show()
full_screen_image.save(captured_folder_path + os.sep + 'Full_screen_image.jpg')

selected_region_image = ImageGrab.grab((x_point, y_point, x_point + width, y_point + height))
print 'Image size of selected region is: ' + str(selected_region_image.size)
print 'Image mode of selected region is: ' + str(selected_region_image.mode)
#selected_region_image.show()
selected_region_image.save(captured_folder_path + os.sep + 'Selected_region_image.jpg')

previous_image = selected_region_image
i = 0
#Total frame = 584
while i < 630:
	time.sleep(0.1)
	current_image = ImageGrab.grab((x_point, y_point, x_point + width, y_point + height))
	if equal(current_image, previous_image) == False:
		image_path_name = captured_folder_path + os.sep + 'captured_image_%d.jpg' % i
		#current_image.show()
		print 'Save the captured image to: ' + image_path_name
		current_image.save(image_path_name)
		previous_image = current_image
		i = i + 1