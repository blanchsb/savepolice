# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "SavePolice",
    "author" : "blanchsb", 
    "description" : "Call upon the save police to serve and protect your work",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 9),
    "location" : "Tool Panel",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "System" 
}


import bpy
import bpy.utils.previews
import blf
import os
import gpu
import gpu_extras
import mathutils
import atexit
from bpy.app.handlers import persistent


addon_keymaps = {}
_icons = None
g_draw_alert_image_3d_view = {'sna_frame': 0, 'sna_stop': False, 'sna_custom_frame_length': 0, }
g_draw_alert_image_image_editor = {'sna_frame': 0, 'sna_custom_frame_length': 0, 'sna_stop': False, }
g_draw_alert_image_node_editor = {'sna_frame': 0, 'sna_custom_frame_length': 0, 'sna_stop': False, }
g_draw_alert_image_vse_editor = {'sna_frame': 0, 'sna_custom_frame_length': 0, 'sna_stop': False, }
graph_debug_testing = {'sna_debug_count': 0, 'sna_var_run_in_intervals': False, }
graph_scripts = {'sna_minutes': 0.0, 'sna_animation_minutes': 0, 'sna_timer_freq': 60.0, 'sna_timer_interval': 10, 'sna_timer_sec': 1, 'sna_time_remaining': 0.0, 'sna_time_message': '(Time)', }
handler_5FE5D = []
handler_D8705 = []
handler_AAAFB = []


def find_areas_of_type(screen, area_type):
    areas = []
    for area in screen.areas:
        if area.type == area_type:
            areas.append(area)
    return areas


def find_biggest_area_by_type(screen, area_type):
    areas = find_areas_of_type(screen, area_type)
    if not areas: return []
    max_area = (areas[0], areas[0].width * areas[0].height)
    for area in areas:
        if area.width * area.height > max_area[1]:
            max_area = (area, area.width * area.height)
    return max_area[0]


handler_CB41D = []
handler_EE591 = []
handler_A1E89 = []
handler_0A529 = []
handler_F57E6 = []


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


handler_64666 = []


def sna_update_sna_call_the_save_police_8EE76(self, context):
    sna_updated_prop = self.sna_call_the_save_police
    bpy.context.scene.sna_save_police_interval = bpy.context.preferences.addons['savepolice'].preferences.sna_interval
    if sna_updated_prop:
        if (bpy.context.preferences.addons['savepolice'].preferences.sna_save_default_file and (not os.path.exists(bpy.data.filepath)) and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_default_folder)):
            bpy.ops.sna.op_save_police_saving_148e8('INVOKE_DEFAULT', )
        sna_fn_start_stop_save_police_timer_34567(True)
        if bpy.context.scene.sna_save_police_countdown_active:
            pass
        else:
            bpy.ops.sna.save_police_preview_countdown_8b9f0('INVOKE_DEFAULT', )
        if bpy.context.preferences.addons['savepolice'].preferences.sna_update_screen_areas:

            def delayed_C2CC4():
                if bpy.context and bpy.context.screen:
                    for a in bpy.context.screen.areas:
                        a.tag_redraw()
                if (not bpy.context.preferences.addons['savepolice'].preferences.sna_update_screen_areas):
                    return None
                return 1.0
            bpy.app.timers.register(delayed_C2CC4, first_interval=0.0)
    else:
        bpy.context.scene.sna_save_police_reminder = False
        sna_fn_start_stop_save_police_timer_34567(False)
        bpy.ops.sna.save_police_end_alert_image_preview_7a41b('INVOKE_DEFAULT', )
        bpy.ops.sna.save_police_end_countdown_preview_8f673('INVOKE_DEFAULT', )


def sna_update_sna_annoyance_only_1467F(self, context):
    sna_updated_prop = self.sna_annoyance_only
    if sna_updated_prop:
        pass
    else:
        bpy.context.scene.sna_save_police_reminder = False
        bpy.ops.sna.op_annoy_restore_theme_colors_954ce('INVOKE_DEFAULT', )
    if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police:
        sna_fn_start_stop_save_police_timer_34567(True)


def sna_update_sna_change_theme_993B2(self, context):
    sna_updated_prop = self.sna_change_theme
    if sna_updated_prop:
        if (bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police and (not bpy.context.scene.sna_save_police_theme_active) and bpy.context.scene.sna_save_police_reminder):
            bpy.ops.sna.op_annoy_store_and_swap_theme_colors_c1b7f('INVOKE_DEFAULT', )
    else:
        bpy.ops.sna.op_annoy_restore_theme_colors_954ce('INVOKE_DEFAULT', )


def sna_update_sna_interval_CA391(self, context):
    sna_updated_prop = self.sna_interval
    bpy.context.scene.sna_save_police_interval = sna_updated_prop


def sna_update_sna_save_police_reminder_9D6ED(self, context):
    sna_updated_prop = self.sna_save_police_reminder
    if sna_updated_prop:
        if bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only:
            sna_fn_start_stop_save_police_timer_34567(False)
            if bpy.context.scene.sna_save_police_animation_active:
                pass
            else:
                bpy.ops.sna.save_police_preview_alert_image_558a3('INVOKE_DEFAULT', )
        else:
            if (bpy.data.is_dirty and bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police):
                bpy.ops.sna.op_save_police_saving_148e8('INVOKE_DEFAULT', )
        if bpy.context.scene.sna_save_police_countdown_active:
            bpy.ops.sna.save_police_end_countdown_preview_8f673('INVOKE_DEFAULT', )
    else:
        if bpy.context.scene.sna_save_police_annoy_active:
            bpy.context.scene.sna_save_police_annoy_active = False
            if bpy.context.preferences.addons['savepolice'].preferences.sna_change_theme:
                bpy.ops.sna.op_annoy_restore_theme_colors_954ce('INVOKE_DEFAULT', )


def sna_update_sna_save_police_interval_8D7BA(self, context):
    sna_updated_prop = self.sna_save_police_interval


def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id


def sna_fn_modal_drawing_2699F():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_message:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_F0888, y_F0888 = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location
            blf.position(font_id, x_F0888, y_F0888, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message)
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)
    if bool(find_areas_of_type(bpy.context.screen, 'VIEW_3D')):
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_background:
            if (os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background)) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_custom_background):
                coords = (  ((1.0, 1.0)[0], (1.0, 1.0)[1])   , ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').width,(1.0, 1.0)[1])  ,  ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').width, (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').height)  ,   ((1.0, 1.0)[0], (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').height)   )
                bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background), check_existing=True, )

                def get_img_name():
                    this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background))
                    for i in range(len(bpy.data.images)):
                        if bpy.data.images[i].name == bpy.data.images[this].name:
                            return bpy.data.images[i]
                texture = gpu.texture.from_image(get_img_name())
                blender_version = bpy.app.version
                if blender_version >= (4, 0, 0):
                    shader = gpu.shader.from_builtin('IMAGE')
                else: 
                    shader = gpu.shader.from_builtin('2D_IMAGE')
                batch = gpu_extras.batch.batch_for_shader(
                    shader, 'TRI_FAN',
                    {
                        "pos": coords,
                        "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                    },
                )
                shader.bind()
                gpu.state.blend_set('ALPHA')
                shader.uniform_sampler("image", texture)
                batch.draw(shader)
            else:
                quads = [[tuple((1.0, 1.0)), tuple((find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').width, 1.0)), tuple((1.0, find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').height)), tuple((find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').width, find_biggest_area_by_type(bpy.context.screen, 'VIEW_3D').height))]]
                vertices = []
                indices = []
                for i_7A2A5, quad in enumerate(quads):
                    vertices.extend(quad)
                    indices.extend([(i_7A2A5 * 4, i_7A2A5 * 4 + 1, i_7A2A5 * 4 + 2), (i_7A2A5 * 4 + 2, i_7A2A5 * 4 + 1, i_7A2A5 * 4 + 3)])
                shader = gpu.shader.from_builtin('UNIFORM_COLOR')
                batch = gpu_extras.batch.batch_for_shader(shader, 'TRIS', {"pos": tuple(vertices)}, indices=tuple(indices))
                shader.bind()
                shader.uniform_float("color", bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background_color)
                gpu.state.blend_set('ALPHA')
                batch.draw(shader)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_image:
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                        directory = bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)

                        def get_sequence_length(directory):
                            if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                                return 0
                            try:
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                return min(len(files), 101)
                            except Exception as e:
                                print(f"An error occurred while getting the sequence length: {e}")
                                return 0
                        if directory:
                            sequence_length = get_sequence_length(directory)
                            start_frame_value = g_draw_alert_image_3d_view['sna_frame']
                            start_frame = max(0, min(100, start_frame_value))
                            end_frame_value = g_draw_alert_image_3d_view['sna_custom_frame_length']
                            end_frame = max(0, min(100, end_frame_value))
                            start_frame = min(start_frame, end_frame)
                            bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                            coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                            def get_image_from_directory(dial_value, directory):
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                files.sort()
                                sequence_length = min(get_sequence_length(directory), 101)
                                if 0 <= dial_value < sequence_length:
                                    image_path = os.path.join(directory, files[dial_value])
                                    bpy.data.images.load(filepath=image_path, check_existing=True)
                                    return bpy.data.images[os.path.basename(image_path)]
                                else:
                                    return None
                            dial_value = g_draw_alert_image_3d_view['sna_frame']
                            image = get_image_from_directory(dial_value, directory)
                            if image is not None:
                                texture = gpu.texture.from_image(image)
                                blender_version = bpy.app.version
                                if blender_version >= (4, 0, 0):
                                    shader = gpu.shader.from_builtin('IMAGE')
                                else: 
                                    shader = gpu.shader.from_builtin('2D_IMAGE')
                                batch = gpu_extras.batch.batch_for_shader(
                                    shader, 'TRI_FAN',
                                    {
                                        'pos': coords,
                                        'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                    },
                                )
                                shader.bind()
                                gpu.state.blend_set('ALPHA')
                                shader.uniform_sampler('image', texture)
                                batch.draw(shader)
                else:
                    directory = os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')

                    def get_sequence_length(directory):
                        if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                            return 0
                        try:
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            return min(len(files), 101)
                        except Exception as e:
                            print(f"An error occurred while getting the sequence length: {e}")
                            return 0
                    if directory:
                        sequence_length = get_sequence_length(directory)
                        start_frame_value = g_draw_alert_image_3d_view['sna_frame']
                        start_frame = max(0, min(100, start_frame_value))
                        end_frame_value = 22
                        end_frame = max(0, min(100, end_frame_value))
                        start_frame = min(start_frame, end_frame)
                        bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                        coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                        def get_image_from_directory(dial_value, directory):
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            files.sort()
                            sequence_length = min(get_sequence_length(directory), 101)
                            if 0 <= dial_value < sequence_length:
                                image_path = os.path.join(directory, files[dial_value])
                                bpy.data.images.load(filepath=image_path, check_existing=True)
                                return bpy.data.images[os.path.basename(image_path)]
                            else:
                                return None
                        dial_value = g_draw_alert_image_3d_view['sna_frame']
                        image = get_image_from_directory(dial_value, directory)
                        if image is not None:
                            texture = gpu.texture.from_image(image)
                            blender_version = bpy.app.version
                            if blender_version >= (4, 0, 0):
                                shader = gpu.shader.from_builtin('IMAGE')
                            else: 
                                shader = gpu.shader.from_builtin('2D_IMAGE')
                            batch = gpu_extras.batch.batch_for_shader(
                                shader, 'TRI_FAN',
                                {
                                    'pos': coords,
                                    'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                },
                            )
                            shader.bind()
                            gpu.state.blend_set('ALPHA')
                            shader.uniform_sampler('image', texture)
                            batch.draw(shader)
            else:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path)):
                        coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                        bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path), check_existing=True, )

                        def get_img_name():
                            this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path))
                            for i in range(len(bpy.data.images)):
                                if bpy.data.images[i].name == bpy.data.images[this].name:
                                    return bpy.data.images[i]
                        texture = gpu.texture.from_image(get_img_name())
                        blender_version = bpy.app.version
                        if blender_version >= (4, 0, 0):
                            shader = gpu.shader.from_builtin('IMAGE')
                        else: 
                            shader = gpu.shader.from_builtin('2D_IMAGE')
                        batch = gpu_extras.batch.batch_for_shader(
                            shader, 'TRI_FAN',
                            {
                                "pos": coords,
                                "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                            },
                        )
                        shader.bind()
                        gpu.state.blend_set('ALPHA')
                        shader.uniform_sampler("image", texture)
                        batch.draw(shader)
                else:
                    coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                    bpy.data.images.load(filepath=os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'), check_existing=True, )

                    def get_img_name():
                        this = os.path.basename(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'))
                        for i in range(len(bpy.data.images)):
                            if bpy.data.images[i].name == bpy.data.images[this].name:
                                return bpy.data.images[i]
                    texture = gpu.texture.from_image(get_img_name())
                    blender_version = bpy.app.version
                    if blender_version >= (4, 0, 0):
                        shader = gpu.shader.from_builtin('IMAGE')
                    else: 
                        shader = gpu.shader.from_builtin('2D_IMAGE')
                    batch = gpu_extras.batch.batch_for_shader(
                        shader, 'TRI_FAN',
                        {
                            "pos": coords,
                            "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                        },
                    )
                    shader.bind()
                    gpu.state.blend_set('ALPHA')
                    shader.uniform_sampler("image", texture)
                    batch.draw(shader)


def sna_fn_draw_siren_start_FE25B():
    g_draw_alert_image_3d_view['sna_frame'] = 0
    g_draw_alert_image_3d_view['sna_custom_frame_length'] = 0
    g_draw_alert_image_3d_view['sna_stop'] = False
    bpy.context.scene.sna_save_police_animation_active = True
    handler_5FE5D.append(bpy.types.SpaceView3D.draw_handler_add(sna_fn_modal_drawing_2699F, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()
    if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:

        def delayed_CF5D6():
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                    if (len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))]) > 0):
                        g_draw_alert_image_3d_view['sna_custom_frame_length'] = len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))])
                    else:
                        g_draw_alert_image_3d_view['sna_custom_frame_length'] = 0
                else:
                    g_draw_alert_image_3d_view['sna_custom_frame_length'] = 0
            g_draw_alert_image_3d_view['sna_frame'] += 1
            if (g_draw_alert_image_3d_view['sna_frame'] >= (g_draw_alert_image_3d_view['sna_custom_frame_length'] if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom else 22)):
                g_draw_alert_image_3d_view['sna_frame'] = 0
            if g_draw_alert_image_3d_view['sna_stop']:
                return None
            return bpy.context.preferences.addons['savepolice'].preferences.sna_siren_interval
        bpy.app.timers.register(delayed_CF5D6, first_interval=0.0)


