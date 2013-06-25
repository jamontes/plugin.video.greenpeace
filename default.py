# -*- coding: utf-8 -*-

'''
   XBMC Greenpeace plugin.
   Copyright (C) 2013 José Antonio Montes (jamontes)

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
   
   This is the first trial of the Greenpeace plugin for XBMC.
   This plugins gets the videos from Greenpeace web site and shows them ordered by appearance.
   This plugin depends on the lutil library functions.
   This plugins depends as well of external plugins: youtube and vimeo from TheCollective.
'''

import lutil

pluginhandle = int(sys.argv[1])
plugin_id = 'plugin.video.greenpeace'

settings = lutil.get_plugin_settings(plugin_id)
lutil.set_debug_mode(settings.getSetting("debug"))
translation = settings.getLocalizedString
site_id = int(settings.getSetting("site_id"))


sites_list = (  'international_en', 'africa_fr', 'africa_fr', 'africa_en', 'argentina_es', 'australia_en', 'belgium_nl', 'brasil_pt', 'chile_es',
                'eastasia', 'finland_fi', 'greece_el', 'hk', 'israel_he', 'italy_it', 'japan_ja', 'mexico_es', 'seasia_ph', 'russia_ru',
                'espana_es', 'switzerland_de', 'switzerland_fr', 'seasia_th')

