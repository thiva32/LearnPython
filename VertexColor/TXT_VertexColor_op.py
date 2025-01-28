import bpy

class PAINT_OT_BaseChannel(bpy.types.Operator):
    """Base Class for Vertex Color Paint Operators"""

    bl_options = {"REGISTER","UNDO"}
    color = (0,0,0) #DefaultVertexColor

    @classmethod
    def poll(cls, context):  
        """Ensure the object is a mesh in vertex paint mode"""
        return (context.object is not None and
                context.object.type == 'MESH' and
                context.object.mode == 'VERTEX_PAINT')

    def execute(self, context):
        context.scene.tool_settings.unified_paint_settings.color = self.color
        return {"FINISHED"}

class PAINT_OT_RedChannel(PAINT_OT_BaseChannel):
        """Paint into Red Channel"""
        bl_idname = "paint.red_channel"
        bl_label = "Red Channel"

        color = (1,0,0) #RedColor

class PAINT_OT_GreenChannel(PAINT_OT_BaseChannel):
        """Paint into Green Channel"""
        bl_idname = "paint.green_channel"
        bl_label = "Green Channel"

        color = (0,1,0) #GreenColor

class PAINT_OT_BlueChannel(PAINT_OT_BaseChannel):
        """Paint into Blue Channel"""
        bl_idname = "paint.blue_channel"
        bl_label = "Blue Channel"

        color = (0,0,1) #BlueColor
    


operators = [PAINT_OT_RedChannel,
             PAINT_OT_BlueChannel,
             PAINT_OT_GreenChannel]

def register():
    for operator in operators:
        bpy.utils.register_class(operator)

def unregister():
    for operator in operators:
        bpy.utils.unregister_class(operator)


