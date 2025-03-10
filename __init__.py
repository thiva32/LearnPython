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


from .import TXtool_ui_panel
from .VertexColor import TXT_VertexColor_op
from .Cleanup import TXT_Cleanup_properties , TXT_Cleanup_op


def register():
    TXtool_ui_panel.register()
    TXT_VertexColor_op.register()
    TXT_Cleanup_op.register()
    TXT_Cleanup_properties.register()
    
    


def unregister():
    TXtool_ui_panel.unregister()
    TXT_VertexColor_op.unregister()
    TXT_Cleanup_op.unregister()
    TXT_Cleanup_properties.unregister()
    
