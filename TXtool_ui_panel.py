import bpy
from bpy_types import Panel 

class TXTOOL_PT_main(Panel):

    bl_idname = "TXT_PT_main"
    bl_label = "TX Tools"
    bl_category = 'Txtool'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self,context):
        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
       
        row.label(text=" Version 0.1a ")

#Import panel from sub category

from .VertexColor import TXT_VertexColor_ui


panels = [TXTOOL_PT_main]

def register():
    
    for pnl in panels:
        bpy.utils.register_class(pnl)
        TXT_VertexColor_ui.register()


def unregister():
    for pnl in panels:
        bpy.utils.unregister_class(pnl)
        TXT_VertexColor_ui.unregister()

