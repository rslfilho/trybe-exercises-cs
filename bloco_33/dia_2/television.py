class Television:
    def __int__(self, size):
        self._volume = 50
        self._channel = 1
        self._size = size
        self._power_on = False

    def volume_up(self):
        if self._volume < 99:
            self._volume += 1

    def volume_down(self):
        if self._volume > 0:
            self._volume -= 1

    def change_channel(self, channel):
        if not 1 <= channel <= 99:
            raise ValueError('Invalid channel')

        self._channel = channel

    def toggle_power(self):
        self._power_on = not self._power_on
