'''this will place a null in the network editor and then push 
the event context to activate the wire so it can be plugged in right away'''

p = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
pos = p.selectPosition()

a = p.pwd().createNode("null")
a.setPosition(pos)
a.setSelected(True)

data = {
        'connection':False,
        'inputitem':None,
        'inputindex':0,
        'outputitem':a,
        'outputindex':0,
        'branch':False,
        'nodetypename':None
        }

p.pushEventContext('nodegraphactivewire', data)
a.setInput(0, data['inputitem'], data['inputindex'])


