.. ros:package:: sphinx_ros_example

###################################
The ``sphinx_ros_example`` package.
###################################

.. contents::
  :local:
  :depth: 1

The :ros:pkg:`sphinx_ros_example` package contains all sorts of ROS objects,
purely for example purposes. Objects can be referenced just like the familiar
default Sphinx references, e.g. :ros:msg:`sphinx_ros_example/Foo` will link
the proper message, and :ros:srv:`sphinx_ros_example/Bar` will link to the
proper service. We can also use the ``~`` to prevent displaying the package
name, e.g. :ros:msg:`~sphinx_ros_example/Foo` still points to the right
message.

The package can now include executables such as :ros:exe:`sphinx_ros_example/foo_bar_node`
and also launch files such as :ros:launch:`sphinx_ros_example/simple_launch.py`.

:Author: `J. Doe <j.doe@mail.com>`_

:Maintainer: `J. Doe <j.doe@mail.com>`_

:Links: * `Repository <http://github.com/user/repo>`_
        * `Bugtracker <http://github.com/user/repo/issues>`_

:Version: 1.2

:License: MIT


************
Dependencies
************

:Build: * :ros:pkg:`message_generation`
        * :ros:pkg:`std_msgs`

:Build export: :ros:pkg:`std_msgs`

:Build tool: :ros:pkg:`catkin`

:Execution: * :ros:pkg:`message_runtime`
            * :ros:pkg:`std_msgs`


********
Messages
********

.. ros:message:: Foo

  We can add descriptions to the message and its parameters.

  .. note:: We can also add notes to the message.

  :msg_param header: Header of the message.
  :msg_paramtype header: :ros:msg:`Header`
  :msg_param pose: The 3D pose of the foo that is detected.
  :msg_paramtype pose: :ros:msg:`geometry_msgs/Pose`
  :msg_param color: The color of the foo.
  :msg_paramtype color: :ros:msg:`string`


********
Services
********

.. ros:service:: Bar

  :req_param one_way: The request parameter.
  :req_paramtype one_way: :ros:msg:`sphinx_ros_example/Foo`
  :resp_param or_another: The response parameter.
  :resp_paramtype or_another: :ros:msg:`int8`
  :resp_param highway: The correct way.
  :resp_paramtype highway: :ros:msg:`uint16`


********
Actions
********

.. ros:action:: FooBar

  This is somehow similar to :ros:act:`nav2_msgs/NavigateToPose`.

  :goal_param setpoint: The setpoint to reach.
  :goal_paramtype setpoint: :ros:msg:`geometry_msgs/Point`
  :result_param steady_state_error: Error between achieved point and setpoint.
  :result_paramtype steady_state_error: :ros:msg:`geometry_msgs/Point`
  :feedback_param tracking_error: Error between ideal trajectory and current
                                  trajectory.
  :feedback_paramtype tracking_error: :ros:msg:`geometry_msgs/Point`
  :feedback_param power: Current power usage per joint.
  :feedback_paramtype power: :ros:msg:`float32[]`


***********
Executables
***********

.. ros:executable:: foo_bar_node

  This node is responsible for controlling the robot.

  :exe_param freq: Frequency.
  :exe_paramtype freq: `double`
  :exe_pub cmd_vel: The velocity command.
  :exe_pubtype cmd_vel: :ros:msg:`geometry_msgs/Twist`
  :exe_sub /odom: the odometry.
  :exe_subtype /odom: :ros:msg:`nav_msgs/Odometry`
  :exe_inaction /setpoint: Action server to set the setpoint.
  :exe_inactiontype /setpoint: :ros:act:`sphinx_ros_example/FooBar`

************
Launch files
************

.. ros:launch:: simple_launch.py

  This launchfile starts the robot.

  :launch_arg target_x: Target x coordinate.
  :launch_argtype target_x: `double`
  :launch_arg target_y: Target y coordinate.
  :launch_argtype target_y: `double`
  :launch_arg target_z: Target z coordinate.
  :launch_argtype target_z: `double`
  :launch_arg use_rviz: Whether to start RViz.
  :launch_argtype use_rviz: `bool`, default: ``False``

  :launch_exe foo_bar_node: The main node.
  :launch_exetype foo_bar_node: :ros:exe:`sphinx_ros_example/foo_bar_node`
  :launch_exe rviz2: A visualization of the robot (only if ``use_rviz:=True``).
  :launch_exe gz: Gazebo simulation (server mode).