def sna_fn_draw_siren_end_5EC29():
    bpy.context.scene.sna_save_police_animation_active = False
    g_draw_alert_image_3d_view['sna_stop'] = True
    if handler_5FE5D:
        bpy.types.SpaceView3D.draw_handler_remove(handler_5FE5D[0], 'WINDOW')
        handler_5FE5D.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_modal_drawing_image_editor_B195C():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_message:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_4468C, y_4468C = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location
            blf.position(font_id, x_4468C, y_4468C, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message)
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)
    if bool(find_areas_of_type(bpy.context.screen, 'IMAGE_EDITOR')):
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_background:
            if (os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background)) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_custom_background):
                coords = (  ((1.0, 1.0)[0], (1.0, 1.0)[1])   , ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').width,(1.0, 1.0)[1])  ,  ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').width, (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').height)  ,   ((1.0, 1.0)[0], (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').height)   )
                bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background), check_existing=True, )

                def get_img_name():
                    this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background))
                    for i in range(len(bpy.data.images)):
                        if bpy.data.images[i].name == bpy.data.images[this].name:
                            return bpy.data.images[i]
                texture = gpu.texture.from_image(get_img_name())
                blender_version = bpy.app.version
                if blender_version >= (4, 0, 0):
                    shader = gpu.shader.from_builtin('IMAGE')
                else: 
                    shader = gpu.shader.from_builtin('2D_IMAGE')
                batch = gpu_extras.batch.batch_for_shader(
                    shader, 'TRI_FAN',
                    {
                        "pos": coords,
                        "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                    },
                )
                shader.bind()
                gpu.state.blend_set('ALPHA')
                shader.uniform_sampler("image", texture)
                batch.draw(shader)
            else:
                quads = [[tuple((1.0, 1.0)), tuple((find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').width, 1.0)), tuple((1.0, find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').height)), tuple((find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').width, find_biggest_area_by_type(bpy.context.screen, 'IMAGE_EDITOR').height))]]
                vertices = []
                indices = []
                for i_B5E84, quad in enumerate(quads):
                    vertices.extend(quad)
                    indices.extend([(i_B5E84 * 4, i_B5E84 * 4 + 1, i_B5E84 * 4 + 2), (i_B5E84 * 4 + 2, i_B5E84 * 4 + 1, i_B5E84 * 4 + 3)])
                shader = gpu.shader.from_builtin('UNIFORM_COLOR')
                batch = gpu_extras.batch.batch_for_shader(shader, 'TRIS', {"pos": tuple(vertices)}, indices=tuple(indices))
                shader.bind()
                shader.uniform_float("color", bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background_color)
                gpu.state.blend_set('ALPHA')
                batch.draw(shader)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_image:
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                        directory = bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)

                        def get_sequence_length(directory):
                            if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                                return 0
                            try:
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                return min(len(files), 101)
                            except Exception as e:
                                print(f"An error occurred while getting the sequence length: {e}")
                                return 0
                        if directory:
                            sequence_length = get_sequence_length(directory)
                            start_frame_value = g_draw_alert_image_image_editor['sna_frame']
                            start_frame = max(0, min(100, start_frame_value))
                            end_frame_value = g_draw_alert_image_image_editor['sna_custom_frame_length']
                            end_frame = max(0, min(100, end_frame_value))
                            start_frame = min(start_frame, end_frame)
                            bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                            coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                            def get_image_from_directory(dial_value, directory):
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                files.sort()
                                sequence_length = min(get_sequence_length(directory), 101)
                                if 0 <= dial_value < sequence_length:
                                    image_path = os.path.join(directory, files[dial_value])
                                    bpy.data.images.load(filepath=image_path, check_existing=True)
                                    return bpy.data.images[os.path.basename(image_path)]
                                else:
                                    return None
                            dial_value = g_draw_alert_image_image_editor['sna_frame']
                            image = get_image_from_directory(dial_value, directory)
                            if image is not None:
                                texture = gpu.texture.from_image(image)
                                blender_version = bpy.app.version
                                if blender_version >= (4, 0, 0):
                                    shader = gpu.shader.from_builtin('IMAGE')
                                else: 
                                    shader = gpu.shader.from_builtin('2D_IMAGE')
                                batch = gpu_extras.batch.batch_for_shader(
                                    shader, 'TRI_FAN',
                                    {
                                        'pos': coords,
                                        'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                    },
                                )
                                shader.bind()
                                gpu.state.blend_set('ALPHA')
                                shader.uniform_sampler('image', texture)
                                batch.draw(shader)
                else:
                    directory = os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')

                    def get_sequence_length(directory):
                        if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                            return 0
                        try:
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            return min(len(files), 101)
                        except Exception as e:
                            print(f"An error occurred while getting the sequence length: {e}")
                            return 0
                    if directory:
                        sequence_length = get_sequence_length(directory)
                        start_frame_value = g_draw_alert_image_image_editor['sna_frame']
                        start_frame = max(0, min(100, start_frame_value))
                        end_frame_value = 22
                        end_frame = max(0, min(100, end_frame_value))
                        start_frame = min(start_frame, end_frame)
                        bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                        coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                        def get_image_from_directory(dial_value, directory):
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            files.sort()
                            sequence_length = min(get_sequence_length(directory), 101)
                            if 0 <= dial_value < sequence_length:
                                image_path = os.path.join(directory, files[dial_value])
                                bpy.data.images.load(filepath=image_path, check_existing=True)
                                return bpy.data.images[os.path.basename(image_path)]
                            else:
                                return None
                        dial_value = g_draw_alert_image_image_editor['sna_frame']
                        image = get_image_from_directory(dial_value, directory)
                        if image is not None:
                            texture = gpu.texture.from_image(image)
                            blender_version = bpy.app.version
                            if blender_version >= (4, 0, 0):
                                shader = gpu.shader.from_builtin('IMAGE')
                            else: 
                                shader = gpu.shader.from_builtin('2D_IMAGE')
                            batch = gpu_extras.batch.batch_for_shader(
                                shader, 'TRI_FAN',
                                {
                                    'pos': coords,
                                    'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                },
                            )
                            shader.bind()
                            gpu.state.blend_set('ALPHA')
                            shader.uniform_sampler('image', texture)
                            batch.draw(shader)
            else:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path)):
                        coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                        bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path), check_existing=True, )

                        def get_img_name():
                            this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path))
                            for i in range(len(bpy.data.images)):
                                if bpy.data.images[i].name == bpy.data.images[this].name:
                                    return bpy.data.images[i]
                        texture = gpu.texture.from_image(get_img_name())
                        blender_version = bpy.app.version
                        if blender_version >= (4, 0, 0):
                            shader = gpu.shader.from_builtin('IMAGE')
                        else: 
                            shader = gpu.shader.from_builtin('2D_IMAGE')
                        batch = gpu_extras.batch.batch_for_shader(
                            shader, 'TRI_FAN',
                            {
                                "pos": coords,
                                "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                            },
                        )
                        shader.bind()
                        gpu.state.blend_set('ALPHA')
                        shader.uniform_sampler("image", texture)
                        batch.draw(shader)
                else:
                    coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                    bpy.data.images.load(filepath=os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'), check_existing=True, )

                    def get_img_name():
                        this = os.path.basename(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'))
                        for i in range(len(bpy.data.images)):
                            if bpy.data.images[i].name == bpy.data.images[this].name:
                                return bpy.data.images[i]
                    texture = gpu.texture.from_image(get_img_name())
                    blender_version = bpy.app.version
                    if blender_version >= (4, 0, 0):
                        shader = gpu.shader.from_builtin('IMAGE')
                    else: 
                        shader = gpu.shader.from_builtin('2D_IMAGE')
                    batch = gpu_extras.batch.batch_for_shader(
                        shader, 'TRI_FAN',
                        {
                            "pos": coords,
                            "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                        },
                    )
                    shader.bind()
                    gpu.state.blend_set('ALPHA')
                    shader.uniform_sampler("image", texture)
                    batch.draw(shader)


def sna_fn_draw_siren_end_8EADA():
    bpy.context.scene.sna_save_police_animation_active = False
    g_draw_alert_image_image_editor['sna_stop'] = True
    if handler_D8705:
        bpy.types.SpaceImageEditor.draw_handler_remove(handler_D8705[0], 'WINDOW')
        handler_D8705.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_draw_siren_start_68E9D():
    g_draw_alert_image_image_editor['sna_frame'] = 0
    g_draw_alert_image_image_editor['sna_custom_frame_length'] = 0
    g_draw_alert_image_image_editor['sna_stop'] = False
    bpy.context.scene.sna_save_police_animation_active = True
    handler_D8705.append(bpy.types.SpaceImageEditor.draw_handler_add(sna_fn_modal_drawing_image_editor_B195C, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()
    if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:

        def delayed_3E6B7():
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                    if (len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))]) > 0):
                        g_draw_alert_image_image_editor['sna_custom_frame_length'] = len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))])
                    else:
                        g_draw_alert_image_image_editor['sna_custom_frame_length'] = 0
                else:
                    g_draw_alert_image_image_editor['sna_custom_frame_length'] = 0
            g_draw_alert_image_image_editor['sna_frame'] += 1
            if (g_draw_alert_image_image_editor['sna_frame'] >= (g_draw_alert_image_image_editor['sna_custom_frame_length'] if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom else 22)):
                g_draw_alert_image_image_editor['sna_frame'] = 0
            if g_draw_alert_image_image_editor['sna_stop']:
                return None
            return bpy.context.preferences.addons['savepolice'].preferences.sna_siren_interval
        bpy.app.timers.register(delayed_3E6B7, first_interval=0.0)


def sna_fn_modal_drawing_node_editor_BA36C():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_message:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_8C5FD, y_8C5FD = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location
            blf.position(font_id, x_8C5FD, y_8C5FD, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message)
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)
    if bool(find_areas_of_type(bpy.context.screen, 'NODE_EDITOR')):
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_background:
            if (os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background)) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_custom_background):
                coords = (  ((1.0, 1.0)[0], (1.0, 1.0)[1])   , ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').width,(1.0, 1.0)[1])  ,  ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').width, (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').height)  ,   ((1.0, 1.0)[0], (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').height)   )
                bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background), check_existing=True, )

                def get_img_name():
                    this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background))
                    for i in range(len(bpy.data.images)):
                        if bpy.data.images[i].name == bpy.data.images[this].name:
                            return bpy.data.images[i]
                texture = gpu.texture.from_image(get_img_name())
                blender_version = bpy.app.version
                if blender_version >= (4, 0, 0):
                    shader = gpu.shader.from_builtin('IMAGE')
                else: 
                    shader = gpu.shader.from_builtin('2D_IMAGE')
                batch = gpu_extras.batch.batch_for_shader(
                    shader, 'TRI_FAN',
                    {
                        "pos": coords,
                        "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                    },
                )
                shader.bind()
                gpu.state.blend_set('ALPHA')
                shader.uniform_sampler("image", texture)
                batch.draw(shader)
            else:
                quads = [[tuple((1.0, 1.0)), tuple((find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').width, 1.0)), tuple((1.0, find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').height)), tuple((find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').width, find_biggest_area_by_type(bpy.context.screen, 'NODE_EDITOR').height))]]
                vertices = []
                indices = []
                for i_1A51A, quad in enumerate(quads):
                    vertices.extend(quad)
                    indices.extend([(i_1A51A * 4, i_1A51A * 4 + 1, i_1A51A * 4 + 2), (i_1A51A * 4 + 2, i_1A51A * 4 + 1, i_1A51A * 4 + 3)])
                shader = gpu.shader.from_builtin('UNIFORM_COLOR')
                batch = gpu_extras.batch.batch_for_shader(shader, 'TRIS', {"pos": tuple(vertices)}, indices=tuple(indices))
                shader.bind()
                shader.uniform_float("color", bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background_color)
                gpu.state.blend_set('ALPHA')
                batch.draw(shader)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_image:
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                        directory = bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)

                        def get_sequence_length(directory):
                            if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                                return 0
                            try:
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                return min(len(files), 101)
                            except Exception as e:
                                print(f"An error occurred while getting the sequence length: {e}")
                                return 0
                        if directory:
                            sequence_length = get_sequence_length(directory)
                            start_frame_value = g_draw_alert_image_node_editor['sna_frame']
                            start_frame = max(0, min(100, start_frame_value))
                            end_frame_value = g_draw_alert_image_node_editor['sna_custom_frame_length']
                            end_frame = max(0, min(100, end_frame_value))
                            start_frame = min(start_frame, end_frame)
                            bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                            coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                            def get_image_from_directory(dial_value, directory):
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                files.sort()
                                sequence_length = min(get_sequence_length(directory), 101)
                                if 0 <= dial_value < sequence_length:
                                    image_path = os.path.join(directory, files[dial_value])
                                    bpy.data.images.load(filepath=image_path, check_existing=True)
                                    return bpy.data.images[os.path.basename(image_path)]
                                else:
                                    return None
                            dial_value = g_draw_alert_image_node_editor['sna_frame']
                            image = get_image_from_directory(dial_value, directory)
                            if image is not None:
                                texture = gpu.texture.from_image(image)
                                blender_version = bpy.app.version
                                if blender_version >= (4, 0, 0):
                                    shader = gpu.shader.from_builtin('IMAGE')
                                else: 
                                    shader = gpu.shader.from_builtin('2D_IMAGE')
                                batch = gpu_extras.batch.batch_for_shader(
                                    shader, 'TRI_FAN',
                                    {
                                        'pos': coords,
                                        'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                    },
                                )
                                shader.bind()
                                gpu.state.blend_set('ALPHA')
                                shader.uniform_sampler('image', texture)
                                batch.draw(shader)
                else:
                    directory = os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')

                    def get_sequence_length(directory):
                        if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                            return 0
                        try:
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            return min(len(files), 101)
                        except Exception as e:
                            print(f"An error occurred while getting the sequence length: {e}")
                            return 0
                    if directory:
                        sequence_length = get_sequence_length(directory)
                        start_frame_value = g_draw_alert_image_node_editor['sna_frame']
                        start_frame = max(0, min(100, start_frame_value))
                        end_frame_value = 22
                        end_frame = max(0, min(100, end_frame_value))
                        start_frame = min(start_frame, end_frame)
                        bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                        coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                        def get_image_from_directory(dial_value, directory):
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            files.sort()
                            sequence_length = min(get_sequence_length(directory), 101)
                            if 0 <= dial_value < sequence_length:
                                image_path = os.path.join(directory, files[dial_value])
                                bpy.data.images.load(filepath=image_path, check_existing=True)
                                return bpy.data.images[os.path.basename(image_path)]
                            else:
                                return None
                        dial_value = g_draw_alert_image_node_editor['sna_frame']
                        image = get_image_from_directory(dial_value, directory)
                        if image is not None:
                            texture = gpu.texture.from_image(image)
                            blender_version = bpy.app.version
                            if blender_version >= (4, 0, 0):
                                shader = gpu.shader.from_builtin('IMAGE')
                            else: 
                                shader = gpu.shader.from_builtin('2D_IMAGE')
                            batch = gpu_extras.batch.batch_for_shader(
                                shader, 'TRI_FAN',
                                {
                                    'pos': coords,
                                    'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                },
                            )
                            shader.bind()
                            gpu.state.blend_set('ALPHA')
                            shader.uniform_sampler('image', texture)
                            batch.draw(shader)
            else:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path)):
                        coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                        bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path), check_existing=True, )

                        def get_img_name():
                            this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path))
                            for i in range(len(bpy.data.images)):
                                if bpy.data.images[i].name == bpy.data.images[this].name:
                                    return bpy.data.images[i]
                        texture = gpu.texture.from_image(get_img_name())
                        blender_version = bpy.app.version
                        if blender_version >= (4, 0, 0):
                            shader = gpu.shader.from_builtin('IMAGE')
                        else: 
                            shader = gpu.shader.from_builtin('2D_IMAGE')
                        batch = gpu_extras.batch.batch_for_shader(
                            shader, 'TRI_FAN',
                            {
                                "pos": coords,
                                "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                            },
                        )
                        shader.bind()
                        gpu.state.blend_set('ALPHA')
                        shader.uniform_sampler("image", texture)
                        batch.draw(shader)
                else:
                    coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                    bpy.data.images.load(filepath=os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'), check_existing=True, )

                    def get_img_name():
                        this = os.path.basename(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'))
                        for i in range(len(bpy.data.images)):
                            if bpy.data.images[i].name == bpy.data.images[this].name:
                                return bpy.data.images[i]
                    texture = gpu.texture.from_image(get_img_name())
                    blender_version = bpy.app.version
                    if blender_version >= (4, 0, 0):
                        shader = gpu.shader.from_builtin('IMAGE')
                    else: 
                        shader = gpu.shader.from_builtin('2D_IMAGE')
                    batch = gpu_extras.batch.batch_for_shader(
                        shader, 'TRI_FAN',
                        {
                            "pos": coords,
                            "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                        },
                    )
                    shader.bind()
                    gpu.state.blend_set('ALPHA')
                    shader.uniform_sampler("image", texture)
                    batch.draw(shader)


def sna_fn_draw_siren_end_2CF21():
    bpy.context.scene.sna_save_police_animation_active = False
    g_draw_alert_image_node_editor['sna_stop'] = True
    if handler_AAAFB:
        bpy.types.SpaceNodeEditor.draw_handler_remove(handler_AAAFB[0], 'WINDOW')
        handler_AAAFB.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_draw_siren_start_00FEB():
    g_draw_alert_image_node_editor['sna_frame'] = 0
    g_draw_alert_image_node_editor['sna_custom_frame_length'] = 0
    g_draw_alert_image_node_editor['sna_stop'] = False
    bpy.context.scene.sna_save_police_animation_active = True
    handler_AAAFB.append(bpy.types.SpaceNodeEditor.draw_handler_add(sna_fn_modal_drawing_node_editor_BA36C, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()
    if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:

        def delayed_EAB06():
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                    if (len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))]) > 0):
                        g_draw_alert_image_node_editor['sna_custom_frame_length'] = len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))])
                    else:
                        g_draw_alert_image_node_editor['sna_custom_frame_length'] = 0
                else:
                    g_draw_alert_image_node_editor['sna_custom_frame_length'] = 0
            g_draw_alert_image_node_editor['sna_frame'] += 1
            if (g_draw_alert_image_node_editor['sna_frame'] >= (g_draw_alert_image_node_editor['sna_custom_frame_length'] if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom else 22)):
                g_draw_alert_image_node_editor['sna_frame'] = 0
            if g_draw_alert_image_node_editor['sna_stop']:
                return None
            return bpy.context.preferences.addons['savepolice'].preferences.sna_siren_interval
        bpy.app.timers.register(delayed_EAB06, first_interval=0.0)


