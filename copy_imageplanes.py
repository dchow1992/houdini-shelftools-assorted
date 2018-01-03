#copies imageplanes between rops and handles overlaps. select src rop then any destinations

def transferImagePlanes():
    sel = hou.selectedNodes()
    if len(sel) < 2:
        hou.ui.displayMessage('select at least 2 rops')
    else:
        src = sel[0]

        #extra image planes rop tab parm templates
        p = [a for a in src.parmTemplateGroup().findFolder('Images').parmTemplates() if a.label() == 'Extra Image Planes'][0].parmTemplates()

        #quickplane parms
        qpp = [a for a in p if 'quickplane' in a.name()]

        #src img plane parms
        ipp = src.parm('vm_numaux').parmTemplate().parmTemplates()

        #find if any dest rops have aovs
        existing_planes = 0
        for rop in sel[1:]:
            if rop.evalParm('vm_numaux') > 0:
                existing_planes = 1

        ############## startui #############

        #to do anything, need image planes on src rop
        if src.evalParm('vm_numaux') > 0:
            called_ui = 0
            behavior = 0
            srcdict = {}
            srcnamelist = []

            #key = image plane name, value = rop image plane indice, namelist = image plane names sorted by indices
            for i in range(1, src.evalParm('vm_numaux')+1):
                srcdict[src.evalParm('vm_variable_plane' + '{x}'.format(x=i))] = i
                srcnamelist.append(src.evalParm('vm_variable_plane' + '{x}'.format(x=i)))

            label = 'Some ROPS have existing image planes'
            buttons = ('Replace', 'Append and Merge (Priority: Existing)', 'Append and Merge (Priority: Source)')
            #ui_options = ['MODE: replace (image planes)', 'MODE: append new, replace duplicates (image planes)', 'Export Components', 'Quickplanes'] + srcnamelist
            ui_options = ['Export Components', 'Quickplanes'] + srcnamelist
            ui_sel = []

            #launch ui if any dest rops have existing planes
            if existing_planes == 1:
                called_ui = 1
                defaults = range(len(ui_options))
                behavior = hou.ui.displayMessage(label, buttons=buttons)
                ui_indices = hou.ui.selectFromList(ui_options, default_choices=tuple(defaults), message='Mode: ' + buttons[behavior], title='Selection')

                for i in ui_indices:
                    ui_sel.append(ui_options[i])

        ############# endui #############

            #do stuff
            if len(ui_sel) > 0 or existing_planes == 0:

                for rop in sel[1:]:

                    #export components
                    if ui_options[0] in ui_sel or existing_planes == 0:
                        rop.parm('vm_exportcomponents').set(src.evalParm('vm_exportcomponents'))

                    #quickplane parms
                    if ui_options[1] in ui_sel or existing_planes == 0:
                        for parm in qpp:
                            rop.parm(parm.name()).set(src.evalParm(parm.name()))

                    #img planes
                    #if any selected in the menu, or if the menu didn't get called
                    if len(list(set(ui_sel) & set(srcnamelist))) or called_ui == 0:
                        #init ropdict
                        ropdict = {}
                        for i in range(1, rop.evalParm('vm_numaux') + 1):
                            ropdict[rop.evalParm('vm_variable_plane' + '{x}'.format(x=i))] = i

                        #selected image planes
                        ss = [a for a in ui_sel if a in srcnamelist]

                        #replace mode,                      ###default mode if neither are selected###
                        if called_ui == 0 or behavior == 0:
                            print "replace mode"
                            print srcdict.keys()
                            ss = srcdict.keys()
                            rop.parm('vm_numaux').set(len(ss))

                            for aov in srcdict.keys():
                                idx = srcdict[aov]
                                for parm in ipp:
                                    rop.parm(parm.name().replace('#', '{x}'.format(x=ss.index(aov)+1))).set(src.evalParm(parm.name().replace('#', '{x}'.format(x=idx))))

                        else:
                            duplicates = list(set(ss) & set(ropdict.keys()))
                            new_ip = [a for a in ss if a not in duplicates]
                            current_ip_num = rop.evalParm('vm_numaux')
                            rop.parm('vm_numaux').set(current_ip_num + len(new_ip))
                            

                            #append new, give existing duplicates priority so don't do anything to them
                            if behavior == 1:
                                for aov in ss:
                                    idx = srcdict[aov]
                                    if aov not in duplicates:
                                        ropidx = current_ip_num + new_ip.index(aov) + 1
                                        for parm in ipp:
                                            rop.parm(parm.name().replace('#', '{x}'.format(x=ropidx))).set(src.evalParm(parm.name().replace('#', '{x}'.format(x=idx))))

                            #append and overwrite with source if duplicate image plane
                            elif behavior == 2:
                                #if duplicate, use rop image plane index as suffix, else append to bottom of list
                                for aov in ss:               
                                    idx = srcdict[aov]                     
                                    if aov in duplicates:
                                        ropidx = ropdict[aov]
                                        for parm in ipp:
                                            rop.parm(parm.name().replace('#', '{x}'.format(x=ropidx))).set(src.evalParm(parm.name().replace('#', '{x}'.format(x=idx))))
                                    else:
                                        ropidx = current_ip_num + new_ip.index(aov) + 1
                                        for parm in ipp:
                                            rop.parm(parm.name().replace('#', '{x}'.format(x=ropidx))).set(src.evalParm(parm.name().replace('#', '{x}'.format(x=idx))))

transferImagePlanes()
