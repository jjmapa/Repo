### ############################################################################################################
###	#	
### # Project: 			#		Connect 4 (Game) - by The Highway 2013-2014.
### # Author: 			#		The Highway
### # Version:			#		
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Plugin Settings ###
def ps(x):
	if (x=='_addon_id') or (x=='addon_id') or (x=='_plugin_id') or (x=='plugin_id'): return 'script.game.connect4'
	try: 
		return {
			'__plugin__': 					"Connect 4"
			,'__authors__': 				"[COLOR white]The[COLOR tan]Highway[/COLOR][/COLOR]"
			,'__credits__': 				""
			,'_domain_url': 				"http://example.com"
			,'_database_name': 			"test"
			,'_addon_path_art': 		"art"
			,'special.home.addons': 'special:'+os.sep+os.sep+'home'+os.sep+'addons'+os.sep
			,'special.home': 				'special:'+os.sep+os.sep+'home'
			,'content_movies': 			"movies"
			,'content_tvshows': 		"tvshows"
			,'content_episodes': 		"episodes"
			,'content_links': 			"list"
			,'common_word': 				"Anime"
			,'common_word2': 				"Watch"
			,'default_art_ext': 		'.png'
			,'default_cFL_color': 	'green'
			,'cFL_color': 					'lime'
			,'cFL_color2': 					'yellow'
			,'cFL_color3': 					'red'
			,'cFL_color4': 					'grey'
			,'cFL_color5': 					'white'
			,'cFL_color6': 					'blanchedalmond'
			,'clr0': 								'white'
			,'clr1': 								'blue'
			,'clr2': 								'white'
			,'clr3': 								'blue'
			,'clr4': 								'white'
			,'clr5': 								'pink'
			,'clr6': 								'red'
			,'clr7': 								'white'
			,'clr8': 								'white'
			,'clr9': 								'white'
			,'clr10': 							'ghostwhite'
			,'clr11': 							'green'
			,'clr12': 							'green'
			,'clr13': 							'lavender'
			,'default_section': 		'movies'
			,'section.wallpaper':		'wallpapers'
			,'section.movie': 			'movies'
			,'section.tvshows': 		'tvshows'
			,'section.anime': 			'anime'
			,'section.trailers':		'trailers'
			,'section.trailers.popular':			'trailerspopular'
			,'section.trailers.releasedate':	'trailersreleasedate'
			,'section.users':				'users'
			,'section.tv': 					'tv'
			,'cMI.showinfo.name': 						'Show Information'
			,'cMI.showinfo.url': 							'XBMC.Action(Info)'
			,'cMI.favorites.tv.add.url': 			'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&dbid=%s&subfav=%s)'
			,'cMI.favorites.tv.add.name': 		'Add Favorite'
			,'cMI.favorites.tv.add.mode': 		'FavoritesAdd'
			,'cMI.favorites.movie.add.url': 	'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&subfav=%s)'
			,'cMI.favorites.tv.remove.url': 	'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&dbid=%s&subfav=%s)'
			,'cMI.favorites.tv.remove.name': 	'Remove Favorite'
			,'cMI.favorites.tv.remove.mode': 	'FavoritesRemove'
			,'cMI.favorites.movie.remove.url': 'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&subfav=%s)'
			,'cMI.airdates.find.name': 				'Find AirDates'
			,'cMI.airdates.find.url': 				'XBMC.RunPlugin(%s?mode=%s&title=%s)'
			,'cMI.airdates.find.mode': 				'SearchForAirDates'
			,'cMI.showinfo.name': 						'Show Information'
			,'cMI.showinfo.url': 							'XBMC.Action(Info)'
			,'cMI.1ch.search.folder': 				'plugin.video.1channel'
			,'cMI.1ch.search.name': 					'Search 1Channel'
			,'cMI.1ch.search.url': 						'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)'
			,'cMI.1ch.search.plugin': 				'plugin://plugin.video.1channel/'
			,'cMI.1ch.search.section': 				'movies'
			,'cMI.1ch.search.section.tv': 		'tv'
			,'cMI.primewire.search.folder': 	'plugin.video.primewire'
			,'cMI.primewire.search.name': 		'Search PrimeWire.ag'
			,'cMI.primewire.search.url': 			'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)'
			,'cMI.primewire.search.plugin': 	'plugin://plugin.video.primewire/'
			,'cMI.primewire.search.section': 	'movies'
			,'cMI.primewire.search.section.tv':	'tv'
			,'cMI.jDownloader.addlink.url':		'XBMC.RunPlugin(plugin://plugin.program.jdownloader/?action=addlink&url=%s)'
		}[x]
	except: return ''
### ##### /\ ##### Plugin Settings ###
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
##### Imports #####
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import re,os,sys,string,StringIO,logging,random,array,time,datetime
try:
	try: 		import StorageServer
	except: import storageserverdummy as StorageServer
except: pass
try: 			from addon.common.addon 				import Addon
except: 
	try: 		from t0mm0.common.addon 				import Addon
	except: from t0mm0_common_addon 				import Addon
try: 			from addon.common.net 					import Net
except: 
	try: 		from t0mm0.common.net 					import Net
	except: from t0mm0_common_net 					import Net
import glob
##### /\ ##### Imports #####
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
__plugin__=ps('__plugin__'); __authors__=ps('__authors__'); __credits__=ps('__credits__'); 
_plugin_id=ps('_addon_id'); _addon_id=ps('_addon_id'); _domain_url=ps('_domain_url'); _du=ps('_domain_url'); 
_database_name=ps('_database_name'); _database_file=os.path.join(xbmc.translatePath("special://database"),ps('_database_name')+'.db'); 
### 
try: _addon=Addon(ps('_addon_id'), sys.argv); 
except: _addon=Addon(ps('_addon_id'), 0); 
addon=_addon; 
_plugin=xbmcaddon.Addon(id=ps('_addon_id')); 
cache=StorageServer.StorageServer(ps('_addon_id'))
### 
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
##Notes-> I placed these here so that they would be before the stuff that they use during setup.
def addstv(id,value=''): _addon.addon.setSetting(id=id,value=value) ## Save Settings
def addst(r,s=''): return _addon.get_setting(r)   ## Get Settings
def addpr(r,s=''): return _addon.queries.get(r,s) ## Get Params
def tfalse(r,d=False): ## Get True / False
	if   (r.lower()=='true' ): return True
	elif (r.lower()=='false'): return False
	else: return d
