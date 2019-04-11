#   script.mantenimiento
#   Copyright (C) 2016  SchisM
#   Script modificado y traducido por Netai.
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys , xbmcvfs , glob
import shutil
import urllib2 , urllib
import re
import os
IiII1IiiIiI1 = 'script.mantenimiento'
iIiiiI1IiI1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'fanart.jpg' ) )
o0OoOoOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'icon.png' ) )
if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
o0OOO = xbmc . translatePath ( 'special://thumbnails' ) ;
iIiiiI = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
Iii1ii1II11i = xbmc . translatePath ( 'special://temp' )
iI111iI = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'script.mantenimiento' )
IiII = os . path . join ( iI111iI , 'media' )
iI1Ii11111iIi = xbmc . translatePath ( 'special://database' )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Thumbnails' , '' ) )
if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
if 56 - 56: ooO00oOoo - O0OOo
if 8 - 8: Oooo0000 * i1IIi11111i / OOOo0 % ooO00oOoo * ooO00oOoo * II111iiii
if 79 - 79: O0OOo
class oOo0oooo00o :
 def __init__ ( self , namei , pathi ) :
  self . name = namei
  self . path = pathi
  if 65 - 65: o0OO0 * iIii1I11I1II1 * i1IIi11111i
  if 18 - 18: iIii1I11I1II1 / o00 + I1i1iI1i / Oo - II111iiii - o00
  if 1 - 1: o00 - o00ooo0 % O0 + OOOo0 - ooO00oOoo / o00
def iIiiI1 ( ) :
 if 68 - 68: OOOo0 - i11iIiiIii - Ooo00oOo00o / o00ooo0 - Ooo00oOo00o + i1IIi
 IiiIII111ii ( 'Borrar la cache' , 'url' , 1 , o0OoOoOO00 )
 IiiIII111ii ( 'Borrar imagenes' , 'url' , 2 , o0OoOoOO00 )
 IiiIII111ii ( 'Purgar paquetes de archivos' , 'url' , 3 , o0OoOoOO00 )
 if 3 - 3: ooO00oOoo + O0
 if 42 - 42: o00ooo0 / i1IIi + i11iIiiIii - Oo0oO0ooo
 if 78 - 78: Ooo00oOo00o
 if 18 - 18: O0 - ooO00oOoo / ooO00oOoo + i1IIi11111i % i1IIi11111i - O0OOo
 if 62 - 62: ooO00oOoo - O0OOo - I1IiI % i1IIi / I1i1iI1i
def OoooooOoo ( name , url , iconimage ) :
 OO = True
 oO0O = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = oO0O )
 return OO
 if 70 - 70: Oo % Oo . O0OOo % Ooo00oOo00o * o0OO0 % I1i1iI1i
 if 23 - 23: i11iIiiIii + OOOo0
def oOo ( name , url , mode , iconimage ) :
 oOoOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO = True
 oO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if 6 - 6: OOOo0 / Oo % Oo0oO0ooo
 OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoO , listitem = oO0O , isFolder = True )
 return OO
 if 84 - 84: i11iIiiIii . o0OO0
def IiiIII111ii ( name , url , mode , iconimage ) :
 oOoOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO = True
 oO0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oO0O . setProperty ( 'fanart_image' , iIiiiI1IiI1I1 )
 OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoO , listitem = oO0O , isFolder = False )
 return OO
 if 100 - 100: Oo0oO0ooo - Oo0oO0ooo - Oooo0000
 if 20 - 20: OoooooooOO
 if 13 - 13: i1IIi - Oo0oO0ooo % I1i1iI1i / iIii1I11I1II1 % ooO00oOoo
 if 97 - 97: i11iIiiIii
 if 32 - 32: Oo * O0 % I1i1iI1i % Oo0oO0ooo . O0OOo
