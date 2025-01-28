import bpy
from bpy_types import Panel

class VTX_PT_main(Panel):

    bl_idname = "VTX_PT_vtxmain"
    bl_label = "Vertex Color"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Txtool'

    def draw(self, context):
        layout = self.layout

class VTX_PT_PaintChannel(Panel):
    
    bl_idname = "VTX_PT_paintchannel"
    bl_label = "Paint Channel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'VTX_PT_vtxmain'

    def draw(self, context):
        layout = self.layout

        layout.operator('paint.red_channel',text="Red Channel",icon='CUBE')
        
        
    
vtxpanels = [VTX_PT_main,VTX_PT_PaintChannel]

def register():
    for vtp in vtxpanels:
        bpy.utils.register_class(vtp)

def unregister():
    for vtp in vtxpanels:
        bpy.utils.register_class(vtp)

