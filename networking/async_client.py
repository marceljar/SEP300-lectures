import asyncio

HOST = "127.0.0.1"   # Server's hostname or IP
PORT = 65435         # Same port as the server

async def tcp_client():
    reader, writer = await asyncio\
            .open_connection(HOST, PORT)
    print("Connected to server")

    async def send_messages():
        while True:
            msg = await asyncio.get_event_loop() \
                    .run_in_executor(None, input, "Client> ")
            writer.write(msg.encode())
            await writer.drain()

    async def receive_messages():
        while True:
            data = await reader.read(1024)
            if not data:
                print("Server disconnected")
                break
            print(f"\nServer: {data.decode()}\nClient> ", \
                                                     end="")

    await asyncio.gather(send_messages(), receive_messages())

asyncio.run(tcp_client())
