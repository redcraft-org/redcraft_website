import os
import time
import re

from django.core.management.base import BaseCommand, CommandError
import sass
from django_sass import compile_sass, find_static_paths, find_static_scss
from django.conf import settings

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Command(BaseCommand):
    help = "Runs libsass including all paths from SASS_FILES."

    def handle(self, *arg, **options):
        self.stdout.write("Watch static...")
        self.stdout.write("Watching :")

        sass_handler = sassHandler()
        observer = Observer()
        for path_in, path_out in settings.SASS_FILES:
            try:
                compile_sass(
                    inpath=path_in,
                    outpath=path_out,
                    output_style="expanded",
                    precision=8,
                    source_map=False
                ) 
                self.stdout.write(f'compile sass: {path_in} -> {path_out}')
            except sass.CompileError as exc:
                self.stdout.write(str(exc))

            observer.schedule(sass_handler, path_in, recursive=True)

        observer.start()
        try:
            while observer.is_alive():
                observer.join(1)
        except KeyboardInterrupt:
            observer.stop()
        self.stdout.write("Bye!")


class sassHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        time.sleep(0.5)
        path_in = re.findall(r'[a-z\/]*scss\/', event.src_path)[0]
        path_out = path_in.replace("scss", "css")

        try:
            compile_sass(
                inpath=path_in,
                outpath=path_out,
                output_style="expanded",
                precision=8,
                source_map=False
            )
            print(f"compile sass: {path_in} -> {path_out}")
        except sass.CompileError as exc:
            print(str(exc)) 
