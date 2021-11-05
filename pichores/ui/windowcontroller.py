import asyncio

class WindowController():
    def __init__(self, loop, oled):
        self.loop = loop
        self.oled = oled
        self.windows = {}
        self.activewindow = []

        self.loop.create_task(self.render())
        print("Render task created")

    def add_window(self, windowid, window):
        self.windows[windowid] = window
        print(f"Added {windowid} window")
    
    def set_window(self, windowid):
        if windowid in self.windows:
            try:
                self.activewindow.deactivate()
            except (NotImplementedError, AttributeError):
                pass
            
            self.activewindow = self.windows[windowid]
            try:
                self.activewindow.activate()
            except (NotImplementedError, AttributeError):
                pass
            print(f"Activated {windowid} window")
        else:
            print(f"Window {windowid} not found")

    async def render(self):
        while self.loop.is_running():
            try:
                self.activewindow.render()
            except (NotImplementedError, AttributeError):
                pass
        await asyncio.sleep(0.25)