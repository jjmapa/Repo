# coding=utf-8
import base64
import os
from base import tools

""" Menu Ppal de Fusion"""
def categoriasprincipales():
    categorias = ['Television [COLOR green] Beta[/COLOR]', 'Peliculas', 'TV Shows', 'Colecciones', 'Buscador','Herramientas']
    return categorias

def fanartsprincipales():
    dir_fan_pri = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'principal', 'fanart')
    fanarts = ['tv.jpg', 'movie.jpg', 'tv_show.jpg', 'collections.jpg', 'buscar.jpg', 'herramientas.jpg']
    fanartss = []
    for fanart in fanarts:
        fanartss.append(os.path.join(dir_fan_pri, fanart))
    return fanartss

def postersprincipales():
    dir_pos_pri = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'principal', 'poster')
    posters = ['tv.png', 'movie.png', 'tv_show.png', 'collections.png', 'buscar.png', 'herramientas.png']
    posterss = []
    for poster in posters:
        posterss.append(os.path.join(dir_pos_pri, poster))
    return posterss

def infosprincipales():
    infos = ['Agrega tus listas de IPTV o usa una compartida por los demas usuarios.',
             'Disfruta de las peliculas agregadas por todos los usuarios,',
             'Disfruta de tus series favoritas.',
             'Colecciones de peliculas',
             'Buscar en la biblioteca de Fusion.',
             'Usa las herramientas para las listas de IPTV.']
    return infos


def modesprincipales():
    modes = ['mode01','mode02','mode03','collections','mode04','mode05','mode06']
    return modes

""" Subcategorias de Peliculas"""
def subcategoriasmovies():
    subcategorias = ['Ultimas Agregadas','Mas Populares','Mejor Valoradas','Por Año','Estrenos','Accion','Animacion','Aventura','Ciencia Ficcion','Comedia','Crimen','Documental','Drama','Familia','Fantasia','Guerra','Historia','Misterio','Musica','Romance','Suspenso','Terror','Western', 'Otros']
    return subcategorias


def archivosmovies():
    archivos = ['ultimas','populares','mejores','year','estrenos','accion','animacion','aventura','ficcion','comedia','crimen','documental','drama','familia','fantasia','guerra','historia','misterio','musica','romance','suspense','terror','western', 'otros']
    return archivos

def subpostersmovies():
    dir_pos_pel = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'peliculas', 'poster')
    subposters = ['ultimas agregadas.png','mas populares.png','mejor valoradas.png','year.png','estrenos.png','Accion.png','animacion.png','aventura.png','ciencia ficcion.png','Comedia.png','Crimen.png','documental.png','drama.png','Familia.png','Fantasia.png','guerra.png','Historia.png','misterio.png','musica.png','romance.png','suspenso.png','terror.png','western.png','otros.png']
    subposterss = []
    for subposter in subposters:
        subposterss.append(os.path.join(dir_pos_pel, subposter))
    return subposterss

def subfanartsmovies():
    dir_fan_pel = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'peliculas', 'fanart')
    subfanarts = ['fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png','fanart.png']
    subfanartss = []
    for subfanart in subfanarts:
        subfanartss.append(os.path.join(dir_fan_pel, subfanart))
    return subfanartss

def subinfosmovies():
    subinfos = ['Ultimas Agregadas','Las Más Populares (Trending)','Las Méjor valoradas','Por Año','Estrenos','Acción','Animación','Aventura','Ciencia Ficción','Comedia','Crimen','Documentales','Drama','Familia','Fantasia','Bélicas','Historicas','Misterio','Músicales','Romance','Suspenso','Terror','Occidentales','Aún no catalogados']
    return subinfos


def submodesmovies():
    submodes = ['movies','movies','movies','for_year','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies','movies']
    return submodes

# Subcategorias de Series
def subcategoriastvshows():
    subcategoriastvshows = ['Todos los TV Shows', 'Mas Populares', 'Mejor Valoradas', 'Acción y Aventura', 'Animación', 'Ciencia Ficción y Fantasía', 'Comedia', 'Crimen', 'Documental', 
                            'Drama', 'Familia', 'Guerra y Politica', 'Historia', 'Kids', 'Misterio', 'Occidental', 'Reality', 'Romance', 'Terror', 'Otros']
    return subcategoriastvshows

