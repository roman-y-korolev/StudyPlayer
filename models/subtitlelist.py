import datetime


class Subtitle:

    def __init__(self, time_start, time_end, text, next_subtitle=None, previous_subtitle=None):
        """
        Subtitle constructor
        :param time_start: start time
        :param time_end: end time
        :param text: text of subtitle
        :param next_subtitle: next subtitle
        :param previous_subtitle: previous one
        """
        self.time_start = datetime.datetime.strptime(time_start, '%H:%M:%S,%f').time()
        self.time_end = datetime.datetime.strptime(time_end, '%H:%M:%S,%f').time()
        self.text = text
        self.next = next_subtitle
        self.previous = previous_subtitle

    def set_next(self, next_subtitle):
        self.next = next_subtitle

    def set_previous(self, previous_subtitle):
        self.previous = previous_subtitle


class SubtitleList:
    def __init__(self, path):
        """
        SubtitleList constructor
        :param path: path to subtitle file
        TODO make support of different subtitle formats
        """
        self.root = None
        with open(path, 'r') as f:
            text = f.read()
            splited_text = text.split('\n\n')
            last = None
            for phrase in splited_text:
                if phrase != '':
                    splited_phrase = phrase.split('\n')
                    time_start, time_end = tuple(splited_phrase[1].split(' --> '))
                    subtitle_text = '\n'.join(splited_phrase[2:])
                    subtitle = Subtitle(time_start=time_start, time_end=time_end, text=subtitle_text)
                    if self.root is None:
                        self.root = subtitle
                    else:
                        last.set_next(subtitle)
                        subtitle.set_previous(last)

                    last = subtitle

    def get_subtitle(self, player_time):
        """
        Get subtitle for given time
        :param player_time:
        :return:
        """
        is_found = False
        current_subtitle = self.root
        while not is_found:
            if current_subtitle.time_end <= player_time and current_subtitle.next is not None:
                current_subtitle = current_subtitle.next
            else:
                is_found = True
        return current_subtitle

