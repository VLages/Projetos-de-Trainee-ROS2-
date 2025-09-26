import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vitor/Projetos-de-Trainee-ROS2-/install/publ_ass'
