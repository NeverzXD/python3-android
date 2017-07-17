from ..source import URLSource
from ..package import Package
from ..util import target_arch


class Expat(Package):
    source = URLSource('https://sourceforge.net/projects/expat/files/expat/2.2.2/expat-2.2.2.tar.bz2')

    def prepare(self):
        self.run_with_env([
            './configure',
            '--prefix=/usr',
            '--host=' + target_arch().ANDROID_TARGET,
            '--disable-shared',
        ])

    def build(self):
        self.run(['make'])
        self.run(['make', 'install', f'DESTDIR={self.DESTDIR}'])