##### Paths #####
### # ps('')
_addonPath	=xbmc.translatePath(_plugin.getAddonInfo('path'))
_artPath		=xbmc.translatePath(os.path.join(_addonPath,ps('_addon_path_art')))
_datapath 	=xbmc.translatePath(_addon.get_profile()); _artIcon		=_addon.get_icon(); _artFanart	=_addon.get_fanart()
##### /\ ##### Paths #####
##### Important Functions with some dependencies #####
def art(f,fe=ps('default_art_ext')): return xbmc.translatePath(os.path.join(_artPath,f+fe)) ### for Making path+filename+ext data for Art Images. ###
##### /\ ##### Important Functions with some dependencies #####
##### Settings #####
_setting={}; 
##Notes-> options from the settings.xml file.
_setting['enableMeta']	=	_enableMeta			=tfalse(addst("enableMeta"))
_setting['debug-enable']=	_debugging			=tfalse(addst("debug-enable")); _setting['debug-show']	=	_shoDebugging		=tfalse(addst("debug-show"))
_setting['label-empty-favorites']=tfalse(addst('label-empty-favorites'))
##Notes-> some custom settings.
#_setting['meta.movie.domain']=ps('meta.movie.domain'); _setting['meta.movie.search']=ps('meta.movie.search')
#_setting['meta.tv.domain']   =ps('meta.tv.domain');    _setting['meta.tv.search']   =ps('meta.tv.search')
#_setting['meta.tv.page']=ps('meta.tv.page'); _setting['meta.tv.fanart.url']=ps('meta.tv.fanart.url'); 
#_setting['meta.tv.fanart.url2']=ps('meta.tv.fanart.url2'); 
##### /\ ##### Settings #####
##### Variables #####
_default_section_=ps('default_section'); net=Net(); DB=_database_file; BASE_URL=_domain_url;
### ############################################################################################################
##Notes-> Some important time saving functions to shorten your work later.
def eod(): _addon.end_of_directory() ## used at the end of a folder listing to print the list to the screen.
def myNote(header='',msg='',delay=5000,image=''): _addon.show_small_popup(title=header,msg=msg,delay=delay,image=image)
def cFL( t,c=ps('default_cFL_color')): return '[COLOR '+c+']'+t+'[/COLOR]' ### For Coloring Text ###
def cFL_(t,c=ps('default_cFL_color')): return '[COLOR '+c+']'+t[0:1]+'[/COLOR]'+t[1:] ### For Coloring Text (First Letter-Only) ###
def notification(header="", message="", sleep=5000 ): xbmc.executebuiltin( "XBMC.Notification(%s,%s,%i)" % ( header, message, sleep ) )
def WhereAmI(t): ### for Writing Location Data to log file ###
	if (_debugging==True): print 'Where am I:  '+t
def deb(s,t): ### for Writing Debug Data to log file ###
	if (_debugging==True): print s+':  '+t
def debob(t): ### for Writing Debug Object to log file ###
	if (_debugging==True): print t
def nolines(t):
	it=t.splitlines(); t=''
	for L in it: t=t+L
	t=((t.replace("\r","")).replace("\n","")); return t
def isPath(path): return os.path.exists(path)
def isFile(filename): return os.path.isfile(filename)
def askSelection(option_list=[],txtHeader=''):
	if (option_list==[]): 
		if (debugging==True): print 'askSelection() >> option_list is empty'
		return None
	dialogSelect=xbmcgui.Dialog(); index=dialogSelect.select(txtHeader,option_list); return index
def iFL(t): return '[I]'+t+'[/I]' ### For Italic Text ###
def bFL(t): return '[B]'+t+'[/B]' ### For Bold Text ###
def _FL(t,c,e=''): ### For Custom Text Tags ###
	if (e==''): d=''
	else: d=' '+e
	return '['+c.upper()+d+']'+t+'[/'+c.upper()+']'
def ParseDescription(plot): ## Cleans up the dumb number stuff thats ugly.
	if ("&amp;"  in plot):  plot=plot.replace('&amp;'  ,'&')#&amp;#x27;
	if ("&nbsp;" in plot):  plot=plot.replace('&nbsp;' ," ")
	if ('&#' in plot) and (';' in plot):
		if ("&#8211;" in plot): plot=plot.replace("&#8211;",";") #unknown
		if ("&#8216;" in plot): plot=plot.replace("&#8216;","'")
		if ("&#8217;" in plot): plot=plot.replace("&#8217;","'")
		if ("&#8220;" in plot): plot=plot.replace('&#8220;','"')
		if ("&#8221;" in plot): plot=plot.replace('&#8221;','"')
		if ("&#215;"  in plot): plot=plot.replace('&#215;' ,'x')
		if ("&#x27;"  in plot): plot=plot.replace('&#x27;' ,"'")
		if ("&#xF4;"  in plot): plot=plot.replace('&#xF4;' ,"o")
		if ("&#xb7;"  in plot): plot=plot.replace('&#xb7;' ,"-")
		if ("&#xFB;"  in plot): plot=plot.replace('&#xFB;' ,"u")
		if ("&#xE0;"  in plot): plot=plot.replace('&#xE0;' ,"a")
		if ("&#0421;" in plot): plot=plot.replace('&#0421;',"")
		if ("&#xE9;" in plot):  plot=plot.replace('&#xE9;' ,"e")
		if ("&#xE2;" in plot):  plot=plot.replace('&#xE2;' ,"a")
		#if (chr(239) in plot):  plot=plot.replace(chr(239) ,"'")
		#plot=plot.replace(chr('0x92'),"'")
		if ('&#' in plot) and (';' in plot):
			try:		matches=re.compile('&#(.+?);').findall(plot)
			except:	matches=''
			if (matches is not ''):
				for match in matches:
					if (match is not '') and (match is not ' ') and ("&#"+match+";" in plot):  plot=plot.replace("&#"+match+";" ,"")
		#if ("\xb7"  in plot):  plot=plot.replace('\xb7'   ,"-")
		#if ('&#' in plot) and (';' in plot): plot=unescape_(plot)
	for i in xrange(127,256): plot=plot.replace(chr(i),"")
	return plot
def unescape_(s): p=htmllib.HTMLParser(None); p.save_bgn(); p.feed(s); return p.save_end()
def messupText(t,_html=False,_ende=False,_a=False,Slashes=False):
	if (_html==True): 
		try: t=HTMLParser.HTMLParser().unescape(t)
		except: t=t
		try: t=ParseDescription(t)
		except: t=t
	if (_ende==True): 
		try: t=t.encode('ascii', 'ignore'); t=t.decode('iso-8859-1')
		except: t=t
	if (_a==True): 
		try: t=_addon.decode(t); t=_addon.unescape(t)
		except: t=t
	if (Slashes==True): 
		try: t=t.replace( '_',' ')
		except: t=t
	#t=t.replace("text:u","")
	return t
def aSortMeth(sM,h=''):
	if h=='':
		try: h=int(sys.argv[1])
		except: h=0
	xbmcplugin.addSortMethod(handle=h, sortMethod=sM)
def set_view(content='none',view_mode=50,do_sort=False):
	h=int(sys.argv[1]); deb('content type',str(content)); deb('view mode',str(view_mode))
	if (content is not 'none'): xbmcplugin.setContent(h, content)
	if (tfalse(addst("auto-view"))==True): xbmc.executebuiltin("Container.SetViewMode(%s)" % view_mode)
def showkeyboard(txtMessage="",txtHeader="",passwordField=False):
	if txtMessage=='None': txtMessage=''
	keyboard=xbmc.Keyboard(txtMessage,txtHeader,passwordField); keyboard.doModal()
	if keyboard.isConfirmed(): return keyboard.getText()
	else: return False
