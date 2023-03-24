from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import cv2
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        layout= MDBoxLayout(orientation='vertical')
        self.image=Image(source="img.jpg")
        self.label= MDLabel()
        layout.add_widget(self.image)
        layout.add_widget(self.label)
        self.save_img_button = MDRaisedButton(
            text="CLICK HERE",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None))
        self.save_img_button.bind(on_press=self.remove_watermark)
        layout.add_widget(self.save_img_button)
        return layout
    def remove_watermark(self,*args):
        src = cv2.imread(self.image.source)
        mask = cv2.imread("wm.jpg", cv2.IMREAD_GRAYSCALE)
        (h, w, _) = src.shape
        mask = cv2.resize(mask, (w, h))
        dest=cv2.inpaint(src, mask, 1, cv2.INPAINT_NS)
        buffer = cv2.flip(dest, 0).tostring()
        texture = Texture.create(size=(dest.shape[1], dest.shape[0]))
        texture.blit_buffer(buffer, bufferfmt='ubyte')
        self.image.texture = texture

if __name__=="__main__":
    MainApp().run()