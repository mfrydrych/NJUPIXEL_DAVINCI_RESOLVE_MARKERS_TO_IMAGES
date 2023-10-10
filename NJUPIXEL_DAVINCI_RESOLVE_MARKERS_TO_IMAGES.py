# -*- coding: utf-8 -*-
#
#   Davinci Resolve timeline markers to images exporter.
#   This application allow you to export timeline markers to image files.
#   You can choose JPEG, PNG, DPX, TIFF, CIN, PPM, BMP, XPM file type.
#
#   This application use PyQt6 framework and SMPTE timecode conversion module by Igor Ridanovic
#   https://github.com/IgorRidanovic/smpte/blob/master/SMPTE.py
#
#
#   NJUPIXEL Maciej Frydrych 2023
#   njupixel@gmail.com

import sys
import os
import os.path
import subprocess
from datetime import datetime
import PySide6
import PySide6.QtGui
from PySide6.QtGui import QColor, QPalette, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)

from python_module.python_get_resolve import GetResolve
from python_module.SMPTE import SMPTE
from python_module.gui_main import Ui_MAIN_WINDOW
from python_module.gui_about import Ui_ABOUT_WINDOW

startpath = str
user_folder_path = ""
marker_chosen = ""
user_file_type = "jpg"

time_now = datetime.now()
time_now_format = time_now.strftime("%H-%M-%S_")

# check if it is Windows or Mac
if sys.platform == "win32":
    startpath = os.path.expanduser("~")

elif sys.platform == "darwin":
    startpath = "/Users"


resolve_texts_and_colors = {
    "Blue": "#0E7CD8",
    "Cyan": "#03CFCF",
    "Green": "#03AD0B",
    "Yellow": "#EA9B0F",
    "Red": "#E32600",
    "Pink": "#FB42CF",
    "Purple": "#7815CC",
    "Fuchsia": "#C92B70",
    "Rose": "#F9A1B6",
    "Lavender": "#A191CF",
    "Sky": "#96DDF2",
    "Mint": "#6DDE05",
    "Lemon": "#DDEA57",
    "Sand": "#C3945F",
    "Cocoa": "#6e5143",
    "Cream": "#F8EBDE",
}