class SNA_OT_Save_Police_Preview_Alert_Image_558A3(bpy.types.Operator):
    bl_idname = "sna.save_police_preview_alert_image_558a3"
    bl_label = "Save Police Preview Alert Image"
    bl_description = "Preview the Alert Message"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('Image is active wait until it is inactive')
        return not bpy.context.scene.sna_save_police_animation_active

    def execute(self, context):
        if (not bpy.context.scene.sna_save_police_animation_active):
            if (bool(find_areas_of_type(bpy.context.screen, 'VIEW_3D')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_3d_viewport):
                sna_fn_draw_siren_start_FE25B()
            if (bool(find_areas_of_type(bpy.context.screen, 'NODE_EDITOR')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_node_editors):
                sna_fn_draw_siren_start_00FEB()
            if (bool(find_areas_of_type(bpy.context.screen, 'IMAGE_EDITOR')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_editor):
                sna_fn_draw_siren_start_68E9D()
            if (bool(find_areas_of_type(bpy.context.screen, 'SEQUENCE_EDITOR')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_video_sequencer):
                sna_fn_draw_siren_start_279D8()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Save_Police_End_Alert_Image_Preview_7A41B(bpy.types.Operator):
    bl_idname = "sna.save_police_end_alert_image_preview_7a41b"
    bl_label = "Save Police End Alert Image Preview"
    bl_description = "Preview the Alert Message"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_fn_draw_siren_end_5EC29()
        sna_fn_draw_siren_end_2CF21()
        sna_fn_draw_siren_end_8EADA()
        sna_fn_draw_siren_end_CC28D()
        sna_fn_removed_unused_images_A2907()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_fn_modal_drawing_vse_F7409():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_message:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_0081E, y_0081E = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location
            blf.position(font_id, x_0081E, y_0081E, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message)
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)
    if bool(find_areas_of_type(bpy.context.screen, 'SEQUENCE_EDITOR')):
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_background:
            if (os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background)) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_custom_background):
                coords = (  ((1.0, 1.0)[0], (1.0, 1.0)[1])   , ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').width,(1.0, 1.0)[1])  ,  ((1.0, 1.0)[0]+find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').width, (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').height)  ,   ((1.0, 1.0)[0], (1.0, 1.0)[1]+find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').height)   )
                bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background), check_existing=True, )

                def get_img_name():
                    this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background))
                    for i in range(len(bpy.data.images)):
                        if bpy.data.images[i].name == bpy.data.images[this].name:
                            return bpy.data.images[i]
                texture = gpu.texture.from_image(get_img_name())
                blender_version = bpy.app.version
                if blender_version >= (4, 0, 0):
                    shader = gpu.shader.from_builtin('IMAGE')
                else: 
                    shader = gpu.shader.from_builtin('2D_IMAGE')
                batch = gpu_extras.batch.batch_for_shader(
                    shader, 'TRI_FAN',
                    {
                        "pos": coords,
                        "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                    },
                )
                shader.bind()
                gpu.state.blend_set('ALPHA')
                shader.uniform_sampler("image", texture)
                batch.draw(shader)
            else:
                quads = [[tuple((1.0, 1.0)), tuple((find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').width, 1.0)), tuple((1.0, find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').height)), tuple((find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').width, find_biggest_area_by_type(bpy.context.screen, 'SEQUENCE_EDITOR').height))]]
                vertices = []
                indices = []
                for i_91289, quad in enumerate(quads):
                    vertices.extend(quad)
                    indices.extend([(i_91289 * 4, i_91289 * 4 + 1, i_91289 * 4 + 2), (i_91289 * 4 + 2, i_91289 * 4 + 1, i_91289 * 4 + 3)])
                shader = gpu.shader.from_builtin('UNIFORM_COLOR')
                batch = gpu_extras.batch.batch_for_shader(shader, 'TRIS', {"pos": tuple(vertices)}, indices=tuple(indices))
                shader.bind()
                shader.uniform_float("color", bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background_color)
                gpu.state.blend_set('ALPHA')
                batch.draw(shader)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_image:
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                        directory = bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)

                        def get_sequence_length(directory):
                            if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                                return 0
                            try:
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                return min(len(files), 101)
                            except Exception as e:
                                print(f"An error occurred while getting the sequence length: {e}")
                                return 0
                        if directory:
                            sequence_length = get_sequence_length(directory)
                            start_frame_value = g_draw_alert_image_vse_editor['sna_frame']
                            start_frame = max(0, min(100, start_frame_value))
                            end_frame_value = g_draw_alert_image_vse_editor['sna_custom_frame_length']
                            end_frame = max(0, min(100, end_frame_value))
                            start_frame = min(start_frame, end_frame)
                            bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                            coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                            def get_image_from_directory(dial_value, directory):
                                files = [f for f in os.listdir(directory) if f.endswith('.png')]
                                files.sort()
                                sequence_length = min(get_sequence_length(directory), 101)
                                if 0 <= dial_value < sequence_length:
                                    image_path = os.path.join(directory, files[dial_value])
                                    bpy.data.images.load(filepath=image_path, check_existing=True)
                                    return bpy.data.images[os.path.basename(image_path)]
                                else:
                                    return None
                            dial_value = g_draw_alert_image_vse_editor['sna_frame']
                            image = get_image_from_directory(dial_value, directory)
                            if image is not None:
                                texture = gpu.texture.from_image(image)
                                blender_version = bpy.app.version
                                if blender_version >= (4, 0, 0):
                                    shader = gpu.shader.from_builtin('IMAGE')
                                else: 
                                    shader = gpu.shader.from_builtin('2D_IMAGE')
                                batch = gpu_extras.batch.batch_for_shader(
                                    shader, 'TRI_FAN',
                                    {
                                        'pos': coords,
                                        'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                    },
                                )
                                shader.bind()
                                gpu.state.blend_set('ALPHA')
                                shader.uniform_sampler('image', texture)
                                batch.draw(shader)
                else:
                    directory = os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')

                    def get_sequence_length(directory):
                        if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
                            return 0
                        try:
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            return min(len(files), 101)
                        except Exception as e:
                            print(f"An error occurred while getting the sequence length: {e}")
                            return 0
                    if directory:
                        sequence_length = get_sequence_length(directory)
                        start_frame_value = g_draw_alert_image_vse_editor['sna_frame']
                        start_frame = max(0, min(100, start_frame_value))
                        end_frame_value = 22
                        end_frame = max(0, min(100, end_frame_value))
                        start_frame = min(start_frame, end_frame)
                        bl = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
                        coords = ((bl[0], bl[1]), (bl[0] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1]), (bl[0] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bl[1] + bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]), (bl[0], bl[1] + 
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1]))

                        def get_image_from_directory(dial_value, directory):
                            files = [f for f in os.listdir(directory) if f.endswith('.png')]
                            files.sort()
                            sequence_length = min(get_sequence_length(directory), 101)
                            if 0 <= dial_value < sequence_length:
                                image_path = os.path.join(directory, files[dial_value])
                                bpy.data.images.load(filepath=image_path, check_existing=True)
                                return bpy.data.images[os.path.basename(image_path)]
                            else:
                                return None
                        dial_value = g_draw_alert_image_vse_editor['sna_frame']
                        image = get_image_from_directory(dial_value, directory)
                        if image is not None:
                            texture = gpu.texture.from_image(image)
                            blender_version = bpy.app.version
                            if blender_version >= (4, 0, 0):
                                shader = gpu.shader.from_builtin('IMAGE')
                            else: 
                                shader = gpu.shader.from_builtin('2D_IMAGE')
                            batch = gpu_extras.batch.batch_for_shader(
                                shader, 'TRI_FAN',
                                {
                                    'pos': coords,
                                    'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                                },
                            )
                            shader.bind()
                            gpu.state.blend_set('ALPHA')
                            shader.uniform_sampler('image', texture)
                            batch.draw(shader)
            else:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path)):
                        coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                        bpy.data.images.load(filepath=bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path), check_existing=True, )

                        def get_img_name():
                            this = os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path))
                            for i in range(len(bpy.data.images)):
                                if bpy.data.images[i].name == bpy.data.images[this].name:
                                    return bpy.data.images[i]
                        texture = gpu.texture.from_image(get_img_name())
                        blender_version = bpy.app.version
                        if blender_version >= (4, 0, 0):
                            shader = gpu.shader.from_builtin('IMAGE')
                        else: 
                            shader = gpu.shader.from_builtin('2D_IMAGE')
                        batch = gpu_extras.batch.batch_for_shader(
                            shader, 'TRI_FAN',
                            {
                                "pos": coords,
                                "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                            },
                        )
                        shader.bind()
                        gpu.state.blend_set('ALPHA')
                        shader.uniform_sampler("image", texture)
                        batch.draw(shader)
                else:
                    coords = (  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])   , (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0],bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1])  ,  (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])  ,   (bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[0], bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location[1]+bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size[1])   )
                    bpy.data.images.load(filepath=os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'), check_existing=True, )

                    def get_img_name():
                        this = os.path.basename(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'))
                        for i in range(len(bpy.data.images)):
                            if bpy.data.images[i].name == bpy.data.images[this].name:
                                return bpy.data.images[i]
                    texture = gpu.texture.from_image(get_img_name())
                    blender_version = bpy.app.version
                    if blender_version >= (4, 0, 0):
                        shader = gpu.shader.from_builtin('IMAGE')
                    else: 
                        shader = gpu.shader.from_builtin('2D_IMAGE')
                    batch = gpu_extras.batch.batch_for_shader(
                        shader, 'TRI_FAN',
                        {
                            "pos": coords,
                            "texCoord": ((0, 0), (1, 0), (1, 1), (0, 1)),
                        },
                    )
                    shader.bind()
                    gpu.state.blend_set('ALPHA')
                    shader.uniform_sampler("image", texture)
                    batch.draw(shader)


def sna_fn_draw_siren_end_CC28D():
    bpy.context.scene.sna_save_police_animation_active = False
    g_draw_alert_image_vse_editor['sna_stop'] = True
    if handler_CB41D:
        bpy.types.SpaceSequenceEditor.draw_handler_remove(handler_CB41D[0], 'WINDOW')
        handler_CB41D.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_draw_siren_start_279D8():
    g_draw_alert_image_vse_editor['sna_frame'] = 0
    g_draw_alert_image_vse_editor['sna_custom_frame_length'] = 0
    g_draw_alert_image_vse_editor['sna_stop'] = False
    bpy.context.scene.sna_save_police_animation_active = True
    handler_CB41D.append(bpy.types.SpaceSequenceEditor.draw_handler_add(sna_fn_modal_drawing_vse_F7409, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()
    if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:

        def delayed_8C706():
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                if os.path.isdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
                    if (len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))]) > 0):
                        g_draw_alert_image_vse_editor['sna_custom_frame_length'] = len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))])
                    else:
                        g_draw_alert_image_vse_editor['sna_custom_frame_length'] = 0
                else:
                    g_draw_alert_image_vse_editor['sna_custom_frame_length'] = 0
            g_draw_alert_image_vse_editor['sna_frame'] += 1
            if (g_draw_alert_image_vse_editor['sna_frame'] >= (g_draw_alert_image_vse_editor['sna_custom_frame_length'] if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom else 22)):
                g_draw_alert_image_vse_editor['sna_frame'] = 0
            if g_draw_alert_image_vse_editor['sna_stop']:
                return None
            return bpy.context.preferences.addons['savepolice'].preferences.sna_siren_interval
        bpy.app.timers.register(delayed_8C706, first_interval=0.0)


def sna_fn_modal_drawing_D4923():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_use_countdown:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_ACAA8, y_ACAA8 = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location
            blf.position(font_id, x_ACAA8, y_ACAA8, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, (graph_scripts['sna_time_message'] + ' ' + bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_suffix_message if bpy.data.is_dirty else 'Saved ' + ' ' + os.path.basename(bpy.path.abspath(bpy.data.filepath))[:-6]))
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)


