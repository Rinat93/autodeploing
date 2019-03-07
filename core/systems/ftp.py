import aioftp
# Загрузка файлов на сервер
async def ftp_upload(src,to,server,writeInto=False):
    print(server)
    async with aioftp.ClientSession(server['host'],21, server['user'], server['password']) as client:
        print(client)
        await client.upload(src,to,write_into=writeInto)