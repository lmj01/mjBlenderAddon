import bpy 
from bpy.types import Panel, Menu, UIList, PropertyGroup

class HelloWorld(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_idname = 'hello_world'
    bl_label = 'HelloWorld'

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()

        subcol = col.column()
        subcol.prop(view, 'lens', text='Foclal Length')
        subcol = col.column(align=True)
        subcol.prop(view, 'clip_start', text='Clip Near')
        subcol.prop(view, 'clip_end', text='Clip Far')

        layout.separator()

        col = layout.column(align=True)
        col.prop(view, 'use_render_border')

        layout.separator()

        layout.label(text='Hello, Panel')

        col = layout.column(align=True)
        # 路径对应的操作
        col.operator('object.simple_operator', text = 'Simple Operator')

        layout.separator()

class ImageEditorTool(Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_idname = 'hello_world'
    bl_label = 'HelloWorld'