def sna_fn_draw_siren_start_9B9BB():
    bpy.context.scene.sna_save_police_countdown_active = True
    handler_EE591.append(bpy.types.SpaceView3D.draw_handler_add(sna_fn_modal_drawing_D4923, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_draw_siren_end_4F626():
    bpy.context.scene.sna_save_police_countdown_active = False
    if handler_EE591:
        bpy.types.SpaceView3D.draw_handler_remove(handler_EE591[0], 'WINDOW')
        handler_EE591.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_modal_drawing_7B865():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_use_countdown:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_9D87E, y_9D87E = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location
            blf.position(font_id, x_9D87E, y_9D87E, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, (graph_scripts['sna_time_message'] + ' ' + bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_suffix_message if bpy.data.is_dirty else 'Saved ' + ' ' + os.path.basename(bpy.path.abspath(bpy.data.filepath))[:-6]))
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)


def sna_fn_draw_siren_start_D3208():
    bpy.context.scene.sna_save_police_countdown_active = True
    handler_A1E89.append(bpy.types.SpaceImageEditor.draw_handler_add(sna_fn_modal_drawing_7B865, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_modal_drawing_18530():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_use_countdown:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_9030D, y_9030D = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location
            blf.position(font_id, x_9030D, y_9030D, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, (graph_scripts['sna_time_message'] + ' ' + bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_suffix_message if bpy.data.is_dirty else 'Saved ' + ' ' + os.path.basename(bpy.path.abspath(bpy.data.filepath))[:-6]))
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)


def sna_fn_draw_siren_start_99929():
    bpy.context.scene.sna_save_police_countdown_active = True
    handler_0A529.append(bpy.types.SpaceNodeEditor.draw_handler_add(sna_fn_modal_drawing_18530, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_draw_siren_end_05897():
    bpy.context.scene.sna_save_police_countdown_active = False
    if handler_0A529:
        bpy.types.SpaceNodeEditor.draw_handler_remove(handler_0A529[0], 'WINDOW')
        handler_0A529.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


class SNA_OT_Save_Police_Preview_Countdown_8B9F0(bpy.types.Operator):
    bl_idname = "sna.save_police_preview_countdown_8b9f0"
    bl_label = "Save Police Preview Countdown"
    bl_description = "Draw the countdown on screen"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('Must disable drawing first')
        return not bpy.context.scene.sna_save_police_countdown_active

    def execute(self, context):
        if (not bpy.context.scene.sna_save_police_countdown_active):
            if (bool(find_areas_of_type(bpy.context.screen, 'VIEW_3D')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_3d_viewport):
                sna_fn_draw_siren_start_9B9BB()
            if (bool(find_areas_of_type(bpy.context.screen, 'NODE_EDITOR')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_node_editors):
                sna_fn_draw_siren_start_99929()
            if (bool(find_areas_of_type(bpy.context.screen, 'IMAGE_EDITOR')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_editor):
                sna_fn_draw_siren_start_D3208()
            if (bool(find_areas_of_type(bpy.context.screen, 'SEQUENCE_EDITOR')) and bpy.context.preferences.addons['savepolice'].preferences.sna_alert_video_sequencer):
                sna_fn_draw_siren_start_89390()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Save_Police_End_Countdown_Preview_8F673(bpy.types.Operator):
    bl_idname = "sna.save_police_end_countdown_preview_8f673"
    bl_label = "Save Police End Countdown Preview"
    bl_description = "Stop drawing the countdown on screen"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_fn_draw_siren_end_4F626()
        sna_fn_draw_siren_end_05897()
        sna_fn_draw_siren_end_05897()
        sna_fn_draw_siren_end_CFEC7()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_fn_modal_drawing_4D6EA():
    if bpy.context.preferences.addons['savepolice'].preferences.sna_use_countdown:
        font_id = 0
        if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font and os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font):
            font_id = blf.load(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_font)
        if font_id == -1:
            print("Couldn't load font!")
        else:
            x_C929F, y_C929F = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location
            blf.position(font_id, x_C929F, y_C929F, 0)
            if bpy.app.version >= (3, 4, 0):
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size)
            else:
                blf.size(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_dpi)
            clr = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_color
            blf.color(font_id, clr[0], clr[1], clr[2], clr[3])
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap:
                blf.enable(font_id, blf.WORD_WRAP)
                blf.word_wrap(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_wrap)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation:
                blf.enable(font_id, blf.ROTATION)
                blf.rotation(font_id, bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_rotation)
            blf.enable(font_id, blf.WORD_WRAP)
            blf.draw(font_id, (graph_scripts['sna_time_message'] + ' ' + bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_suffix_message if bpy.data.is_dirty else 'Saved ' + ' ' + os.path.basename(bpy.path.abspath(bpy.data.filepath))[:-6]))
            blf.disable(font_id, blf.ROTATION)
            blf.disable(font_id, blf.WORD_WRAP)


def sna_fn_draw_siren_start_89390():
    bpy.context.scene.sna_save_police_countdown_active = True
    handler_F57E6.append(bpy.types.SpaceSequenceEditor.draw_handler_add(sna_fn_modal_drawing_4D6EA, (), 'WINDOW', 'POST_PIXEL'))
    for a in bpy.context.screen.areas: a.tag_redraw()


def sna_fn_draw_siren_end_CFEC7():
    bpy.context.scene.sna_save_police_countdown_active = False
    if handler_F57E6:
        bpy.types.SpaceSequenceEditor.draw_handler_remove(handler_F57E6[0], 'WINDOW')
        handler_F57E6.pop(0)
        for a in bpy.context.screen.areas: a.tag_redraw()


_DA3AC_running = False
class SNA_OT_Save_Police_Move_Countdown_Da3Ac(bpy.types.Operator):
    bl_idname = "sna.save_police_move_countdown_da3ac"
    bl_label = "Save Police Move Countdown"
    bl_description = "Move the Countdown with the Cursor"
    bl_options = {"REGISTER", "UNDO"}
    sna_countdown_loc_initial: bpy.props.FloatVectorProperty(name='countdown_loc_initial', description='', size=2, default=(1.0, 1.0), subtype='NONE', unit='NONE', min=1.0, step=10, precision=1)
    sna_countdown_size_initial: bpy.props.FloatProperty(name='countdown_size_initial', description='', default=1.0, subtype='NONE', unit='NONE', min=1.0, step=5, precision=1)
    cursor = "CROSSHAIR"
    _handle = None
    _event = {}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        if not False or context.area.spaces[0].bl_rna.identifier == 'SpaceNodeEditor':
            return not False
        return False

    def save_event(self, event):
        event_options = ["type", "value", "alt", "shift", "ctrl", "oskey", "mouse_region_x", "mouse_region_y", "mouse_x", "mouse_y", "pressure", "tilt"]
        if bpy.app.version >= (3, 2, 1):
            event_options += ["type_prev", "value_prev"]
        for option in event_options: self._event[option] = getattr(event, option)

    def draw_callback_px(self, context):
        event = self._event
        if event.keys():
            event = dotdict(event)
            try:
                pass
            except Exception as error:
                print(error)

    def execute(self, context):
        global _DA3AC_running
        _DA3AC_running = False
        context.window.cursor_set("DEFAULT")
        for area in context.screen.areas:
            area.tag_redraw()
        return {"FINISHED"}

    def modal(self, context, event):
        global _DA3AC_running
        if not context.area or not _DA3AC_running:
            self.execute(context)
            return {'CANCELLED'}
        self.save_event(event)
        context.window.cursor_set('CROSSHAIR')
        try:
            if ((event.type == 'ESC') or (event.type == 'RIGHTMOUSE')):
                bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location = self.sna_countdown_loc_initial
                bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size = self.sna_countdown_size_initial
                if event.type in ['RIGHTMOUSE', 'ESC']:
                    self.execute(context)
                    return {'CANCELLED'}
                return {"CANCELLED"}
            else:
                if ((event.type == 'LEFTMOUSE') or (event.type == 'RET')):
                    if event.type in ['RIGHTMOUSE', 'ESC']:
                        self.execute(context)
                        return {'CANCELLED'}
                    self.execute(context)
                    return {"FINISHED"}
                else:
                    if (event.type == 'WHEELUPMOUSE'):
                        bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size = float(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size + 10.0)
                    else:
                        if (event.type == 'WHEELDOWNMOUSE'):
                            bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size = float(bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size - 10.0)
                        else:
                            bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location = (event.mouse_x, event.mouse_y)
                            if bpy.context and bpy.context.screen:
                                for a in bpy.context.screen.areas:
                                    a.tag_redraw()
        except Exception as error:
            print(error)
        if event.type in ['RIGHTMOUSE', 'ESC']:
            self.execute(context)
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        global _DA3AC_running
        if _DA3AC_running:
            _DA3AC_running = False
            return {'FINISHED'}
        else:
            self.save_event(event)
            self.start_pos = (event.mouse_x, event.mouse_y)
            bpy.context.window.cursor_warp(x=int(tuple(map(lambda v: int(v), bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location))[0]), y=int(tuple(map(lambda v: int(v), bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location))[1]), )
            self.sna_countdown_loc_initial = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_location
            self.sna_countdown_size_initial = bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_size
            context.window_manager.modal_handler_add(self)
            _DA3AC_running = True
            return {'RUNNING_MODAL'}


_F9F28_running = False
class SNA_OT_Save_Police_Move_Image_F9F28(bpy.types.Operator):
    bl_idname = "sna.save_police_move_image_f9f28"
    bl_label = "Save Police Move Image"
    bl_description = "Move the Image with the Cursor"
    bl_options = {"REGISTER", "UNDO"}
    sna_alert_loc_initial: bpy.props.FloatVectorProperty(name='alert_loc_initial', description='', size=2, default=(1.0, 1.0), subtype='NONE', unit='NONE', min=1.0, step=5, precision=1)
    sna_alert_size_initial: bpy.props.FloatVectorProperty(name='alert_size_initial', description='', size=2, default=(1.0, 1.0), subtype='NONE', unit='NONE', min=8.0, step=10, precision=1)
    cursor = "HAND"
    _handle = None
    _event = {}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        if not False or context.area.spaces[0].bl_rna.identifier == 'SpaceNodeEditor':
            return not False
        return False

    def save_event(self, event):
        event_options = ["type", "value", "alt", "shift", "ctrl", "oskey", "mouse_region_x", "mouse_region_y", "mouse_x", "mouse_y", "pressure", "tilt"]
        if bpy.app.version >= (3, 2, 1):
            event_options += ["type_prev", "value_prev"]
        for option in event_options: self._event[option] = getattr(event, option)

    def draw_callback_px(self, context):
        event = self._event
        if event.keys():
            event = dotdict(event)
            try:
                pass
            except Exception as error:
                print(error)

    def execute(self, context):
        global _F9F28_running
        _F9F28_running = False
        context.window.cursor_set("DEFAULT")
        for area in context.screen.areas:
            area.tag_redraw()
        return {"FINISHED"}

    def modal(self, context, event):
        global _F9F28_running
        if not context.area or not _F9F28_running:
            self.execute(context)
            return {'CANCELLED'}
        self.save_event(event)
        context.window.cursor_set('HAND')
        try:
            if ((event.type == 'ESC') or (event.type == 'RIGHTMOUSE')):
                bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location = self.sna_alert_loc_initial
                bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size = self.sna_alert_size_initial
                if event.type in ['RIGHTMOUSE', 'ESC']:
                    self.execute(context)
                    return {'CANCELLED'}
                return {"CANCELLED"}
            else:
                if ((event.type == 'LEFTMOUSE') or (event.type == 'RET')):
                    if event.type in ['RIGHTMOUSE', 'ESC']:
                        self.execute(context)
                        return {'CANCELLED'}
                    self.execute(context)
                    return {"FINISHED"}
                else:
                    if (event.type == 'WHEELUPMOUSE'):
                        bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size = tuple(mathutils.Vector(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size) + mathutils.Vector((40.0, 40.0)))
                    else:
                        if (event.type == 'WHEELDOWNMOUSE'):
                            bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size = tuple(mathutils.Vector(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size) - mathutils.Vector((40.0, 40.0)))
                        else:
                            bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location = (event.mouse_x, event.mouse_y)
                            if bpy.context and bpy.context.screen:
                                for a in bpy.context.screen.areas:
                                    a.tag_redraw()
        except Exception as error:
            print(error)
        if event.type in ['RIGHTMOUSE', 'ESC']:
            self.execute(context)
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        global _F9F28_running
        if _F9F28_running:
            _F9F28_running = False
            return {'FINISHED'}
        else:
            self.save_event(event)
            self.start_pos = (event.mouse_x, event.mouse_y)
            bpy.context.window.cursor_warp(x=int(tuple(map(lambda v: int(v), bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location))[0]), y=int(tuple(map(lambda v: int(v), bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location))[1]), )
            self.sna_alert_loc_initial = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_location
            self.sna_alert_size_initial = bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_size
            context.window_manager.modal_handler_add(self)
            _F9F28_running = True
            return {'RUNNING_MODAL'}


_582F8_running = False
class SNA_OT_Save_Police_Move_Message_582F8(bpy.types.Operator):
    bl_idname = "sna.save_police_move_message_582f8"
    bl_label = "Save Police Move Message"
    bl_description = "Move the Message with the Cursor"
    bl_options = {"REGISTER", "UNDO"}
    sna_alert_loc_initial: bpy.props.FloatVectorProperty(name='alert_loc_initial', description='initial location of alert image', size=2, default=(1.0, 1.0), subtype='NONE', unit='NONE', min=1.0, step=10, precision=1)
    sna_alert_size_initial: bpy.props.FloatProperty(name='alert_size_initial', description='', default=1.0, subtype='NONE', unit='NONE', min=1.0, step=5, precision=1)
    cursor = "HAND"
    _handle = None
    _event = {}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        if not False or context.area.spaces[0].bl_rna.identifier == 'SpaceNodeEditor':
            return not False
        return False

    def save_event(self, event):
        event_options = ["type", "value", "alt", "shift", "ctrl", "oskey", "mouse_region_x", "mouse_region_y", "mouse_x", "mouse_y", "pressure", "tilt"]
        if bpy.app.version >= (3, 2, 1):
            event_options += ["type_prev", "value_prev"]
        for option in event_options: self._event[option] = getattr(event, option)

    def draw_callback_px(self, context):
        event = self._event
        if event.keys():
            event = dotdict(event)
            try:
                pass
            except Exception as error:
                print(error)

    def execute(self, context):
        global _582F8_running
        _582F8_running = False
        context.window.cursor_set("DEFAULT")
        for area in context.screen.areas:
            area.tag_redraw()
        return {"FINISHED"}

    def modal(self, context, event):
        global _582F8_running
        if not context.area or not _582F8_running:
            self.execute(context)
            return {'CANCELLED'}
        self.save_event(event)
        context.window.cursor_set('HAND')
        try:
            if ((event.type == 'ESC') or (event.type == 'RIGHTMOUSE')):
                bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location = self.sna_alert_loc_initial
                bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size = self.sna_alert_size_initial
                if event.type in ['RIGHTMOUSE', 'ESC']:
                    self.execute(context)
                    return {'CANCELLED'}
                return {"CANCELLED"}
            else:
                if ((event.type == 'LEFTMOUSE') or (event.type == 'RET')):
                    if event.type in ['RIGHTMOUSE', 'ESC']:
                        self.execute(context)
                        return {'CANCELLED'}
                    self.execute(context)
                    return {"FINISHED"}
                else:
                    if (event.type == 'WHEELUPMOUSE'):
                        bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size = float(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size + 10.0)
                    else:
                        if (event.type == 'WHEELDOWNMOUSE'):
                            bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size = float(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size - 10.0)
                        else:
                            bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location = (event.mouse_x, event.mouse_y)
                            if bpy.context and bpy.context.screen:
                                for a in bpy.context.screen.areas:
                                    a.tag_redraw()
        except Exception as error:
            print(error)
        if event.type in ['RIGHTMOUSE', 'ESC']:
            self.execute(context)
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        global _582F8_running
        if _582F8_running:
            _582F8_running = False
            return {'FINISHED'}
        else:
            self.save_event(event)
            self.start_pos = (event.mouse_x, event.mouse_y)
            bpy.context.window.cursor_warp(x=int(tuple(map(lambda v: int(v), bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location))[0]), y=int(tuple(map(lambda v: int(v), bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location))[1]), )
            self.sna_alert_loc_initial = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_location
            self.sna_alert_size_initial = bpy.context.preferences.addons['savepolice'].preferences.sna_alert_message_size
            context.window_manager.modal_handler_add(self)
            _582F8_running = True
            return {'RUNNING_MODAL'}


def sna_fn_removed_unused_images_A2907():
    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path)):
        if (property_exists("bpy.data.images", globals(), locals()) and os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path)) in bpy.data.images):
            if (0 == bpy.data.images[os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path))].users):
                bpy.data.images.remove(image=bpy.data.images[os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_path))], do_unlink=True, do_id_user=True, do_ui_user=True, )
    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)):
        if [os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))]:
            for i_BCF06 in range(len([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))])):
                if os.path.exists([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))][i_BCF06]):
                    if (property_exists("bpy.data.images", globals(), locals()) and os.path.basename([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))][i_BCF06]) in bpy.data.images):
                        if (0 == bpy.data.images[os.path.basename([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))][i_BCF06])].users):
                            bpy.data.images.remove(image=bpy.data.images[os.path.basename([os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f) for f in os.listdir(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory)) if os.path.isfile(os.path.join(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence_directory), f))][i_BCF06])], do_unlink=True, do_id_user=True, do_ui_user=True, )
    if os.path.exists(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))):
        if [os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f) for f in os.listdir(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))) if os.path.isfile(os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f))]:
            for i_85208 in range(len([os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f) for f in os.listdir(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))) if os.path.isfile(os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f))])):
                if os.path.exists([os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f) for f in os.listdir(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))) if os.path.isfile(os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f))][i_85208]):
                    if (property_exists("bpy.data.images", globals(), locals()) and os.path.basename([os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f) for f in os.listdir(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))) if os.path.isfile(os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f))][i_85208]) in bpy.data.images):
                        if (0 == bpy.data.images[os.path.basename([os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f) for f in os.listdir(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))) if os.path.isfile(os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f))][i_85208])].users):
                            bpy.data.images.remove(image=bpy.data.images[os.path.basename([os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f) for f in os.listdir(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'))) if os.path.isfile(os.path.join(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256')), f))][i_85208])], do_unlink=True, do_id_user=True, do_ui_user=True, )
    if os.path.exists(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'))):
        if (property_exists("bpy.data.images", globals(), locals()) and os.path.basename(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png'))) in bpy.data.images):
            if (0 == bpy.data.images[os.path.basename(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png')))].users):
                bpy.data.images.remove(image=bpy.data.images[os.path.basename(bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'Siren_256x256_Render0013.png')))], do_unlink=True, do_id_user=True, do_ui_user=True, )
    if os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background)):
        if (property_exists("bpy.data.images", globals(), locals()) and os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background)) in bpy.data.images):
            if (0 == bpy.data.images[os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background))].users):
                bpy.data.images.remove(image=bpy.data.images[os.path.basename(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_alert_background))], do_unlink=True, do_id_user=True, do_ui_user=True, )


class SNA_OT_Op_Start_Drawing_E7A6D(bpy.types.Operator):
    bl_idname = "sna.op_start_drawing_e7a6d"
    bl_label = "Op_Start_Drawing"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        handler_64666.append(bpy.types.SpaceNodeEditor.draw_handler_add(sna_function_execute_4A9EF, (os.path.join(os.path.dirname(__file__), 'assets', 'Becon Composites 256 x 256'), ), 'WINDOW', 'POST_PIXEL'))
        for a in bpy.context.screen.areas: a.tag_redraw()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Op_End_Drawing_3823D(bpy.types.Operator):
    bl_idname = "sna.op_end_drawing_3823d"
    bl_label = "Op_End_Drawing"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if handler_0B5B1:
            bpy.types.SpaceNodeEditor.draw_handler_remove(handler_0B5B1[0], 'WINDOW')
            handler_0B5B1.pop(0)
            for a in bpy.context.screen.areas: a.tag_redraw()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_function_execute_4A9EF(Asset):
    directory = Asset

    def get_sequence_length(directory):
        if not directory or not os.path.exists(directory):  # Check if the directory is empty or does not exist
            return 0
        try:
            files = [f for f in os.listdir(directory) if f.endswith('.png')]
            return min(len(files), 101)
        except Exception as e:
            print(f"An error occurred while getting the sequence length: {e}")
            return 0
    if directory:
        sequence_length = get_sequence_length(directory)
        start_frame_value = 0
        start_frame = max(0, min(100, start_frame_value))
        end_frame_value = 0
        end_frame = max(0, min(100, end_frame_value))
        start_frame = min(start_frame, end_frame)
        bl = (1.0, 1.0)
        coords = ((bl[0], bl[1]), (bl[0] + 100.0, bl[1]), (bl[0] + 
        100.0, bl[1] + 100.0), (bl[0], bl[1] + 
        100.0))

        def get_image_from_directory(dial_value, directory):
            files = [f for f in os.listdir(directory) if f.endswith('.png')]
            files.sort()
            sequence_length = min(get_sequence_length(directory), 101)
            if 0 <= dial_value < sequence_length:
                image_path = os.path.join(directory, files[dial_value])
                bpy.data.images.load(filepath=image_path, check_existing=True)
                return bpy.data.images[os.path.basename(image_path)]
            else:
                return None
        dial_value = 0
        image = get_image_from_directory(dial_value, directory)
        if image is not None:
            texture = gpu.texture.from_image(image)
            blender_version = bpy.app.version
            if blender_version >= (4, 0, 0):
                shader = gpu.shader.from_builtin('IMAGE')
            else: 
                shader = gpu.shader.from_builtin('2D_IMAGE')
            batch = gpu_extras.batch.batch_for_shader(
                shader, 'TRI_FAN',
                {
                    'pos': coords,
                    'texCoord': ((0, 0), (1, 0), (1, 1), (0, 1)),
                },
            )
            shader.bind()
            gpu.state.blend_set('ALPHA')
            shader.uniform_sampler('image', texture)
            batch.draw(shader)


