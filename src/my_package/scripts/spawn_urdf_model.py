import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

rospy.init_node('spawn_urdf_model')

# Create a ROS service proxy for the spawn_urdf_model service
spawn_urdf_model = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)

# Read the URDF file content from a file
with open('/home/control.urdf', 'r') as f:
    urdf_file_content = f.read()

# Define the model name and initial pose
model_name = 'bot'
initial_pose = Pose()
initial_pose.position.x = 0.0
initial_pose.position.y = 0.0
initial_pose.position.z = 0.0
initial_pose.orientation.x = 0.0
initial_pose.orientation.y = 0.0
initial_pose.orientation.z = 0.0
initial_pose.orientation.w = 0.0

# Call the spawn_urdf_model service to spawn the URDF model
try:
    spawn_urdf_model(model_name, urdf_file_content, "", initial_pose)
    rospy.loginfo("URDF model spawned successfully!")
except rospy.ServiceException as e:
    rospy.logerr("Failed to spawn URDF model: %s", str(e))