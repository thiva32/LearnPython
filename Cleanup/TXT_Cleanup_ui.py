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

        options = [
            ("option_1", "Freeze Transform"),
            ("option_2", "Check 2"),
            ("option_3", "Check 3")
        ]

        for option, label in options:
            row = box.row()
            row.prop(context.scene, option, text=label)
            row.alignment = 'RIGHT'
            row.operator("scene.fix",text="",icon='SEQUENCE_COLOR_05').issue_option = option

        layout.separator()
        layout.operator("scene.cleanup_validate", text="Validate")



panels = [CLEANUP_PT_MainPanel]

def register():
    for pnl in panels:
        bpy.utils.register_class(pnl)



def unregister():
    for pnl in panels:
        bpy.utils.unregister_class(pnl)


        