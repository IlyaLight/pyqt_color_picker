import numpy as np
from PyQt5.QtGui import QPixmap, QMouseEvent, QColor, QLinearGradient, QBrush, QPalette

from window.window import Ui_MainWindow


class ColorController:

    def __init__(self, win: Ui_MainWindow):
        self.win = win
        self.color = QColor()
        pixmap = QPixmap('window\\resources\\multicolored-circle.png')
        self.pixmap = pixmap.scaledToHeight(win.l_color_role.height())
        win.l_color_role.setPixmap(self.pixmap)
        win.l_color_role.mousePressEvent = self._get_pixel
        win.sl_saturation.valueChanged.connect(self._slider_change_event)
        win.sl_value.valueChanged.connect(self._slider_change_event)
        self._slider_change_event()
        self.set_gradient_in_saturation_slider()


    def _get_pixel(self, event: QMouseEvent):
        x = event.pos().x()
        y = event.pos().y()
        c = self.pixmap.toImage().pixel(x,y)  # color code (integer): 3235912
        self.color.setRgba(c)  # color object
        self.set_gradient_in_saturation_slider()
        self._slider_change_event(event)

    def set_gradient_in_saturation_slider(self):
        self.win.sl_saturation.setStyleSheet(f'''QSlider::groove:horizontal {{
                                                    background:qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                                    stop:0 #fff, stop:1 rgb{self.color.getRgb()},);
                                                    height: 10px;
                                                }}
                                                QSlider::handle::horizontal
                                                {{
                                                    background: #333;
                                                    width:8px;
                                                    margin: -6px 0;
                                                }}
                                                ''')

    def _slider_change_event(self, event=None):
        self.color.setHsv(self.color.getHsv()[0], self.win.sl_saturation.value(), self.win.sl_value.value())
        self.win.l_current_color.setText(self.color.name().upper())
        text_color = QColor()
        if np.sum(self.color.getRgb()) > 470:
            text_color.setNamedColor('#000')
        else:
            text_color.setNamedColor('#fff')
        self.win.l_current_color.setStyleSheet(
            f'background-color:rgb{self.color.getRgb()}; color : rgb{text_color.getRgb()};')
