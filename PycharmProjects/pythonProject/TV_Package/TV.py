class Television:
    channel: 0
    volume_level: 0
    is_on: False

    def __init__(self) -> None:
        super().__init__()

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_channel(self) -> int:
            return self.channel

    # @self.setter
    def set_channel(self, new_channel):
        if 0 < new_channel < 100:
            self.channel = new_channel

    def get_volume(self) -> int:
        return self.volume_level

    # @self.setter
    def set_volume(self, volume):
        if 0 < volume < 50:
            self.volume_level = volume

    def channel_up(self):
        if self.channel < 100:
            self.channel += 1

    def channel_down(self):
        if self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.volume_level < 50:
            self.volume_level += 1

    def volume_down(self):
        if self.volume_level > 1:
            self.volume_level -= 1