def subposterstvshows():
    dir_pos_tvs = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'tv show', 'poster')
    subposterstvshows = ['todos los tv shows.png', 'mas populares.png', 'mejor valoradas.png', 'accion y aventura.png', 'animacion.png', 'ciencia ficcion y fantasia.png', 'Comedia.png', 
                         'Crimen.png', 'documental.png', 'drama.png', 'Familia.png', 'guerra y politica.png', 'Historia.png', 'kids.png', 'misterio.png', 'occidental.png', 'Reality.png', 
                         'romance.png', 'terror.png', 'otros.png']
    subposterstvshowss = []
    for subposterstvshow in subposterstvshows:
        subposterstvshowss.append(os.path.join(dir_pos_tvs, subposterstvshow))
    return subposterstvshowss

def subfanartstvshows():
    dir_fan_tvs = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'tv show', 'fanart')
    subfanartstvshows = ['fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png', 'fanart.png']
    subfanartstvshowss = []
    for subfanartstvshow in subfanartstvshows:
        subfanartstvshowss.append(os.path.join(dir_fan_tvs, subfanartstvshow))
    return subfanartstvshowss

def subinfostvshows():
    subinfostvshows = ['Todos los TV Shows','Mas Populares','Mejor Valoradas', 'Acción y Aventura', 'Animación', 'Ciencia Ficción y Fantasía', 'Comedia', 'Crimen', 'Documental', 'Drama', 'Familia', 'Guerra y Politica', 'Historia', 'Kids', 'Misterio', 'Occidental', 'Reality', 'Romance', 'Terror', 'Aún no catalogados']
    return subinfostvshows

def submodestvshows():
    submodestvshows = ['tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows', 'tvshows']
    return submodestvshows

def subtagstvshows():
    submodestvshows = ['all','populares','mejor', 'accion', 'animacion', 'ciencia', 'comedia', 'crimen', 'documental', 'drama', 'familia', 'guerra', 'historia', 'kids', 'misterio', 'occidental', 'reality', 'romance', 'terror', 'otros']
    return submodestvshows


#Subcategorias de Television

def subcategoriastv():
    subcategoriastv = ['Mis Listas', 'Listas Compartidas', 'Mis Listas Compartidas']
    return subcategoriastv

def subfanartstv():
    subfanartstv = ['http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg']
    return subfanartstv

def subinfostv():
    subinfostv = ['','','']
    return subinfostv

def submodestv():
    submodestv = ['read_my_lists', 'get_shared_lists', 'get_my_shared_lists']
    return submodestv

def subposterstv():
    submodestv = ['http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg']
    return submodestv


#Subcategorias de Herramientas
def subtools():
    subtools = ['Conversion de M3U a JSON', 'Agregar una Lista[COLOR green] Activo en ajustes[/COLOR]', 'Compartir una Lista Local[COLOR green] Activo en ajustes[/COLOR]', 'Compatir una Lista de RED[COLOR green] Activo en ajustes[/COLOR]']
    return subtools

def subtoolsinfos():
    subtoolsinfos = ['','','','']
    return subtoolsinfos

def subtoolsposters():
    subtoolsfanarts = ['http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg']
    return subtoolsfanarts

def subtoolsfanarts():
    subtoolsfanarts = ['http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg','http://fusionorg.net/images/fanart.jpg']
    return subtoolsfanarts

def subtoolsmodes():
    subtoolsmodes = ['conversion','open_settings', 'open_settings','open_settings']
    return subtoolsmodes

""" Subcategorias de Colecciones"""
def subcategoriascollections():
    subcategoriascollections = ['Coleciones de Actores','Colecciones de Películas']
    return subcategoriascollections


def suburlcollections():
    urlcollections = ['http://fusionorg.net/colecciones/index.php?type=persons','http://fusionorg.net/colecciones/index.php?type=movies']
    return urlcollections

def subposterscollections():
    dir_pos_col = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'collections')
    subposters = ['persons.png','movies.png']
    subposterss = []
    for subposter in subposters:
        subposterss.append(os.path.join(dir_pos_col, subposter))
    return subposterss

def subfanartscollections():
    dir_fan_pel = os.path.join(tools.get_dir_addon(), 'resources', 'media', 'peliculas', 'fanart')
    subfanarts = ['fanart.png','fanart.png']
    subfanartss = []
    for subfanart in subfanarts:
        subfanartss.append(os.path.join(dir_fan_pel, subfanart))
    return subfanartss

def subinfoscollections():
    subinfos = ['Coleccion de peliculas por Actores o Directores','Coleccion de peliculas por Secuela']
    return subinfos


def submodescollections():
    submodes = ['collection','collection']
    return submodes
