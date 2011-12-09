AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/local/bin'
CC = ['/usr/bin/gcc']
CCLNK_SRC_F = ''
CCLNK_TGT_F = ['-o', '']
CC_NAME = 'gcc'
CC_SRC_F = ''
CC_TGT_F = ['-c', '-o', '']
CC_VERSION = ('4', '6', '2')
CFLAGS_CAIRO = ['-pthread']
CFLAGS_GDK = ['-pthread', '-pthread']
CFLAGS_GEE = ['-pthread', '-pthread']
CFLAGS_GOBJECT = ['-pthread', '-pthread']
CFLAGS_GTHREAD = ['-pthread', '-pthread']
CFLAGS_GTK+ = ['-pthread', '-pthread']
CFLAGS_INDICATOR = ['-pthread', '-pthread']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_UNIQUE = ['-pthread', '-pthread']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
CPPPATH_ST = '-I%s'
CXXFLAGS_CAIRO = ['-pthread']
CXXFLAGS_GDK = ['-pthread', '-pthread']
CXXFLAGS_GEE = ['-pthread', '-pthread']
CXXFLAGS_GOBJECT = ['-pthread', '-pthread']
CXXFLAGS_GTHREAD = ['-pthread', '-pthread']
CXXFLAGS_GTK+ = ['-pthread', '-pthread']
CXXFLAGS_INDICATOR = ['-pthread', '-pthread']
CXXFLAGS_UNIQUE = ['-pthread', '-pthread']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['HAVE_GOBJECT=1', 'HAVE_GTHREAD=1', 'HAVE_GLIB=1', 'HAVE_GTK_=1', 'HAVE_CAIRO=1', 'HAVE_GDK=1', 'HAVE_INDICATOR=1', 'HAVE_GEE=1', 'HAVE_UNIQUE=1', 'GETTEXT_PACKAGE="wingpanel"']
DEFINES_GTK+ = ['GSEAL_ENABLE']
DEFINES_INDICATOR = ['GSEAL_ENABLE']
DEFINES_ST = '-D%s'
DEFINES_UNIQUE = ['GSEAL_ENABLE']
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc/wingpanel'
DVIDIR = '/usr/local/share/doc/wingpanel'
EXEC_PREFIX = '/usr/local'
HAVE_CAIRO = 1
HAVE_GDK = 1
HAVE_GEE = 1
HAVE_GLIB = 1
HAVE_GOBJECT = 1
HAVE_GTHREAD = 1
HAVE_GTK_ = 1
HAVE_INDICATOR = 1
HAVE_UNIQUE = 1
HTMLDIR = '/usr/local/share/doc/wingpanel'
INCLUDEDIR = '/usr/local/include'
INCLUDES_CAIRO = ['/usr/include/cairo', '/usr/include/glib-2.0', '/usr/lib/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng14']
INCLUDES_GDK = ['/usr/include/gtk-3.0', '/usr/include/pango-1.0', '/usr/include/gdk-pixbuf-2.0', '/usr/include/cairo', '/usr/include/glib-2.0', '/usr/lib/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng14']
INCLUDES_GEE = ['/usr/include/gee-1.0', '/usr/include/glib-2.0', '/usr/lib/glib-2.0/include']
INCLUDES_GLIB = ['/usr/include/glib-2.0', '/usr/lib/glib-2.0/include']
INCLUDES_GOBJECT = ['/usr/include/glib-2.0', '/usr/lib/glib-2.0/include']
INCLUDES_GTHREAD = ['/usr/include/glib-2.0', '/usr/lib/glib-2.0/include']
INCLUDES_GTK+ = ['/usr/include/gtk-3.0', '/usr/include/atk-1.0', '/usr/include/cairo', '/usr/include/gdk-pixbuf-2.0', '/usr/include/pango-1.0', '/usr/include/glib-2.0', '/usr/lib/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng14']
INCLUDES_INDICATOR = ['/usr/include/libindicator-0.4', '/usr/include/gtk-3.0', '/usr/include/atk-1.0', '/usr/include/cairo', '/usr/include/gdk-pixbuf-2.0', '/usr/include/pango-1.0', '/usr/include/glib-2.0', '/usr/lib/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng14']
INCLUDES_UNIQUE = ['/usr/include/unique-3.0', '/usr/include/gtk-3.0', '/usr/include/atk-1.0', '/usr/include/cairo', '/usr/include/gdk-pixbuf-2.0', '/usr/include/pango-1.0', '/usr/include/glib-2.0', '/usr/lib/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng14']
INFODIR = '/usr/local/share/info'
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_ST = '-L%s'
LIB_CAIRO = ['cairo']
LIB_GDK = ['gdk-3', 'pangocairo-1.0', 'gdk_pixbuf-2.0', 'cairo-gobject', 'pango-1.0', 'gmodule-2.0', 'cairo', 'gobject-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LIB_GEE = ['gee', 'gobject-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LIB_GLIB = ['glib-2.0']
LIB_GOBJECT = ['gobject-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LIB_GTHREAD = ['gthread-2.0', 'rt', 'glib-2.0']
LIB_GTK+ = ['gtk-3', 'gdk-3', 'atk-1.0', 'gio-2.0', 'pangoft2-1.0', 'pangocairo-1.0', 'gdk_pixbuf-2.0', 'cairo-gobject', 'cairo', 'pango-1.0', 'freetype', 'fontconfig', 'gobject-2.0', 'gmodule-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LIB_INDICATOR = ['indicator3', 'gtk-3', 'gdk-3', 'atk-1.0', 'gio-2.0', 'pangoft2-1.0', 'pangocairo-1.0', 'gdk_pixbuf-2.0', 'cairo-gobject', 'cairo', 'pango-1.0', 'freetype', 'fontconfig', 'gobject-2.0', 'gmodule-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LIB_ST = '-l%s'
LIB_UNIQUE = ['unique-3.0', 'gtk-3', 'gdk-3', 'atk-1.0', 'gio-2.0', 'pangoft2-1.0', 'pangocairo-1.0', 'gdk_pixbuf-2.0', 'cairo-gobject', 'cairo', 'pango-1.0', 'freetype', 'fontconfig', 'gobject-2.0', 'gmodule-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LINKFLAGS_CAIRO = ['-pthread']
LINKFLAGS_GDK = ['-pthread', '-pthread']
LINKFLAGS_GEE = ['-pthread', '-pthread']
LINKFLAGS_GOBJECT = ['-pthread', '-pthread']
LINKFLAGS_GTHREAD = ['-pthread', '-pthread']
LINKFLAGS_GTK+ = ['-pthread', '-pthread']
LINKFLAGS_INDICATOR = ['-pthread', '-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_UNIQUE = ['-pthread', '-pthread']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'wingpanel'
PDFDIR = '/usr/local/share/doc/wingpanel'
PKGCONFIG = '/usr/bin/pkg-config'
PREFIX = '/usr/local'
PSDIR = '/usr/local/share/doc/wingpanel'
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SYSCONFDIR = '/usr/local/etc'
VALAC = '/usr/bin/valac'
VALAC_VERSION = (0, 14, 1)
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_GOBJECT', 'HAVE_GTHREAD', 'HAVE_GLIB', 'HAVE_GTK_', 'HAVE_CAIRO', 'HAVE_GDK', 'HAVE_INDICATOR', 'HAVE_GEE', 'HAVE_UNIQUE', 'GETTEXT_PACKAGE']
macbundle_PATTERN = '%s.bundle'