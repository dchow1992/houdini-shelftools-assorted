for n in hou.selectedNodes():
    if n.isGenericFlagSet(hou.nodeFlag.DisplayDescriptiveName):
        n.setGenericFlag(hou.nodeFlag.DisplayDescriptiveName, False)
    else:
        n.setGenericFlag(hou.nodeFlag.DisplayDescriptiveName, True)