def sna_add_to_filebrowser_mt_editor_menus_8EBE1(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_file_browser)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_assetbrowser_mt_editor_menus_EDC93(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_asset_browser)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_spreadsheet_ht_header_8B3EB(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_spreadhseet)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_fn_start_stop_save_police_timer_34567(Start_Timer):
    if Start_Timer:
        graph_scripts['sna_minutes'] = 0.0
        graph_scripts['sna_animation_minutes'] = 0
    graph_scripts['sna_timer_freq'] = int(bpy.context.preferences.addons['savepolice'].preferences.sna_interval * 60.0)
    graph_scripts['sna_timer_interval'] = bpy.context.preferences.addons['savepolice'].preferences.sna_interval
    graph_scripts['sna_timer_interval'] = 1
    start = Start_Timer
    timer_interval = bpy.context.preferences.addons['savepolice'].preferences.sna_interval
    timer_sec = 1
    timer_freq = int(bpy.context.preferences.addons['savepolice'].preferences.sna_interval * 60.0)
    if not start:
        if bpy.app.timers.is_registered(fn_save_police_timer_2):
            bpy.app.timers.unregister(fn_save_police_timer_2)
    else:
        if not bpy.app.timers.is_registered(fn_save_police_timer_2):
            bpy.app.timers.register(fn_save_police_timer_2)


def before_exit_handler_8A0D1():
    bpy.ops.sna.save_police_end_alert_image_preview_7a41b('INVOKE_DEFAULT', )


@persistent
def load_post_handler_0B793(dummy):
    bpy.context.scene.sna_save_police_interval = bpy.context.preferences.addons['savepolice'].preferences.sna_interval
    graph_scripts['sna_timer_freq'] = int(bpy.context.preferences.addons['savepolice'].preferences.sna_interval * 60.0)
    graph_scripts['sna_timer_interval'] = bpy.context.preferences.addons['savepolice'].preferences.sna_interval
    graph_scripts['sna_timer_interval'] = 1
    if (bpy.context.preferences.addons['savepolice'].preferences.sna_save_on_load and bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police):
        sna_fn_start_stop_save_police_timer_34567(False)
        if bool(bpy.data.filepath):
            pass
        else:
            bpy.ops.sna.op_save_police_saving_148e8('INVOKE_DEFAULT', )
            bpy.ops.wm.splash('INVOKE_DEFAULT', )
    if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police:

        def delayed_78357():
            bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police = True
        bpy.app.timers.register(delayed_78357, first_interval=1.0)
        bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police = False
    print('🚨 Save Police: Save Startup is Active')


@persistent
def save_post_handler_70958(dummy):
    bpy.context.scene.sna_save_police_reminder = False
    if bpy.context.preferences.addons['savepolice'].preferences.sna_change_theme:
        bpy.ops.sna.op_annoy_restore_theme_colors_954ce('INVOKE_DEFAULT', )
    sna_fn_start_stop_save_police_timer_34567(False)
    if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police:
        sna_fn_start_stop_save_police_timer_34567(True)
    if (bpy.context.preferences.addons['savepolice'].preferences.sna_interval != bpy.context.scene.sna_save_police_interval):
        bpy.context.scene.sna_save_police_interval = bpy.context.preferences.addons['savepolice'].preferences.sna_interval
    if bpy.context.scene.sna_save_police_animation_active:
        bpy.ops.sna.save_police_end_alert_image_preview_7a41b('INVOKE_DEFAULT', )
    sna_fn_removed_unused_images_A2907()
    if ((not bpy.context.scene.sna_save_police_reminder) and (not bpy.context.scene.sna_save_police_countdown_active) and bpy.context.preferences.addons['savepolice'].preferences.sna_use_countdown and bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police):
        bpy.ops.sna.save_police_preview_countdown_8b9f0('INVOKE_DEFAULT', )


class SNA_OT_Op_Save_Police_Saving_148E8(bpy.types.Operator):
    bl_idname = "sna.op_save_police_saving_148e8"
    bl_label = "Op Save Police Saving"
    bl_description = "Time for a save"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bool(bpy.data.filepath):
            print('🚨 Save Police: Attempting a file save')
            if ((len(os.path.basename(bpy.data.filepath)) > 0) and (len(bpy.context.preferences.addons['savepolice'].preferences.sna_default_save_prefix) > 0) and bpy.context.preferences.addons['savepolice'].preferences.sna_default_save_prefix in bpy.data.filepath and bpy.context.preferences.addons['savepolice'].preferences.sna_save_default_file):
                bpy.ops.wm.save_mainfile(filepath=bpy.path.abspath(os.path.join(bpy.context.preferences.addons['savepolice'].preferences.sna_default_folder,bpy.context.preferences.addons['savepolice'].preferences.sna_default_save_prefix + '_' + str(datetime.now().date().year) + '-' + str(datetime.now().date().month) + '-' + str(datetime.now().date().day) + '_' + str(datetime.now().time().hour) + '-' + str(datetime.now().time().minute) + '-' + str(datetime.now().time().second) + '.blend')))
            else:
                bpy.ops.wm.save_mainfile(filepath=bpy.data.filepath, incremental=bpy.context.preferences.addons['savepolice'].preferences.sna_incremental_saving)
                self.report({'INFO'}, message='🚨 Saved: ' + bpy.data.filepath)
        else:
            if bpy.context.preferences.addons['savepolice'].preferences.sna_save_default_file:
                print('🚨 Save Police: Attempting a default file save')
                if os.path.exists(bpy.context.preferences.addons['savepolice'].preferences.sna_default_folder):
                    bpy.ops.wm.save_mainfile(filepath=bpy.path.abspath(os.path.join(bpy.context.preferences.addons['savepolice'].preferences.sna_default_folder,bpy.context.preferences.addons['savepolice'].preferences.sna_default_save_prefix + '_' + str(datetime.now().date().year) + '-' + str(datetime.now().date().month) + '-' + str(datetime.now().date().day) + '_' + str(datetime.now().time().hour) + '-' + str(datetime.now().time().minute) + '-' + str(datetime.now().time().second) + '.blend')))
                    self.report({'INFO'}, message='🚨 Saved: ' + bpy.data.filepath)
            else:
                bpy.ops.wm.save_mainfile('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Op_Annoy_Store_And_Swap_Theme_Colors_C1B7F(bpy.types.Operator):
    bl_idname = "sna.op_annoy_store_and_swap_theme_colors_c1b7f"
    bl_label = "Op Annoy Store and Swap Theme Colors"
    bl_description = "Store and swap theme colors to remind to save"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (not bpy.context.scene.sna_save_police_theme_active):
            bpy.context.scene.sna_theme_color__menu = bpy.context.preferences.themes['Default'].user_interface.wcol_menu.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_menu.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__list_item = bpy.context.preferences.themes['Default'].user_interface.wcol_list_item.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_list_item.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__list_item_sel = bpy.context.preferences.themes['Default'].user_interface.wcol_list_item.text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_list_item.text_sel = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__number = bpy.context.preferences.themes['Default'].user_interface.wcol_num.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_num.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__option = bpy.context.preferences.themes['Default'].user_interface.wcol_option.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_option.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__pulldown = bpy.context.preferences.themes['Default'].user_interface.wcol_pulldown.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_pulldown.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__regular = bpy.context.preferences.themes['Default'].user_interface.wcol_regular.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_regular.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__tab = bpy.context.preferences.themes['Default'].user_interface.wcol_tab.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_tab.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__tab_sel = bpy.context.preferences.themes['Default'].user_interface.wcol_tab.text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_tab.text_sel = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__radio_buttons = bpy.context.preferences.themes['Default'].user_interface.wcol_radio.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_radio.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__text = bpy.context.preferences.themes['Default'].user_interface.wcol_text.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_text.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__tool = bpy.context.preferences.themes['Default'].user_interface.wcol_tool.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_tool.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__toolbar_item_selected = bpy.context.preferences.themes['Default'].user_interface.wcol_toolbar_item.inner_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_toolbar_item.inner_sel = (bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color[0], bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color[1], bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color[2], 1.0)
            bpy.context.scene.sna_theme_color__value_slider = bpy.context.preferences.themes['Default'].user_interface.wcol_numslider.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_numslider.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__toggle_text = bpy.context.preferences.themes['Default'].user_interface.wcol_toggle.text
            bpy.context.preferences.themes['Default'].user_interface.wcol_toggle.text = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__toggle_text_sel = bpy.context.preferences.themes['Default'].user_interface.wcol_toggle.text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_toggle.text_sel = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__scroll_bar_item = bpy.context.preferences.themes['Default'].user_interface.wcol_scroll.item
            bpy.context.preferences.themes['Default'].user_interface.wcol_scroll.item = (bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color[0], bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color[1], bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color[2], 1.0)
            bpy.context.scene.sna_theme_color__regular_sel = bpy.context.preferences.themes['Default'].user_interface.wcol_regular.text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_regular.text_sel = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__radio_buttons_sel = bpy.context.preferences.themes['Default'].user_interface.wcol_radio.text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_radio.text_sel = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_theme_color__option_text_sel = bpy.context.preferences.themes['Default'].user_interface.wcol_option.text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_option.text_sel = bpy.context.preferences.addons['savepolice'].preferences.sna_save_police_annoy_color
            bpy.context.scene.sna_save_police_theme_active = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Op_Annoy_Restore_Theme_Colors_954Ce(bpy.types.Operator):
    bl_idname = "sna.op_annoy_restore_theme_colors_954ce"
    bl_label = "Op Annoy Restore Theme Colors"
    bl_description = "Restore theme colors after annoying is complete"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.scene.sna_save_police_theme_active:
            bpy.context.preferences.themes['Default'].user_interface.wcol_menu.text = bpy.context.scene.sna_theme_color__menu
            bpy.context.preferences.themes['Default'].user_interface.wcol_list_item.text = bpy.context.scene.sna_theme_color__list_item
            bpy.context.preferences.themes['Default'].user_interface.wcol_list_item.text_sel = bpy.context.scene.sna_theme_color__list_item_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_num.text = bpy.context.scene.sna_theme_color__number
            bpy.context.preferences.themes['Default'].user_interface.wcol_option.text = bpy.context.scene.sna_theme_color__option
            bpy.context.preferences.themes['Default'].user_interface.wcol_pulldown.text = bpy.context.scene.sna_theme_color__pulldown
            bpy.context.preferences.themes['Default'].user_interface.wcol_regular.text = bpy.context.scene.sna_theme_color__regular
            bpy.context.preferences.themes['Default'].user_interface.wcol_tab.text = bpy.context.scene.sna_theme_color__tab
            bpy.context.preferences.themes['Default'].user_interface.wcol_tab.text_sel = bpy.context.scene.sna_theme_color__tab_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_radio.text = bpy.context.scene.sna_theme_color__radio_buttons
            bpy.context.preferences.themes['Default'].user_interface.wcol_text.text = bpy.context.scene.sna_theme_color__text
            bpy.context.preferences.themes['Default'].user_interface.wcol_tool.text = bpy.context.scene.sna_theme_color__tool
            bpy.context.preferences.themes['Default'].user_interface.wcol_toolbar_item.inner_sel = bpy.context.scene.sna_theme_color__toolbar_item_selected
            bpy.context.preferences.themes['Default'].user_interface.wcol_numslider.text = bpy.context.scene.sna_theme_color__value_slider
            bpy.context.preferences.themes['Default'].user_interface.wcol_toggle.text = bpy.context.scene.sna_theme_color__toggle_text
            bpy.context.preferences.themes['Default'].user_interface.wcol_toggle.text_sel = bpy.context.scene.sna_theme_color__toggle_text_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_scroll.item = bpy.context.scene.sna_theme_color__scroll_bar_item
            bpy.context.preferences.themes['Default'].user_interface.wcol_regular.text_sel = bpy.context.scene.sna_theme_color__regular_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_radio.text_sel = bpy.context.scene.sna_theme_color__radio_buttons_sel
            bpy.context.preferences.themes['Default'].user_interface.wcol_option.text_sel = bpy.context.scene.sna_theme_color__option_text_sel
            bpy.context.scene.sna_save_police_theme_active = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Op_Preview_Theme_Change_2Ea4A(bpy.types.Operator):
    bl_idname = "sna.op_preview_theme_change_2ea4a"
    bl_label = "Op Preview Theme Change"
    bl_description = "See a 3 second preview of your alert via theme changing color"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('Theme is already active. Preview is disabled')
        return not bpy.context.scene.sna_save_police_theme_active

    def execute(self, context):

        def delayed_CDF5B():
            bpy.ops.sna.op_annoy_restore_theme_colors_954ce('INVOKE_DEFAULT', )
        bpy.app.timers.register(delayed_CDF5B, first_interval=3.0)
        bpy.ops.sna.op_annoy_store_and_swap_theme_colors_c1b7f('INVOKE_DEFAULT', )
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def fn_save_police_timer_2():
    #print("Running")
    temp_duration = (graph_scripts['sna_timer_interval']*graph_scripts['sna_timer_freq'])
    if bpy.data.is_dirty:
        if graph_scripts['sna_minutes'] >= temp_duration:
            graph_scripts['sna_minutes'] = 1
            bpy.context.scene.sna_save_police_reminder = True
            if bpy.context and bpy.context.screen:
                for a in bpy.context.screen.areas:
                    a.tag_redraw()
        else:
            graph_scripts['sna_minutes'] += 1
        #print(f"Save Police timer is running for {graph_scripts['sna_minutes']} seconds")
    else:
        if bpy.context.scene.sna_save_police_reminder:
            bpy.context.scene.sna_save_police_reminder = False
    temp_time_remaining_sec = temp_duration - graph_scripts['sna_minutes']
    temp_time_remaining_min = temp_time_remaining_sec/60
    if temp_time_remaining_min < 1.0:
        graph_scripts['sna_time_remaining'] = temp_time_remaining_sec
        graph_scripts['sna_time_message'] = str(round(graph_scripts['sna_time_remaining'],1)) + ' sec'
    else:
        graph_scripts['sna_time_remaining'] = temp_time_remaining_min
        graph_scripts['sna_time_message'] = str(round(graph_scripts['sna_time_remaining'],1)) + ' min'
    return graph_scripts['sna_timer_sec']


def sna_add_to_view3d_mt_editor_menus_9786F(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_3d_viewport)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_ui_fn_animate_icons_E6878(layout_function, ):
    row_D5430 = layout_function.row(heading='', align=True)
    row_D5430.alert = False
    row_D5430.enabled = True
    row_D5430.active = True
    row_D5430.use_property_split = False
    row_D5430.use_property_decorate = False
    row_D5430.scale_x = 1.0
    row_D5430.scale_y = 1.0
    row_D5430.alignment = 'Expand'.upper()
    row_D5430.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    row_D5430.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_call_the_save_police', text='', icon_value=((((((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0023.png') if (graph_scripts['sna_animation_minutes'] > 4) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0019.png')) if (graph_scripts['sna_animation_minutes'] > 3) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if (graph_scripts['sna_animation_minutes'] > 2) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0007.png')) if (graph_scripts['sna_animation_minutes'] > 1) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0001.png')) if bpy.context.preferences.addons['savepolice'].preferences.sna_animate else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if bpy.context.scene.sna_save_police_reminder else ((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_blue_256x256.png') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_grey_256x256.png')) if bpy.data.is_dirty else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_green_256x256.png'))), emboss=False, toggle=True)
    row_D5430.label(text=((((graph_scripts['sna_time_message'] if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_on_ui else '') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else '') if (not bpy.context.scene.sna_save_police_reminder) else '') if bpy.data.is_dirty else ''), icon_value=0)
    if (bpy.context.scene.sna_save_police_reminder and bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only):
        row_D5430.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\S.png'))
        row_D5430.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\A.png'))
        row_D5430.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\V.png'))
        row_D5430.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\E.png'))


