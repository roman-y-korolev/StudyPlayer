import datetime
import functools
import os
import time

import vlc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QEvent
from PyQt5.QtWidgets import QFileDialog, QAction
from py_translator import Translator

import config
from models.subtitlelist import SubtitleList
from templates.player import Ui_MainWindow as PlayerWindow


class PlayerApplication(QtWidgets.QMainWindow, PlayerWindow):
    def __init__(self):
        """
        Player initialisation
        """
        super().__init__()
        self.setupUi(self)

        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()

        self.play_slider.setMaximum(1000)
        self.play_slider.sliderMoved.connect(self.set_position)

        self.sound_slider.setMaximum(200)
        self.sound_slider.valueChanged.connect(self.set_volume)

        self.actionOpen.triggered.connect(self.open_file)

        self.play_button.clicked.connect(self.play_pause)

        self.media = None

        self.timer = QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_ui)

        self.is_play = False

        self.subtitles = None

        self.translator = Translator()

        QtWidgets.qApp.installEventFilter(self)

    def eventFilter(self, source, event):
        """
        Overwrite eventFilter to catch key events
        :param source: Widget
        :param event: Event
        :return: None
        """
        if event.type() == QEvent.KeyPress and type(source) == QtGui.QWindow:
            if event.key() == 16777236:  # right arrow
                self.move_forward()
            if event.key() == 16777234:  # left arrow
                self.move_backward()
            if event.key() == 32:  # space
                self.play_pause()
        return super(PlayerApplication, self).eventFilter(source, event)

    def move_forward(self):
        player_time = self.media_player.get_time()
        if player_time != -1:
            self.media_player.set_time(player_time + config.FORWARD_TIME)

    def move_backward(self):
        player_time = self.media_player.get_time()
        if player_time != -1:
            new_time = player_time - config.FORWARD_TIME
            new_time = new_time if new_time > 0 else 0
            self.media_player.set_time(new_time)

    def open_file(self, filename=None):
        """
        Open video file and prepare to show the video
        :param filename:
        :return:
        """
        if filename is None or filename is False:
            filename = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser('~'))[0]
        if not filename:
            return

        self.media = self.instance.media_new(filename)
        self.media_player.set_media(self.media)
        self.media.parse()

        self.set_audio_options()

        self.media_player.set_xwindow(self.video_frame.winId())

        subtitle_path = '.'.join(filename.split('.')[:-1] + ['srt'])
        self.media_player.video_set_subtitle_file(subtitle_path)
        self.subtitles = SubtitleList(path=subtitle_path)

        # initialize vls
        self.media_player.play()
        while self.media_player.audio_get_track() == -1:
            time.sleep(0.1)
        self.media_player.pause()

        self.sound_slider.setValue(self.media_player.audio_get_volume())
        self.timer.start()
        self.is_play = True

    def set_position(self, position):
        """
        Set player position.
        :param position:
        :return:
        """
        self.media_player.set_position(position / 1000.0)

    def set_volume(self, volume):
        """
        Set audio volume
        :param volume:
        :return:
        """
        self.media_player.audio_set_volume(volume)

    def set_audio_options(self):
        """
        Fill audio menu. After that you can choose audiotrack.
        :return:
        """
        self.menu_Audio.clear()

        for track in self.media.tracks_get():
            if track.type == vlc.TrackType.audio:
                track_menu = QAction(track.description.decode("utf-8"), self)
                track_menu.triggered.connect(functools.partial(self.media_player.audio_set_track, track.id))
                self.menu_Audio.addAction(track_menu)

    def play_pause(self):
        """
        Play and Pause player
        :return:
        """
        if self.media_player.is_playing():
            self.media_player.pause()
            self.is_play = False

            player_time_ms = self.media_player.get_time()
            player_time_ms = player_time_ms if player_time_ms > 0 else 0
            ms = player_time_ms % 1000 * 1000
            seconds = (player_time_ms // 1000) % 60
            minutes = ((player_time_ms // 1000) // 60) % 60
            hours = (((player_time_ms // 1000) // 60) // 60) % 24
            player_time = datetime.datetime(year=2018, month=1, day=1, hour=hours, minute=minutes, second=seconds,
                                            microsecond=ms).time()

            subtitle = self.subtitles.get_subtitle(player_time)

            try:
                # full phrase translation
                translated_subtitle_text_1 = self.translator.translate(subtitle.text, dest=config.OUTPUT_LANGUAGE).text

                # word by word translation
                to_translate_list = subtitle.text.replace('\n', ' ').split()
                to_translate_str = '\n'.join(to_translate_list)
                translated_subtitle_text_2 = self.translator.translate(to_translate_str, dest=config.OUTPUT_LANGUAGE).text
                translated_subtitle_text_2 = translated_subtitle_text_2.replace('\n', ' ')

                self.subtitle_label_1.setText(translated_subtitle_text_1)
                self.subtitle_label_2.setText(translated_subtitle_text_2)
            except:
                pass
        else:
            self.subtitle_label_1.setText("")
            self.subtitle_label_2.setText("")
            if self.media_player.play() == -1:
                self.open_file()
                return
            self.media_player.play()
            self.timer.start()
            self.is_play = True

    def update_ui(self):
        self.play_slider.setValue(self.media_player.get_position() * 1000)

        if not self.media_player.is_playing():
            self.timer.stop()
            if self.is_play:
                self.stop()

    def stop(self):
        self.media_player.stop()
        self.is_play = False
