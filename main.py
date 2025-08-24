from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout,QVBoxLayout,QListWidget,QPushButton,QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
from PIL import Image,ImageFilter

class ImageHandler():
    def __init__(self):
        self.image=None
        self.dir=None
        self.filename=None
    def load_image(self,filename):
        self.filename=filename
        self.full_name=os.path.join(self.dir,filename)
        self.image=Image.open(self.full_name)
    def show_image(self):
        label.hide()
        pix_map=QPixmap(self.full_name)
        w=label.width()
        h=label.height()
        pix_map=pix_map.scaled(w,h,Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pix_map)
        label.show()
    def save_image(self):
        path=os.path.join(self.dir,'changed')
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.full_name=os.path.join(path,self.filename)
        self.image.save(self.full_name)
    def make_wb(self):
        self.image=self.image.convert('L')
        self.save_image()
        self.show_image()
    def turn_left(self):
        self.image=self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.show_image()
    def turn_right(self):
        self.image=self.image.transpose(Image.ROTATE_270)
        self.save_image()
        self.show_image()
    def make_mirror(self):
        self.image=self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        self.show_image()
    def make_sharp(self):
        self.image=self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        self.show_image()
image=ImageHandler()
app=QApplication(list())
window=QWidget()
window.show()
label=QLabel('картинка')
main_horizontal_layout=QHBoxLayout()
vertical_layout=QVBoxLayout()
button_vertical_layout=QVBoxLayout()
button_horizontal_layout=QHBoxLayout()
list_widdget=QListWidget()
folder_button=QPushButton('папка')
left_button=QPushButton('лево')
right_button=QPushButton('право')
mirror_button=QPushButton('зеркало')
sharpness_button=QPushButton('резкость')
wb_button=QPushButton('ч/б')
wb_button.clicked.connect(image.make_wb)
left_button.clicked.connect(image.turn_left)
right_button.clicked.connect(image.turn_right)
mirror_button.clicked.connect(image.make_mirror)
sharpness_button.clicked.connect(image.make_sharp)

window.setLayout(main_horizontal_layout)

main_horizontal_layout.addLayout(vertical_layout)
vertical_layout.addWidget(folder_button)
vertical_layout.addWidget(list_widdget)
main_horizontal_layout.addLayout(button_vertical_layout)
button_vertical_layout.addWidget(label)
button_vertical_layout.addLayout(button_horizontal_layout)

button_horizontal_layout.addWidget(left_button)
button_horizontal_layout.addWidget(right_button)
button_horizontal_layout.addWidget(mirror_button)
button_horizontal_layout.addWidget(sharpness_button)
button_horizontal_layout.addWidget(wb_button)


def get_files():
    extensions=['.png','.webp','.jpg','.jpeg']
    workdir=QFileDialog.getExistingDirectory()
    files=os.listdir(workdir)
    files=filter_files(files,extensions)
    list_widdget.addItems(files)
    image.dir=workdir

folder_button.clicked.connect(get_files)

def filter_files(files,extensions):
    filtered_files=list()
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                filtered_files.append(file)

                break
    return filtered_files

def show_chosen_image():
    filename=list_widdget.currentItem().text()
    image.load_image(filename)
    image.show_image()
list_widdget.itemClicked.connect(show_chosen_image)
app.exec()