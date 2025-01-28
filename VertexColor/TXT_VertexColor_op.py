import bpy


class PAINT_OT_RedChannel(bpy.types.Operator):
    """Paint into Red Channel of Vertex Color"""
    bl_idname = "paint.red_channel"
    bl_label = "Red Channel"
    bl_description = "Paint into Red Channel of Vertex Color"
    bl_options = {"REGISTER","UNDO"}

    color = (0,0,0) #Default Vertex Color

    @classmethod
    def poll(cls, context):  
        """Ensure the object is a mesh in vertex paint mode"""
        return (context.object is not None and
                context.object.type == 'MESH' and
                context.object.mode == 'VERTEX_PAINT')

    def execute(self, context):
        context.scene.tool_settings.unified_paint_settings.color = self.color
        return {"FINISHED"}


operators = [PAINT_OT_RedChannel]

def register():
    for operator in operators:
        bpy.utils.register_class(operator)

def unregister():
    for operator in operators:
        bpy.utils.unregister_class(operator)


