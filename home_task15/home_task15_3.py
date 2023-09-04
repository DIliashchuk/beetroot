CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_channel_index = N - 1
            return self.channels[self.current_channel_index]

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, N):
        if isinstance(N, int) and 1 <= N <= len(self.channels):
            return "Yes"
        elif isinstance(N, str) and N in self.channels:
            return "Yes"
        else:
            return "No"


controller = TVController(CHANNELS)


print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist(4) == "No")
print(controller.is_exist("BBC") == "Yes")