### ############################################################################################################
### ############################################################################################################
### Skinning Stuff ###
_mediaPath=xbmc.translatePath(os.path.join(_addonPath,'resources','skins','default','media'))
_soundPath=xbmc.translatePath(os.path.join(_addonPath,'resources','skins','default','sounds'))
def media (f,fe=''): return xbmc.translatePath(os.path.join(_mediaPath,f+fe))
def mediaj(f,fe='.jpg'): return media(f,fe)
def mediap(f,fe='.png'): return media(f,fe)
def mediab(f,fe='.bmp'): return media(f,fe)
def mediag(f,fe='.gif'): return media(f,fe)
def sound (f,fe=''): return xbmc.translatePath(os.path.join(_soundPath,f+fe))
def soundw(f,fe='.wav'): return sound(f,fe)
def myNote2(header='',msg='',delay=5000,image=media('4hub-board.png')): _addon.show_small_popup(title=header,msg=msg,delay=delay,image=image)


CWD=os.getcwd().rstrip(";")
def getUserSkin():
	current_skin=xbmc.getSkinDir()
	force_fallback=os.path.exists(os.path.join(CWD,"resources","skins",current_skin))
	if not force_fallback: current_skin="Default"
	return current_skin, force_fallback

#import glob
#if glob.sounds_effect: 
SFX=tfalse(addst('SFX','true'))
def Sounds(track):	
	if SFX==True: xbmc.Player().play(track)
def Songs(track):		xbmc.Player().play(track)
def Talk(track):		xbmc.Player().play(track)

class Image(xbmcgui.ControlImage):
	def __new__(cls, *args, **kwargs): return super(Image, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)

class TextBox(xbmcgui.ControlTextBox):
	def __new__(cls, *args, **kwargs): return super(TextBox, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)

class Label(xbmcgui.ControlLabel):
	def __new__(cls, *args, **kwargs): return super(Label, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)

class FadeLabel(xbmcgui.ControlFadeLabel):
	def __new__(cls, *args, **kwargs): return super(FadeLabel, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)

#class Button(xbmcgui.ControlButton):
#	def __new__(cls, *args, **kwargs): 
#		textures = {'focusTexture': os.path.join(_images, 'Button', 'KeyboardKey.png'),'noFocusTexture': os.path.join(_images, 'Button', 'KeyboardKeyNF.png')}
#		_set_textures(textures, kwargs)
#		try: kwargs['alignment']
#		except KeyError: kwargs['alignment'] = ALIGN_CENTER
#		return super(Button, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)

#class Edit(xbmcgui.ControlEdit):
#	def __new__(cls, *args, **kwargs):
#		textures = {'focusTexture': os.path.join(_images, 'Edit', 'button-focus.png'),'noFocusTexture': os.path.join(_images, 'Edit', 'black-back2.png')}
#		_set_textures(textures, kwargs)
#		return super(Edit, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)

#class List(xbmcgui.ControlList):
#	def __new__(cls, *args, **kwargs):
#		textures = {'buttonTexture': os.path.join(_images, 'List', 'MenuItemNF.png'),'buttonFocusTexture': os.path.join(_images, 'List', 'MenuItemFO.png')}
#		_set_textures(textures, kwargs)
#		return super(List, cls).__new__(cls, -10, -10, 1, 1, *args, **kwargs)




