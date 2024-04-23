import maya.cmds as cmds


def create_controls_for_joints():
    # Get the currently selected joints
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.warning("Please select at least one joint.")
        return

    for joint in selected_joints:
        # Determine the base name by stripping "_Jnt" or similar suffix if exists
        base_name = joint.rsplit('_', 1)[0] if '_' in joint else joint

        # Create a NURBS circle
        control_name = base_name + '_Ctrl'
        group_name = base_name + '_Ctrl_Grp'
        control = cmds.circle(name=control_name, normal=[0, 1, 0], radius=1.0)[0]

        # Group the control
        group = cmds.group(control, name=group_name)

        # Match the group's transformation to the joint
        cmds.delete(cmds.parentConstraint(joint, group))
        cmds.delete(cmds.scaleConstraint(joint, group))

        # Rename the group and control to match the new naming convention
        cmds.rename(group, group_name)
        cmds.rename(control, control_name)

        # Print control and group names for confirmation
        print("Created Control: {}, Group: {}".format(control, group))


# Run the function
create_controls_for_joints()
