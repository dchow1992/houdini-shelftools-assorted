#creates a bold text label in the network editor

network_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
n = network_editor.pwd()
pos = network_editor.selectPosition()

a = n.createStickyNote()
a.setSize(hou.Vector2(4.0,2.0))
a.setPosition(pos - hou.Vector2(1,1))
a.setText("label1")
a.setTextSize(0.35)
a.setTextColor(hou.Color(.65,.65,.85))
a.setDrawBackground(0)
