# Coded By can-codev

import sys
import random
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyaudio
import threading
from datetime import datetime


class GitarAkorAsistani(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setWindowTitle("Gitar Akor Asistanı")
        self.setGeometry(100, 100, 1180, 840)
        self.setMinimumSize(1080, 780)
        self.setFocusPolicy(Qt.StrongFocus)
        self.drag_pos = None
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0e27;
                border: 1px solid #1e3a8a;
            }
            QWidget {
                background-color: #0a0e27;
                color: #e0e0ff;
                font-family: 'Segoe UI';
            }
            QPushButton {
                background-color: #1a1f2e;
                border: 1px solid #3b82f6;
                padding: 9px 16px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 12px;
                color: #e0e0ff;
            }
            QPushButton:hover {
                background-color: #232a3d;
                border: 1px solid #60a5fa;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #111827;
                border: 1px solid #93c5fd;
            }
            QPushButton:disabled {
                background-color: #161b28;
                color: #64748b;
                border: 1px solid #334155;
            }
            QComboBox {
                background-color: #0f172a;
                border: 1px solid #1e3a8a;
                padding: 6px;
                padding-right: 20px;
                border-radius: 4px;
                color: #e0e0ff;
                selection-background-color: #1e3a8a;
                selection-color: #ffffff;
            }
            QComboBox:hover {
                border: 1px solid #3b82f6;
            }
            QComboBox:focus {
                border: 1px solid #60a5fa;
            }
            QComboBox::drop-down {
                border: none;
                background: transparent;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 6px solid #3b82f6;
                margin-right: 6px;
            }
            QComboBox QAbstractItemView {
                background-color: #0f172a;
                color: #e0e0ff;
                border: 1px solid #1e3a8a;
                selection-background-color: #2563eb;
                selection-color: #ffffff;
                outline: 0;
                padding: 4px;
            }
            QComboBox QAbstractItemView::item {
                background-color: #0f172a;
                color: #e0e0ff;
                min-height: 28px;
                padding: 6px 10px;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #2563eb;
                color: #ffffff;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #1e40af;
                color: #ffffff;
            }
            QGroupBox {
                border: 1px solid #1e3a8a;
                border-radius: 8px;
                margin-top: 10px;
                font-weight: bold;
                color: #60a5fa;
                background-color: #0b112f;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px 0 6px;
            }
            QProgressBar {
                border: 1px solid #1e3a8a;
                border-radius: 5px;
                text-align: center;
                color: white;
                background-color: #0f172a;
            }
            QProgressBar::chunk {
                background-color: #3b82f6;
                border-radius: 5px;
            }
            QLabel {
                color: #e0e0ff;
            }
            QLineEdit {
                background-color: #0f172a;
                border: 1px solid #1e3a8a;
                border-radius: 4px;
                padding: 6px;
                color: #e0e0ff;
            }
            QLineEdit:focus {
                border: 1px solid #3b82f6;
            }
            QListWidget {
                background-color: #0f172a;
                border: 1px solid #1e3a8a;
                border-radius: 6px;
                padding: 5px;
                color: #e0e0ff;
            }
            QListWidget::item {
                padding: 6px;
                border-radius: 3px;
            }
            QListWidget::item:selected {
                background-color: #1e3a8a;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #1e40af;
            }
            QTabWidget::pane {
                border: 1px solid #1e3a8a;
                background-color: #0a0e27;
                border-radius: 8px;
                margin-top: 4px;
            }
            QTabBar::tab {
                background-color: #0f172a;
                color: #94a3b8;
                padding: 10px 22px;
                margin-right: 4px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                border: 1px solid #1e3a8a;
            }
            QTabBar::tab:selected {
                background-color: #1e3a8a;
                color: white;
            }
            QTabBar::tab:hover {
                background-color: #1e40af;
                color: white;
            }
            QSpinBox {
                background-color: #0f172a;
                border: 1px solid #1e3a8a;
                border-radius: 4px;
                padding: 4px;
                color: #e0e0ff;
            }
            QSpinBox:focus {
                border: 1px solid #3b82f6;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #1e293b;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #3b82f6;
                border: 1px solid #60a5fa;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QCheckBox {
                spacing: 8px;
                color: #e0e0ff;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox::indicator:unchecked {
                border: 1px solid #3b82f6;
                background: #0f172a;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                border: 1px solid #3b82f6;
                background: #2563eb;
                border-radius: 4px;
            }
            QStatusBar {
                background-color: #0f172a;
                color: #60a5fa;
                border-top: 1px solid #1e3a8a;
            }
        """)

        self.akorlar = {
            "A": ["x", "0", "2", "2", "2", "0"],
            "A#": ["x", "1", "3", "3", "3", "1"],
            "B": ["x", "2", "4", "4", "4", "2"],
            "C": ["x", "3", "2", "0", "1", "0"],
            "C#": ["x", "4", "3", "1", "2", "1"],
            "D": ["x", "x", "0", "2", "3", "2"],
            "D#": ["x", "x", "1", "3", "4", "3"],
            "E": ["0", "2", "2", "1", "0", "0"],
            "F": ["1", "3", "3", "2", "1", "1"],
            "F#": ["2", "4", "4", "3", "2", "2"],
            "G": ["3", "2", "0", "0", "0", "3"],
            "G#": ["4", "3", "1", "1", "1", "4"],

            "Am": ["x", "0", "2", "2", "1", "0"],
            "A#m": ["x", "1", "3", "3", "2", "1"],
            "Bm": ["x", "2", "4", "4", "3", "2"],
            "Cm": ["x", "3", "5", "5", "4", "3"],
            "C#m": ["x", "4", "6", "6", "5", "4"],
            "Dm": ["x", "x", "0", "2", "3", "1"],
            "D#m": ["x", "x", "1", "3", "4", "2"],
            "Em": ["0", "2", "2", "0", "0", "0"],
            "Fm": ["1", "3", "3", "1", "1", "1"],
            "F#m": ["2", "4", "4", "2", "2", "2"],
            "Gm": ["3", "5", "5", "3", "3", "3"],
            "G#m": ["4", "6", "6", "4", "4", "4"],

            "A7": ["x", "0", "2", "0", "2", "0"],
            "B7": ["x", "2", "1", "2", "0", "2"],
            "C7": ["x", "3", "2", "3", "1", "0"],
            "D7": ["x", "x", "0", "2", "1", "2"],
            "E7": ["0", "2", "0", "1", "0", "0"],
            "F7": ["1", "3", "1", "2", "1", "1"],
            "G7": ["3", "2", "0", "0", "0", "1"],

            "Amaj7": ["x", "0", "2", "1", "2", "0"],
            "Cmaj7": ["x", "3", "2", "0", "0", "0"],
            "Dmaj7": ["x", "x", "0", "2", "2", "2"],
            "Emaj7": ["0", "2", "2", "1", "0", "0"],
            "Fmaj7": ["x", "3", "2", "1", "1", "0"],
            "Gmaj7": ["3", "2", "0", "0", "0", "2"],
        }

        self.parmak_pozisyonlari = {
            "A":      ["x", "0", "1", "2", "3", "0"],
            "A#":     ["x", "1", "3", "4", "2", "1"],
            "B":      ["x", "1", "3", "4", "2", "1"],
            "C":      ["x", "3", "2", "0", "1", "0"],
            "C#":     ["x", "4", "3", "1", "2", "1"],
            "D":      ["x", "x", "0", "1", "3", "2"],
            "D#":     ["x", "x", "1", "2", "4", "3"],
            "E":      ["0", "2", "3", "1", "0", "0"],
            "F":      ["1", "3", "4", "2", "1", "1"],
            "F#":     ["1", "3", "4", "2", "1", "1"],
            "G":      ["2", "1", "0", "0", "0", "3"],
            "G#":     ["4", "3", "1", "1", "1", "4"],

            "Am":     ["x", "0", "2", "3", "1", "0"],
            "A#m":    ["x", "1", "3", "4", "2", "1"],
            "Bm":     ["x", "1", "3", "4", "2", "1"],
            "Cm":     ["x", "1", "3", "4", "2", "1"],
            "C#m":    ["x", "1", "3", "4", "2", "1"],
            "Dm":     ["x", "x", "0", "2", "3", "1"],
            "D#m":    ["x", "x", "1", "3", "4", "2"],
            "Em":     ["0", "2", "3", "0", "0", "0"],
            "Fm":     ["1", "3", "4", "1", "1", "1"],
            "F#m":    ["1", "3", "4", "1", "1", "1"],
            "Gm":     ["1", "3", "4", "1", "1", "1"],
            "G#m":    ["1", "3", "4", "1", "1", "1"],

            "A7":     ["x", "0", "2", "0", "1", "0"],
            "B7":     ["x", "2", "1", "3", "0", "4"],
            "C7":     ["x", "3", "2", "4", "1", "0"],
            "D7":     ["x", "x", "0", "2", "1", "3"],
            "E7":     ["0", "2", "0", "1", "0", "0"],
            "F7":     ["1", "3", "1", "2", "1", "1"],
            "G7":     ["2", "1", "0", "0", "0", "3"],

            "Amaj7":  ["x", "0", "2", "1", "3", "0"],
            "Cmaj7":  ["x", "3", "2", "0", "0", "0"],
            "Dmaj7":  ["x", "x", "0", "1", "2", "3"],
            "Emaj7":  ["0", "2", "3", "1", "0", "0"],
            "Fmaj7":  ["x", "3", "2", "1", "1", "0"],
            "Gmaj7":  ["2", "1", "0", "0", "0", "3"],
        }

        self.major_akorlar = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

        self.mikrofon_aktif = False
        self.audio = pyaudio.PyAudio()
        self.stream = None

        self.piano_sample_rate = 44100
        self.piano_volume = 0.35
        self.current_pressed_keys = set()
        self.piyano_aktif = False
        self.piano_octave_shift = 0
        self.sustain_enabled = False

        self.key_note_map = {
            Qt.Key_Z: "C3", Qt.Key_S: "C#3", Qt.Key_X: "D3", Qt.Key_D: "D#3",
            Qt.Key_C: "E3", Qt.Key_V: "F3", Qt.Key_G: "F#3", Qt.Key_B: "G3",
            Qt.Key_H: "G#3", Qt.Key_N: "A3", Qt.Key_J: "A#3", Qt.Key_M: "B3",
            Qt.Key_Q: "C4", Qt.Key_2: "C#4", Qt.Key_W: "D4", Qt.Key_3: "D#4",
            Qt.Key_E: "E4", Qt.Key_R: "F4", Qt.Key_5: "F#4", Qt.Key_T: "G4",
            Qt.Key_6: "G#4", Qt.Key_Y: "A4", Qt.Key_7: "A#4", Qt.Key_U: "B4",
        }

        self.key_label_map = {
            "C3": "Z", "C#3": "S", "D3": "X", "D#3": "D", "E3": "C", "F3": "V",
            "F#3": "G", "G3": "B", "G#3": "H", "A3": "N", "A#3": "J", "B3": "M",
            "C4": "Q", "C#4": "2", "D4": "W", "D#4": "3", "E4": "E", "F4": "R",
            "F#4": "5", "G4": "T", "G#4": "6", "A4": "Y", "A#4": "7", "B4": "U",
        }

        self.setup_ui()

    def combo_stil_uygula(self, combo):
        view = QListView()
        combo.setView(view)
        palette = combo.view().palette()
        palette.setColor(QPalette.Base, QColor("#0f172a"))
        palette.setColor(QPalette.Text, QColor("#e0e0ff"))
        palette.setColor(QPalette.Highlight, QColor("#2563eb"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        combo.view().setPalette(palette)

    def akor_tipe_uygun_mu(self, akor, akor_tipi):
        if akor_tipi == "Tümü":
            return True
        if akor_tipi == "Majör":
            return akor in self.major_akorlar
        if akor_tipi == "Minör":
            return ("m" in akor and "maj7" not in akor)
        if akor_tipi == "7'li":
            return ("7" in akor and "maj7" not in akor)
        if akor_tipi == "Majör7":
            return "maj7" in akor
        return True

    def create_title_bar(self, parent_layout):
        self.title_bar = QWidget()
        self.title_bar.setFixedHeight(48)
        self.title_bar.setStyleSheet("""
            background-color: #0b112f;
            border-bottom: 1px solid #1e3a8a;
        """)

        layout = QHBoxLayout(self.title_bar)
        layout.setContentsMargins(12, 6, 10, 6)
        layout.setSpacing(8)

        self.window_title_label = QLabel("Gitar Akor Asistanı")
        self.window_title_label.setStyleSheet("""
            color: #dbeafe;
            font-size: 13px;
            font-weight: bold;
        """)
        layout.addWidget(self.window_title_label)

        layout.addStretch()

        ortak_stil = """
            QPushButton {
                background-color: #1a1f2e;
                color: #dbeafe;
                border: 1px solid #3b82f6;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #232a3d;
                color: #ffffff;
                border: 1px solid #60a5fa;
            }
            QPushButton:pressed {
                background-color: #111827;
                border: 1px solid #93c5fd;
            }
        """

        self.min_btn = QPushButton("")
        self.min_btn.setFixedSize(42, 30)
        self.min_btn.setToolTip("Küçült")
        self.min_btn.setStyleSheet(ortak_stil)
        self.min_btn.clicked.connect(self.showMinimized)
        layout.addWidget(self.min_btn)

        self.max_btn = QPushButton("")
        self.max_btn.setFixedSize(42, 30)
        self.max_btn.setToolTip("Büyüt / Geri Al")
        self.max_btn.setStyleSheet(ortak_stil)
        self.max_btn.clicked.connect(self.toggle_max_restore)
        layout.addWidget(self.max_btn)

        self.close_btn = QPushButton("")
        self.close_btn.setFixedSize(42, 30)
        self.close_btn.setToolTip("Kapat")
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: #1a1f2e;
                color: #fecdd3;
                border: 1px solid #ef4444;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3b1020;
                color: white;
                border: 1px solid #fb7185;
            }
            QPushButton:pressed {
                background-color: #2a0d18;
                border: 1px solid #fda4af;
            }
        """)
        self.close_btn.clicked.connect(self.close)
        layout.addWidget(self.close_btn)

        parent_layout.addWidget(self.title_bar)

    def setup_ui(self):
        outer = QWidget()
        self.setCentralWidget(outer)

        outer_layout = QVBoxLayout(outer)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)

        self.create_title_bar(outer_layout)

        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: #0a0e27;")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(12, 12, 12, 12)
        content_layout.setSpacing(10)

        title = QLabel("Gitar Akor Asistanı Pro")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #3b82f6;
            padding: 18px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #0a0e27, stop:0.5 #1e3a8a, stop:1 #0a0e27);
            border-radius: 10px;
            margin: 4px;
        """)
        content_layout.addWidget(title)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("QTabWidget::tab-bar { alignment: center; }")
        self.tabs.currentChanged.connect(self.tab_degisti)
        content_layout.addWidget(self.tabs)

        self.akor_tab = QWidget()
        self.pratik_tab = QWidget()
        self.mikrofon_tab = QWidget()
        self.piyano_tab = QWidget()

        self.tabs.addTab(self.akor_tab, "Akor Sözlüğü")
        self.tabs.addTab(self.pratik_tab, "Akor Pratiği")
        self.tabs.addTab(self.mikrofon_tab, "Akor Tanıma")
        self.tabs.addTab(self.piyano_tab, "Sanal Piyano")

        self.akor_sozlugu()
        self.akor_pratigi()
        self.mikrofon_tanima()
        self.sanal_piyano()

        outer_layout.addWidget(content_widget)
        self.statusBar().showMessage("Hazır")

    def toggle_max_restore(self):
        if self.isMaximized():
            self.showNormal()
            self.max_btn.setText("")
        else:
            self.showMaximized()
            self.max_btn.setText("")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.title_bar.geometry().contains(event.pos()):
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos is not None:
            if not self.isMaximized():
                self.move(event.globalPos() - self.drag_pos)
                event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
        super().mouseReleaseEvent(event)

    def tab_degisti(self, index):
        self.piyano_aktif = (self.tabs.tabText(index) == "Sanal Piyano")
        self.statusBar().showMessage(self.tabs.tabText(index))

    def akor_sozlugu(self):
        layout = QVBoxLayout(self.akor_tab)
        layout.setSpacing(10)

        filter_panel = QHBoxLayout()
        filter_panel.addWidget(QLabel("Ara:"))

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Akor adı girin...")
        self.search_input.textChanged.connect(self.akor_ara)
        filter_panel.addWidget(self.search_input)

        filter_panel.addWidget(QLabel("Tip:"))
        self.tip_combo = QComboBox()
        self.tip_combo.addItems(["Tümü", "Majör", "Minör", "7'li", "Majör7"])
        self.combo_stil_uygula(self.tip_combo)
        self.tip_combo.currentTextChanged.connect(self.akor_ara)
        filter_panel.addWidget(self.tip_combo)

        filter_panel.addStretch()
        layout.addLayout(filter_panel)

        content = QHBoxLayout()
        content.setSpacing(12)

        left_panel = QVBoxLayout()
        left_panel.addWidget(QLabel("Akorlar:"))

        self.akor_listesi = QListWidget()
        self.akor_listesi.setMaximumWidth(220)
        self.akor_listesi.itemClicked.connect(self.akor_listeden_goster)
        left_panel.addWidget(self.akor_listesi)
        content.addLayout(left_panel)

        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("Akor Şeması:"))

        self.akor_canvas = QLabel()
        self.akor_canvas.setAlignment(Qt.AlignCenter)
        self.akor_canvas.setMinimumHeight(450)
        self.akor_canvas.setStyleSheet("""
            background-color: #0f172a;
            border-radius: 12px;
            border: 2px solid #1e3a8a;
        """)
        right_panel.addWidget(self.akor_canvas)

        self.akor_bilgi_label = QLabel("")
        self.akor_bilgi_label.setAlignment(Qt.AlignCenter)
        self.akor_bilgi_label.setStyleSheet("color: #93c5fd; font-size: 13px; padding: 8px;")
        right_panel.addWidget(self.akor_bilgi_label)

        content.addLayout(right_panel, 1)
        layout.addLayout(content)

        self.akor_ara()

        if self.akor_listesi.count() > 0:
            self.akor_listesi.setCurrentRow(0)
            self.akor_listeden_goster(self.akor_listesi.item(0))

    def akor_ara(self):
        search_text = self.search_input.text().lower().strip()
        akor_tipi = self.tip_combo.currentText()
        self.akor_listesi.clear()

        for akor in sorted(self.akorlar.keys()):
            if search_text and search_text not in akor.lower():
                continue
            if not self.akor_tipe_uygun_mu(akor, akor_tipi):
                continue
            self.akor_listesi.addItem(akor)

    def akor_listeden_goster(self, item):
        self.ciz_akor(item.text())

    def otomatik_parmak_numaralari(self, akor):
        basili = [(tel, int(poz)) for tel, poz in enumerate(akor) if poz not in ["x", "0"]]
        if not basili:
            return {}

        parmak_map = {}
        kullanilan = 1
        perdeler = sorted(set(p for _, p in basili))

        for perde in perdeler:
            teller = sorted([tel for tel, p in basili if p == perde])
            for tel in teller:
                parmak_map[(tel, perde)] = min(kullanilan, 4)
                kullanilan = min(kullanilan + 1, 4)

        return parmak_map

    def ciz_akor(self, akor_adi):
        if akor_adi not in self.akorlar:
            return

        akor = self.akorlar[akor_adi]
        parmak_veri = self.parmak_pozisyonlari.get(akor_adi, None)

        pixmap = QPixmap(600, 450)
        pixmap.fill(QColor("#0f172a"))

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        start_x, start_y = 100, 90
        tel_aralik = 70
        perde_aralik = 55
        gorunen_perde_sayisi = 5

        basili_perdeler = [int(p) for p in akor if p not in ["x", "0"]]
        min_perde = min(basili_perdeler) if basili_perdeler else 1
        base_fret = 1 if min_perde <= 3 else min_perde

        painter.setPen(QPen(QColor("#3b82f6"), 2))
        for i in range(6):
            x = start_x + i * tel_aralik
            painter.drawLine(x, start_y, x, start_y + gorunen_perde_sayisi * perde_aralik)

        for i in range(gorunen_perde_sayisi + 1):
            y = start_y + i * perde_aralik
            kalinlik = 4 if i == 0 and base_fret == 1 else 2
            painter.setPen(QPen(QColor("#3b82f6"), kalinlik))
            painter.drawLine(start_x, y, start_x + 5 * tel_aralik, y)

        painter.setPen(QPen(QColor("#60a5fa")))
        painter.setFont(QFont("Arial", 24, QFont.Bold))
        painter.drawText(start_x + 150, 45, akor_adi)

        if base_fret > 1:
            painter.setFont(QFont("Arial", 11, QFont.Bold))
            painter.setPen(QPen(QColor("#fbbf24")))
            painter.drawText(start_x - 45, start_y + 35, f"{base_fret}.fr")

        painter.setFont(QFont("Arial", 10))
        painter.setPen(QPen(QColor("#94a3b8")))
        tel_isimleri = ["E", "A", "D", "G", "B", "E"]
        for i, tel in enumerate(tel_isimleri):
            painter.drawText(start_x + i * tel_aralik - 5, start_y - 10, tel)

        # Sadece gerçekten aynı parmak numarasıyla çizilmişse bare say
        bare_gruplar = {}
        if parmak_veri:
            for tel, (poz, parmak) in enumerate(zip(akor, parmak_veri)):
                if poz not in ["x", "0"] and parmak not in ["x", "0"]:
                    key = (int(poz), str(parmak))
                    bare_gruplar.setdefault(key, []).append(tel)

        for (perde_no, parmak_no), teller in bare_gruplar.items():
            if len(teller) >= 2:
                x1 = start_x + min(teller) * tel_aralik
                x2 = start_x + max(teller) * tel_aralik
                y = start_y + ((perde_no - base_fret) + 0.5) * perde_aralik
                painter.setPen(Qt.NoPen)
                painter.setBrush(QBrush(QColor("#2563eb")))
                painter.drawRoundedRect(int(x1 - 15), int(y - 12), int((x2 - x1) + 30), 24, 10, 10)
                painter.setPen(QPen(QColor("#ffffff")))
                painter.setFont(QFont("Arial", 11, QFont.Bold))
                painter.drawText(int((x1 + x2) / 2 - 4), int(y + 5), parmak_no)

        otomatik_map = self.otomatik_parmak_numaralari(akor)

        for tel, poz in enumerate(akor):
            x = start_x + tel * tel_aralik

            if poz == "x":
                painter.setPen(QPen(QColor("#f87171")))
                painter.setFont(QFont("Arial", 12, QFont.Bold))
                painter.drawText(x - 8, start_y - 28, "✗")
            elif poz == "0":
                painter.setPen(QPen(QColor("#4ade80")))
                painter.setFont(QFont("Arial", 12, QFont.Bold))
                painter.drawText(x - 8, start_y - 28, "○")
            else:
                perde_no = int(poz)
                y_ortasi = start_y + ((perde_no - base_fret) + 0.5) * perde_aralik

                if parmak_veri:
                    parmak_no = parmak_veri[tel]
                else:
                    parmak_no = str(otomatik_map.get((tel, perde_no), ""))

                barede_mi = False
                if parmak_veri and parmak_no not in ["x", "0"]:
                    ayni = [
                        t for t, (p, pn) in enumerate(zip(akor, parmak_veri))
                        if p not in ["x", "0"] and pn == parmak_no and int(p) == perde_no
                    ]
                    if len(ayni) >= 2:
                        barede_mi = True

                if not barede_mi:
                    painter.setBrush(QBrush(QColor("#3b82f6")))
                    painter.setPen(QPen(QColor("#3b82f6")))
                    painter.drawEllipse(int(x - 15), int(y_ortasi - 15), 30, 30)
                    painter.setPen(QPen(QColor("#ffffff")))
                    painter.setFont(QFont("Arial", 11, QFont.Bold))
                    painter.drawText(int(x - 4), int(y_ortasi + 5), str(parmak_no))

        painter.end()
        self.akor_canvas.setPixmap(pixmap.scaled(600, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.akor_bilgi_label.setText("")

    def akor_pratigi(self):
        layout = QVBoxLayout(self.pratik_tab)
        layout.setSpacing(10)

        settings_group = QGroupBox("Pratik Ayarları")
        settings_layout = QGridLayout()

        settings_layout.addWidget(QLabel("Zorluk:"), 0, 0)
        self.zorluk_combo = QComboBox()
        self.zorluk_combo.addItems(["Kolay", "Orta", "Zor"])
        self.combo_stil_uygula(self.zorluk_combo)
        settings_layout.addWidget(self.zorluk_combo, 0, 1)

        settings_layout.addWidget(QLabel("Akor Tipi:"), 1, 0)
        self.pratik_tip = QComboBox()
        self.pratik_tip.addItems(["Tümü", "Majör", "Minör", "7'li", "Majör7"])
        self.combo_stil_uygula(self.pratik_tip)
        settings_layout.addWidget(self.pratik_tip, 1, 1)

        settings_layout.addWidget(QLabel("Süre (dakika):"), 2, 0)
        self.pratik_sure = QSpinBox()
        self.pratik_sure.setRange(1, 10)
        self.pratik_sure.setValue(3)
        settings_layout.addWidget(self.pratik_sure, 2, 1)

        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)

        self.pratik_akor_label = QLabel("🎸")
        self.pratik_akor_label.setAlignment(Qt.AlignCenter)
        self.pratik_akor_label.setStyleSheet("""
            font-size: 86px;
            font-weight: bold;
            color: #3b82f6;
            padding: 40px;
            background-color: #0f172a;
            border-radius: 15px;
            border: 2px solid #1e3a8a;
        """)
        layout.addWidget(self.pratik_akor_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        stats_group = QGroupBox("İstatistikler")
        stats_layout = QGridLayout()

        self.skor_label = QLabel("Skor: 0")
        self.skor_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #4ade80;")
        self.dogru_label = QLabel("Doğru: 0")
        self.yanlis_label = QLabel("Yanlış: 0")
        self.basari_label = QLabel("Başarı: 0%")
        self.seri_label = QLabel("Seri: 0")

        stats_layout.addWidget(self.skor_label, 0, 0)
        stats_layout.addWidget(self.dogru_label, 0, 1)
        stats_layout.addWidget(self.yanlis_label, 0, 2)
        stats_layout.addWidget(self.basari_label, 0, 3)
        stats_layout.addWidget(self.seri_label, 0, 4)

        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)

        self.pratik_gecmis = QListWidget()
        self.pratik_gecmis.setMaximumHeight(130)
        layout.addWidget(self.pratik_gecmis)

        btn_layout = QHBoxLayout()

        self.baslat_btn = QPushButton("Pratiği Başlat")
        self.baslat_btn.clicked.connect(self.pratik_baslat)
        btn_layout.addWidget(self.baslat_btn)

        self.durdur_btn = QPushButton("Durdur")
        self.durdur_btn.clicked.connect(self.pratik_durdur)
        self.durdur_btn.setEnabled(False)
        btn_layout.addWidget(self.durdur_btn)

        self.dogru_btn = QPushButton("Doğru")
        self.dogru_btn.clicked.connect(self.pratik_dogru)
        self.dogru_btn.setEnabled(False)
        btn_layout.addWidget(self.dogru_btn)

        self.yanlis_btn = QPushButton("Yanlış")
        self.yanlis_btn.clicked.connect(self.pratik_yanlis)
        self.yanlis_btn.setEnabled(False)
        btn_layout.addWidget(self.yanlis_btn)

        self.goster_btn = QPushButton("Akoru Göster")
        self.goster_btn.clicked.connect(self.pratik_akor_goster)
        self.goster_btn.setEnabled(False)
        btn_layout.addWidget(self.goster_btn)

        layout.addLayout(btn_layout)

        self.pratik_aktif = False
        self.skor = 0
        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0
        self.seri = 0
        self.pratik_timer = None
        self.kalan_sure = 0
        self.suanki_akor = None

    def pratik_icin_uygun_akorlar(self):
        zorluk = self.zorluk_combo.currentText()
        akor_tipi = self.pratik_tip.currentText()

        uygun_akorlar = []
        for akor in self.akorlar.keys():
            if not self.akor_tipe_uygun_mu(akor, akor_tipi):
                continue

            if zorluk == "Kolay":
                if len(akor) <= 2:
                    uygun_akorlar.append(akor)
            elif zorluk == "Orta":
                if len(akor) <= 4:
                    uygun_akorlar.append(akor)
            else:
                uygun_akorlar.append(akor)

        return uygun_akorlar if uygun_akorlar else list(self.akorlar.keys())

    def pratik_baslat(self):
        if self.pratik_aktif:
            return

        self.pratik_aktif = True
        self.skor = 0
        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0
        self.seri = 0
        self.pratik_gecmis.clear()
        self.guncelle_istatistikler()

        self.kalan_sure = self.pratik_sure.value() * 60
        self.progress_bar.setVisible(True)
        self.progress_bar.setMaximum(self.kalan_sure)
        self.progress_bar.setValue(self.kalan_sure)

        self.pratik_timer = QTimer()
        self.pratik_timer.timeout.connect(self.pratik_sure_guncelle)
        self.pratik_timer.start(1000)

        self.baslat_btn.setEnabled(False)
        self.durdur_btn.setEnabled(True)
        self.dogru_btn.setEnabled(True)
        self.yanlis_btn.setEnabled(True)
        self.goster_btn.setEnabled(True)

        self.sonraki_akor()

    def pratik_durdur(self):
        if self.pratik_timer:
            self.pratik_timer.stop()

        self.pratik_aktif = False
        self.baslat_btn.setEnabled(True)
        self.durdur_btn.setEnabled(False)
        self.dogru_btn.setEnabled(False)
        self.yanlis_btn.setEnabled(False)
        self.goster_btn.setEnabled(False)
        self.progress_bar.setVisible(False)

        toplam = self.dogru_sayisi + self.yanlis_sayisi
        basari = (self.dogru_sayisi * 100 / toplam) if toplam > 0 else 0

        QMessageBox.information(
            self,
            "Pratik Tamamlandı",
            f"Toplam: {toplam}\n"
            f"Doğru: {self.dogru_sayisi}\n"
            f"Yanlış: {self.yanlis_sayisi}\n"
            f"Başarı: %{basari:.1f}\n"
            f"Skor: {self.skor}\n"
            f"En son seri: {self.seri}"
        )
        self.pratik_akor_label.setText("🎸")
        self.statusBar().showMessage("Pratik tamamlandı")

    def pratik_sure_guncelle(self):
        self.kalan_sure -= 1
        self.progress_bar.setValue(self.kalan_sure)
        self.statusBar().showMessage(f"Pratik sürüyor • Kalan süre: {self.kalan_sure} sn")
        if self.kalan_sure <= 0:
            self.pratik_durdur()

    def sonraki_akor(self):
        if not self.pratik_aktif:
            return

        uygun_akorlar = self.pratik_icin_uygun_akorlar()

        if len(uygun_akorlar) > 1 and self.suanki_akor in uygun_akorlar:
            secenekler = [a for a in uygun_akorlar if a != self.suanki_akor]
        else:
            secenekler = uygun_akorlar

        self.suanki_akor = random.choice(secenekler)
        self.pratik_akor_label.setText(self.suanki_akor)

    def pratik_dogru(self):
        if not self.pratik_aktif or not self.suanki_akor:
            return

        self.dogru_sayisi += 1
        self.seri += 1
        self.skor += 10 + min(self.seri * 2, 20)
        self.pratik_gecmis.insertItem(0, f"✅ {self.suanki_akor}")
        if self.pratik_gecmis.count() > 20:
            self.pratik_gecmis.takeItem(self.pratik_gecmis.count() - 1)

        self.guncelle_istatistikler()
        self.sonraki_akor()

    def pratik_yanlis(self):
        if not self.pratik_aktif or not self.suanki_akor:
            return

        self.yanlis_sayisi += 1
        self.seri = 0
        self.skor = max(0, self.skor - 5)
        self.pratik_gecmis.insertItem(0, f"❌ {self.suanki_akor}")
        if self.pratik_gecmis.count() > 20:
            self.pratik_gecmis.takeItem(self.pratik_gecmis.count() - 1)

        self.guncelle_istatistikler()
        self.sonraki_akor()

    def pratik_akor_goster(self):
        if not self.suanki_akor:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle(f"Akor: {self.suanki_akor}")
        dialog.resize(650, 550)
        dialog.setStyleSheet("QDialog { background-color: #0a0e27; }")
        layout = QVBoxLayout(dialog)

        gecici_pixmap = self.akor_olustur_pixmap(self.suanki_akor)
        img = QLabel()
        img.setAlignment(Qt.AlignCenter)
        img.setPixmap(gecici_pixmap)
        layout.addWidget(img)

        btn = QPushButton("Tamam")
        btn.clicked.connect(dialog.accept)
        layout.addWidget(btn)

        dialog.exec_()

    def guncelle_istatistikler(self):
        toplam = self.dogru_sayisi + self.yanlis_sayisi
        basari = (self.dogru_sayisi * 100 / toplam) if toplam > 0 else 0
        self.skor_label.setText(f"Skor: {self.skor}")
        self.dogru_label.setText(f"Doğru: {self.dogru_sayisi}")
        self.yanlis_label.setText(f"Yanlış: {self.yanlis_sayisi}")
        self.basari_label.setText(f"Başarı: %{basari:.1f}")
        self.seri_label.setText(f"Seri: {self.seri}")

    def mikrofon_tanima(self):
        layout = QVBoxLayout(self.mikrofon_tab)

        self.mikrofon_btn = QPushButton("Mikrofonu Başlat")
        self.mikrofon_btn.clicked.connect(self.mikrofon_toggle)
        layout.addWidget(self.mikrofon_btn)

        self.mikrofon_durum = QLabel("Mikrofon kapalı")
        self.mikrofon_durum.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mikrofon_durum)

        self.taninan_akor = QLabel("---")
        self.taninan_akor.setAlignment(Qt.AlignCenter)
        self.taninan_akor.setStyleSheet("""
            font-size: 86px;
            font-weight: bold;
            color: #3b82f6;
            background-color: #0f172a;
            padding: 40px;
            border-radius: 12px;
            border: 2px solid #1e3a8a;
        """)
        layout.addWidget(self.taninan_akor)

        self.ses_seviyesi = QProgressBar()
        self.ses_seviyesi.setRange(0, 100)
        layout.addWidget(self.ses_seviyesi)

        self.akor_gecmisi = QListWidget()
        layout.addWidget(self.akor_gecmisi)

    def mikrofon_toggle(self):
        if not self.mikrofon_aktif:
            try:
                self.stream = self.audio.open(
                    format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=2048,
                    stream_callback=self.audio_callback
                )
                self.stream.start_stream()
                self.mikrofon_aktif = True
                self.mikrofon_btn.setText("Mikrofonu Durdur")
                self.mikrofon_durum.setText("Mikrofon aktif - Gitarınızı çalın")
                self.statusBar().showMessage("Mikrofon aktif")
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Mikrofon başlatılamadı:\n{str(e)}")
        else:
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
            self.mikrofon_aktif = False
            self.mikrofon_btn.setText("Mikrofonu Başlat")
            self.mikrofon_durum.setText("Mikrofon kapalı")
            self.taninan_akor.setText("---")
            self.ses_seviyesi.setValue(0)
            self.statusBar().showMessage("Mikrofon kapatıldı")

    def audio_callback(self, in_data, frame_count, time_info, status):
        if self.mikrofon_aktif:
            data = np.frombuffer(in_data, dtype=np.int16).astype(np.float64)
            volume = np.sqrt(np.mean(data ** 2))
            seviye = min(int(volume / 400), 100)

            QMetaObject.invokeMethod(
                self.ses_seviyesi, "setValue",
                Qt.QueuedConnection, Q_ARG(int, seviye)
            )

            if volume > 500:
                self.akor_tanima(data)

        return (in_data, pyaudio.paContinue)

    def akor_tanima(self, ses_data):
        pencere = np.hanning(len(ses_data))
        fft = np.fft.fft(ses_data * pencere)
        frekanslar = np.fft.fftfreq(len(fft), 1 / 44100)
        guc = np.abs(fft[:len(fft) // 2])

        max_index = np.argmax(guc[10:]) + 10
        dominant_freq = abs(frekanslar[max_index])

        nota_frekans = {
            'E2': 82.41, 'F2': 87.31, 'F#2': 92.50, 'G2': 98.00, 'G#2': 103.83,
            'A2': 110.00, 'A#2': 116.54, 'B2': 123.47, 'C3': 130.81, 'C#3': 138.59,
            'D3': 146.83, 'D#3': 155.56, 'E3': 164.81, 'F3': 174.61, 'F#3': 185.00,
            'G3': 196.00, 'G#3': 207.65, 'A3': 220.00, 'A#3': 233.08, 'B3': 246.94,
            'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63,
            'F4': 349.23, 'F#4': 369.99, 'G4': 392.00, 'G#4': 415.30, 'A4': 440.00
        }

        en_yakin_nota = min(nota_frekans.keys(), key=lambda x: abs(nota_frekans[x] - dominant_freq))
        tahmin_edilen_akor = self.notadan_akora(en_yakin_nota)

        if tahmin_edilen_akor:
            zaman = datetime.now().strftime('%H:%M:%S')
            metin = f"🎸 {tahmin_edilen_akor} ({en_yakin_nota}) - {zaman}"

            QMetaObject.invokeMethod(
                self.taninan_akor, "setText",
                Qt.QueuedConnection, Q_ARG(str, tahmin_edilen_akor)
            )
            QMetaObject.invokeMethod(
                self.akor_gecmisi, "insertItem",
                Qt.QueuedConnection,
                Q_ARG(int, 0),
                Q_ARG(str, metin)
            )

    def notadan_akora(self, nota):
        akor_map = {
            'E2': 'E', 'F2': 'F', 'F#2': 'F#', 'G2': 'G', 'G#2': 'G#',
            'A2': 'A', 'A#2': 'A#', 'B2': 'B', 'C3': 'C', 'C#3': 'C#',
            'D3': 'D', 'D#3': 'D#', 'E3': 'E', 'F3': 'F', 'F#3': 'F#',
            'G3': 'G', 'G#3': 'G#', 'A3': 'A', 'A#3': 'A#', 'B3': 'B',
            'C4': 'C', 'C#4': 'C#', 'D4': 'D', 'D#4': 'D#', 'E4': 'E',
        }
        return akor_map.get(nota, None)

    def sanal_piyano(self):
        main_layout = QVBoxLayout(self.piyano_tab)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        top_bar = QHBoxLayout()
        top_bar.setSpacing(12)

        top_bar.addWidget(QLabel("Ses:"))
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(10, 100)
        self.volume_slider.setValue(35)
        self.volume_slider.setFixedWidth(180)
        self.volume_slider.valueChanged.connect(self.volume_degisti)
        top_bar.addWidget(self.volume_slider)

        self.volume_label = QLabel("%35")
        self.volume_label.setMinimumWidth(40)
        top_bar.addWidget(self.volume_label)

        top_bar.addSpacing(10)
        top_bar.addWidget(QLabel("Oktav:"))

        self.oktav_combo = QComboBox()
        self.oktav_combo.addItems(["-1", "0", "+1"])
        self.oktav_combo.setCurrentText("0")
        self.combo_stil_uygula(self.oktav_combo)
        self.oktav_combo.setFixedWidth(80)
        self.oktav_combo.currentTextChanged.connect(self.piano_octave_changed)
        top_bar.addWidget(self.oktav_combo)

        self.sustain_checkbox = QCheckBox("Sustain")
        self.sustain_checkbox.stateChanged.connect(self.sustain_degisti)
        top_bar.addWidget(self.sustain_checkbox)

        top_bar.addStretch()

        self.piyano_bilgi = QLabel("Son nota: ---")
        self.piyano_bilgi.setStyleSheet("""
            background-color: #0f172a;
            border: 1px solid #1e3a8a;
            border-radius: 8px;
            padding: 8px 14px;
            font-weight: bold;
            color: #93c5fd;
        """)
        top_bar.addWidget(self.piyano_bilgi)

        main_layout.addLayout(top_bar)

        info_bar = QLabel("Alt: Z S X D C V G B H N J M   |   Üst: Q 2 W 3 E R 5 T 6 Y 7 U   |   ← ↓ → oktav | Space sustain")
        info_bar.setAlignment(Qt.AlignCenter)
        info_bar.setStyleSheet("""
            background-color: #0f172a;
            border: 1px solid #1e3a8a;
            border-radius: 8px;
            padding: 8px;
            color: #cbd5e1;
            font-weight: bold;
        """)
        main_layout.addWidget(info_bar)

        piano_frame = QFrame()
        piano_frame.setStyleSheet("""
            QFrame {
                background-color: #0f172a;
                border: 2px solid #1e3a8a;
                border-radius: 12px;
            }
        """)
        piano_layout = QVBoxLayout(piano_frame)
        piano_layout.setContentsMargins(8, 8, 8, 8)

        self.key_area = QWidget()
        self.key_area.setFixedSize(1000, 250)
        self.key_area.setStyleSheet("background-color: transparent; border: none;")

        self.white_keys = {}
        self.black_keys = {}

        white_notes = ["C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4"]
        black_positions = {
            "C#3": 57, "D#3": 129, "F#3": 273, "G#3": 345, "A#3": 417,
            "C#4": 561, "D#4": 633, "F#4": 777, "G#4": 849, "A#4": 921
        }

        white_width = 70
        white_step = 72
        white_height = 220
        black_width = 44
        black_height = 130

        x = 0
        for note in white_notes:
            key_text = f"{note}\n[{self.key_label_map.get(note, '')}]"
            btn = QPushButton(key_text, self.key_area)
            btn.setFixedSize(white_width, white_height)
            btn.move(x, 12)
            btn.setStyleSheet(self.white_key_style())
            btn.clicked.connect(lambda checked, n=note: self.play_piano_note_by_name(n))
            self.white_keys[note] = btn
            x += white_step

        for note, xpos in black_positions.items():
            key_text = f"{note}\n[{self.key_label_map.get(note, '')}]"
            btn = QPushButton(key_text, self.key_area)
            btn.setFixedSize(black_width, black_height)
            btn.move(xpos, 12)
            btn.setStyleSheet(self.black_key_style())
            btn.raise_()
            btn.clicked.connect(lambda checked, n=note: self.play_piano_note_by_name(n))
            self.black_keys[note] = btn

        piano_layout.addWidget(self.key_area, alignment=Qt.AlignCenter)
        main_layout.addWidget(piano_frame, alignment=Qt.AlignTop | Qt.AlignHCenter)
        main_layout.addStretch()

    def white_key_style(self):
        return """
            QPushButton {
                background-color: #f8fafc;
                color: #111827;
                border: 1px solid #94a3b8;
                border-radius: 0px 0px 6px 6px;
                font-weight: bold;
                font-size: 10px;
                padding-top: 120px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #e2e8f0;
            }
            QPushButton:pressed {
                background-color: #93c5fd;
            }
        """

    def black_key_style(self):
        return """
            QPushButton {
                background-color: #111827;
                color: white;
                border: 1px solid #020617;
                border-radius: 0px 0px 5px 5px;
                font-weight: bold;
                font-size: 8px;
                padding-top: 55px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #1e293b;
            }
            QPushButton:pressed {
                background-color: #2563eb;
            }
        """

    def piano_octave_changed(self, text):
        self.piano_octave_shift = {"-1": -1, "0": 0, "+1": 1}.get(text, 0)

    def sustain_degisti(self, state):
        self.sustain_enabled = (state == Qt.Checked)

    def volume_degisti(self, value):
        self.piano_volume = value / 100.0
        self.volume_label.setText(f"%{value}")

    def shift_note_octave(self, note_name, shift):
        if len(note_name) == 2:
            note = note_name[0]
            octave = int(note_name[1])
        else:
            note = note_name[:2]
            octave = int(note_name[2])
        return f"{note}{octave + shift}"

    def note_to_frequency(self, note_name):
        A4 = 440.0
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        if len(note_name) == 2:
            note = note_name[0]
            octave = int(note_name[1])
        else:
            note = note_name[:2]
            octave = int(note_name[2])

        n = note_names.index(note)
        semitones_from_a4 = (octave - 4) * 12 + (n - 9)
        return A4 * (2 ** (semitones_from_a4 / 12))

    def play_piano_note_by_name(self, note_name):
        shifted_note = self.shift_note_octave(note_name, self.piano_octave_shift)
        self.piyano_bilgi.setText(f"Son nota: {shifted_note}")

        self.highlight_piano_key(note_name)
        QTimer.singleShot(160, lambda n=note_name: self.unhighlight_piano_key(n))

        freq = self.note_to_frequency(shifted_note)
        duration = 1.1 if self.sustain_enabled else 0.42

        threading.Thread(
            target=self.generate_and_play_tone,
            args=(freq, duration),
            daemon=True
        ).start()

    def generate_and_play_tone(self, frequency, duration=0.42):
        sample_rate = self.piano_sample_rate
        t = np.linspace(0, duration, int(sample_rate * duration), False)

        wave = (
            0.55 * np.sin(2 * np.pi * frequency * t) +
            0.22 * np.sin(2 * np.pi * frequency * 2 * t) +
            0.11 * np.sin(2 * np.pi * frequency * 3 * t) +
            0.06 * np.sin(2 * np.pi * frequency * 4 * t)
        )

        attack = max(1, int(len(t) * 0.02))
        decay = len(t) - attack
        envelope = np.concatenate([
            np.linspace(0, 1, attack),
            np.exp(-3.8 * np.linspace(0, 1, decay))
        ])

        wave *= envelope
        wave = np.clip(wave, -1, 1)
        audio_data = (wave * 32767 * self.piano_volume).astype(np.int16)

        try:
            stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                output=True
            )
            stream.write(audio_data.tobytes())
            stream.stop_stream()
            stream.close()
        except Exception as e:
            print("Piyano sesi çalma hatası:", e)

    def highlight_piano_key(self, note):
        if note in self.white_keys:
            self.white_keys[note].setStyleSheet("""
                QPushButton {
                    background-color: #93c5fd;
                    color: #111827;
                    border: 2px solid #3b82f6;
                    border-radius: 0px 0px 6px 6px;
                    font-weight: bold;
                    font-size: 10px;
                    padding-top: 120px;
                    text-align: center;
                }
            """)
        elif note in self.black_keys:
            self.black_keys[note].setStyleSheet("""
                QPushButton {
                    background-color: #2563eb;
                    color: white;
                    border: 2px solid #60a5fa;
                    border-radius: 0px 0px 5px 5px;
                    font-weight: bold;
                    font-size: 8px;
                    padding-top: 55px;
                    text-align: center;
                }
            """)

    def unhighlight_piano_key(self, note):
        if note in self.white_keys:
            self.white_keys[note].setStyleSheet(self.white_key_style())
        elif note in self.black_keys:
            self.black_keys[note].setStyleSheet(self.black_key_style())

    def akor_olustur_pixmap(self, akor_adi):
        self.ciz_akor(akor_adi)
        return self.akor_canvas.pixmap()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_Escape:
            self.close()
            return

        if not self.piyano_aktif:
            super().keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_Left:
            self.oktav_combo.setCurrentText("-1")
            return
        elif key == Qt.Key_Down:
            self.oktav_combo.setCurrentText("0")
            return
        elif key == Qt.Key_Right:
            self.oktav_combo.setCurrentText("+1")
            return
        elif key == Qt.Key_Space:
            self.sustain_checkbox.setChecked(not self.sustain_checkbox.isChecked())
            return

        if key in self.key_note_map and key not in self.current_pressed_keys:
            self.current_pressed_keys.add(key)
            note = self.key_note_map[key]
            self.play_piano_note_by_name(note)

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key in self.current_pressed_keys:
            self.current_pressed_keys.remove(key)

        super().keyReleaseEvent(event)

    def closeEvent(self, event):
        try:
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
        except:
            pass

        try:
            self.audio.terminate()
        except:
            pass

        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = GitarAkorAsistani()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()