def sna_add_to_console_mt_editor_menus_F4F8C(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_console)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_info_mt_editor_menus_80618(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_info_log)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_text_mt_editor_menus_DB6C3(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_text_editor)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_topbar_mt_editor_menus_1996C(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_header)):
        layout = self.layout
        row_A10DE = layout.row(heading='', align=True)
        row_A10DE.alert = False
        row_A10DE.enabled = True
        row_A10DE.active = True
        row_A10DE.use_property_split = False
        row_A10DE.use_property_decorate = False
        row_A10DE.scale_x = 1.0
        row_A10DE.scale_y = 1.0
        row_A10DE.alignment = 'Expand'.upper()
        row_A10DE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_A10DE.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_call_the_save_police', text='', icon_value=((((((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0023.png') if (graph_scripts['sna_animation_minutes'] > 4) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0019.png')) if (graph_scripts['sna_animation_minutes'] > 3) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if (graph_scripts['sna_animation_minutes'] > 2) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0007.png')) if (graph_scripts['sna_animation_minutes'] > 1) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0001.png')) if bpy.context.preferences.addons['savepolice'].preferences.sna_animate else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if bpy.context.scene.sna_save_police_reminder else ((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_blue_256x256.png') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_grey_256x256.png')) if bpy.data.is_dirty else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_green_256x256.png'))), emboss=False, toggle=True)
        row_A10DE.label(text=((((graph_scripts['sna_time_message'] if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_on_ui else '') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else '') if (not bpy.context.scene.sna_save_police_reminder) else '') if bpy.data.is_dirty else ''), icon_value=0)
        if (bpy.context.scene.sna_save_police_reminder and bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only):
            row_A10DE.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\S.png'))
            row_A10DE.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\A.png'))
            row_A10DE.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\V.png'))
            row_A10DE.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\E.png'))


def sna_add_to_statusbar_ht_header_11903(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_footer)):
        layout = self.layout
        row_9EFD5 = layout.row(heading='', align=True)
        row_9EFD5.alert = False
        row_9EFD5.enabled = True
        row_9EFD5.active = True
        row_9EFD5.use_property_split = False
        row_9EFD5.use_property_decorate = False
        row_9EFD5.scale_x = 1.0
        row_9EFD5.scale_y = 1.0
        row_9EFD5.alignment = 'Expand'.upper()
        row_9EFD5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_9EFD5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_call_the_save_police', text='', icon_value=((((((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0023.png') if (graph_scripts['sna_animation_minutes'] > 4) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0019.png')) if (graph_scripts['sna_animation_minutes'] > 3) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if (graph_scripts['sna_animation_minutes'] > 2) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0007.png')) if (graph_scripts['sna_animation_minutes'] > 1) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0001.png')) if bpy.context.preferences.addons['savepolice'].preferences.sna_animate else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if bpy.context.scene.sna_save_police_reminder else ((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_blue_256x256.png') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_grey_256x256.png')) if bpy.data.is_dirty else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_green_256x256.png'))), emboss=False, toggle=True)
        row_9EFD5.label(text=((((graph_scripts['sna_time_message'] if bpy.context.preferences.addons['savepolice'].preferences.sna_countdown_on_ui else '') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else '') if (not bpy.context.scene.sna_save_police_reminder) else '') if bpy.data.is_dirty else ''), icon_value=0)
        if (bpy.context.scene.sna_save_police_reminder and bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only):
            row_9EFD5.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\S.png'))
            row_9EFD5.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\A.png'))
            row_9EFD5.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\V.png'))
            row_9EFD5.label(text='', icon_value=load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Save Icons\E.png'))


def sna_add_to_node_mt_editor_menus_5168E(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_node_editors)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_outliner_ht_header_F6026(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_outliner)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_userpref_mt_editor_menus_095CF(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_preferences)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_properties_ht_header_B2B08(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_properties)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_ui_fn_save_police_B9591(layout_function, ):
    col_6ADD0 = layout_function.column(heading='', align=True)
    col_6ADD0.alert = False
    col_6ADD0.enabled = True
    col_6ADD0.active = True
    col_6ADD0.use_property_split = True
    col_6ADD0.use_property_decorate = False
    col_6ADD0.scale_x = 1.0
    col_6ADD0.scale_y = 1.0
    col_6ADD0.alignment = 'Expand'.upper()
    col_6ADD0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_6ADD0.label(text='General', icon_value=0)
    col_6ADD0.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_call_the_save_police', text='Activate', icon_value=0, emboss=True, toggle=True)
    col_E9CE3 = col_6ADD0.column(heading='', align=True)
    col_E9CE3.alert = False
    col_E9CE3.enabled = (not bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police)
    col_E9CE3.active = True
    col_E9CE3.use_property_split = True
    col_E9CE3.use_property_decorate = False
    col_E9CE3.scale_x = 1.0
    col_E9CE3.scale_y = 1.0
    col_E9CE3.alignment = 'Expand'.upper()
    col_E9CE3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_E9CE3.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_interval', text='Timer (min)', icon_value=0, emboss=True, toggle=True)
    col_E9CE3.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_update_screen_areas', text='Always Update Screen', icon_value=0, emboss=True, toggle=True)
    col_6ADD0.separator(factor=2.0)
    col_6ADD0.label(text='Defaults (Worry-Free Save)', icon_value=0)
    col_6ADD0.label(text='Prefix_YYYY-MM-DD_HH_MM_SS', icon_value=0)
    col_1F900 = col_6ADD0.column(heading='', align=True)
    col_1F900.alert = False
    col_1F900.enabled = True
    col_1F900.active = (not bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only)
    col_1F900.use_property_split = True
    col_1F900.use_property_decorate = False
    col_1F900.scale_x = 1.0
    col_1F900.scale_y = 1.0
    col_1F900.alignment = 'Expand'.upper()
    col_1F900.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_1F900.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_save_default_file', text='Default Save', icon_value=_icons['Save Icon.png'].icon_id, emboss=True, toggle=True)
    col_6ADD0.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_save_on_load', text='Startup Save', icon_value=15, emboss=True, toggle=True)
    col_B91E4 = col_6ADD0.column(heading='', align=True)
    col_B91E4.alert = False
    col_B91E4.enabled = True
    col_B91E4.active = bpy.context.preferences.addons['savepolice'].preferences.sna_save_default_file
    col_B91E4.use_property_split = True
    col_B91E4.use_property_decorate = False
    col_B91E4.scale_x = 1.0
    col_B91E4.scale_y = 1.0
    col_B91E4.alignment = 'Expand'.upper()
    col_B91E4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_B91E4.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_default_folder', text='Default Folder', icon_value=0, emboss=True)
    col_B91E4.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_default_save_prefix', text='Prefix', icon_value=0, emboss=True)
    if (os.path.exists(bpy.path.abspath(bpy.context.preferences.addons['savepolice'].preferences.sna_default_folder)) and bpy.context.preferences.addons['savepolice'].preferences.sna_save_default_file):
        row_1400C = col_B91E4.row(heading='', align=False)
        row_1400C.alert = False
        row_1400C.enabled = True
        row_1400C.active = True
        row_1400C.use_property_split = True
        row_1400C.use_property_decorate = False
        row_1400C.scale_x = 1.0
        row_1400C.scale_y = 1.0
        row_1400C.alignment = 'Right'.upper()
        row_1400C.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_1400C.label(text=bpy.path.abspath(os.path.join(bpy.context.preferences.addons['savepolice'].preferences.sna_default_folder,bpy.context.preferences.addons['savepolice'].preferences.sna_default_save_prefix + '_' + str(datetime.now().date().year) + '-' + str(datetime.now().date().month) + '-' + str(datetime.now().date().day) + '_' + str(datetime.now().time().hour) + '-' + str(datetime.now().time().minute) + '-' + str(datetime.now().time().second) + '.blend')), icon_value=0)
    col_B91E4.separator(factor=2.0)
    col_6ADD0.label(text='Advanced', icon_value=15)
    col_6ADD0.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_incremental_saving', text='Increment Saves', icon_value=695, emboss=True, toggle=True)
    col_6ADD0.separator(factor=2.0)


def sna_ui_fn_save_police_alerts_props_C4E09(layout_function, ):
    col_ACFCB = layout_function.column(heading='', align=True)
    col_ACFCB.alert = False
    col_ACFCB.enabled = True
    col_ACFCB.active = True
    col_ACFCB.use_property_split = True
    col_ACFCB.use_property_decorate = False
    col_ACFCB.scale_x = 1.0
    col_ACFCB.scale_y = 1.0
    col_ACFCB.alignment = 'Expand'.upper()
    col_ACFCB.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_ACFCB.label(text='Alerts Only (No Autosave)', icon_value=((((((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0023.png') if (graph_scripts['sna_animation_minutes'] > 4) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0019.png')) if (graph_scripts['sna_animation_minutes'] > 3) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if (graph_scripts['sna_animation_minutes'] > 2) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0007.png')) if (graph_scripts['sna_animation_minutes'] > 1) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0001.png')) if bpy.context.preferences.addons['savepolice'].preferences.sna_animate else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if bpy.context.scene.sna_save_police_reminder else ((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_blue_256x256.png') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_grey_256x256.png')) if bpy.data.is_dirty else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_green_256x256.png'))))
    col_ACFCB.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_annoyance_only', text='Alert Instead', icon_value=((((((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0023.png') if (graph_scripts['sna_animation_minutes'] > 4) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0019.png')) if (graph_scripts['sna_animation_minutes'] > 3) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if (graph_scripts['sna_animation_minutes'] > 2) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0007.png')) if (graph_scripts['sna_animation_minutes'] > 1) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0001.png')) if bpy.context.preferences.addons['savepolice'].preferences.sna_animate else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if bpy.context.scene.sna_save_police_reminder else ((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_blue_256x256.png') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_grey_256x256.png')) if bpy.data.is_dirty else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_green_256x256.png'))), emboss=True, toggle=True)
    if bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only:
        pass


def sna_ui_fn_save_police_alert_image_78119(layout_function, ):
    col_17647 = layout_function.column(heading='', align=True)
    col_17647.alert = False
    col_17647.enabled = True
    col_17647.active = True
    col_17647.use_property_split = True
    col_17647.use_property_decorate = False
    col_17647.scale_x = 1.0
    col_17647.scale_y = 1.0
    col_17647.alignment = 'Expand'.upper()
    col_17647.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_17647.separator(factor=2.0)
    if bpy.context.preferences.addons['savepolice'].preferences.sna_annoyance_only:
        col_17647.label(text='Image', icon_value=183)
        col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_use_image', text='Use Image', icon_value=764, emboss=True)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_image:
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_siren_image_sequence', text='Image Sequence', icon_value=697, emboss=True)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:
                col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_siren_interval', text='Interval (sec)', icon_value=0, emboss=True)
            col_17647.separator(factor=2.0)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_siren_custom', text=('Custom Sequence' if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence else 'Custom Image'), icon_value=(111 if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence else 696), emboss=True)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_custom:
                if bpy.context.preferences.addons['savepolice'].preferences.sna_siren_image_sequence:
                    col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_siren_image_sequence_directory', text='Sequence Folder', icon_value=0, emboss=True)
                else:
                    col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_siren_image_path', text='Image Path', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_siren_image_size', text='Size', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_image_location', text='Location', icon_value=0, emboss=True)
            col_21B14 = col_17647.column(heading='', align=True)
            col_21B14.alert = False
            col_21B14.enabled = True
            col_21B14.active = True
            col_21B14.use_property_split = True
            col_21B14.use_property_decorate = False
            col_21B14.scale_x = 1.0
            col_21B14.scale_y = 1.0
            col_21B14.alignment = 'Expand'.upper()
            col_21B14.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            split_8720C = col_21B14.split(factor=0.5, align=True)
            split_8720C.alert = False
            split_8720C.enabled = bpy.context.scene.sna_save_police_animation_active
            split_8720C.active = True
            split_8720C.use_property_split = False
            split_8720C.use_property_decorate = False
            split_8720C.scale_x = 1.0
            split_8720C.scale_y = 1.0
            split_8720C.alignment = 'Expand'.upper()
            if not True: split_8720C.operator_context = "EXEC_DEFAULT"
            split_8720C.label(text='', icon_value=0)
            op = split_8720C.operator('sna.save_police_move_image_f9f28', text='Set with Cursor', icon_value=256, emboss=True, depress=False)
        col_17647.separator(factor=2.0)
        col_17647.label(text='Message', icon_value=701)
        col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_use_message', text='Use Message', icon_value=701, emboss=True, toggle=True)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_message:
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_message', text='Message', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_message_size', text='Size', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_font', text='Font', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_message_dpi', text='DPI', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_message_wrap', text='Wrap Width', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_color', text='Color', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_message_location', text='Location', icon_value=0, emboss=True)
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_message_rotation', text='Rotation', icon_value=0, emboss=True)
            col_086E8 = col_17647.column(heading='', align=True)
            col_086E8.alert = False
            col_086E8.enabled = True
            col_086E8.active = True
            col_086E8.use_property_split = True
            col_086E8.use_property_decorate = False
            col_086E8.scale_x = 1.0
            col_086E8.scale_y = 1.0
            col_086E8.alignment = 'Expand'.upper()
            col_086E8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            split_0F711 = col_086E8.split(factor=0.5, align=True)
            split_0F711.alert = False
            split_0F711.enabled = bpy.context.scene.sna_save_police_animation_active
            split_0F711.active = True
            split_0F711.use_property_split = False
            split_0F711.use_property_decorate = False
            split_0F711.scale_x = 1.0
            split_0F711.scale_y = 1.0
            split_0F711.alignment = 'Expand'.upper()
            if not True: split_0F711.operator_context = "EXEC_DEFAULT"
            split_0F711.label(text='', icon_value=0)
            op = split_0F711.operator('sna.save_police_move_message_582f8', text='Set with Cursor', icon_value=256, emboss=True, depress=False)
            op.sna_alert_size_initial = 0.0
        col_17647.separator(factor=2.0)
        col_17647.label(text='Background', icon_value=362)
        col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_use_background', text='Use Background', icon_value=27, emboss=True, toggle=True)
        if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_use_background:
            col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_custom_background', text='Custom Background', icon_value=362, emboss=True, toggle=True)
            if bpy.context.preferences.addons['savepolice'].preferences.sna_alert_custom_background:
                col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_background', text='Background', icon_value=0, emboss=True)
            else:
                col_17647.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_background_color', text='Background Color', icon_value=0, emboss=True)
            col_17647.separator(factor=1.0)
            split_DC8D8 = col_17647.split(factor=0.5, align=True)
            split_DC8D8.alert = False
            split_DC8D8.enabled = True
            split_DC8D8.active = True
            split_DC8D8.use_property_split = False
            split_DC8D8.use_property_decorate = False
            split_DC8D8.scale_x = 1.0
            split_DC8D8.scale_y = 1.0
            split_DC8D8.alignment = 'Expand'.upper()
            if not True: split_DC8D8.operator_context = "EXEC_DEFAULT"
            split_DC8D8.label(text='', icon_value=0)
        if bpy.context.scene.sna_save_police_animation_active:
            op = col_17647.operator('sna.save_police_end_alert_image_preview_7a41b', text='End Preview', icon_value=3, emboss=True, depress=False)
        else:
            op = col_17647.operator('sna.save_police_preview_alert_image_558a3', text='Preview Alert', icon_value=503, emboss=True, depress=False)


def sna_ui_fn_alert_countdown_090BA(layout_function, ):
    col_052C5 = layout_function.column(heading='', align=True)
    col_052C5.alert = False
    col_052C5.enabled = True
    col_052C5.active = True
    col_052C5.use_property_split = True
    col_052C5.use_property_decorate = False
    col_052C5.scale_x = 1.0
    col_052C5.scale_y = 1.0
    col_052C5.alignment = 'Expand'.upper()
    col_052C5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_052C5.label(text='Countdown', icon_value=678)
    col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_use_countdown', text='Draw Countdown', icon_value=678, emboss=True, toggle=True)
    if bpy.context.preferences.addons['savepolice'].preferences.sna_use_countdown:
        col_052C5.separator(factor=1.0)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_suffix_message', text='Suffix', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_size', text='Size', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_font', text='Font', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_dpi', text='DPI', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_wrap', text='Wrap Width', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_color', text='Color', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_location', text='Location', icon_value=0, emboss=True)
        col_052C5.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_rotation', text='Rotation', icon_value=0, emboss=True)
        col_5FA86 = col_052C5.column(heading='', align=True)
        col_5FA86.alert = False
        col_5FA86.enabled = True
        col_5FA86.active = True
        col_5FA86.use_property_split = True
        col_5FA86.use_property_decorate = False
        col_5FA86.scale_x = 1.0
        col_5FA86.scale_y = 1.0
        col_5FA86.alignment = 'Expand'.upper()
        col_5FA86.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        split_D8148 = col_5FA86.split(factor=0.5, align=True)
        split_D8148.alert = False
        split_D8148.enabled = bpy.context.scene.sna_save_police_countdown_active
        split_D8148.active = True
        split_D8148.use_property_split = False
        split_D8148.use_property_decorate = False
        split_D8148.scale_x = 1.0
        split_D8148.scale_y = 1.0
        split_D8148.alignment = 'Expand'.upper()
        if not True: split_D8148.operator_context = "EXEC_DEFAULT"
        split_D8148.label(text='', icon_value=0)
        op = split_D8148.operator('sna.save_police_move_countdown_da3ac', text='Set with Cursor', icon_value=256, emboss=True, depress=False)
        if bpy.context.scene.sna_save_police_countdown_active:
            op = col_5FA86.operator('sna.save_police_end_countdown_preview_8f673', text='End Preview', icon_value=3, emboss=True, depress=False)
        else:
            op = col_5FA86.operator('sna.save_police_preview_countdown_8b9f0', text='Preview Countdown', icon_value=503, emboss=True, depress=False)


