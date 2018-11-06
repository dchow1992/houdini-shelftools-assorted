if len(hou.selectedNodes()):
    src = hou.selectedNodes()[0]
     
    root = src.parent()
     
    a = (src,)
    target = hou.copyNodesTo(a, root)[0]
     
    # nudge copy
    target.move(hou.Vector2(.5,-.5))
     
    src_parms = src.parmTuples()
     
    target_parms = target.parmTuples()
     
    for idx, p in enumerate(target_parms): # for each parmTuple
        for idx2, pp in enumerate(target_parms[idx]): # for each parm inside
            parm_path = src.path() + '/' + pp.name()
             
            pp.revertToAndRestorePermanentDefaults()
             
            pp.deleteAllKeyframes()
             
            if pp.parmTemplate().type() == hou.parmTemplateType.String:               
                pp.set('`chs("{x}")`'.format(x=parm_path))
            else:
                pp.setExpression('ch("{x}")'.format(x=parm_path))
             
    target.setSelected(True, clear_all_selected=1)
    target.setComment('Reference of ' + src.path())
    target.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    target.setColor(hou.Color((.525,.035,.215)))
