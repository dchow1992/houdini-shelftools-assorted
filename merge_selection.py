network_editor = kwargs['pane']
def mergeSel():
    x = hou.selectedNodes()    
    
    pos = network_editor.selectPosition()

    a = network_editor.pwd().createNode("merge")
    
    a.setPosition(pos)
    
    if(len(x) > 0):       
        for node in x:
            a.setNextInput(node)
        
    network_editor.setCurrentNode(a)
        
    a.setSelected(True, clear_all_selected=1)
        
mergeSel()