#class MyWindow(xbmcgui.BaseWindowDialog):
#class MyWindow( xbmcgui.WindowXML ):
#class MyWindow(xbmcgui.WindowDialog):
class MyWindow(xbmcgui.WindowXMLDialog):
	WindowID=9099
	Background=media('black1.png')     #Pure Black
	Backdrop="" #media('bg-hub-01.png') #background image
	TextWindowBackdrop=''; TextName=''; TextSaid=''
	MyStrings={}; GameSlot1x1=''; CurrentPlayerCoin=''
	CoinPlayer1=media('coin-4hub-black.png') #4hub-black.png
	CoinPlayer2=media('coin-4hub-red.png')   #4hub-red.png
	BoardImgZ=media('4hub-board.png')
	BoardImg=media('4hub-board2a.png')
	BoardImgBS=media('HLP-ScrollBarV_bar_focus.png')
	WP1=addst("name-Player1","1st Player")+" Wins"; WP2=addst("name-Player2","2nd Player")+" Wins"
	#def __init__(self):
	#SKIN_PATH = os.path.join( __addonDir__, "resources", "skins", "Default/" ).replace( "\\", "/" )
	def __init__(self, *args, **kwargs):
		self.Backdrop=self.GetBackgroundSetting()
		self.CoinPlayer1=self.SetCoinLook(1); self.CoinPlayer2=self.SetCoinLook(2); self.MyStrings['WindowBack']=self.Background; self.MyStrings['WindowBG']=self.Backdrop; self.MyStrings['GameSlotBlank']=self.BoardImgBS; 
		self.MyStrings['WindowBack']
		self.change('WindowBack',self.MyStrings['WindowBack']); self.change('WindowBG',self.MyStrings['WindowBG'])
		for yy in range(1,7):   #--- y=1,7
			for xx in range(1,8): #||| x=1,8
				try: 
					self.MyStrings['GameSlot'+str(yy)+'x'+str(xx)]=self.BoardImg
					self.change('GameSlot'+str(yy)+'x'+str(xx),self.MyStrings['GameSlot'+str(yy)+'x'+str(xx)])
				except: pass
				try: self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)]=self.MyStrings['GameSlotBlank']
				except: pass
				try: 
					self.MyStrings['pbGameSlot'+str(yy)+'x'+str(xx)]=self.MyStrings['GameSlotBlank']
					self.change('pbGameSlot'+str(yy)+'x'+str(xx),self.MyStrings['pbGameSlot'+str(yy)+'x'+str(xx)])
				except: pass
				try: self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)+'A']=''
				except: pass
				try: self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)+'V']=''
				except: pass
		for xx in range(1,8): #x=1,8
			self.MyStrings['GameSlot0x'+str(xx)+'TC']='silver'; self.MyStrings['GameSlot0x'+str(xx)]=self.BoardImgZ
			self.MyStrings['GameSlot0x'+str(xx)+'E']='true'
			self.MyStrings['GameSlot0x'+str(xx)+'V']='true'
		###self.MyStrings['GameSlot0x'+str(3)+'E']=''
		#tTt=['','X','B','M','C','H','U','B']; 
		tTt=['',addst("button-text1",'X'),addst("button-text2",'B'),addst("button-text3",'M'),addst("button-text4",'C'),addst("button-text5",'H'),addst("button-text6",'U'),addst("button-text7",'B')]; 
		self.MyStrings['GameSlot0x'+str(1)+'LT']=tTt[1]; self.MyStrings['GameSlot0x'+str(2)+'LT']=tTt[2]; self.MyStrings['GameSlot0x'+str(3)+'LT']=tTt[3]; self.MyStrings['GameSlot0x'+str(4)+'LT']=tTt[4]; self.MyStrings['GameSlot0x'+str(5)+'LT']=tTt[5]; self.MyStrings['GameSlot0x'+str(6)+'LT']=tTt[6]; self.MyStrings['GameSlot0x'+str(7)+'LT']=tTt[7]
		self.MyStrings['WhosTurnTC']='red'; self.MyStrings['WhosTurnLT']="Onwards and Hubwards" #"Player #[COLOR maroon]1[/COLOR]'s turn."
		self.MyStrings['TextNameClr']='purple'; self.MyStrings['TextName']='Author'
		self.MyStrings['Titleimg']=media('4hub-title01.png'); self.MyStrings['TitleTC']='gold'; self.MyStrings['TitleLT']='' #'C  o  n  n  e  c  t      4'
		self.MyStrings['GamePR']=self.CoinPlayer2; self.MyStrings['GamePB']=self.CoinPlayer1; self.switchPlayers(); 
		###
		
		#self.TestA=Image(self.CoinPlayer1,aspectRatio=0)
		#self.TestA=xbmcgui.ControlImage(126,215,93,93,filename=self.CoinPlayer1,aspectRatio=0)
		#self.addControl(self.TestA)
		
		#cSetImage(self,1,media('coin-4hub-punkin.png'))
		#cSetImage(self,2,media('coin-4hub-punkin.png'))
		#cSetImage(self,3,media('coin-4hub-punkin.png'))
		#cSetImage(self,4,media('coin-4hub-punkin.png'))
		
		###
		self.ScreenUpdate()
		###
	def ScreenUpdate(self):
		##self.change('WindowBack',self.MyStrings['WindowBack']); self.change('WindowBG',self.MyStrings['WindowBG'])
		for xx in range(1,8): #x=1,8
			self.change('GameSlot0x'+str(xx)+'LT',self.MyStrings['GameSlot0x'+str(xx)+'LT']); 
			self.change('GameSlot0x'+str(xx)+'TC',self.MyStrings['GameSlot0x'+str(xx)+'TC']); 
			self.change('GameSlot0x'+str(xx)+'',self.MyStrings['GameSlot0x'+str(xx)])
			self.change('GameSlot0x'+str(xx)+'E',self.MyStrings['GameSlot0x'+str(xx)+'E']); 
			self.change('GameSlot0x'+str(xx)+'V',self.MyStrings['GameSlot0x'+str(xx)+'V']); 
		
		#self.setC(self.TestA,126,215,93,93)
		#self.TestB=xbmcgui.ControlImage(126,215,93,93,filename=self.CoinPlayer1,aspectRatio=0)
		#self.addControl(self.TestB)
		#self.TestC=xbmcgui.ControlLabel(126,315,93,93,label="Hello",textColor="0xFFFFFFFF")
		#self.addControl(self.TestC)
		#self.TestB.show()
		#self.TestC.show()
		self.change('Titleimg',self.MyStrings['Titleimg']); self.change('WhosTurnTC',self.MyStrings['WhosTurnTC']); self.change('WhosTurnLT',self.MyStrings['WhosTurnLT']); self.change('TitleTC',self.MyStrings['TitleTC']); self.change('TitleLT',self.MyStrings['TitleLT']); self.change('GamePR',self.MyStrings['GamePR']); self.change('GamePB',self.MyStrings['GamePB'])
		#self.change('TitleimgX',str(100));
		for yy in range(1,7):   #y=1,7
			for xx in range(1,8): #x=1,8
				try: self.change('pGameSlot'+str(yy)+'x'+str(xx),self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)])
				except: pass
				try: self.change('pGameSlot'+str(yy)+'x'+str(xx)+'V',self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)+'V'])
				except: pass
		#
	def setC(self,control,x=0,y=0,w=0,h=0,aC=True):
		control.setPosition(x,y); control.setWidth(w); control.setHeight(h)
		if aC==True: self.addControl(control)
	def GetBackgroundSetting(self,x=""):
		if x=="": x=addst("BackgroundImg","XBMCHub01")
		try:
			return {
				"XBMCHub01": media('bg-hub-01.png')
				,"Black": media('black.png')
				,"XBMC13GothamOct": "http://xbmc.org/wp-content/uploads/xbmc-gotham-teaser-600x336.jpg"
				,"XBMC13GothamNOv": "http://xbmc.org/wp-content/uploads/xbmc-gotham-teaser2-600x336.jpg"
				,"XBMCHub02Screens": "http://www.mirrorservice.org/sites/addons.superrepo.org/Frodo/.metadata/repository.xbmchub.jpg"
				,"XBMCHub03Raindrops": "http://www.mirrorservice.org/sites/addons.superrepo.org/Frodo/.metadata/plugin.video.tv-release.jpg"
				,"XBMCHub04Future": "http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg"
				,"XBMCHub05": "http://oi43.tinypic.com/j996vn.jpg"
				,"XBMCHub06Karaoke": "http://img5.imageshack.us/img5/8058/5abl.jpg"
				,"XBMCHub07ThirdPartyAddons": "http://longhoang.ca/blog/wp-content/uploads/2012/12/atv2_xbmc_hub_1.jpg"
			}[x]
		except: return media('bg-hub-01.png')
	def GetCoinSetting(self,WhichCoin=1):
		if   WhichCoin==1: CoinImgS=addst('CoinImg1','Hub-Black')
		elif WhichCoin==2: CoinImgS=addst('CoinImg2','Hub-Red')
		## Hub-Black|Hub-Red|Black|Red|Hub-Pumpkin|BlueBox|MovieFilm|UsbLizard|
		## XBMC-Cool3D|XBMC-Fan|XBMC-Gamer|XBMC-Pizza|XBMC-Owl1|XBMC-Pose|TVToon|Viking-Fied|Viking-Dahls
		try:
			return {
				'Hub-Black': media('coin-4hub-black.png'),'Hub-Red': media('coin-4hub-red.png')
				,'Black': media('coin-black.png'),'Red': media('coin-red.png')
				,'Hub-Pumpkin': media('coin-4hub-punkin.png')
				,'BlueBox': media('coin-bluebox.png'),'BlueMoon': media('coin-bluemoon2.jpg')
				,'MovieFilm': media('coin-moviefilm2.png')
				,'UsbLizard': media('coin-usb-lizard.png'),'TVToon': media('coin-xbmc-tvtoon.png')
				,'XBMC-Cool3D': media('coin-xbmc-cool3d.jpg'),'XBMC-Fan': media('coin-xbmc-fan.jpg'),'XBMC-Gamer': media('coin-xbmc-gamer.jpg'),'XBMC-Pizza': media('coin-xbmc-pizza.jpg')
				,'XBMC-Owl1': media('coin-xbmc-owl1.jpg'),'XBMC-Pose': media('coin-xbmc-pose-painted2.png')
				,'Viking-Fied': media('coin-xbmc-spiff-zappyfied.png'),'Viking-Dahls': media('coin-xbmc-spiff-zappyfied-dahls.png')
				,'SuperRepo':media('coin-SuperRepo3.png')
				,'Ouya': media('coin-ouya2.jpg')
				,'AppleTV2': media('coin-AppleTV2b.png'),'AppleTV1': media('coin-AppleTV1a.png')
				,'AndroidToon': media('coin-AndroidToon.png'),'AndroidToon2': media('coin-AndroidToon2.jpg') #,'AndroidToon3': media('coin-AndroidToon3.png')
				,'GBoxMX2': media('coin-GBoxMX2c.jpg')
				,'BoxeeLogo': media('coin-BoxeeLogoA.jpg')
				###
				,'Avatar-BlazeTamer': media('coin-avatar-blazetamer.png')
				,'Avatar-Showgun': media('coin-avatar-showgun.jpg')
				###
				,'Addon-RadioPlayerUK': media('coin-audio-RadioPlayerUK-icon.png')
				,'Addon-SearchMP3mobi': media('coin-audio-SearchMp3Mobi-icon.png')
				,'Addon-TheFunkStation': media('coin-audio-TheFunkStation-icon.png')
				,'Addon-IrcChat': media('coin-program-IrcChat-icon.png')
				,'Repo-BlazeTamer': media('coin-repo-Blaze-icon.png')
				,'Repo-Lamda': media('coin-repo-Lambda-icon.png')
				,'Repo-Rodrigo': media('coin-repo-Rodrigo-icon.png')
				,'Repo-SuperRepo': media('coin-repo-SuperRepo-icon.png')
				,'Repo-TheHighway': media('coin-repo-TheHighway-icon.png')
				,'Repo-TheSilencer': media('coin-repo-TheSilencer-icon.png')
				,'Repo-XBMCHub': media('coin-repo-XBMCHub-icon.png')
				,'Addon-XBMCHub-FreshStart': media('coin-tool-XBMCHubFreshStart-icon.png')
				,'Addon-XBMCHub-MaintenanceTool': media('coin-tool-XBMCHubMaintenanceTool-icon.png')
				,'Addon-XBMCHub-Wizard': media('coin-tool-XBMCHubWizard-icon.png')
				,'Addon-1Channel': media('coin-video-1Channel-icon.png')
				,'Addon-Anime44': media('coin-video-Anime44-icon.png')
				#,'Addon-AnimeGet': media('coin-video-AnimeGET-icon.png')
				,'Addon-CanadaOnDemand': media('coin-video-CanadaOnDemand-icon.png')
				,'Addon-CelticTV': media('coin-video-CelticTV-icon.png')
				,'Addon-CrunchyRoll': media('coin-video-CrunchyRoll-icon.png')
				,'Addon-DailyMotion': media('coin-video-DailyMotion-icon.png')
				#,'Addon-DocuHub': media('coin-video-DocuHub-icon.png')
				,'Addon-FamilyFunFlix': media('coin-video-FamilyFunFlix-icon.png')
				,'Addon-FreeCable': media('coin-video-FreeCable-icon.png')
				,'Addon-FTV': media('coin-video-FTV-icon.png')
				,'Addon-GoTV': media('coin-video-GoTV-icon.png')
				,'Addon-Hulu': media('coin-video-Hulu-icon.png')
				,'Addon-IceFilms': media('coin-video-IceFilms-icon.png')
				,'Addon-JustinTV': media('coin-video-JustinTV-icon.png')
				,'Addon-KidsPlace': media('coin-video-KidsPlace-icon.png')
				,'Addon-KissAnime-New': media('coin-video-KissAnime-icon.png')
				,'Addon-KissAnime-Lips': media('coin-video-KissAnime-icon1.png')
				,'Addon-KissManga-Lips': media('coin-manga-KissManga-icon.png')
				,'Addon-MerDB': media('coin-video-MerDB-icon.png')
				,'Addon-MovieFork': media('coin-video-MovieFork-icon.png')
				,'Addon-PopcornFlix': media('coin-video-PopcornFlix-icon.png')
				,'Addon-PrimeWire': media('coin-video-PrimeWire-icon.png')
				,'Addon-ProjectFreeTV': media('coin-video-ProejctFreeTV-icon.png')
				,'Addon-SolarMovie': media('coin-video-SolarMovieSO-icon.png')
				,'Addon-SportsDevil': media('coin-video-SportsDevil-icon.png')
				,'Addon-TheBinaryHighway': media('coin-video-TheBinaryHighway-icon.png')
				,'Addon-TheDareTV': media('coin-video-TheDareTV-icon.png')
				,'Addon-TheVideoDevil': media('coin-video-TheVideoDevil-icon.png')
				,'Addon-VideoPhile': media('coin-video-VideoPhile-icon.png')
				#,'Addon-Vidics4': media('coin-video-Vidics4-icon.png')
				,'Addon-WhatTheFurk': media('coin-video-WhatTheFurk-icon.png')
				,'Addon-XBMCHub-Karaoke': media('coin-video-XBMCHubKaraoke-icon.png')
				,'Addon-2Movies': media('coin-video-2Movies-Icon.png')
				#
				#,'': media('')
				#,'': media('')
				#,'': media('')
				#,'': media('')
				#,'': media('')
			}[CoinImgS]
		except: 
			if   WhichCoin==1: return media('coin-4hub-black.png')
			elif WhichCoin==2: return media('coin-4hub-red.png')
		CoinImgS
	def SetCoinLook(self,WhichCoin=1):
		return self.GetCoinSetting(WhichCoin)
		#if   WhichCoin==1: return self.GetCoinSetting(WhichCoin) #media('4hub-black.png') #4hub-black.png
		#elif WhichCoin==2: return self.GetCoinSetting(WhichCoin) #media('4hub-red.png') #4hub-red.png
	def getStringValue(self,Tag,ErResult=''): 
		try: return xbmc.getInfoLabel('Skin.String('+Tag+')')
		except: return ErResult
	def change(self,Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetString('+Tag+', %s)' % NewValue)
	def nchange(self,Tag,NewValue=0):  xbmc.executebuiltin('Skin.SetNumeric('+Tag+', %s)' % NewValue)
	def gchange(self,Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetImage('+Tag+', %s)' % NewValue)
	def gLchange(self,Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetLargeImage('+Tag+', %s)' % NewValue)
	def bchange(self,Tag,NewValue=False):  xbmc.executebuiltin('Skin.SetBool('+Tag+', %s)' % NewValue)
	def tchange(self,Tag,NewValue=False):  xbmc.executebuiltin('Skin.ToggleSetting('+Tag+', %s)' % NewValue)
	def setStringValue(self,Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetString('+Tag+', %s)' % NewValue)
	def TextName_change(self,NewValue=''): xbmc.executebuiltin('Skin.SetString(TextName, %s)' % NewValue)
	def TextSaid_change(self,NewValue=''): xbmc.executebuiltin('Skin.SetString(TextSaid, %s)' % NewValue)
	def TextName_update(self): self.change('TextNameClr',self.MyStrings['TextNameClr']); xbmc.executebuiltin('Skin.SetString(TextName, %s)' % self.MyStrings['TextName'])
	def TextSaid_update(self): self.change('TextSaidClr',self.MyStrings['TextSaidClr']); xbmc.executebuiltin('Skin.SetString(TextSaid, %s)' % self.MyStrings['TextSaid'])
	#def onInit(self): pass
	def onFocus(self,controlID): return
	def onClick(self,controlID):
		try:
			if   controlID==161: self.placeCoin('1',self.MyStrings['CurrentPlayerCoin'])
			elif controlID==162: self.placeCoin('2',self.MyStrings['CurrentPlayerCoin'])
			elif controlID==163: self.placeCoin('3',self.MyStrings['CurrentPlayerCoin'])
			elif controlID==164: self.placeCoin('4',self.MyStrings['CurrentPlayerCoin'])
			elif controlID==165: self.placeCoin('5',self.MyStrings['CurrentPlayerCoin'])
			elif controlID==166: self.placeCoin('6',self.MyStrings['CurrentPlayerCoin'])
			elif controlID==167: self.placeCoin('7',self.MyStrings['CurrentPlayerCoin'])
			elif controlID in (300,330): self._close_game()
		except: pass
		return
	def UpdateWinStats(self,PlayerNo=1):
		#myNote("Player #"+str(PlayerNo)+"'s ","Wins:"+str(addst("wins-Player"+str(PlayerNo),0))+":")
		#try: addstv("wins-Player"+str(PlayerNo),str(addst("wins-Player"+str(PlayerNo),0)+1)); 
		try: t=addst("wins-Player"+str(PlayerNo),0); t=int(t)+1; addstv("wins-Player"+str(PlayerNo),str(t)); 
		except: pass
		myNote2(addst("name-Player"+str(PlayerNo),"Player #"+str(PlayerNo))+"'s ","Wins:"+str(addst("wins-Player"+str(PlayerNo),0))+":")
	def checkSlotsForAWin(self):
		L="|"; WP1=self.WP1; WP2=self.WP2; Winner=""; CP1=self.CoinPlayer1+L+self.CoinPlayer1+L+self.CoinPlayer1+L+self.CoinPlayer1; CP2=self.CoinPlayer2+L+self.CoinPlayer2+L+self.CoinPlayer2+L+self.CoinPlayer2
		### ====
		BTable=''; 
		for yy in range(1,7):   #y=1,7
			BTable+=L+L+L
			for xx in range(1,8): #x=1,8
				BTable+=self.getSlot(yy,xx)+L
		if   BTable.find(CP1) > 0: Winner=WP1; self.UpdateWinStats(1); return Winner
		elif BTable.find(CP2) > 0: Winner=WP2; self.UpdateWinStats(2); return Winner
		### ||||
		BTable=''; 
		for xx in range(1,8): #x=1,8
			BTable+=L+L+L
			for yy in range(1,7):   #y=1,7
				BTable+=self.getSlot(yy,xx)+L
		if   BTable.find(CP1) > 0: Winner=WP1; self.UpdateWinStats(1); return Winner
		elif BTable.find(CP2) > 0: Winner=WP2; self.UpdateWinStats(2); return Winner
		### ////
		BTable=''; 
		BTable+=L+L+L+self.getSlot(4,1)+L+self.getSlot(3,2)+L+self.getSlot(2,3)+L+self.getSlot(1,4)+L
		BTable+=L+L+L+self.getSlot(5,1)+L+self.getSlot(4,2)+L+self.getSlot(3,3)+L+self.getSlot(2,4)+L+self.getSlot(1,5)+L
		BTable+=L+L+L+self.getSlot(6,1)+L+self.getSlot(5,2)+L+self.getSlot(4,3)+L+self.getSlot(3,4)+L+self.getSlot(2,5)+L+self.getSlot(1,6)+L
		BTable+=L+L+L+self.getSlot(6,2)+L+self.getSlot(5,3)+L+self.getSlot(4,4)+L+self.getSlot(3,5)+L+self.getSlot(2,6)+L+self.getSlot(1,7)+L
		BTable+=L+L+L+self.getSlot(6,3)+L+self.getSlot(5,4)+L+self.getSlot(4,5)+L+self.getSlot(3,6)+L+self.getSlot(2,7)+L
		BTable+=L+L+L+self.getSlot(6,4)+L+self.getSlot(5,5)+L+self.getSlot(4,6)+L+self.getSlot(3,7)+L
		if   BTable.find(CP1) > 0: Winner=WP1; self.UpdateWinStats(1); return Winner
		elif BTable.find(CP2) > 0: Winner=WP2; self.UpdateWinStats(2); return Winner
		### \\\\
		BTable=''; 
		BTable+=L+L+L+self.getSlot(3,1)+L+self.getSlot(4,2)+L+self.getSlot(5,3)+L+self.getSlot(6,4)+L
		BTable+=L+L+L+self.getSlot(2,1)+L+self.getSlot(3,2)+L+self.getSlot(4,3)+L+self.getSlot(5,4)+L+self.getSlot(6,5)+L
		BTable+=L+L+L+self.getSlot(1,1)+L+self.getSlot(2,2)+L+self.getSlot(3,3)+L+self.getSlot(4,4)+L+self.getSlot(5,5)+L+self.getSlot(6,6)+L
		BTable+=L+L+L+self.getSlot(1,2)+L+self.getSlot(2,3)+L+self.getSlot(3,4)+L+self.getSlot(4,5)+L+self.getSlot(5,6)+L+self.getSlot(6,7)+L
		BTable+=L+L+L+self.getSlot(1,3)+L+self.getSlot(2,4)+L+self.getSlot(3,5)+L+self.getSlot(4,6)+L+self.getSlot(5,7)+L
		BTable+=L+L+L+self.getSlot(1,4)+L+self.getSlot(2,5)+L+self.getSlot(3,6)+L+self.getSlot(4,7)+L
		if   BTable.find(CP1) > 0: Winner=WP1; self.UpdateWinStats(1); return Winner
		elif BTable.find(CP2) > 0: Winner=WP2; self.UpdateWinStats(2); return Winner
		### Coding not setup for the Victory-Check. ###
		#
		#	Sounds(sound('spin.wav')); return True
		return ""
	def switchPlayers(self,PlayerImage=""):
		try: 
			if   PlayerImage==self.CoinPlayer2: self.MyStrings['CurrentPlayerCoin']=self.CoinPlayer1
			elif PlayerImage==self.CoinPlayer1: self.MyStrings['CurrentPlayerCoin']=self.CoinPlayer2
			else: self.MyStrings['CurrentPlayerCoin']=self.CoinPlayer1
		except: self.MyStrings['CurrentPlayerCoin']=self.CoinPlayer1
		if   self.MyStrings['CurrentPlayerCoin']==self.CoinPlayer1: self.MyStrings['WhosTurnTC']=addst("color-Player1","grey"); self.MyStrings['WhosTurnLT']=addst("name-Player1","1st Player")+"'s turn."
		elif self.MyStrings['CurrentPlayerCoin']==self.CoinPlayer2: self.MyStrings['WhosTurnTC']=addst("color-Player2","red" ); self.MyStrings['WhosTurnLT']=addst("name-Player2","2nd Player")+"'s turn."
		self.change('WhosTurnTC',self.MyStrings['WhosTurnTC']); self.change('WhosTurnLT',self.MyStrings['WhosTurnLT'])
	def getSlot(self,yy,xx): return self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)]
	def CheckAvilableMoves(self):
		for yy in range(1,7):   #y=1,7
			for xx in range(1,8): #x=1,8
				if self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)]==self.MyStrings['GameSlotBlank']: return True
		return False
	def ResetGame(self): self.__init__(); self.switchPlayers(); return
	def placeCoin(self,GameSlotNo,PlayerImage):
		#myNote("in Slot",str(GameSlotNo)) ## For Testing ##
		#deb('GameSlotBlank',self.MyStrings['GameSlotBlank']); deb('pGameSlot6x',self.MyStrings['pGameSlot6x'+str(GameSlotNo)]); deb('pGameSlot5x',self.MyStrings['pGameSlot5x'+str(GameSlotNo)]); deb('pGameSlot4x',self.MyStrings['pGameSlot4x'+str(GameSlotNo)]); deb('pGameSlot3x',self.MyStrings['pGameSlot3x'+str(GameSlotNo)]); deb('pGameSlot2x',self.MyStrings['pGameSlot2x'+str(GameSlotNo)]); deb('pGameSlot1x',self.MyStrings['pGameSlot1x'+str(GameSlotNo)])
		if   self.MyStrings['pGameSlot6x'+str(GameSlotNo)]==self.MyStrings['GameSlotBlank']: ik='6'
		elif self.MyStrings['pGameSlot5x'+str(GameSlotNo)]==self.MyStrings['GameSlotBlank']: ik='5'
		elif self.MyStrings['pGameSlot4x'+str(GameSlotNo)]==self.MyStrings['GameSlotBlank']: ik='4'
		elif self.MyStrings['pGameSlot3x'+str(GameSlotNo)]==self.MyStrings['GameSlotBlank']: ik='3'
		elif self.MyStrings['pGameSlot2x'+str(GameSlotNo)]==self.MyStrings['GameSlotBlank']: ik='2'
		elif self.MyStrings['pGameSlot1x'+str(GameSlotNo)]==self.MyStrings['GameSlotBlank']: ik='1'
		else: 
			if self.CheckAvilableMoves()==False: myNote2(addst("game-msg2a","!! Game Over !!"),addst("game-msg2b","No more moves are available.")); Sounds(sound('spinner.wav')); self.ResetGame(); 
			else: myNote2(addst("game-msg1a","Slot Full"),addst("game-msg1b","Try a different slot")); Sounds(sound('stop.wav')); 
			return #Try A Dif Slot
		#myNote("Slot",str(GameSlotNo)+'x'+str(ik)); ## For Testing ##
		self.MyStrings['pGameSlot'+ik+'x'+str(GameSlotNo)]=self.MyStrings['CurrentPlayerCoin']; Sounds(sound('coin.wav')); 
		self.change('pGameSlot'+ik+'x'+str(GameSlotNo),self.MyStrings['pGameSlot'+ik+'x'+str(GameSlotNo)]); 
		self.MyStrings['pGameSlot'+str(ik)+'x'+str(GameSlotNo)+'A']='true'
		self.MyStrings['pGameSlot'+str(ik)+'x'+str(GameSlotNo)+'V']='true'
		self.change('pGameSlot'+ik+'x'+str(GameSlotNo)+'A',self.MyStrings['pGameSlot'+ik+'x'+str(GameSlotNo)+'A']); 
		self.change('pGameSlot'+ik+'x'+str(GameSlotNo)+'V',self.MyStrings['pGameSlot'+ik+'x'+str(GameSlotNo)+'V']); 
		#xbmc.sleep(1800)
		#self.MyStrings['pGameSlot'+str(ik)+'x'+str(GameSlotNo)+'A']=''
		
		
		############################################################
		######################## System to check if someone Won. ###
		try: Winner=self.checkSlotsForAWin()
		except: Winner=""
		#myNote("Winner System",str(Winner)) ## For Testing ##
		if len(Winner) > 0: 
			self.MyStrings['WhosTurnTC']='purple'; self.MyStrings['WhosTurnLT']=Winner
			self.change('WhosTurnTC',self.MyStrings['WhosTurnTC']); self.change('WhosTurnLT',self.MyStrings['WhosTurnLT'])
			for yy in range(1,7):   #y=1,7
				for xx in range(1,8): #x=1,8
					if self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)]==self.MyStrings['GameSlotBlank']:
						self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)]=self.MyStrings['CurrentPlayerCoin']
					try: self.change('pGameSlot'+str(yy)+'x'+str(xx),self.MyStrings['pGameSlot'+str(yy)+'x'+str(xx)])
					except: pass
			Sounds(sound('spin.wav')); 
			return ###################################################
		self.switchPlayers(self.MyStrings['CurrentPlayerCoin']); 
	def onAction(self,action): 
		if   action==ACTION_NAV_BACK: self.close()
		#if action==ACTION_PREVIOUS_MENU: self.close()
		if action==ACTION_MOVE_UP: self.setFocusId(161)
		if action==ACTION_MOVE_DOWN: self.setFocusId(167)
		if action==ACTION_MOVE_RIGHT: 
			try:
				if (int(self.getFocus().getId()) > 160) and (int(self.getFocus().getId()) < 167): self.setFocusId(self.getFocus().getId()+1)
				elif int(self.getFocus().getId())==167: self.setFocusId(161)
				else: self.setFocusId(167)
			except: self.setFocusId(167)
		if action==ACTION_MOVE_LEFT: 
			#myNote("Control #","value:"+str(int(self.getFocus().getId()))+":")
			try:
				if (int(self.getFocus().getId()) > 161) and (int(self.getFocus().getId()) < 168): self.setFocusId(self.getFocus().getId()-1)
				elif int(self.getFocus().getId())==161: self.setFocusId(167)
				else: self.setFocusId(161)
			except: self.setFocusId(161)
			#
			#self.getControl(312).setPosition(100,300)
			#
		if action==5: return			## - Page UP
		if action==6: return			## + Page DOWN
		if action==7: #return			## Enter
			#controlID=int(self.getFocus().getId())
			#try:
			#	if controlID==161: self.placeCoin('1',self.MyStrings['CurrentPlayerCoin'])
			#	if controlID==162: self.placeCoin('2',self.MyStrings['CurrentPlayerCoin'])
			#	if controlID==163: self.placeCoin('3',self.MyStrings['CurrentPlayerCoin'])
			#	if controlID==164: self.placeCoin('4',self.MyStrings['CurrentPlayerCoin'])
			#	if controlID==165: self.placeCoin('5',self.MyStrings['CurrentPlayerCoin'])
			#	if controlID==166: self.placeCoin('6',self.MyStrings['CurrentPlayerCoin'])
			#	if controlID==167: self.placeCoin('7',self.MyStrings['CurrentPlayerCoin'])
			#	#if controlID in (300,330): self._close_game()
			#except: pass
			#xbmc.sleep(4000)
			return
		if action==11: return			## i
		if action==12: return			## Space
		if action==13: return			## x
		#
		return
	def _close_game(self): xbmc.sleep(100); self.close()