def o0OOOOO00o0O0 ( ) :
 o0o0OOO0o0 = [ ]
 ooOOOo0oo0O0 = sys . argv [ 2 ]
 if len ( ooOOOo0oo0O0 ) >= 2 :
  o0 = sys . argv [ 2 ]
  I11II1i = o0 . replace ( '?' , '' )
  if ( o0 [ len ( o0 ) - 1 ] == '/' ) :
   o0 = o0 [ 0 : len ( o0 ) - 2 ]
  IIIII = I11II1i . split ( '&' )
  o0o0OOO0o0 = { }
  for ooooooO0oo in range ( len ( IIIII ) ) :
   IIiiiiiiIi1I1 = { }
   IIiiiiiiIi1I1 = IIIII [ ooooooO0oo ] . split ( '=' )
   if ( len ( IIiiiiiiIi1I1 ) ) == 2 :
    o0o0OOO0o0 [ IIiiiiiiIi1I1 [ 0 ] ] = IIiiiiiiIi1I1 [ 1 ]
    if 13 - 13: O0OOo + I1IiI - OoooooooOO + Oooo0000 . ooO00oOoo + Ooo00oOo00o
 return o0o0OOO0o0
 if 8 - 8: iIii1I11I1II1 . OOOo0 - iIii1I11I1II1 * Oo0oO0ooo
 if 61 - 61: o0OO0 / Ooo00oOo00o + i1IIi11111i * I1i1iI1i / I1i1iI1i
 if 75 - 75: i1IIi / OoooooooOO - O0 / I1IiI . II111iiii - i1IIi
 if 71 - 71: o00ooo0 + Oo0oO0ooo * o00ooo0 - Ooo00oOo00o * o0OO0
def Oooo0Ooo000 ( ) :
 oo = 5
 ii11I = [ "Realstream" , "Palantir" , "Alfa" , "Url Resolver" , "Cine" ]
 Ooo0OO0oOO = [ "special://profile/addon_data/plugin.video.realstream/cache" , "special://profile/addon_data/plugin.video.palantir/cache" ,
 "special://profile/addon_data/plugin.video.alfa/cache" , "special://profile/addon_data/script.module.urlresolver" ,
 "special://profile/addon_data/plugin.video.cine/cache" ]
 if 50 - 50: OOOo0
 Ii1i11IIii1I = [ ]
 if 52 - 52: o0OO0 - OoooooooOO + Oo0oO0ooo + Oo0oO0ooo - o0OO0 / Oooo0000
 for I1I in range ( oo ) :
  Ii1i11IIii1I . append ( oOo0oooo00o ( ii11I [ I1I ] , Ooo0OO0oOO [ I1I ] ) )
  if 24 - 24: Oo0ooO0oo0oO
 return Ii1i11IIii1I
 if 56 - 56: i1IIi11111i
