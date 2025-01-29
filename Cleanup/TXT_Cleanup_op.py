import bpy

class CleanupValidate(bpy.types.Operator):
    bl_idname = "scene.cleanup_validate"
    bl_label = "Validate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        checks = [
            ("option_1", "Check 1"),
            ("option_2", "Check 2"),
            ("option_3", "Check 3"),
        ]

        for option, label in checks:
            if getattr(context.scene, option):
                self.report({'INFO'}, f"{label} is enabled")

        return {'FINISHED'}

class IssueFix(bpy.types.Operator):
    bl_idname = "scene.fix"
    bl_label = "Fix"

    issue_option = bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        
        if self.issue_option == "option_1":
            self.report({'INFO'}, "Fixing Freeze Transform")
            # Add your freeze transform fix logic here

        elif self.issue_option == "option_2":
            self.report({'INFO'}, "Performing Check 2 Fix")
            # Add your check 2 fix logic here

        elif self.issue_option == "option_3":
            self.report({'INFO'}, "Performing Check 3 Fix")
            # Add your check 3 fix logic here

        return {'FINISHED'}
    

def option_1_func():
    print("Option 1 function called")

def option_2_func():
    print("Option 2 function called")

def option_3_func():
    print("Option 3 function called")

# List of operator classes to register
classes = [CleanupValidate,IssueFix]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)