def sna_ui_fn_save_police_ui_settings_8BC5F(layout_function, ):
    col_AFDCC = layout_function.column(heading='', align=True)
    col_AFDCC.alert = False
    col_AFDCC.enabled = True
    col_AFDCC.active = True
    col_AFDCC.use_property_split = True
    col_AFDCC.use_property_decorate = False
    col_AFDCC.scale_x = 1.0
    col_AFDCC.scale_y = 1.0
    col_AFDCC.alignment = 'Expand'.upper()
    col_AFDCC.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    col_AFDCC.label(text='Toggle UI', icon_value=107)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_countdown_on_ui', text='Countdown on UI', icon_value=678, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_header', text='Header', icon_value=49, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_footer', text='Footer', icon_value=50, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_3d_viewport', text='3D Viewport', icon_value=104, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_image_editor', text='Image Editor', icon_value=109, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_node_editors', text='Node Editors', icon_value=24, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_video_sequencer', text='VSE', icon_value=111, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_movie_clip_editor', text='Movie Clip', icon_value=123, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_dopesheet', text='Dope Sheet', icon_value=115, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_timeline', text='Timeline', icon_value=118, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_nla', text='NLA Editor', icon_value=116, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_text_editor', text='Text Editor', icon_value=112, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_console', text='Console', icon_value=121, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_info_log', text='Info Log', icon_value=110, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_outliner', text='Outliner', icon_value=106, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_properties', text='Properties', icon_value=107, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_file_browser', text='File Browser', icon_value=108, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_asset_browser', text='Asset Browser', icon_value=124, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_spreadhseet', text='Spreadsheet', icon_value=113, emboss=True)
    col_AFDCC.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_alert_preferences', text='Preferences', icon_value=117, emboss=True)


