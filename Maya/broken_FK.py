import maya.cmds as cmds

# Make viewport selection, Parent control(s), and then child control(s)

# Get selection, assuming the first is the parent control and the rest are child controls
sels = cmds.ls(sl=True)  # [parent control, child controls...]
parent_ctrl = sels[0]
child_ctrls = sels[1:]  # All remaining selections are child controls

# Iterate over each child control
for child_ctrl in child_ctrls:
    # Get the parent group of the child control
    child_ctrl_grp = cmds.listRelatives(child_ctrl, parent=True)[0]  # [child control's parent node]

    # Create constraints
    p_constraint1 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipRotate=['x', 'y', 'z'], weight=1)[
        0]  # constrain translate
    p_constraint2 = \
    cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipTranslate=['x', 'y', 'z'], weight=1)[
        0]  # constrain rotate
    s_constraint = cmds.scaleConstraint(parent_ctrl, child_ctrl_grp, mo=True, weight=1)[0]  # constrain scale

    # Create attributes on the child control
    cmds.addAttr(child_ctrl, ln='FollowTranslate', at='double', min=0, max=1, dv=1)
    cmds.setAttr('%s.FollowTranslate' % (child_ctrl), e=True, keyable=True)

    cmds.addAttr(child_ctrl, ln='FollowRotate', at='double', min=0, max=1, dv=1)
    cmds.setAttr('%s.FollowRotate' % (child_ctrl), e=True, keyable=True)

    # Connect attributes from child control to constraint weights
    cmds.connectAttr('%s.FollowTranslate' % (child_ctrl), '%s.%sW0' % (p_constraint1, parent_ctrl), f=True)
    cmds.connectAttr('%s.FollowRotate' % (child_ctrl), '%s.%sW0' % (p_constraint2, parent_ctrl), f=True)
