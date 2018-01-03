#clones a node with abs references, this one isn't perfect, but I haven't had the time to go in and fix it up
def absCopy():
    sel = hou.selectedNodes()
    if len(sel) == 0:
        hou.ui.displayMessage('no node selected')
    else:
        root = hou.node(sel[0].parent().path())
        final_sel = []
        for c in sel:
            x = (c,)
            copy = hou.copyNodesTo(x, root)[0]

            #nudge copy
            nudge = hou.Vector2(.5,-.5)
            copy.move(nudge)

            #make abs references
            ref_parms = c.parmTuples()
            c_parms = copy.parmTuples()

            #for each parm tuple
            for p in range(len(ref_parms)):
                ptype = ref_parms[p].parmTemplate().type()

                #for each index of the tuple
                if ptype == hou.parmTemplateType.String:
                    for i in range(len(ref_parms[p])):
                        c_parms[p][i].setExpression('chs("' + ref_parms[p][i].path() + '")')
                else:
                    for i in range(len(ref_parms[p])):
                        c_parms[p][i].setExpression('ch("' + ref_parms[p][i].path() + '")')

            #add to final_sel
            final_sel.append(copy)

            #add comment
            copy.setComment('Referenced from ' + c.path())
            copy.setGenericFlag(hou.nodeFlag.DisplayComment, True)

            #set color
            copy.setColor(hou.Color((.45,.15,.45)))

        #select final_sel
        for node in final_sel:
            node.setSelected(True)           

absCopy()
