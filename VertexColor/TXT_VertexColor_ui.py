import bpy


class PAINT_PT_MainPanel(bpy.types.Panel):

    bl_idname = "PAINT_PT_MainPanel"
    bl_label = "Vertex Color"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Txtool'

    def draw(self, context):
        """Draws the Main Vertex Color Panel"""
        layout = self.layout
        layout.label(text="Tools for Vertex Color Painting")

class PAINT_PT_PaintChannel(bpy.types.Panel):
    
    bl_idname = "PAINT_PT_PaintChannel"
    bl_label = "Paint Channels"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'PAINT_PT_MainPanel'

    def draw(self, context):
        """Draws The Channel Selection Panel"""
        layout = self.layout

        row = layout.row()
        row.operator('paint.red_channel',text="Red",icon='SEQUENCE_COLOR_01')
        row.operator('paint.green_channel',text="Green",icon='SEQUENCE_COLOR_04')
        row.operator('paint.blue_channel',text="Blue",icon='SEQUENCE_COLOR_05')
        
        
    
vtxpanels = [PAINT_PT_MainPanel,PAINT_PT_PaintChannel]

def register():
    for vtp in vtxpanels:
        bpy.utils.register_class(vtp)

def unregister():
    for vtp in vtxpanels:
        bpy.utils.register_class(vtp)

