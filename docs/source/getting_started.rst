###############
Getting started
###############

.. contents::
  :local:

=============
Configuration
=============

.. confval:: ros_msg_reference_version

  The used |ROS| version to use when referencing to default message types, e.g.
  ``'jazzy'`` or ``'kilted'``. It defaults to ``'jazzy'`` and is set to
  ``'jazzy'`` for this documentation.

.. confval:: ros_add_package_names

  Can be set to ``False`` to prevent package names from showing in message,
  service, or action type descriptions. Defaults to ``True``.


==========
Directives
==========

.. rst:directive:: .. ros:package:: package

  Similar to the Python domain's ``.. py:module::`` directive. It will not
  output any nodes, but serves to set the context's |ROS| package and will
  produce a hyperlink target and an index entry for ``package``. Defined
  packages can be referenced with ``:ros:pkg:`package```.

  :Options: * **noindex** -- Prevents adding the package to the index,
              basically turns this directive into
              :rst:dir:`ros:currentpackage`.
            * **deprecated** -- Flags this package as deprecated. This wil
              show up in the index.


.. rst:directive:: .. ros:currentpackage:: package

  Similar to the Python domain's ``.. py:currentmodule::`` directive. It will
  not produce any nodes nor an index entry but will set the context's |ROS|
  package such that Sphinx knows that we are documenting stuff in that package.

  This directive has no options.

.. rst:directive:: .. ros:message:: message

  Can be used to describe a message type definition. It will create an index entry and a hyperlink target for this message type. It will also output nodes to describe the message.

  :options: * **noindex** -- Prevents adding the message to the index and
              creating a hyperlink target node.
            * **deprecated** -- Flags this message as deprecated. This wil show
              up in the index.

  Message fields are described using the a pair of flags:
  
  - ``:msg_param <name>: <description>`` defines a parameter that is contained in the message, 
  - ``:msg_paramtype <name>: <type>`` defines the same parameter's type.
  
  All parameters will be grouped in a list. Each parameter will be listed with its type and description.
  typically formated as:

  **<name> (<type>)**: <description>

.. rst:directive:: .. ros:service:: service

  Can be used to describe a service type definition. It will create a hyperlink
  target for the service type. It will also output nodes to describe the
  service.

  :options: * **noindex** -- Prevents creating a hyperlink target node for the
              service.
            * **deprecated** -- Flags this service as deprecated.

  Request fields are described using the flags ``:req_param <name>:`` and ``:req_paramtype <name>:``.

  Response fields are described using the flags ``:resp_param <name>:`` and ``:resp_paramtype <name>:``.

.. rst:directive:: .. ros:action:: action

  Can be used to describe a action type definition. It will create a hyperlink
  target for the action type. It will also output nodes to describe the
  action.

  :options: * **noindex** -- Prevents creating a hyperlink target node for the
              action.
            * **deprecated** -- Flags this action as deprecated.
  
  Goal fields are described using the flags ``:goal_param <name>:`` and ``:goal_paramtype <name>:``.

  Result fields are described using the flags ``:result_param <name>:`` and ``:result_paramtype <name>:``.
  
  Feedback fields are described using the flags ``:feedback_param <name>:`` and ``:feedback_paramtype <name>:``.


.. rst:directive:: .. ros:executable:: executable

  Can be used to describe an executable, typically a script or a node. It will
  create a hyperlink target for the executable. It will also output nodes to
  describe the executable.

  Parameters can be added to the executable using the following flags: ``:exe_param <name>:`` and ``:exe_paramtype <name>:``. They will be listed as "Parameters" in the output.

  Input interfaces can be added to the executable using the following flags: 
  
  * ``:exe_sub <name>:`` and ``:exe_subtype <name>:``
  * ``:exe_inmsg <name>:`` and ``:exe_inmsgtype <name>:``
  * ``:exe_insrv <name>:`` and ``:exe_insrvtype <name>:``
  * ``:exe_inact <name>:`` and ``:exe_inacttype <name>:``
  * ``:exe_inaction <name>:`` and ``:exe_inactiontype <name>:``

  All of these will be listed as "Input Interfaces" in the output.

  Similarely for the output interfaces.

.. rst:directive:: .. ros:launch:: launch_file

  Can be used to describe a launch file. It will create a hyperlink target for
  the launch file. It will also output nodes to describe the launch file.

  Launch arguments can be added to the launch file using the following flags: ``:launch_arg <name>:`` and ``:launch_argtype <name>:``. They will be listed as "Launch arguments" in the output.

  Launched nodes and script can be added to the launch file using the following flags: ``:launch_exe <name>:`` and ``:launch_exe <name>:``. They will be listed as "Launched executables" in the output.


=====
Roles
=====

.. rst:role:: ros:pkg

  Can be used to reference a defined package.

.. rst:role:: ros:msg

  Can be used to reference a defined message type. Adding the ``~`` prefix to
  the message name will let it print *only* the message name and not the
  package name. First it is checked if the message is one of the |ROS|
  primitive message types (**bool**, **int8**, **uint8**, **int16**,
  **uint16**, **int32**, **uint32**, **int64**, **uint64**, **float32**,
  **float64**, **string**, **time**, **duration**). If so, it will not link
  anywhere. If it is of the type **Header** or it is a message in one of the
  default |ROS| message packages, it will link to the proper documentation,
  keeping into account the |ROS| version set by
  :confval:`ros_msg_reference_version`.

  The default |ROS| message packages that are correctly handled as of now are:
  **std_msgs**, **geometry_msgs**, and **sensor_msgs**.

.. rst:role:: ros:srv

  Can be used to reference a defined service type. Adding the ``~`` prefix to
  the service name will let it print *only* the service name and not the
  package name.

.. rst:role:: ros:act

  Can be used to reference a defined action type. Adding the ``~`` prefix to
  the action name will let it print *only* the action name and not the package
  name.

.. rst:role:: ros:exe

  Can be used to reference an executable. Adding the ``~`` prefix to the
  executable name will let it print *only* the executable name and not the
  package name.

.. rst:role:: ros:launch

  Can be used to reference a launch file. Adding the ``~`` prefix to the launch
  file name will let it print *only* the launch file name and not the package
  name.

===============
Package example
===============

.. toctree::
  :maxdepth: 1

  getting_started/full_document_example

.. literalinclude:: getting_started/full_document_example.rst
  :caption: Source
  :language: restructuredtext


=======
Indices
=======

These indices are generated by this Sphinx extension. They are autogenerated
and can be referenced with ``:ref:`ros-pkgindex``` and ``:ref:`ros-msgindex```
respectively.

* :ref:`ros-pkgindex`
* :ref:`ros-msgindex`
