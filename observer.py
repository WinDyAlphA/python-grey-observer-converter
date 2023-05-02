import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image

class MonHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Afficher le nom du fichier ajouté
        print("Le fichier {} a été ajouté au dossier.".format(event.src_path))
        if event.src_path.endswith("_grey.jpg"):
            print('no need to convert')
        else:
            with open(event.src_path, "rb") as imageFile:
                f = imageFile.read()
                b = bytearray(f)
            im = Image.open(event.src_path)
            im = im.convert("L")
            im.save(event.src_path.replace(".jpg", "_grey.jpg"))

def surveiller_dossier():
    event_handler = MonHandler()
    observer = Observer()
    observer.schedule(event_handler, path='folder', recursive=False)
    observer.start()
    observer.join()

if __name__ == "__main__":
    surveiller_dossier()

