import bpy, time, threading
from math import radians

#Camera -> Type of active data to display and edit: Data -> Focal Len: 35 change to 19
#Camera -> Type of active data to display and edit: Data -> Focal Len: 35 change to 17	Chong: find 17 can achieve better performance

#Load the trajectory info from the file.
pos = open('C:/Chong_dxxz_Projects/3D_Reconstruction/database/ZED/BUM_ROOM_1F06_MESH_FILES/meeting_room_BUM06_5/translation_5.txt').read().split('\n')
rot = open('C:/Chong_dxxz_Projects/3D_Reconstruction/database/ZED/BUM_ROOM_1F06_MESH_FILES/meeting_room_BUM06_5/rotation_5.txt').read().split('\n')

#Initialization
time_duration = 10						#Read from the file
camera_obj_initial_location_x = 0		#Read from the file
camera_obj_initial_location_y = 0		#Read from the file
camera_obj_initial_location_z = 0		#Read from the file
camera_obj_initial_roll = radians(0)	#Read from the file
camera_obj_initial_pitch = radians(0)	#Read from the file
camera_obj_initial_yaw = radians(0)	    #Read from the file

if(len(bpy.data.cameras) == 1):
    camera_obj = bpy.data.objects['Camera']
    camera_obj.location.x = camera_obj_initial_location_x
    camera_obj.location.y = camera_obj_initial_location_y
    camera_obj.location.z = camera_obj_initial_location_z
    camera_obj.rotation_euler = (camera_obj_initial_roll, camera_obj_initial_pitch, camera_obj_initial_yaw)

def fc(a):
    for i in range(len(pos)):
        if i == 0:
            time.sleep(5)	#for full screen operation when want to capture the images
        #time.sleep(0.1)
        time.sleep(1)		#should change to large value for capture the images
        p = pos[i].split()
        r = rot[i].split()
        #camera_obj.location.x = float(p[0])
        #camera_obj.location.y = float(p[1])
        #camera_obj.location.z = float(p[2])
        # cheat to keep the camera in the (0, 0, 0)
        camera_obj.location.x = float(0)
        camera_obj.location.y = float(0)
        camera_obj.location.z = float(0)
        # cheat to keep the camera not tilt due to noise
        #camera_obj.rotation_euler = (float(r[0]), float(r[1]), float(r[2]))
        camera_obj.rotation_euler = (float(0), float(r[1]), float(0))
        print(camera_obj.rotation_euler)

t=threading.Thread(target=fc, args=(10,))
t.start()