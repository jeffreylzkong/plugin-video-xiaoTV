# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/nba
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.xiaoTV'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# Entry point
def run():
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):

    plugintools.add_item(
        #action="",
        title="SuperSimpleSongs",
        url="plugin://plugin.video.youtube/user/SuperSimpleSongs/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item(
        #action="",
        title="Kids Channel",
        url="plugin://plugin.video.youtube/user/edukatetv/",
        thumbnail=icon,
        folder=True )


    plugintools.add_item(
        #action="",
        title="The kids club",
        url="plugin://plugin.video.youtube/user/ChildrenGamesTV/",
        thumbnail=icon,
        folder=True )


run()