import psutil
from debug_toolbar.panels import DebugPanel, Panel
import sys
import os,sys
import django
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

class SysInfo(Panel):
    title = _("Sys Info")
    template = "debug_toolbar/panels/sysInfo.html"
    @property
    def nav_title(self):
        """
        Title shown in the side bar. Defaults to :attr:`title`.
        """
        return self.title

    def generate_stats(self, request, response):
        process_data=[]
        for proc in psutil.process_iter():
            process=[]
            try:
                # Get process name & pid from process object.
                process.append(proc.pid)
                process.append(proc.name())
                process.append(proc.memory_info()[0])
                process.append(proc.memory_info()[1])
                process_data.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        self.record_stats(
            {"pid":os.getpid(),"path":sys.path,"process_data": process_data, "paths": sys.path}
        )
