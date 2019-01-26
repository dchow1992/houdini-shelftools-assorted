import toolutils

current_node = toolutils.activePane(kwargs).currentNode()
if current_node:
    if current_node.type().category() == hou.sopNodeTypeCategory():
        if current_node.type() == hou.nodeType(hou.sopNodeTypeCategory(),"blast"):
            negate = current_node.parm("negate").eval()
            current_node = current_node.changeNodeType('split',keep_name=False,keep_network_contents=False,keep_parms=True)
            current_node.parm('negate').set(1-negate)
        elif current_node.type() == hou.nodeType(hou.sopNodeTypeCategory(),"split"):
            negate = current_node.parm("negate").eval()
            current_node = current_node.changeNodeType('blast',keep_name=False,keep_network_contents=False,keep_parms=True)
            current_node.parm('negate').set(1-negate)
