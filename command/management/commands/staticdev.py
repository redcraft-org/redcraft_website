import os
import time

from django.core.management.base import BaseCommand, CommandError
import sass
from django_sass import compile_sass, find_static_paths, find_static_scss
from django.conf import settings

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Command(BaseCommand):
    help = "Runs libsass including all paths from SASS_FILES & JS_FILES."


    def handle(self, *arg, **options):
        sass_handler = sassHandler()
        observer = Observer()
        for path_in, path_out in settings.SASS_FILES:
            observer.schedule(sass_handler, path_in, recursive=True)        
        observer.start()

        self.stdout.write("Watch static...")
        self.stdout.write("Watching :")
        for path_in, path_out in settings.SASS_FILES:
            self.stdout.write(f'{path_in} -> {path_out}')

        try:
            while observer.is_alive():
                observer.join(1)
        except KeyboardInterrupt:
            observer.stop()
        self.stdout.write("Bye!")


class sassHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        time.sleep(0.5)
        dirs = find_static_paths()
        path_in = event.src_path
        path_out = event.src_path.replace("scss", "css")
        try:
            compile_sass(
                inpath=path_in,
                outpath=path_out,
                output_style="expanded",
                precision=8,
                source_map=True,
                include_paths=dirs
            )
            print(f"compile sass: {path_in} > {path_out}")
        except sass.CompileError as exc:
            print(str(exc)) 
