import bpy


class CLEANUP_PT_MainPanel(bpy.types.Panel):
    """Tools to assist with mesh cleanup"""
    bl_idname = "CLEANUP_PT_MainPanel"
    bl_label = "Cleanup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Txtool'

    def draw(self, context):
        
        layout = self.layout
        layout.label(text="Cleanup Options")
    
        box = layout.box()

        row = box.row()
        row.prop(context.scene, "option_1",text="Freeze Transform")
        row.alignment = 'RIGHT'
        row.operator("scene.fix",icon = 'SEQUENCE_COLOR_05')

        row = box.row()
        row.prop(context.scene, "option_2",text="Check 2")
        row.alignment = 'RIGHT'
        row.operator("scene.fix",icon = 'SEQUENCE_COLOR_05')
        

        row = box.row()
        row.prop(context.scene, "option_3",text="Check 3")
        row.alignment = 'RIGHT'
        row.operator("scene.fix",icon = 'SEQUENCE_COLOR_05')

        layout.separator()
        layout.operator("scene.cleanup_validate",text="Validate")


panels = [CLEANUP_PT_MainPanel]

def register():
    for pnl in panels:
        bpy.utils.register_class(pnl)



def unregister():
    for pnl in panels:
        bpy.utils.unregister_class(pnl)


        