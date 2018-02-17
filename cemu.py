import ctypes
import subprocess
import re
import ConfigParser

if starting:
	# CONFIGURATION
	config_dir = 'E:\\rampage\\Documents\\Google Drive\\profiles\\freepie\\cemu\\'
	
	# variables
	bindings = {}
	settings = {}
	vJoyMax = vJoy[0].axisMax
	vJoyMin = -vJoyMax
	enabled = False

# hotkey
toggle = keyboard.getPressed(Key.F1)
if toggle:
	enabled = not enabled
	if enabled:
		readConfig(config_dir, bindings, settings)

# update vJoy
if enabled:
	vJoy[0].setButton(0, bindings['a']()) #A - Use/ok
	vJoy[0].setButton(1, bindings['b']()) #B - Run/drop/cancel/Holster weapons
	vJoy[0].setButton(2, bindings['x']()) #X - Jump
	vJoy[0].setButton(3, bindings['y']()) #Y - Attack
	vJoy[0].setButton(4, bindings['l']()) #L - Rune
	vJoy[0].setButton(5, bindings['r']()) #R - Throw
	vJoy[0].setButton(6, bindings['zl']()) #ZL - Lock/Block
	vJoy[0].setButton(7, bindings['zr']()) #ZR - Aim bow
	vJoy[0].setButton(8, bindings['+']()) #+ - Menu
	vJoy[0].setButton(9, bindings['-']()) #- - Map
	vJoy[0].setButton(10, bindings['lp']()) #press left joy - crouch
	vJoy[0].setButton(11, bindings['rp']()) #press right joy - binocular
	vJoy[0].setButton(12, bindings['du']()) #dpad-u - switch rune
	vJoy[0].setButton(13, bindings['dd']()) #dpad-d - call horse
	vJoy[0].setButton(14, bindings['dl']()) #dpad-l - switch shield
	vJoy[0].setButton(15, bindings['dr']()) #dpad-r - switch weapon	
	vJoy[0].rx = bindings['lx']()
	vJoy[0].ry = bindings['ly']()
	vJoy[0].x = bindings['rx']()
	vJoy[0].y = bindings['ry']()

	if settings['trap_mouse']:
		ctypes.windll.user32.SetCursorPos(settings['mouse_x'], settings['mouse_y'])
		
# binding helpers	
def keys2Axis(keyMax, keyMin):
	global vJoyMin
	global vJoyMax
	if keyMax:
		return vJoyMax
	if keyMin:
		return vJoyMin
	return 0
	
def delta2Axis(value, sensitivity):
	global vJoyMin
	global vJoyMax
	return value / sensitivity * vJoyMax
	
# config parsing
def getTitleId():
	output = subprocess.check_output(['tasklist', '/V', '/FO', 'CSV', '/FI', 'IMAGENAME eq cemu.exe', '/NH'], shell=True)
	try:
		titleId = re.search('\[TitleId\: ([0-9a-z]{,8}-[0-9a-z]{,8})\]', output).group(1)
	except AttributeError:
		titleId = 'default'
	return titleId
		
def readConfig(config_dir, bindings, settings):
	config_file = config_dir + getTitleId() + '.ini';
	section = 'controller'
	config = ConfigParser.ConfigParser()
	config.read(config_file)
	options = config.options(section)
	for option in options:
		try:
			bindings[option] = eval('lambda: ' + config.get(section, option))
		except:
			diagnostics.debug("error binding %s!" % option)
			bindings[option] = None
			
	section = 'settings'
	settings['trap_mouse'] = config.getboolean(section, 'trap_mouse')
	settings['mouse_x'] = config.getint(section, 'mouse_x')
	settings['mouse_y'] = config.getint(section, 'mouse_y')