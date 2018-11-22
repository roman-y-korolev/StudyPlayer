import sys

from PyQt5.QtWidgets import QApplication

from controllers.player import PlayerApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = PlayerApplication()
    player.show()
    if sys.argv[1:]:
        player.open_file(sys.argv[1])
    sys.exit(app.exec_())
