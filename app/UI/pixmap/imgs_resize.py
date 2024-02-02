from PIL import Image


class ImagesResize(object):

    def __init__(self, img_path: str, window_width: int, window_height: int):
        self.img_path = img_path
        self.window_width = window_width
        self.window_height = window_height
    

    def resize_image(self) -> tuple:

        with Image.open(self.img_path) as img:
            original_width, original_height = img.size
            aspect_ratio = original_width / original_height

            if original_width > original_height:
                new_width = self.window_width
                new_height = int(self.window_width / aspect_ratio)
            else:
                new_height = self.window_height
                new_width = int(self.window_height * aspect_ratio)

            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            sindex = self.img_path[::-1].find("/")

            resized_img.save(f"{self.img_path[:5]}resized{self.img_path[sindex:-4]}.jpg")
            
            return (f"{self.img_path[:5]}resized{self.img_path[sindex:-4]}.jpg", aspect_ratio)