ACTION_PREVIOUS_MENU = 10	## ESC action
ACTION_NAV_BACK = 92	## Backspace action
ACTION_MOVE_LEFT = 1	## Left arrow key
ACTION_MOVE_RIGHT = 2	## Right arrow key
ACTION_MOVE_UP = 3	## Up arrow key
ACTION_MOVE_DOWN = 4	## Down arrow key
ACTION_MOUSE_WHEEL_UP = 104	## Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN = 105	## Mouse wheel down
ACTION_MOUSE_DRAG = 106	## Mouse drag
ACTION_MOUSE_MOVE = 107	## Mouse move

### Images
def cSetImage(WiNdOw,iD,img):  WiNdOw.getControl(iD).setImage(img)
def cSetColorDiffuse(WiNdOw,iD,C):  WiNdOw.getControl(iD).setColorDiffuse(C) #hexString - (example, '0xC0FF0000' (red tint))
### Images, Labels, FadeLabels, Edit
def cSetPos(WiNdOw,iD,X=0,Y=0):  WiNdOw.getControl(iD).setPosition(X,Y)
def cSetSize(WiNdOw,iD,W=0,H=0): WiNdOw.getControl(iD).setWidth(W); WiNdOw.getControl(iD).setHeight(H)
def cSetW(WiNdOw,iD,W=0): WiNdOw.getControl(iD).setWidth(W)
def cSetH(WiNdOw,iD,H=0): WiNdOw.getControl(iD).setHeight(H)
def cSetVisible(WiNdOw,iD,V=True): WiNdOw.getControl(iD).setVisible(V) #bool - True=visible / False=hidden.
def cSetEnabled(WiNdOw,iD,E=True): WiNdOw.getControl(iD).setEnabled(E)
def cSetAnimations(WiNdOw,iD,A=""): WiNdOw.getControl(iD).setAnimations(A) #.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
def cSetConnectDirections(WiNdOw,iD,L=0,R=0,U=0,D=0): 
	if L > 0: WiNdOw.getControl(iD).controlLeft(L)
	if R > 0: WiNdOw.getControl(iD).controlRight(R)
	if U > 0: WiNdOw.getControl(iD).controlUp(U)
	if D > 0: WiNdOw.getControl(iD).controlDown(D)

