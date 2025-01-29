import bpy

class Cleanup_Property(bpy.types.PropertyGroup):
        
        value = bpy.props.BoolProperty(name="value", default=False)


# List of operator classes to register
classes = [Cleanup_Property]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.option_1 = bpy.props.BoolProperty(name="Option 1",default=False)
    bpy.types.Scene.option_2 = bpy.props.BoolProperty(name="Option 2",default=False)
    bpy.types.Scene.option_3 = bpy.props.BoolProperty(name="Option 3",default=False)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.option_1
    del bpy.types.Scene.option_2  
    del bpy.types.Scene.option_3
