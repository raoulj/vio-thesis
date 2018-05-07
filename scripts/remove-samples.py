import rosbag
import sys

print(sys.argv)
counter = 0
with rosbag.Bag(sys.argv[2] , 'w') as outbag:
    for topic, msg, t in rosbag.Bag(sys.argv[1]).read_messages():
        if topic == "/imu0":
            if counter % 3 == 0:
                outbag.write(topic, msg)
            counter += 1
        else:
            outbag.write(topic, msg)
print('downsampled imu data in bag by 3')