### Labels, Edit
def cSetLabel(WiNdOw,iD,L=""): 
	try: WiNdOw.getControl(iD).setLabel(L)
	except: pass
def cGetLabel(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getLabel()
	except: return ""
### Edit
def cGetText(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getText()
	except: return ""
def cSetText(WiNdOw,iD,T=""): 
	try: WiNdOw.getControl(iD).setText(T)
	except: pass
def cSetIsPassword(WiNdOw,iD,B=False): 
	try: WiNdOw.getControl(iD).isPassword=B
	except: pass
def cSetNoFocusTexture(WiNdOw,iD,T=""): 
	try: WiNdOw.getControl(iD).noFocusTexture=T
	except: pass
def cSetFocusTexture(WiNdOw,iD,T=""): 
	try: WiNdOw.getControl(iD).focusTexture=T
	except: pass
### CheckMark
def cGetSelected(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getSelected()
	except: return ""
def cSetSelected(WiNdOw,iD,b=False): 
	try: WiNdOw.getControl(iD).setSelected(b) #bool - True=selected (on) / False=not selected (off)
	except: pass
def cSetCheckMarkLabel(WiNdOw,iD,Label="",Font="",textColor="",disabledColor=""): 
	try: WiNdOw.getControl(iD).setSelected(Label,font=Font,textColor=textColor,disabledColor=disabledColor)
	except: pass
### CheckMark, Button
def cSetDisabledColor(WiNdOw,iD,C=""): 
	try: WiNdOw.getControl(iD).setDisabledColor(C) #hexstring - color of disabled checkmark's label. (e.g. '0xFFFF3300')
	except: pass
### Button
def cSetBtnLabel(WiNdOw,iD,Label="",Font="",textColor="",disabledColor="",shadowColor="",focusedColor="",Label2=""): 
	try: WiNdOw.getControl(iD).setSelected(Label,font=Font,textColor=textColor,disabledColor=disabledColor,shadowColor=shadowColor,focusedColor=focusedColor,Label2=Label2)
	except: pass
def cGetLabel2(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getLabel2()
	except: return ""
### Progress
def cGetPercent(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getPercent()
	except: return ""
def cSetPercent(WiNdOw,iD,P): 
	try: WiNdOw.getControl(iD).setPercent(P) #*Note, valid range for percent is 0-100
	except: pass
### Radio
def cSetRadioDimension(WiNdOw,iD,x=0,y=0,w=0,h=0): 
	try: WiNdOw.getControl(iD).setRadioDimension(x,y,w,h)
	except: pass
### List
def cAddItem(WiNdOw,iD,i): 
	try: WiNdOw.getControl(iD).addItem(i) #string, unicode or ListItem - item to add.
	except: pass
def cAddItems(WiNdOw,iD,i): 
	try: WiNdOw.getControl(iD).addItems(i) #List - list of strings, unicode objects or ListItems to add.
	except: pass
def cGetSpace(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getSpace()
	except: return ""
def cGetPosition(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).getSelectedPosition()
	except: return ""
def cGetSize(WiNdOw,iD): 
	try: return WiNdOw.getControl(iD).size()
	except: return ""




### Labels, FadeLabels
def cSetColor(WiNdOw,iD,textcolor="[NULL]",shadowcolor="[NULL]",disabledcolor="[NULL]"): 
	try: 
		if textcolor=="[NULL]": t=""
		else: WiNdOw.getControl(iD).textColor=textcolor
		if shadowcolor=="[NULL]": t=""
		else: WiNdOw.getControl(iD).shadowColor=shadowcolor
		if disabledcolor=="[NULL]": t=""
		else: WiNdOw.getControl(iD).disabledColor=disabledcolor
	except: pass
### Labels, FadeLabels
def cSetFont(WiNdOw,iD,F): 
	try: WiNdOw.getControl(iD).font=F
	except: pass
### Labels
def cSetAngle(WiNdOw,iD,A): 
	try: WiNdOw.getControl(iD).angle=A
	except: pass

### FadeLabels
def cReset(WiNdOw,iD): WiNdOw.getControl(iD).reset()
def cAddLabel(WiNdOw,iD,L=""): WiNdOw.getControl(iD).addLabel(L)






if  __name__ == "__main__": deb('Path',_plugin.getAddonInfo('path')); MyWindow("connect4.xml",_plugin.getAddonInfo('path'),'default').doModal(); del MyWindow
### ############################################################################################################
### ############################################################################################################
##### Queries #####
_param={}
###_param['']=_addon.queries.get('','')
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
##### Player Functions #####
def PlayURL(url):
	play=xbmc.Player(xbmc.PLAYER_CORE_AUTO) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
	try: _addon.resolve_url(url)
	except: t=''
	try: play.play(url)
	except: t=''
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
