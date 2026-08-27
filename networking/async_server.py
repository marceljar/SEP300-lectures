import asyncio

HOST = "127.0.0.1"   # Server's hostname or IP
PORT = 65435         # Same port as the server

async def handle_client(reader, writer):
    print(f"New client connected")

    async def send_messages():
        while True:
            msg = await asyncio.get_event_loop()\
                     .run_in_executor(None, input, "Server> ")
            writer.write(msg.encode())
            await writer.drain()

    async def receive_messages():
        while True:
            data = await reader.read(1024)
            if not data:
                print(f"Client disconnected")
                break
            print(f"\nClient: {data.decode()}\nServer> ",\
                                                   end="")

    await asyncio.gather(send_messages(), receive_messages())

async def main():
    server = await asyncio.start_server(handle_client, \
                                        HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"Server running on {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())
