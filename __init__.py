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

classes = (
    panel.HelloWorld,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
