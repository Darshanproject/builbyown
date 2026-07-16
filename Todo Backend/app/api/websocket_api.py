# from fastapi import APIRouter
# from fastapi import WebSocket
# from fastapi import WebSocketDisconnect

# from app.websocket.connection_manager import manager

# router = APIRouter(
#     tags=["WebSocket"]
# )
# @router.websocket("/ws/{user_id}")
# async def websocket_endpoint(
#         websocket: WebSocket,
#         user_id: str
# ):

#     await manager.connect(
#         user_id,
#         websocket
#     )

#     try:
#         while True:
#             await websocket.receive_text()

#     except WebSocketDisconnect:
#         manager.disconnect(user_id)

from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.connection_manager import manager

router = APIRouter(tags=["WebSocket"])
print("WebSocket Router Loaded")


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: str
):
    print("Client Connected:", user_id)

    await manager.connect(user_id, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print("Received:", data)

    except WebSocketDisconnect:
        print("Disconnected")
        manager.disconnect(user_id)