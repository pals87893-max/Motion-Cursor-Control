import asyncio
import pyautogui
import websockets
import socket
import json

HOST="0.0.0.0"
PORT=8080

pyautogui.FAILSAFE=True
pyautogui.PAUSE=0

SENSITIVITY=0.2
DEADLOCK=5.0

screen_w,screen_h=pyautogui.size()

INVERT_X= True
INVERT_Y= False
SWAP_AXES=False

def get_local_ip():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8",80))
        ip=s.getsockname()[0]
    except Exception:
        ip="127.0.0.1"
    finally:
        s.close()
    print(f"your PC's local IP is:{ip}")

def compute_deltas(rb,rg):
    if SWAP_AXES:
        raw_x,raw_y=rb,rg
    else:
        raw_x,raw_y=rg,rb

    if INVERT_X:
        raw_x=-raw_x

    else:
        raw_y=-raw_y

    return raw_x,raw_y


def move_cursor(dx,dy):
    x,y=pyautogui.position()
    new_x=min(max(x+dx,0),screen_w-1)
    new_y=min(max(y+dy,0),screen_h-1)
    pyautogui.moveTo(new_x,new_y,duration=0)

async def handle_client(websocket):
    print("Phone Successfully Connected:",websocket.remote_address[0])
    try:
        async for message in websocket:
            data=json.loads(message)
            if data.get("type")=="click":
                button =data.get("button")
                if button=="left":
                    pyautogui.click()
                elif button=="right":
                    pyautogui.click(button="right")
                continue
            rb=data["rb"]
            rg=data["rg"]

            if abs(rg)<DEADLOCK:
                rg=0
            if abs(rb)<DEADLOCK:
                rb=0
            
            raw_x,raw_y=compute_deltas(rb,rg)
            dx=raw_x*SENSITIVITY
            dy=raw_y*SENSITIVITY
            move_cursor(dx,dy)
        
    except websockets.exceptions.ConnectionClosed:
        print("Phone Disconnected!")

async def main():
    async with websockets.serve(handle_client,HOST,PORT):
        get_local_ip()
        await asyncio.Future()

asyncio.run(main())


