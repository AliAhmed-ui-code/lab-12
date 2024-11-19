from itertools import filterfalse


class Television:
    MIN_VOLUME:int = 0
    MAX_VOLUME:int = 2
    MIN_CHANNEL:int = 0
    MAX_CHANNEL:int = 3
    def __init__(self):
        self.__muted:bool = False
        self.__status:bool = False
        self.__volume:int = Television.MIN_VOLUME
        self.__channel:int = Television.MIN_CHANNEL
    def power(self):
        """
        Decides if the TV is on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self):
        """
        Decides if the TV is muted or not
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
    def channel_up(self):
        """
        the TV's channel goes up
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self):
        """
        The TV's channel goes down
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -=1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self):
        """
        Raises the TV's volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME
    def volume_down(self):
        """
      Lowers the TV's volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME
    def __str__(self):
        """
        :return:  The power, the channel and the volume
        """
        if self.__muted:
            return f' Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'