sites_supported = {

        'international_en' : {  'url_site' : 'http://www.greenpeace.org/international/en/',
                                'url_post' : 'http://www.greenpeace.org/international/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'     : 'en-GB' },

        'africa_fr'        : {  'url_site' : 'http://www.greenpeace.org/africa/fr/',
                                'url_post' : 'http://www.greenpeace.org/africa/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'     : 'fr' },

        'africa_en'        : {  'url_site'  : 'http://www.greenpeace.org/africa/en/',
                                'url_post'  : 'http://www.greenpeace.org/africa/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'en-ZA' },

        'argentina_es'     : {  'url_site'  : 'http://www.greenpeace.org/argentina/es/',
                                'url_post'  : 'http://www.greenpeace.org/argentina/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'es-AR' },

        'australia_en'     : {  'url_site'  : 'http://www.greenpeace.org/australia/en/',
                                'url_post'  : 'http://www.greenpeace.org/australia/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'en-AU' },

        'belgium_nl'       : {  'url_site'  : 'http://www.greenpeace.org/belgium/nl/',
                                'url_post'  : 'http://www.greenpeace.org/belgium/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'nl-BE' },

        'brasil_pt'        : {  'url_site'  : 'http://www.greenpeace.org/brasil/pt/',
                                'url_post'  : 'http://www.greenpeace.org/brasil/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'pt-BR' },

        'chile_es'         : {  'url_site'  : 'http://www.greenpeace.org/chile/es/',
                                'url_post'  : 'http://www.greenpeace.org/chile/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'es-CL' },

        'eastasia'         : {  'url_site'  : 'http://www.greenpeace.org/eastasia/',
                                'url_post'  : 'http://www.greenpeace.org/eastasia/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'en-CN' },

        'finland_fi'       : {  'url_site'  : 'http://www.greenpeace.org/finland/fi/',
                                'url_post'  : 'http://www.greenpeace.org/finland/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'fi-FI' },

        'greece_el'        : {  'url_site'  : 'http://www.greenpeace.org/greece/el/',
                                'url_post'  : 'http://www.greenpeace.org/greece/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'el-GR' },

        'hk'               : {  'url_site'  : 'http://www.greenpeace.org/hk/',
                                'url_post'  : 'http://www.greenpeace.org/hk/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'zh-HK' },

        'israel_he'        : {  'url_site'  : 'http://www.greenpeace.org/israel/he/',
                                'url_post'  : 'http://www.greenpeace.org/israel/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'he-IL' },

        'italy_it'         : {  'url_site'  : 'http://www.greenpeace.org/italy/it/',
                                'url_post'  : 'http://www.greenpeace.org/italy/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'it-IT' },

        'japan_ja'         : {  'url_site'  : 'http://www.greenpeace.org/japan/ja/',
                                'url_post'  : 'http://www.greenpeace.org/japan/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'ja-JP' },

        'mexico_es'        : {  'url_site'  : 'http://www.greenpeace.org/mexico/es/',
                                'url_post'  : 'http://www.greenpeace.org/mexico/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'es-MX' },

        'seasia_ph'        : {  'url_site'  : 'http://www.greenpeace.org/seasia/ph/',
                                'url_post'  : 'http://www.greenpeace.org/seasia/ph/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'en-PH' },

        'russia_ru'        : {  'url_site'  : 'http://www.greenpeace.org/russia/ru/',
                                'url_post'  : 'http://www.greenpeace.org/russia/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'ru-RU' },

        'espana_es'        : {  'url_site'  : 'http://www.greenpeace.org/espana/es/',
                                'url_post'  : 'http://www.greenpeace.org/espana/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'es-ES' },

        'switzerland_de'   : {  'url_site'  : 'http://www.greenpeace.org/switzerland/de/',
                                'url_post'  : 'http://www.greenpeace.org/switzerland/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'de-CH' },

        'switzerland_fr'   : {  'url_site'  : 'http://www.greenpeace.org/switzerland/fr/',
                                'url_post'  : 'http://www.greenpeace.org/switzerland/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'fr-CH' },

        'seasia_th'        : {  'url_site'  : 'http://www.greenpeace.org/seasia/th/',
                                'url_post'  : 'http://www.greenpeace.org/seasia/th/Templates/Planet3/Handlers/GetControl.ashx',
                                'lang'      : 'th-TH' },

    }

site_name = sites_list[site_id]
lutil.log("greenpeace.main site_name: %s" % site_name)

root_url = 'http://www.greenpeace.org'

# Entry point
def run():
    lutil.log("greenpeace.run")
    
    # Get params
    params = lutil.get_plugin_parms()
    
    if params.get("action") is None:
        create_index(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    

# Main menu
def create_index(params):
    lutil.log("greenpeace.create_index "+repr(params))

    buffer_html, cookies_web = lutil.carga_web_cookies(sites_supported[site_name]['url_site'])
    category_block_pattern = '<select>(.*?)</select>'
    category_pattern = '<option value="([^"]+)">([^<]+)</option>'

    category_block = lutil.find_first(buffer_html, category_block_pattern)
    
    for category, category_title in lutil.find_multiple(category_block, category_pattern):
        action    = 'main_list'
        category  =  category
        title     =  category_title
        url       =  sites_supported[site_name]['url_post']
        cookies   =  cookies_web
        page      = '1'
        tab       = '0'
        lutil.log('greenpeace.create_index action=["%s"] title=["%s"] url=["%s"] category=["%s"] page=["%s"] tab=["%s"]' % (action, title, url, category, page, tab))
        lutil.addDir(action=action, title=title, url=url, cookies=cookies, category=category, page=page, tab=tab)

    lutil.close_dir(pluginhandle)


def main_list(params):
    lutil.log("greenpeace.main_list "+repr(params))

    action    = params.get('action')
    cookies   = params.get('cookies')
    referer   = sites_supported[site_name]['url_site']
    category  = params.get('category')
    tab       = '0'
    lang      = sites_supported[site_name]['lang']
    uiculture = lang
    page      = params.get('page')
    url_post  = sites_supported[site_name]['url_post']

    my_headers = {
                    'Accept'            : '*/*',
                    'Accept-Language'   : 'es-es,es;q=0.8,en-us;q=0.5,en;q=0.3',
                    'Accept-Encoding'   : 'deflate',
                    'Content-type'      : 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With'  : 'XMLHttpRequest',
                    'Referer'           :  referer,
                    'Cookie'            :  cookies,
                    'Pragma'            : 'no-cache',
                    'Cache-Control'     : 'no-cache'
                }

    my_query_loadControl = 'loadControl=~/Templates/Planet3/UserControls/Teasers/TeaserLister.ascx'

    my_query_parms = {
                        'l'     :  lang,
                        'ps'    : '12',
                        'ta'    : 'multimediavideo%257cmultimediaimage%257cmultimediaimagegallery%257cmultimediaphotoessay%257cecard',
                        'to'    : '',
                        'dp'    : 'True',
                        'gv'    : 'True',
                        'dgvs'  : 'True',
                        'dta'   :  tab,
                        'dto'   : '',
                        'mpc'   : '0',
                        'tgs'   : '',
                        'cpid'  : '20731',
                        'opc'   : 'False',
                        'st'    :  category,
                        'tab'   :  tab,
                        'gvs'   : 'true',
                        'page'  :  page
                    }

    my_query_string = ''
    amp = ''
    for keyparm in my_query_parms:
        my_query_string = "%s%s%s%s%s" % (my_query_string, amp, keyparm, '%3D', my_query_parms[keyparm])
        amp = '%26'

    my_data = "%s&queryString=%s&uiculture=%s" % (my_query_loadControl, my_query_string, uiculture)

    buffer_web, cookies_web = lutil.send_post_data(url_post, my_headers, my_data)

    # Extract video items from the html content
    pattern_videos = '<a href="([^"]+)" title="([^"]+)">[^<]+<em class="image-holder"><img title="[^"]+" src="([^"]+)"'
    videolist = lutil.find_multiple(buffer_web, pattern_videos)

    for url, title, thumbnail in videolist:
        title = title.replace('&quot;', '"').replace('&#39;', '´')  # Cleanup the title.
        lutil.log('Videolist: URL: "%s" Title: "%s" Thumbnail: "%s"' % (url, title, thumbnail))
        
        plot = title # The description only appears when we load the link, so a this point we copy the description with the title content.
        # Appends a new item to the xbmc item list
        lutil.addLink(action="play_video", title=title, plot=plot, url="%s%s" % (root_url, url), thumbnail="%s%s" % (root_url,thumbnail))
 
    # Here we get the next page URL to add it at the end of the current video list page.
    pattern_nextpage = '<a class="next" href="\?.*?page=([^"]+)" title="([^"]+)" rel="nofollow">[^<]+</a>.+page=([^"]+)" title="[^"]+" rel="nofollow">[^<]+</a>'
    for next_page, title_next, last_page in lutil.find_multiple(buffer_web, pattern_nextpage):
        lutil.log('next_page=%s title_next="%s" last_page=%s category="%s" tab=%s' % (next_page, title_next, last_page, category, tab))
        lutil.addDir(action="main_list", title=">> %s (%s/%s)" % (title_next, next_page, last_page), url=url_post, cookies=cookies, category=category, page=next_page, tab=tab)

    lutil.close_dir(pluginhandle)

# This funtion search into the URL link to get the video link from the different sources.
# Right now it can play the videos from the following sources: Youtube and Vimeo.
def play_video(params):
    lutil.log("greenpeace.play "+repr(params))

    # Here we define the list of video sources supported.
    video_sources = ('youtube', 'vimeo')
    buffer_link = lutil.carga_web(params.get("url"))
    for  source in video_sources:
        video_url = eval("get_playable_%s_url(buffer_link)" % source)
        if video_url:
            try:
                return lutil.play_resolved_url(pluginhandle = pluginhandle, url = video_url)
            except:
                lutil.log('greenpeace.play ERROR: we cannot reproduce this video URL: "%s"' % video_url)
            return lutil.showWarning(translation(30012))
    
    lutil.log('greenpeace.play ERROR: we cannot play the video from this source yet: "%s"' % params.get("url"))
    return lutil.showWarning(translation(30011))


# This funtion search into the URL link to get the video URL for Youtube.
def get_playable_youtube_url(html):

    pattern_youtube = '<input type="text" id="linkvideo" value="http://www.youtube.com/watch\?v=([0-9A-Za-z_-]{11})'
    video_id = lutil.find_first(html, pattern_youtube)

    if video_id:
        lutil.log("greenpeace.play: We have found this Youtube video with video_id: %s and let's going to play it!" % video_id)
        video_url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + video_id
        return video_url

    return ""


# This funtion search into the URL link to get the video URL for Vimeo.
def get_playable_vimeo_url(html):

    pattern_vimeo = '<input type="text" id="linkvideo" value="http://vimeo.com/([0-9]+)'
    video_id = lutil.find_first(html, pattern_vimeo)

    if video_id:
        lutil.log("greenpeace.play: We have found this Vimeo video with video_id: %s and let's going to play it!" % video_id)
        video_url = "plugin://plugin.video.vimeo/?path=/root/video&action=play_video&videoid=" + video_id
        return video_url

    return ""

run()
