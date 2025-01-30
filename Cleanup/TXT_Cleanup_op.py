import bpy

# Global functions
def option_1_check_func(context):
    print("Option 1 check function called")
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

    # Add logic here
def option_1_fix_func(context):
    print("Option 1 fix function called")
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)



    # Add logic here

def option_2_check_func(context):
    print("Option 2 check function called")
    # Add logic here

def option_3_check_func(context):
    print("Option 3 check function called")
    # Add logic here

# Operators
class CleanupValidate(bpy.types.Operator):
    bl_idname = "scene.cleanup_validate"
    bl_label = "Validate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        checks = [
            ("option_1", "Check 1", option_1_check_func),
            ("option_2", "Check 2", option_2_check_func),
            ("option_3", "Check 3", option_3_check_func),
        ]

        for option, label, func in checks:
            if getattr(context.scene, option):
                self.report({'INFO'}, f"{label} is enabled")
                func(context)  # Call the corresponding function

        return {'FINISHED'}

class IssueFix(bpy.types.Operator):
    bl_idname = "scene.fix"
    bl_label = "Fix"

    issue_option = bpy.props.StringProperty()

    def execute(self, context):
        issue_fix_mapping = {
            "option_1": ("Fixing Freeze Transform", option_1_fix_func),
            "option_2": ("Performing Check 2 Fix", option_1_fix_func),
            "option_3": ("Performing Check 3 Fix", option_1_fix_func),
        }

        if self.issue_option in issue_fix_mapping:
            message, func = issue_fix_mapping[self.issue_option]
            self.report({'INFO'}, message)
            func(context)  # Call the corresponding function
        else:
            self.report({'ERROR'}, "Invalid issue option")

        return {'FINISHED'}
    


# Registration
classes = [CleanupValidate, IssueFix]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register scene properties
    bpy.types.Scene.option_1 = bpy.props.BoolProperty(name="Option 1", default=False)
    bpy.types.Scene.option_2 = bpy.props.BoolProperty(name="Option 2", default=False)
    bpy.types.Scene.option_3 = bpy.props.BoolProperty(name="Option 3", default=False)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    # Unregister scene properties
    del bpy.types.Scene.option_1
    del bpy.types.Scene.option_2
    del bpy.types.Scene.option_3

