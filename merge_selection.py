def mergeSel():
    x = hou.selectedNodes()
    
    if(len(x) > 0):
    
        network_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)   
        
        pos = network_editor.selectPosition()
        
        a = network_editor.pwd().createNode("merge")
        
        a.setPosition(pos)
        
        for node in x:
            a.setNextInput(node)
        
        network_editor.setCurrentNode(a)
        
        a.setSelected(True, clear_all_selected=1)
        
mergeSel()
