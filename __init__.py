bl_info = {
    "name": "Meijie Addon",
    "author": "meijie",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Tool Shelf > Meijie Panel",
    "description": "use meijie test",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

import bpy
from .ui import panel
from .operators import example

classes = (
    panel.HelloWorld,
    example.SimpleOperator,
)

# register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(example.menu_func)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_object.remove(example.menu_func)

if __name__ == "__main__":
    register()

    # bpy.ops.object.simple_operator()