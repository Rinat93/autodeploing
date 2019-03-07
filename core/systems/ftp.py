import asyncssh
# Загрузка файлов на сервер
async def ftp_upload(src,to,server,writeInto=False):
    async with asyncssh.connect(host=server['host'], username=server['user'], password=server['password'], known_hosts=None) as conn:
        async with conn.start_sftp_client() as sftp:
            await sftp.put(src,remotepath=to,recurse=True)