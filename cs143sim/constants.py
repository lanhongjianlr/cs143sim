"""This file contains all constant definitions

.. moduleauthor:: Lan Hongjian <lanhongjianlr@gmail.com>
.. moduleauthor:: Yamei Ou <oym111@gmail.com>
.. moduleauthor:: Samuel Richerd <dondiego152@gmail.com>
.. moduleauthor:: Jan Van Bruggen <jancvanbruggen@gmail.com>
.. moduleauthor:: Junlin Zhang <neicullyn@gmail.com>
"""

DEBUG = False
"""Whether to run the simulation in debug mode, with extra print statements"""

PACKET_SIZE = 8192
"""Size of every :class:`.Packet` in the simulation, in bits"""

ACK_PACKET_SIZE = 512
"""Size of every :class:`.Packet` in the simulation, in bits"""

GENERATE_ROUTERPACKET_TIME_INTEVAL = 20
"""Time for every :class:`.Router` to wait before generating a new
:class:`.RouterPacket`, in milliseconds"""

INPUT_FILE_RATE_SCALE_FACTOR = 1000000/1000.0
""" Conversion factor for Mbps to bits per millisecond (for rate)"""

INPUT_FILE_DATA_SCALE_FACTOR = 8000000
"""Conversion factor for MBytes to bits (for flow total data size)"""

INPUT_FILE_TIME_SCALE_FACTOR = 1000
"""Conversion factor for seconds to milliseconds (for flow start time)"""

INPUT_FILE_BUFFER_SCALE_FACTOR = 8000
"""Conversion factor for KB to bits (for buffer size)"""