class SNA_PT_SAVE_POLICE_99DE7(bpy.types.Panel):
    bl_label = 'Save Police'
    bl_idname = 'SNA_PT_SAVE_POLICE_99DE7'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Tool'
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout
        layout.prop(bpy.context.preferences.addons['savepolice'].preferences, 'sna_call_the_save_police', text='', icon_value=((((((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0023.png') if (graph_scripts['sna_animation_minutes'] > 4) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0019.png')) if (graph_scripts['sna_animation_minutes'] > 3) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if (graph_scripts['sna_animation_minutes'] > 2) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0007.png')) if (graph_scripts['sna_animation_minutes'] > 1) else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0001.png')) if bpy.context.preferences.addons['savepolice'].preferences.sna_animate else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Becon Composites 256 x 256\Siren_256x256_Render0013.png')) if bpy.context.scene.sna_save_police_reminder else ((load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_blue_256x256.png') if bpy.context.preferences.addons['savepolice'].preferences.sna_call_the_save_police else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_grey_256x256.png')) if bpy.data.is_dirty else load_preview_icon(r'Z:\my-bucket-one\Dev\Personal\Save Police\Icons\Siren_green_256x256.png'))), emboss=False)

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_save_police_B9591(layout_function, )


class SNA_PT_SAVE_POLICE_POPOVER_0C41B(bpy.types.Panel):
    bl_label = 'Save Police Popover'
    bl_idname = 'SNA_PT_SAVE_POLICE_POPOVER_0C41B'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = ''
    bl_order = 0
    bl_options = {'HIDE_HEADER'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_save_police_B9591(layout_function, )
        layout_function = layout
        sna_ui_fn_alert_countdown_090BA(layout_function, )
        layout_function = layout
        sna_ui_fn_save_police_alerts_props_C4E09(layout_function, )
        layout_function = layout
        sna_ui_fn_save_police_alert_image_78119(layout_function, )
        layout_function = layout
        sna_ui_fn_save_police_ui_settings_8BC5F(layout_function, )


def sna_add_to_dopesheet_mt_editor_menus_B8DDE(self, context):
    if not (False):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_time_mt_editor_menus_C76A9(self, context):
    if not (False):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_graph_mt_editor_menus_6C0C5(self, context):
    if not (False):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_nla_mt_editor_menus_DEEAC(self, context):
    if not (False):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_image_mt_editor_menus_FB521(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_image_editor)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_sequencer_mt_editor_menus_D0459(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_video_sequencer)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


def sna_add_to_clip_mt_tracking_editor_menus_7CC27(self, context):
    if not ((not bpy.context.preferences.addons['savepolice'].preferences.sna_alert_movie_clip_editor)):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_animate_icons_E6878(layout_function, )


class SNA_AddonPreferences_70C5B(bpy.types.AddonPreferences):
    bl_idname = 'savepolice'
    sna_call_the_save_police: bpy.props.BoolProperty(name='Call the Save Police', description='Let the police handle the saving from here on out', default=False, update=sna_update_sna_call_the_save_police_8EE76)
    sna_annoyance_only: bpy.props.BoolProperty(name='Annoyance Only', description='Alert only without actually saving', default=False, update=sna_update_sna_annoyance_only_1467F)
    sna_save_police_annoy_color: bpy.props.FloatVectorProperty(name='Save Police Annoy Color', description='The annoyance color', size=3, default=(1.0, 0.11900000274181366, 0.07000000029802322), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    sna_interval: bpy.props.IntProperty(name='Interval', description='Set the number of minutes before the save police intervene', default=10, subtype='TIME', min=1, soft_max=1440, update=sna_update_sna_interval_CA391)
    sna_save_default_file: bpy.props.BoolProperty(name='Save Default File', description='Save a default file when no file save exists', default=False)
    sna_default_folder: bpy.props.StringProperty(name='Default Folder', description='If no save file exists then auto save file here. Leave blank to disable default saving', default='', subtype='DIR_PATH', maxlen=0)
    sna_default_save_prefix: bpy.props.StringProperty(name='Default Save Prefix', description='Enter a prefix for the default save', default='SavePolice', subtype='NONE', maxlen=0)
    sna_save_on_load: bpy.props.BoolProperty(name='Save On Load', description='Save on blender startup or when loading a file', default=False)
    sna_incremental_saving: bpy.props.BoolProperty(name='Incremental Saving', description='Use incremental saving', default=False)
    sna_alert_3d_viewport: bpy.props.BoolProperty(name='Alert 3D Viewport', description='Show Alert on #D Viewport', default=True)
    sna_alert_image_editor: bpy.props.BoolProperty(name='Alert Image Editor', description='Use the Image Editor', default=False)
    sna_alert_uv_editor: bpy.props.BoolProperty(name='Alert UV Editor', description='Use the UV Editor', default=False)
    sna_alert_node_editors: bpy.props.BoolProperty(name='Alert Node Editors', description='Use Node Editors', default=False)
    sna_alert_video_sequencer: bpy.props.BoolProperty(name='Alert Video Sequencer', description='Use the Video Sequencer', default=False)
    sna_alert_movie_clip_editor: bpy.props.BoolProperty(name='Alert Movie Clip Editor', description='USe Movie Clip Editor', default=False)
    sna_alert_dopesheet: bpy.props.BoolProperty(name='Alert Dopesheet', description='Use Dopesheet Editor', default=False)
    sna_alert_timeline: bpy.props.BoolProperty(name='Alert Timeline', description='Use Timeline', default=False)
    sna_alert_nla: bpy.props.BoolProperty(name='Alert NLA', description='USe NLA Editor', default=False)
    sna_alert_text_editor: bpy.props.BoolProperty(name='Alert Text Editor', description='Use Text Editor', default=False)
    sna_alert_console: bpy.props.BoolProperty(name='Alert Console', description='USe Console', default=False)
    sna_alert_info_log: bpy.props.BoolProperty(name='Alert Info Log', description='Use Info Log', default=False)
    sna_alert_outliner: bpy.props.BoolProperty(name='Alert Outliner', description='Use Outliner', default=False)
    sna_alert_properties: bpy.props.BoolProperty(name='Alert Properties', description='Use Properties', default=False)
    sna_alert_file_browser: bpy.props.BoolProperty(name='Alert File Browser', description='Use File Browser', default=False)
    sna_alert_asset_browser: bpy.props.BoolProperty(name='Alert Asset Browser', description='USe Asset Browser', default=False)
    sna_alert_spreadhseet: bpy.props.BoolProperty(name='Alert Spreadhseet', description='USe Spreadsheet', default=False)
    sna_alert_preferences: bpy.props.BoolProperty(name='Alert Preferences', description='Use Preferences', default=False)
    sna_change_theme: bpy.props.BoolProperty(name='Change Theme', description='Change Theme Colors on Alert', default=False, update=sna_update_sna_change_theme_993B2)
    sna_animate: bpy.props.BoolProperty(name='Animate', description='Animate the Alert', default=False)
    sna_alert_footer: bpy.props.BoolProperty(name='Alert Footer', description='Use Footer', default=False)
    sna_alert_header: bpy.props.BoolProperty(name='Alert Header', description='Use Header', default=False)
    sna_siren_image_active: bpy.props.BoolProperty(name='Siren Image Active', description='Siren Image Alert is Active', default=False)
    sna_siren_image_sequence: bpy.props.BoolProperty(name='Siren Image Sequence', description='Use Siren Image Sequence', default=False)
    sna_siren_image_sequence_directory: bpy.props.StringProperty(name='Siren Image Sequence Directory', description='Siren Image Directory', default='', subtype='DIR_PATH', maxlen=0)
    sna_siren_image_path: bpy.props.StringProperty(name='Siren Image Path', description='Siren Image Path', default='', subtype='FILE_PATH', maxlen=0)
    sna_siren_custom: bpy.props.BoolProperty(name='Siren Custom', description='Use Custom Image or Sequence', default=False)
    sna_siren_image_size: bpy.props.FloatVectorProperty(name='Siren Image Size', description='', size=2, default=(100.0, 100.0), subtype='XYZ', unit='NONE', min=10.0, soft_min=10.0, soft_max=1024.0, step=10, precision=0)
    sna_siren_interval: bpy.props.FloatProperty(name='Siren Interval', description='', default=0.25, subtype='TIME', unit='TIME', min=0.10000000149011612, max=60.0, soft_max=2.0, step=5, precision=2)
    sna_alert_message: bpy.props.StringProperty(name='Alert Message', description='Enter a custom message for your alert', default='Save', subtype='NONE', maxlen=0)
    sna_alert_font: bpy.props.StringProperty(name='Alert Font', description='Leave Blank for Default Font', default='', subtype='FILE_PATH', maxlen=0)
    sna_alert_color: bpy.props.FloatVectorProperty(name='Alert Color', description='Color of Alert Font', size=4, default=(0.7940999865531921, 0.7940999865531921, 0.7940999865531921, 0.75), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=1, precision=4)
    sna_alert_message_size: bpy.props.FloatProperty(name='Alert Message Size', description='Size of the Alert Text', default=32.0, subtype='NONE', unit='NONE', min=8.0, soft_max=300.0, step=5, precision=0)
    sna_alert_message_location: bpy.props.FloatVectorProperty(name='Alert Message Location', description='', size=2, default=(20.0, 20.0), subtype='XYZ', unit='NONE', min=1.0, step=10, precision=0)
    sna_alert_image_location: bpy.props.FloatVectorProperty(name='Alert Image Location', description='Location of the Image', size=2, default=(5.0, 50.0), subtype='XYZ', unit='NONE', min=1.0, step=10, precision=0)
    sna_alert_background: bpy.props.StringProperty(name='Alert Background', description='Backgorund Image', default='', subtype='FILE_PATH', maxlen=0)
    sna_alert_use_background: bpy.props.BoolProperty(name='Alert Use Background', description='Add A Background to Your Alert', default=False)
    sna_alert_custom_background: bpy.props.BoolProperty(name='Alert Custom Background', description='Use a Custom Background', default=False)
    sna_alert_background_color: bpy.props.FloatVectorProperty(name='Alert Background Color', description='Set the background color of the alert', size=4, default=(0.05000000074505806, 0.05000000074505806, 0.05000000074505806, 0.5), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=1, precision=4)
    sna_alert_use_image: bpy.props.BoolProperty(name='Alert Use Image', description='Use an Image for the Alert', default=False)
    sna_alert_message_wrap: bpy.props.IntProperty(name='Alert Message Wrap', description='Wrap width of message', default=0, subtype='NONE', min=0)
    sna_alert_message_dpi: bpy.props.IntProperty(name='Alert Message DPI', description='DPI of Text', default=72, subtype='NONE', min=2, soft_min=72)
    sna_alert_message_rotation: bpy.props.FloatProperty(name='Alert Message Rotation', description='Rotation of the Message', default=0.0, subtype='ANGLE', unit='ROTATION', step=5, precision=0)
    sna_alert_use_message: bpy.props.BoolProperty(name='Alert Use Message', description='Use alert Message', default=False)
    sna_use_countdown: bpy.props.BoolProperty(name='Use Countdown', description='Show Countdown on screen', default=False)
    sna_countdown_font: bpy.props.StringProperty(name='Countdown Font', description='Leave Blank for Default Font', default='', subtype='FILE_PATH', maxlen=0)
    sna_countdown_size: bpy.props.FloatProperty(name='Countdown Size', description='', default=32.0, subtype='NONE', unit='NONE', min=8.0, soft_max=300.0, step=5, precision=0)
    sna_countdown_location: bpy.props.FloatVectorProperty(name='Countdown Location', description='Location of the Countdown', size=2, default=(150.0, 20.0), subtype='NONE', unit='NONE', min=1.0, step=10, precision=0)
    sna_countdown_wrap: bpy.props.IntProperty(name='Countdown Wrap', description='Wrap width of the countdown', default=0, subtype='NONE', min=0)
    sna_countdown_dpi: bpy.props.IntProperty(name='Countdown DPI', description='DPI of Countdown text', default=72, subtype='NONE', min=2, soft_min=72)
    sna_countdown_rotation: bpy.props.FloatProperty(name='Countdown Rotation', description='', default=0.0, subtype='ANGLE', unit='ROTATION', step=5, precision=0)
    sna_countdown_color: bpy.props.FloatVectorProperty(name='Countdown Color', description='Color of Countdown Font', size=4, default=(0.7940999865531921, 0.7940999865531921, 0.7940999865531921, 0.75), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=1, precision=4)
    sna_countdown_suffix_message: bpy.props.StringProperty(name='Countdown Suffix Message', description='Leave blank for no suffix', default='', subtype='NONE', maxlen=0)
    sna_update_screen_areas: bpy.props.BoolProperty(name='Update Screen Areas', description='Show updates each second (might affect performance)', default=False)
    sna_countdown_on_ui: bpy.props.BoolProperty(name='Countdown on UI', description='Display time remaining on UI (updates when you hover over it)', default=False)

    def draw(self, context):
        if not (False):
            layout = self.layout 
            layout_function = layout
            sna_ui_fn_save_police_B9591(layout_function, )
            layout_function = layout
            sna_ui_fn_alert_countdown_090BA(layout_function, )
            layout_function = layout
            sna_ui_fn_save_police_alerts_props_C4E09(layout_function, )
            layout_function = layout
            sna_ui_fn_save_police_alert_image_78119(layout_function, )
            layout_function = layout
            sna_ui_fn_save_police_ui_settings_8BC5F(layout_function, )


class SNA_PT_UI_SETTINGS_B2E57(bpy.types.Panel):
    bl_label = 'UI Settings'
    bl_idname = 'SNA_PT_UI_SETTINGS_B2E57'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 3
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_SAVE_POLICE_99DE7'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_save_police_ui_settings_8BC5F(layout_function, )


class SNA_PT_COUNTDOWN_2FEF5(bpy.types.Panel):
    bl_label = 'Countdown'
    bl_idname = 'SNA_PT_COUNTDOWN_2FEF5'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 1
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_SAVE_POLICE_99DE7'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_alert_countdown_090BA(layout_function, )


class SNA_PT_ALERT_BADDF(bpy.types.Panel):
    bl_label = 'Alert'
    bl_idname = 'SNA_PT_ALERT_BADDF'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 2
    bl_parent_id = 'SNA_PT_SAVE_POLICE_99DE7'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        sna_ui_fn_save_police_alerts_props_C4E09(layout_function, )
        layout_function = layout
        sna_ui_fn_save_police_alert_image_78119(layout_function, )


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_save_police_animation_active = bpy.props.BoolProperty(name='Save Police Animation Active', description='The Image Animation is Active', default=False)
    bpy.types.Scene.sna_save_police_countdown_active = bpy.props.BoolProperty(name='Save Police Countdown Active', description='The Countdown is active', default=False)
    bpy.types.Scene.sna_save_police_theme_active = bpy.props.BoolProperty(name='Save Police Theme Active', description='Theme color changing is active', default=False)
    bpy.types.Scene.sna_save_police_interval = bpy.props.IntProperty(name='Save Police Interval', description='Number of minutes for Save Police', default=10, subtype='NONE', min=1, max=1440, update=sna_update_sna_save_police_interval_8D7BA)
    bpy.types.Scene.sna_save_police_script_interval = bpy.props.IntProperty(name='Save Police Script Interval', description='', default=60, subtype='NONE', min=1, soft_min=1440)
    bpy.types.Scene.sna_save_police_timer_freq = bpy.props.IntProperty(name='Save Police Timer Freq', description='How many seconds per minute', default=60, subtype='NONE', min=1, soft_max=60)
    bpy.types.Scene.sna_save_police_reminder = bpy.props.BoolProperty(name='Save Police Reminder', description='Reminder after save police timer completes', default=False, update=sna_update_sna_save_police_reminder_9D6ED)
    bpy.types.Scene.sna_save_police_annoy_active = bpy.props.BoolProperty(name='Save Police Annoy Active', description='Annoyance is now active', default=False)
    bpy.types.Scene.sna_animation_timer = bpy.props.FloatProperty(name='Animation Timer', description='How fast do you want the animation to run in seconds', default=0.25, subtype='NONE', unit='NONE', min=0.009999999776482582, soft_max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_animation_interval = bpy.props.IntProperty(name='Animation Interval', description='Number of animations', default=5, subtype='NONE', min=1, soft_max=23)
    bpy.types.Scene.sna_theme_color__menu = bpy.props.FloatVectorProperty(name='Theme Color - Menu', description='Change Menu text color', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__list_item = bpy.props.FloatVectorProperty(name='Theme Color - List Item', description='Change List Item text color (collection items)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__list_item_sel = bpy.props.FloatVectorProperty(name='Theme Color - List Item Sel', description='Change List Item text color (collection items)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__number = bpy.props.FloatVectorProperty(name='Theme Color - Number', description='Change Number color (all number props)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__option = bpy.props.FloatVectorProperty(name='Theme Color - Option', description='Change Option color (checkbox)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__pulldown = bpy.props.FloatVectorProperty(name='Theme Color - Pulldown', description='Change Pulldown color (Header Pulldowns, etc.)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__regular = bpy.props.FloatVectorProperty(name='Theme Color - Regular', description='Change Regular color (blender icons)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__tab = bpy.props.FloatVectorProperty(name='Theme Color - Tab', description='Change Tab color (Workspaces, etc.)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__tab_sel = bpy.props.FloatVectorProperty(name='Theme Color - Tab Sel', description='Change Tab color (Workspaces, etc.)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__radio_buttons = bpy.props.FloatVectorProperty(name='Theme Color - Radio Buttons', description='Change Radio Buttons color (buttons with text)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__text = bpy.props.FloatVectorProperty(name='Theme Color - Text', description='Change Text color (string props, and search strings)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__tool = bpy.props.FloatVectorProperty(name='Theme Color - Tool', description='Change Tool color (button text)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__toolbar_item_selected = bpy.props.FloatVectorProperty(name='Theme Color - Toolbar Item Selected', description='Change Selected Toolbar Item color (selected items in the toolbar)', size=4, default=(0.749019980430603, 0.749019980430603, 0.749019980430603, 1.0), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__value_slider = bpy.props.FloatVectorProperty(name='Theme Color - Value Slider', description='Change Value Slider color (float values, etc.)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__toggle_text = bpy.props.FloatVectorProperty(name='Theme Color - Toggle Text', description='', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__toggle_text_sel = bpy.props.FloatVectorProperty(name='Theme Color - Toggle Text Sel', description='', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__scroll_bar_item = bpy.props.FloatVectorProperty(name='Theme Color - Scroll Bar Item', description='Change Scroll Bar Item Color', size=4, default=(0.749019980430603, 0.749019980430603, 0.749019980430603, 1.0), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__regular_sel = bpy.props.FloatVectorProperty(name='Theme Color - Regular Sel', description='Change Regular Set color (button color)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__radio_buttons_sel = bpy.props.FloatVectorProperty(name='Theme Color - Radio Buttons Sel', description='Change the Raidio Buttons Sel Color (pref tab)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='COLOR', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.types.Scene.sna_theme_color__option_text_sel = bpy.props.FloatVectorProperty(name='Theme Color - Option Text Sel', description='Change Option color (checkbox selected)', size=3, default=(0.749019980430603, 0.749019980430603, 0.749019980430603), subtype='NONE', unit='NONE', min=0.0, max=1.0, step=3, precision=6)
    bpy.utils.register_class(SNA_OT_Save_Police_Preview_Alert_Image_558A3)
    bpy.utils.register_class(SNA_OT_Save_Police_End_Alert_Image_Preview_7A41B)
    bpy.utils.register_class(SNA_OT_Save_Police_Preview_Countdown_8B9F0)
    bpy.utils.register_class(SNA_OT_Save_Police_End_Countdown_Preview_8F673)
    bpy.utils.register_class(SNA_OT_Save_Police_Move_Countdown_Da3Ac)
    bpy.utils.register_class(SNA_OT_Save_Police_Move_Image_F9F28)
    bpy.utils.register_class(SNA_OT_Save_Police_Move_Message_582F8)
    bpy.utils.register_class(SNA_OT_Op_Start_Drawing_E7A6D)
    bpy.utils.register_class(SNA_OT_Op_End_Drawing_3823D)
    bpy.types.FILEBROWSER_MT_editor_menus.append(sna_add_to_filebrowser_mt_editor_menus_8EBE1)
    bpy.types.ASSETBROWSER_MT_editor_menus.append(sna_add_to_assetbrowser_mt_editor_menus_EDC93)
    bpy.types.SPREADSHEET_HT_header.append(sna_add_to_spreadsheet_ht_header_8B3EB)
    atexit.register(before_exit_handler_8A0D1)
    bpy.app.handlers.load_post.append(load_post_handler_0B793)
    bpy.app.handlers.save_post.append(save_post_handler_70958)
    bpy.utils.register_class(SNA_OT_Op_Save_Police_Saving_148E8)
    bpy.utils.register_class(SNA_OT_Op_Annoy_Store_And_Swap_Theme_Colors_C1B7F)
    bpy.utils.register_class(SNA_OT_Op_Annoy_Restore_Theme_Colors_954Ce)
    bpy.utils.register_class(SNA_OT_Op_Preview_Theme_Change_2Ea4A)
    bpy.types.VIEW3D_MT_editor_menus.append(sna_add_to_view3d_mt_editor_menus_9786F)
    bpy.types.CONSOLE_MT_editor_menus.append(sna_add_to_console_mt_editor_menus_F4F8C)
    bpy.types.INFO_MT_editor_menus.append(sna_add_to_info_mt_editor_menus_80618)
    bpy.types.TEXT_MT_editor_menus.append(sna_add_to_text_mt_editor_menus_DB6C3)
    bpy.types.TOPBAR_MT_editor_menus.append(sna_add_to_topbar_mt_editor_menus_1996C)
    bpy.types.STATUSBAR_HT_header.append(sna_add_to_statusbar_ht_header_11903)
    bpy.types.NODE_MT_editor_menus.append(sna_add_to_node_mt_editor_menus_5168E)
    bpy.types.OUTLINER_HT_header.append(sna_add_to_outliner_ht_header_F6026)
    bpy.types.USERPREF_MT_editor_menus.append(sna_add_to_userpref_mt_editor_menus_095CF)
    bpy.types.PROPERTIES_HT_header.append(sna_add_to_properties_ht_header_B2B08)
    if not 'Save Icon.png' in _icons: _icons.load('Save Icon.png', os.path.join(os.path.dirname(__file__), 'icons', 'Save Icon.png'), "IMAGE")
    bpy.utils.register_class(SNA_PT_SAVE_POLICE_99DE7)
    bpy.utils.register_class(SNA_PT_SAVE_POLICE_POPOVER_0C41B)
    bpy.types.DOPESHEET_MT_editor_menus.append(sna_add_to_dopesheet_mt_editor_menus_B8DDE)
    bpy.types.TIME_MT_editor_menus.append(sna_add_to_time_mt_editor_menus_C76A9)
    bpy.types.GRAPH_MT_editor_menus.append(sna_add_to_graph_mt_editor_menus_6C0C5)
    bpy.types.NLA_MT_editor_menus.append(sna_add_to_nla_mt_editor_menus_DEEAC)
    bpy.types.IMAGE_MT_editor_menus.append(sna_add_to_image_mt_editor_menus_FB521)
    bpy.types.SEQUENCER_MT_editor_menus.append(sna_add_to_sequencer_mt_editor_menus_D0459)
    bpy.types.CLIP_MT_tracking_editor_menus.append(sna_add_to_clip_mt_tracking_editor_menus_7CC27)
    bpy.utils.register_class(SNA_AddonPreferences_70C5B)
    bpy.utils.register_class(SNA_PT_UI_SETTINGS_B2E57)
    bpy.utils.register_class(SNA_PT_COUNTDOWN_2FEF5)
    bpy.utils.register_class(SNA_PT_ALERT_BADDF)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_theme_color__option_text_sel
    del bpy.types.Scene.sna_theme_color__radio_buttons_sel
    del bpy.types.Scene.sna_theme_color__regular_sel
    del bpy.types.Scene.sna_theme_color__scroll_bar_item
    del bpy.types.Scene.sna_theme_color__toggle_text_sel
    del bpy.types.Scene.sna_theme_color__toggle_text
    del bpy.types.Scene.sna_theme_color__value_slider
    del bpy.types.Scene.sna_theme_color__toolbar_item_selected
    del bpy.types.Scene.sna_theme_color__tool
    del bpy.types.Scene.sna_theme_color__text
    del bpy.types.Scene.sna_theme_color__radio_buttons
    del bpy.types.Scene.sna_theme_color__tab_sel
    del bpy.types.Scene.sna_theme_color__tab
    del bpy.types.Scene.sna_theme_color__regular
    del bpy.types.Scene.sna_theme_color__pulldown
    del bpy.types.Scene.sna_theme_color__option
    del bpy.types.Scene.sna_theme_color__number
    del bpy.types.Scene.sna_theme_color__list_item_sel
    del bpy.types.Scene.sna_theme_color__list_item
    del bpy.types.Scene.sna_theme_color__menu
    del bpy.types.Scene.sna_animation_interval
    del bpy.types.Scene.sna_animation_timer
    del bpy.types.Scene.sna_save_police_annoy_active
    del bpy.types.Scene.sna_save_police_reminder
    del bpy.types.Scene.sna_save_police_timer_freq
    del bpy.types.Scene.sna_save_police_script_interval
    del bpy.types.Scene.sna_save_police_interval
    del bpy.types.Scene.sna_save_police_theme_active
    del bpy.types.Scene.sna_save_police_countdown_active
    del bpy.types.Scene.sna_save_police_animation_active
    if handler_5FE5D:
        bpy.types.SpaceView3D.draw_handler_remove(handler_5FE5D[0], 'WINDOW')
        handler_5FE5D.pop(0)
    if handler_D8705:
        bpy.types.SpaceImageEditor.draw_handler_remove(handler_D8705[0], 'WINDOW')
        handler_D8705.pop(0)
    if handler_AAAFB:
        bpy.types.SpaceNodeEditor.draw_handler_remove(handler_AAAFB[0], 'WINDOW')
        handler_AAAFB.pop(0)
    bpy.utils.unregister_class(SNA_OT_Save_Police_Preview_Alert_Image_558A3)
    bpy.utils.unregister_class(SNA_OT_Save_Police_End_Alert_Image_Preview_7A41B)
    if handler_CB41D:
        bpy.types.SpaceSequenceEditor.draw_handler_remove(handler_CB41D[0], 'WINDOW')
        handler_CB41D.pop(0)
    if handler_EE591:
        bpy.types.SpaceView3D.draw_handler_remove(handler_EE591[0], 'WINDOW')
        handler_EE591.pop(0)
    if handler_A1E89:
        bpy.types.SpaceImageEditor.draw_handler_remove(handler_A1E89[0], 'WINDOW')
        handler_A1E89.pop(0)
    if handler_0A529:
        bpy.types.SpaceNodeEditor.draw_handler_remove(handler_0A529[0], 'WINDOW')
        handler_0A529.pop(0)
    bpy.utils.unregister_class(SNA_OT_Save_Police_Preview_Countdown_8B9F0)
    bpy.utils.unregister_class(SNA_OT_Save_Police_End_Countdown_Preview_8F673)
    if handler_F57E6:
        bpy.types.SpaceSequenceEditor.draw_handler_remove(handler_F57E6[0], 'WINDOW')
        handler_F57E6.pop(0)
    bpy.utils.unregister_class(SNA_OT_Save_Police_Move_Countdown_Da3Ac)
    bpy.utils.unregister_class(SNA_OT_Save_Police_Move_Image_F9F28)
    bpy.utils.unregister_class(SNA_OT_Save_Police_Move_Message_582F8)
    bpy.utils.unregister_class(SNA_OT_Op_Start_Drawing_E7A6D)
    if handler_64666:
        bpy.types.SpaceNodeEditor.draw_handler_remove(handler_64666[0], 'WINDOW')
        handler_64666.pop(0)
    bpy.utils.unregister_class(SNA_OT_Op_End_Drawing_3823D)
    bpy.types.FILEBROWSER_MT_editor_menus.remove(sna_add_to_filebrowser_mt_editor_menus_8EBE1)
    bpy.types.ASSETBROWSER_MT_editor_menus.remove(sna_add_to_assetbrowser_mt_editor_menus_EDC93)
    bpy.types.SPREADSHEET_HT_header.remove(sna_add_to_spreadsheet_ht_header_8B3EB)
    atexit.unregister(before_exit_handler_8A0D1)
    bpy.app.handlers.load_post.remove(load_post_handler_0B793)
    bpy.app.handlers.save_post.remove(save_post_handler_70958)
    bpy.utils.unregister_class(SNA_OT_Op_Save_Police_Saving_148E8)
    bpy.utils.unregister_class(SNA_OT_Op_Annoy_Store_And_Swap_Theme_Colors_C1B7F)
    bpy.utils.unregister_class(SNA_OT_Op_Annoy_Restore_Theme_Colors_954Ce)
    bpy.utils.unregister_class(SNA_OT_Op_Preview_Theme_Change_2Ea4A)
    bpy.types.VIEW3D_MT_editor_menus.remove(sna_add_to_view3d_mt_editor_menus_9786F)
    bpy.types.CONSOLE_MT_editor_menus.remove(sna_add_to_console_mt_editor_menus_F4F8C)
    bpy.types.INFO_MT_editor_menus.remove(sna_add_to_info_mt_editor_menus_80618)
    bpy.types.TEXT_MT_editor_menus.remove(sna_add_to_text_mt_editor_menus_DB6C3)
    bpy.types.TOPBAR_MT_editor_menus.remove(sna_add_to_topbar_mt_editor_menus_1996C)
    bpy.types.STATUSBAR_HT_header.remove(sna_add_to_statusbar_ht_header_11903)
    bpy.types.NODE_MT_editor_menus.remove(sna_add_to_node_mt_editor_menus_5168E)
    bpy.types.OUTLINER_HT_header.remove(sna_add_to_outliner_ht_header_F6026)
    bpy.types.USERPREF_MT_editor_menus.remove(sna_add_to_userpref_mt_editor_menus_095CF)
    bpy.types.PROPERTIES_HT_header.remove(sna_add_to_properties_ht_header_B2B08)
    bpy.utils.unregister_class(SNA_PT_SAVE_POLICE_99DE7)
    bpy.utils.unregister_class(SNA_PT_SAVE_POLICE_POPOVER_0C41B)
    bpy.types.DOPESHEET_MT_editor_menus.remove(sna_add_to_dopesheet_mt_editor_menus_B8DDE)
    bpy.types.TIME_MT_editor_menus.remove(sna_add_to_time_mt_editor_menus_C76A9)
    bpy.types.GRAPH_MT_editor_menus.remove(sna_add_to_graph_mt_editor_menus_6C0C5)
    bpy.types.NLA_MT_editor_menus.remove(sna_add_to_nla_mt_editor_menus_DEEAC)
    bpy.types.IMAGE_MT_editor_menus.remove(sna_add_to_image_mt_editor_menus_FB521)
    bpy.types.SEQUENCER_MT_editor_menus.remove(sna_add_to_sequencer_mt_editor_menus_D0459)
    bpy.types.CLIP_MT_tracking_editor_menus.remove(sna_add_to_clip_mt_tracking_editor_menus_7CC27)
    bpy.utils.unregister_class(SNA_AddonPreferences_70C5B)
    bpy.utils.unregister_class(SNA_PT_UI_SETTINGS_B2E57)
    bpy.utils.unregister_class(SNA_PT_COUNTDOWN_2FEF5)
    bpy.utils.unregister_class(SNA_PT_ALERT_BADDF)
