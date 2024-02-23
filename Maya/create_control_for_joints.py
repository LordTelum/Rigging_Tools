import maya.cmds as cmds


def create_control_for_joints(joint_names):
    for joint_name in joint_names:
        # Create a NURBS circle control at the joint's position
        control_name = joint_name + "_ctrl"
        control = cmds.circle(n=control_name, nr=(0, 1, 0))[0]  # nr specifies the normal direction for the circle

        # Get the joint's position
        position = cmds.xform(joint_name, q=True, ws=True, t=True)

        # Create an empty group at the joint's position
        group_name = joint_name + "_grp"
        group = cmds.group(em=True, n=group_name)

        # Move the group to the joint's position
        cmds.xform(group, ws=True, t=position)

        # Parent the control under the group
        cmds.parent(control, group)

        # match the joint's orientation to the control
        cmds.xform(control, ws=True, t=position)


# Get all selected joints in the scene
selected_joints = cmds.ls(sl=True, type='joint')
create_control_for_joints(selected_joints)
