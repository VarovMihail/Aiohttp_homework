import os

DSN = os.getenv("DSN","postgresql+asyncpg://app:1234@localhost:5430/aiohttp_homework")
DSN_SYNC = os.getenv("DSN_SYNC", "postgresql://app:1234@localhost:5430/aiohttp_homework")


print(f"{DSN = }")
print(f"{DSN_SYNC = }")



