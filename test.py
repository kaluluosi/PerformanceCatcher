import asyncio
import time
from ios_device.remote.remote_lockdown import RemoteLockdownClient
from ios_device.servers.Instrument import InstrumentServer
from demo.instrument_demo.sysmontap import  sysmontap
from demo.instrument_demo.graphics import cmd_graphics
from pymobiledevice3.remote.common import ConnectionType
from pymobiledevice3.remote.tunnel_service import (
    get_core_device_tunnel_services, 
    get_remote_pairing_tunnel_services, 
    start_tunnel
    )


async def main():
    service = await get_core_device_tunnel_services()
    async with start_tunnel(service[0]):
        await asyncio.sleep(2)

asyncio.run(main())

# host = "fd6c:b46b:5cd6::1"
# port = 49645
# # python -m pymobiledevice3 lockdown start-tunnel
# with RemoteLockdownClient((host, port)) as rsd:
#     rpc = InstrumentServer(rsd).init()
#     cmd_graphics(rpc)
#     rpc.stop()

