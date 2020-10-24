import os
import time

from django.core.management.base import BaseCommand, CommandError
import sass
from django_sass import compile_sass, find_static_paths, find_static_scss
from django.conf import settings
import  dukpy


class Command(BaseCommand):
    help = "Runs libsass including all paths from SASS_FILES & JS_FILES."


    def handle(self, *arg, **options):
        dirs = find_static_paths()
        self.stdout.write("Writing static...")

        try:
            watchfiles = {}
            while True:
                needs_updated = False

                for fullpath in find_static_scss():
                    prev_mtime = watchfiles.get(fullpath, 0)
                    curr_mtime = os.stat(fullpath).st_mtime
                    if curr_mtime > prev_mtime:
                        needs_updated = True
                        watchfiles.update({fullpath: curr_mtime})

                if needs_updated:
                    try:
                        for path_in, path_out in settings.SASS_FILES:
                            compile_sass(
                                inpath=path_in,
                                outpath=path_out,
                                output_style="compressed",
                                precision=8,
                                source_map=True,
                                include_paths=dirs
                            )
                            self.stdout.write(f"compile sass: {path_in} > {path_out}")
                        for path_in, path_out in settings.JS_FILES:
                            dukpy.babel_compile()
                        self.stdout.write("Updated files at %s" % time.time())
                    except sass.CompileError as exc:
                        self.stdout.write(str(exc))

                time.sleep(3)

        except (KeyboardInterrupt, InterruptedError):
            self.stdout.write("Bye.")
            sys.exit(0)
