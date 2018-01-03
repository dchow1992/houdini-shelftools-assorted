def OMSel():
    network_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    parm_view = hou.ui.paneTabOfType(hou.paneTabType.Parm)
    
    pos = network_editor.selectPosition()
    if(len(hou.selectedNodes()) > 0):
        x = hou.selectedNodes()[0]        
        
        a = network_editor.pwd().createNode("object_merge", "ref_"+x.name())        
        
        a.parm('objpath1').set(x.path())
        
    else:
        a = network_editor.pwd().createNode("object_merge")
        
    a.setPosition(pos)
    
    network_editor.setCurrentNode(a)
    
    a.setSelected(True, clear_all_selected=1)
        
OMSel()
