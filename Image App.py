from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from PIL import Image as PILImage

class ImageManipulator(App):
    def __init__(self, **kwargs):
        super(ImageManipulator, self).__init__(**kwargs)    
        self.image = Image()
        self.selected_image_path = ""


    def build(self):
        layout = BoxLayout(orientation='vertical')
    
        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.load_image)
        layout.add_widget(file_chooser)
        
        button_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        crop_button = Button(text='Crop', on_press=self.show_crop_popup)
        resize_button = Button(text='Resize', on_press=self.show_resize_popup)
        filter_button = Button(text='Apply Filter', on_press=self.apply_filter)
        button_box.add_widget(crop_button)
        button_box.add_widget(resize_button)
        button_box.add_widget(filter_button)
        layout.add_widget(button_box)
        
        layout.add_widget(self.image)
        
        return layout
    
    def load_image(self, chooser, file_path, *args):
        self.selected_image_path = file_path[0]
        self.image.source = self.selected_image_path
        
    def crop_image(self, x1, y1, x2, y2):
        if self.selected_image_path:
            img = PILImage.open(self.selected_image_path)
            img = img.crop((x1, y1, x2, y2))
            img.show()
    
    def show_crop_popup(self, instance):
        if self.selected_image_path:
            content = BoxLayout(orientation='vertical')
            x1_input = TextInput(hint_text='X1')
            y1_input = TextInput(hint_text='Y1')
            x2_input = TextInput(hint_text='X2')
            y2_input = TextInput(hint_text='Y2')
            apply_button = Button(text='Apply', on_press=lambda x: self.crop_image(int(x1_input.text), int(y1_input.text), int(x2_input.text), int(y2_input.text)))
            cancel_button = Button(text='Cancel', on_press=lambda x: popup.dismiss())
            buttons_layout = BoxLayout(size_hint_y=None, height=50)
            buttons_layout.add_widget(apply_button)
            buttons_layout.add_widget(cancel_button)
            content.add_widget(x1_input)
            content.add_widget(y1_input)
            content.add_widget(x2_input)
            content.add_widget(y2_input)
            content.add_widget(buttons_layout)
            popup = Popup(title='Crop Image', content=content, size_hint=(None, None), size=(300, 250))
            popup.open()
    
    def show_resize_popup(self, instance):
        if self.selected_image_path:
            content = BoxLayout(orientation='vertical')
            width_input = TextInput(hint_text='Width')
            height_input = TextInput(hint_text='Height')
            apply_button = Button(text='Apply', on_press=lambda x: self.resize_image(width_input.text, height_input.text))
            cancel_button = Button(text='Cancel', on_press=lambda x: popup.dismiss())
            buttons_layout = BoxLayout(size_hint_y=None, height=50)
            buttons_layout.add_widget(apply_button)
            buttons_layout.add_widget(cancel_button)
            content.add_widget(width_input)
            content.add_widget(height_input)
            content.add_widget(buttons_layout)
            popup = Popup(title='Resize Image', content=content, size_hint=(None, None), size=(300, 200))
            popup.open()
    
    def resize_image(self, width, height):
        if self.selected_image_path:
            img = PILImage.open(self.selected_image_path)
            img = img.resize((int(width), int(height)))  
            img.show()
    
    def apply_filter(self, instance):
        if self.selected_image_path:
            img = PILImage.open(self.selected_image_path)
            img = img.convert('L')
            img.show()

if __name__ == '__main__':
    ImageManipulator().run()