def o0O ( ) :
 if 72 - 72: ooO00oOoo / i1IIi * Oo - Oooo0000
 if os . path . exists ( iIiiiI ) == True :
  for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( iIiiiI ) :
   OO00Oo = 0
   OO00Oo += len ( O0o0 )
   if OO00Oo > 0 :
    if 51 - 51: O0OOo * o0OO0 + o00 + Ooo00oOo00o
    o0O0O00 = xbmcgui . Dialog ( )
    if o0O0O00 . yesno ( "Borrar Los archivos de la cache" , str ( OO00Oo ) + " Ficheros encontrados" , "Quiere borrarlos?" ) :
     if 86 - 86: o00 / O0OOo % i11iIiiIii
     for I11IiI1I11i1i in O0o0 :
      try :
       if ( I11IiI1I11i1i == "xbmc.log" or I11IiI1I11i1i == "xbmc.old.log" ) : continue
       os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
      except :
       pass
     for iI1ii1Ii in IIIIii :
      try :
       shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
      except :
       pass
       if 92 - 92: I1IiI
   else :
    pass
 if os . path . exists ( Iii1ii1II11i ) == True :
  for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( Iii1ii1II11i ) :
   OO00Oo = 0
   OO00Oo += len ( O0o0 )
   if OO00Oo > 0 :
    o0O0O00 = xbmcgui . Dialog ( )
    if o0O0O00 . yesno ( "Borrar ficheros temporales" , str ( OO00Oo ) + " Archivos encontrados" , "Quiere borrarlos?" ) :
     for I11IiI1I11i1i in O0o0 :
      try :
       if ( I11IiI1I11i1i == "xbmc.log" or I11IiI1I11i1i == "xbmc.old.log" ) : continue
       os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
      except :
       pass
     for iI1ii1Ii in IIIIii :
      try :
       shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
      except :
       pass
       if 26 - 26: ooO00oOoo . Oooo0000
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oOOOOo0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 20 - 20: i1IIi + Oo0ooO0oo0oO - i1IIi11111i
  for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( oOOOOo0 ) :
   OO00Oo = 0
   OO00Oo += len ( O0o0 )
   if 30 - 30: II111iiii - o00ooo0 - i11iIiiIii % I1IiI - II111iiii * Oo0oO0ooo
   if OO00Oo > 0 :
    if 61 - 61: I1i1iI1i - o00 % o00ooo0
    o0O0O00 = xbmcgui . Dialog ( )
    if o0O0O00 . yesno ( "Delete ATV2 Cache Files" , str ( OO00Oo ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 84 - 84: I1i1iI1i * Ooo00oOo00o / o00 - O0
     for I11IiI1I11i1i in O0o0 :
      os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
     for iI1ii1Ii in IIIIii :
      shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
      if 30 - 30: iIii1I11I1II1 / i1IIi11111i - Oooo0000 - II111iiii % ooO00oOoo
   else :
    pass
  IIi1i11111 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 81 - 81: i11iIiiIii % I1IiI - o00ooo0
  for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( IIi1i11111 ) :
   OO00Oo = 0
   OO00Oo += len ( O0o0 )
   if 68 - 68: Oooo0000 % i1IIi . O0OOo . Oo0ooO0oo0oO
   if OO00Oo > 0 :
    if 92 - 92: ooO00oOoo . Oooo0000
    o0O0O00 = xbmcgui . Dialog ( )
    if o0O0O00 . yesno ( "Delete ATV2 Cache Files" , str ( OO00Oo ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 31 - 31: Oooo0000 . I1IiI / O0
     for I11IiI1I11i1i in O0o0 :
      os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
     for iI1ii1Ii in IIIIii :
      shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
      if 89 - 89: I1IiI
   else :
    pass
    if 68 - 68: Ooo00oOo00o * OoooooooOO % O0 + Ooo00oOo00o + i1IIi11111i
 Ii1i11IIii1I = Oooo0Ooo000 ( )
 if 4 - 4: i1IIi11111i + O0 * o00ooo0
 for OOoo0O in Ii1i11IIii1I :
  Oo0ooOo0o = xbmc . translatePath ( OOoo0O . path )
  if os . path . exists ( Oo0ooOo0o ) == True :
   for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( Oo0ooOo0o ) :
    OO00Oo = 0
    OO00Oo += len ( O0o0 )
    if OO00Oo > 0 :
     if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * II111iiii . o00ooo0 / i11iIiiIii
     o0O0O00 = xbmcgui . Dialog ( )
     if o0O0O00 . yesno ( "Manager" , str ( OO00Oo ) + "%s cache files found" % ( OOoo0O . name ) , "Do you want to delete them?" ) :
      for I11IiI1I11i1i in O0o0 :
       os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
      for iI1ii1Ii in IIIIii :
       shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
       if 2 - 2: OOOo0 / O0 / o0OO0 % I1IiI % Oo0oO0ooo
    else :
     pass
     if 52 - 52: o0OO0
     if 95 - 95: Oo0oO0ooo
 o0O0O00 = xbmcgui . Dialog ( )
 o0O0O00 . ok ( "Mantenimiento" , "Los archivos de la cache fueron borrados" )
 if 87 - 87: i1IIi11111i + I1IiI . o00ooo0 + I1IiI
 if 91 - 91: O0
def oOOo0 ( ) :
 if 54 - 54: O0 - O0OOo % o00ooo0
 if os . path . exists ( o0OOO ) == True :
  o0O0O00 = xbmcgui . Dialog ( )
  if o0O0O00 . yesno ( "Borrar imagenes" , "Esta opcion borrara las imagenes" , "Esta seguro que quiere hacer esto?" ) :
   for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( o0OOO ) :
    OO00Oo = 0
    OO00Oo += len ( O0o0 )
    if OO00Oo > 0 :
     for I11IiI1I11i1i in O0o0 :
      try :
       os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
      except :
       pass
       if 77 - 77: I1IiI / OOOo0 / Ooo00oOo00o + Ooo00oOo00o . o00ooo0
       if 38 - 38: Oooo0000
 if os . path . exists ( i1i1II ) :
  try :
   for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( i1i1II ) :
    OO00Oo = 0
    OO00Oo += len ( O0o0 )
    if 7 - 7: O0 . ooO00oOoo % Oo0ooO0oo0oO - OOOo0 - iIii1I11I1II1
    if OO00Oo > 0 :
     for I11IiI1I11i1i in O0o0 : os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
     for iI1ii1Ii in IIIIii : shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
  except :
   pass
   if 36 - 36: O0OOo % i1IIi11111i % Oo - Oo0ooO0oo0oO
 try :
  Ii1I = os . path . join ( iI1Ii11111iIi , "Textures13.db" )
  os . unlink ( Ii1I )
 except :
  pass
 o0O0O00 . ok ( "Reiniciar Kodi" , "Por favor, reinicie kodi para reconstruir la libreria de imagenes." )
 if 77 - 77: ooO00oOoo % ooO00oOoo * I1i1iI1i - i11iIiiIii
def Oo0oO ( ) :
 if 1 - 1: Ooo00oOo00o - I1i1iI1i . o00 . Ooo00oOo00o / Oo + o00
 Ooo = xbmc . translatePath ( 'special://home/addons/packages' )
 o0O0O00 = xbmcgui . Dialog ( )
 for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( Ooo ) :
  OO00Oo = 0
  OO00Oo += len ( O0o0 )
 if o0O0O00 . yesno ( "Borrar paquetes de archivos" , "%d paquetes encontrados." % OO00Oo , "Borrar?" ) :
  for Oo0O0O0ooO0O , IIIIii , O0o0 in os . walk ( Ooo ) :
   OO00Oo = 0
   OO00Oo += len ( O0o0 )
   if OO00Oo > 0 :
    for I11IiI1I11i1i in O0o0 :
     os . unlink ( os . path . join ( Oo0O0O0ooO0O , I11IiI1I11i1i ) )
    for iI1ii1Ii in IIIIii :
     shutil . rmtree ( os . path . join ( Oo0O0O0ooO0O , iI1ii1Ii ) )
    o0O0O00 = xbmcgui . Dialog ( )
    o0O0O00 . ok ( "Maintenance" , "Deleting Packages all done" )
   else :
    o0O0O00 = xbmcgui . Dialog ( )
    o0O0O00 . ok ( "Maintenance" , "No Packages to Purge" )
    if 62 - 62: o00ooo0 / Ooo00oOo00o + Oo0oO0ooo / Ooo00oOo00o . II111iiii
    if 68 - 68: i11iIiiIii % Oo0ooO0oo0oO + i11iIiiIii
    if 31 - 31: II111iiii . OOOo0
    if 1 - 1: Oo / o0OO0 % ooO00oOoo * O0OOo . i11iIiiIii
    if 2 - 2: Oo0ooO0oo0oO * o00 - iIii1I11I1II1 + OOOo0 . I1i1iI1i % ooO00oOoo
    if 92 - 92: ooO00oOoo
o0 = o0OOOOO00o0O0 ( )
IIiIiiIi = None
O000oo = None
IIi1I11I1II = None
if 63 - 63: OoooooooOO - Ooo00oOo00o . II111iiii / o0OO0 . I1IiI / O0
try :
 IIiIiiIi = urllib . unquote_plus ( o0 [ "url" ] )
except :
 pass
try :
 O000oo = urllib . unquote_plus ( o0 [ "name" ] )
except :
 pass
try :
 IIi1I11I1II = int ( o0 [ "mode" ] )
except :
 pass
 if 84 - 84: O0OOo
if IIi1I11I1II == None or IIiIiiIi == None or len ( IIiIiiIi ) < 1 :
 iIiiI1 ( )
 if 86 - 86: I1IiI - Oo0oO0ooo - Ooo00oOo00o * ooO00oOoo
elif IIi1I11I1II == 1 :
 o0O ( )
 if 66 - 66: OoooooooOO + O0
elif IIi1I11I1II == 2 :
 oOOo0 ( )
 if 11 - 11: o00 + OoooooooOO - Ooo00oOo00o / o0OO0 + Oo . II111iiii
elif IIi1I11I1II == 3 :
 Oo0oO ( )
 if 41 - 41: Oo0oO0ooo - O0 - O0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
if 68 - 68: o00ooo0 % Oooo0000
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
