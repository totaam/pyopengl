'''OpenGL extension AMD.performance_monitor

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.performance_monitor to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables the capture and reporting of performance monitors.
	Performance monitors contain groups of counters which hold arbitrary counted 
	data.  Typically, the counters hold information on performance-related
	counters in the underlying hardware.  The extension is general enough to
	allow the implementation to choose which counters to expose and pick the
	data type and range of the counters.  The extension also allows counting to 
	start and end on arbitrary boundaries during rendering.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/performance_monitor.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.performance_monitor import *
### END AUTOGENERATED SECTION