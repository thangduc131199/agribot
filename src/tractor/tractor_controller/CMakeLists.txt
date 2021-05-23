cmake_minimum_required(VERSION 3.0.2)
project(tractor_controller)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS
  angles
  controller_interface
  control_msgs
  control_toolbox
  forward_command_controller
  realtime_tools
  urdf
  pluginlib
)

include_directories(include ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})

# Declare catkin package
catkin_package(
  CATKIN_DEPENDS
    angles
    controller_interface
    control_msgs
    control_toolbox
    forward_command_controller
    realtime_tools
    urdf
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  )


add_library(joint_steer_controller_lib src/joint_steer_controller.cpp)
target_link_libraries(joint_steer_controller_lib ${catkin_LIBRARIES})
