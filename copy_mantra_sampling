#copies sampling settings between rops, select src, and then any destination rops
def cpSampling():
    sel = hou.selectedNodes()
    if len(sel) == 0:
        hou.ui.displayMessage('no rops selected')
    else:
        src = sel[0]

        #renderingParmTemplates
        r = src.parmTemplateGroup().findFolder('Rendering').parmTemplates()
        folder_labels = ('Renderer, DOF, MB', 'Sampling', 'Limits', 'Shading', 'Render', 'Dicing', 'Statistics')
        label_indices = hou.ui.selectFromList(folder_labels, default_choices=(0,1,2), title='Tabs to Copy')
        valid_labels = []
        for i in label_indices:
            valid_labels.append(folder_labels[i])

        #for each rop
        for node in sel:
            if node == src:
                continue

            #for each parm template
            for t in r:
                pt_name = t.name()
                pt_type = t.type()
                pt_label = t.label()

                if pt_type == hou.parmTemplateType.Folder:
                    if pt_label in valid_labels:

                         #for each parmTemplate inside subfolder
                         for z in t.parmTemplates():
                            src_pt_tuple = hou.parmTuple(src.path() + '/' + z.name())

                            #for each index in the parm tuple
                            for x in src_pt_tuple:
                                src_p = hou.parm(src.path() + '/' + x.name())
                                cp_p = hou.parm(node.path() + '/' + x.name())
                                cp_p.set(src_p.eval())

                elif 'Renderer, DOF, MB' in valid_labels:
                    src_p = hou.parm(src.path() + '/' + pt_name)
                    cp_p = hou.parm(node.path() + '/' + pt_name)
                    cp_p.set(src_p.eval())

cpSampling()