# ---------------------------------------- MAIN PROGRAM ----------------------------------------------------
class MainProgramClass(QWidget, Ui_MAIN_WINDOW):
    """
    Davinci Resolve timeline markers to images exporter.
    This script allow you to export timeline markers to images file.

    """

    def __init__(self):
        super(MainProgramClass, self).__init__()
        self.setupUi(self)

        self.combobox_marker_color_create()
        self.btn_export_stills.clicked.connect(self.check_if_markers_exist)
        self.btn_about.clicked.connect(self.show_about_dialog)
        self.cb_file_type.currentIndexChanged.connect(self.file_type_selection)
        # application window always on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    # ---------------------------------------- SHOW ABOUT DIALOG -------------------------
    def show_about_dialog(self):
        """
        Show about window.
        """
        self.gui_about = QWidget()
        self.ui = Ui_ABOUT_WINDOW()
        self.ui.setupUi(self.gui_about)
        self.gui_about.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.gui_about.show()

    # ---------------------------------------- GENERATE COMBOBOX CONTENT -------------------------
    def combobox_marker_color_create(self):
        """
        Generate 16 items in combobox.
        Each one with name and color from DaVinci palette.
        """
        for index, (text, color_hex) in enumerate(resolve_texts_and_colors.items()):
            self.cb_markers.addItem(str(text))
            color = QColor(color_hex)
            self.cb_markers.setItemData(index + 1, color, 8)

    # -------------------------------------- COMBO BOX FILE TYPE SELECTOR ------------------------
    def file_type_selection(self, event):
        """
        Returns a file type selection.
        """
        global user_file_type
        event = self.cb_file_type.currentText()
        user_file_type = event.lower()
        return user_file_type

    # -------------------------------------- GET TIMELINE NAME ---------------------------
    def return_current_timeline_name(self):
        """
        Returns a timeline name
        """
        resolve = GetResolve()
        project_manager = resolve.GetProjectManager()
        current_project = project_manager.GetCurrentProject()
        current_timeline = current_project.GetCurrentTimeline()
        current_timeline_name = current_timeline.GetName()
        current_video_item = current_timeline.GetCurrentVideoItem()
        get_clip_name = current_video_item.GetName()
        return current_timeline_name

    # -------------------------------------- GET CURRENT CLIP NAME ---------------------------
    def return_current_clip_name(self):
        """
        Returns a clip name from current playhead position on timeline.
        """
        resolve = GetResolve()
        project_manager = resolve.GetProjectManager()
        current_project = project_manager.GetCurrentProject()
        current_timeline = current_project.GetCurrentTimeline()
        current_timeline_name = current_timeline.GetName()
        current_video_item = current_timeline.GetCurrentVideoItem()
        get_clip_name = current_video_item.GetName()
        get_local_version_name = current_video_item.GetVersionNames(0)
        return get_clip_name

    # ---------------------------------------- CHECK IF RESOLVE TIMELINE HAS MARKERS ------------------------------
    def check_if_markers_exist(self):
        """
        Check if markers exist.
        """
        try:
            resolve = GetResolve()
            project_manager = resolve.GetProjectManager()
            current_project = project_manager.GetCurrentProject()
            current_timeline = current_project.GetCurrentTimeline()
            current_timeline_name = current_timeline.GetName()
            markers = current_timeline.GetMarkers()

            if not markers:
                self.message_window("Info", "There are no markers on the timeline.")
            else:
                self.export_stills_dialog()

        except Exception as e:
            self.message_window("Error", f"{e}")
            return

    # ---------------------------------------- GET EXPORT PATH AND START EXPORTING ------------------------------
    def export_stills_dialog(self):
        """
        Open file dialog to get export path.
        """
        global user_folder_path, current_timeline_name
        folder_path = QFileDialog.getExistingDirectory(
            self, "Choose export folder", startpath
        )

        if folder_path:
            print("You choose:", folder_path)
            user_folder_path = folder_path
            # get curent time
            time_now = datetime.now()
            time_now_format = time_now.strftime("%H-%M-%S_")

            current_timeline_name = (
                f"{time_now_format}{self.return_current_timeline_name()}"
            )

            folder_path = os.path.join(user_folder_path, current_timeline_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                self.export_still(folder_path)
                self.reveal_file(folder_path)
            else:
                pass

    # -------------------------------------- EXPORT STILL FROM MARKERS ---------------------------
    def export_still(self, export_path):
        """
        Function is checking timeline settings - fps, interlace/progressive...
        Export all markers or specyfic color only with chosed file type to user defined path.
        """
        try:
            resolve = GetResolve()
            project_manager = resolve.GetProjectManager()
            current_project = project_manager.GetCurrentProject()
            current_timeline = current_project.GetCurrentTimeline()
            markers = current_timeline.GetMarkers()
            current_timecode = current_timeline.GetCurrentTimecode()
            offset = current_timeline.GetStartFrame()
            fps = int(float(current_project.GetSetting("timelineFrameRate")))
            is_current_timeline_interlace = current_timeline.GetSetting(
                "timelineInterlaceProcessing"
            )
            is_current_timeline_drop_frame = current_timeline.GetSetting(
                "timelineDropFrameTimecode"
            )

            if not markers:
                self.message_window("Info", "There are no markers on the timeline.")

            # check if it is drop frame
            if is_current_timeline_drop_frame == "0":
                drop_frame = False
            else:
                drop_frame = True

            # initialize frame to tc converter
            frm_to_tc = SMPTE()
            if fps == 23:
                fps = 23.98
            elif fps == 29:
                fps = 29.97
            elif fps == 59:
                fps = 59.94

            frm_to_tc.fps = fps
            frm_to_tc.df = drop_frame

            #  when timeline is progressive
            if is_current_timeline_interlace == "0":
                for key in markers:
                    markers[key]["TC"] = int(key)
                    marker_tc = markers[key]["TC"]
                    marker_name = markers[key]["name"]
                    marker_color = markers[key]["color"]
                    # export all timeline markers
                    if self.cb_markers.currentText() == "- ALL MARKERS -":
                        print("Export Still from all marker colors")
                        marker_tc_frm = frm_to_tc.gettc(marker_tc + offset)
                        go_to_frame = current_timeline.SetCurrentTimecode(marker_tc_frm)
                        # replace ":" and ";" in file name to "-"
                        marker_tc_frm_formated = marker_tc_frm.replace(
                            ":", "-"
                        ).replace(";", "-")
                        clip_name = self.return_current_clip_name()
                        current_project.ExportCurrentFrameAsStill(
                            f"{export_path}/{clip_name[:-4]}_TC_{marker_tc_frm_formated}_{marker_name}_.{user_file_type}"
                        )
                    else:
                        # export selected timeline markers
                        if self.cb_markers.currentText() == marker_color:
                            print(
                                f"Export Still from {self.cb_markers.currentText()} marker"
                            )
                            marker_tc_frm = frm_to_tc.gettc(marker_tc + offset)
                            go_to_frame = current_timeline.SetCurrentTimecode(
                                marker_tc_frm
                            )
                            # replace ":" and ";" in file name to "-"
                            marker_tc_frm_formated = marker_tc_frm.replace(
                                ":", "-"
                            ).replace(";", "-")
                            clip_name = self.return_current_clip_name()
                            current_project.ExportCurrentFrameAsStill(
                                f"{export_path}/{clip_name[:-4]}_TC_{marker_tc_frm_formated}_{marker_name}_.{user_file_type}"
                            )
            else:
                # when timeline is interlaced
                for key in markers:
                    markers[key]["TC"] = int(key)
                    marker_tc = markers[key]["TC"]
                    marker_name = markers[key]["name"]
                    marker_color = markers[key]["color"]
                    # export all timeline markers
                    if self.cb_markers.currentText() == "- ALL MARKERS -":
                        print("Export Still from all marker colors")
                        marker_tc_frm = frm_to_tc.gettc(marker_tc + offset)
                        # fields to frame conversion and replace ":", ";" to "-" in file name
                        h = int(marker_tc_frm[:2])
                        m = int(marker_tc_frm[3:5])
                        s = int(marker_tc_frm[6:8])
                        f = int(marker_tc_frm[9:])
                        f = round(int(f) / 2)
                        f = "{:02d}".format(f)
                        marker_tc_frm_formated = f"{h}-{m}-{s}-{str(f)}"
                        go_to_frame = current_timeline.SetCurrentTimecode(marker_tc_frm)
                        clip_name = self.return_current_clip_name()
                        current_project.ExportCurrentFrameAsStill(
                            f"{export_path}/{clip_name[:-4]}_TC_{marker_tc_frm_formated}_{marker_name}_.{user_file_type}"
                        )

                    else:
                        # export selected timeline markers
                        if self.cb_markers.currentText() == marker_color:
                            print(
                                f"Export Still from {self.cb_markers.currentText()} marker"
                            )
                            marker_tc_frm = frm_to_tc.gettc(marker_tc + offset)
                            # fields to frame conversion and replace ":", ";" to "-" in file name
                            h = int(marker_tc_frm[:2])
                            m = int(marker_tc_frm[3:5])
                            s = int(marker_tc_frm[6:8])
                            f = int(marker_tc_frm[9:])
                            f = round(int(f) / 2)
                            f = "{:02d}".format(f)
                            marker_tc_frm_formated = f"{h}-{m}-{s}-{str(f)}"
                            go_to_frame = current_timeline.SetCurrentTimecode(
                                marker_tc_frm
                            )
                            clip_name = self.return_current_clip_name()
                            current_project.ExportCurrentFrameAsStill(
                                f"{export_path}/{clip_name[:-4]}_TC_{marker_tc_frm_formated}_{marker_name}_.{user_file_type}"
                            )
            markers.clear()
        except Exception as e:
            self.message_window("Error", f"{e}")
            return

    # ------------------------------------- REVEALE FILE ------------------------------------------------ --------

    def reveal_file(self, user_folder_path):
        """
        After file export reaveal file.
        """
        if sys.platform == "win32":
            path = os.path.realpath(user_folder_path)
            os.startfile(path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            path = os.path.realpath(user_folder_path)
            subprocess.call([opener, path])

    # -------------------------------------- MESSAGE BOX POPUP WINDOW -----------------------------
    def message_window(self, info_1, info_2):
        QMessageBox.information(self, str(info_1), str(info_2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = MainProgramClass()
    # mp.resize(450, 600)
    # mp.move(100, 100)
    mp.show()
    app.exec()
