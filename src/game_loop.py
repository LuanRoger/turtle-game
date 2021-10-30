from threading import Thread, Event
class GameLoop():
    loop_thread: Thread
    thread_event: Event

    def __init__(self, loop_function, thread_name: str = "GameLoop0"):
        self.loop_thread = Thread(target=loop_function, daemon=True)
        self.thread_event = Event()

        self.loop_thread.name = thread_name

    def start(self):
        self.loop_thread.start()
        self.thread_event.set()

    def stop(self):
        self.thread_event.clear()
    
    def wait(self):
        self.thread_event.wait()

    def continue_thread(self):
        self.thread_event.set()