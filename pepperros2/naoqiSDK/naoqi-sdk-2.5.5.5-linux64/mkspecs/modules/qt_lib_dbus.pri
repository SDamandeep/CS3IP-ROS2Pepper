QT.dbus.VERSION = 5.4.1
QT.dbus.MAJOR_VERSION = 5
QT.dbus.MINOR_VERSION = 4
QT.dbus.PATCH_VERSION = 1
QT.dbus.name = QtDBus
QT.dbus.libs = $$QT_MODULE_LIB_BASE
QT.dbus.rpath = /usr/local/Qt-5.4.1/lib
QT.dbus.includes = $$QT_MODULE_INCLUDE_BASE $$QT_MODULE_INCLUDE_BASE/QtDBus
QT.dbus.bins = $$QT_MODULE_BIN_BASE
QT.dbus.libexecs = $$QT_MODULE_LIBEXEC_BASE
QT.dbus.plugins = $$QT_MODULE_PLUGIN_BASE
QT.dbus.imports = $$QT_MODULE_IMPORT_BASE
QT.dbus.qml = $$QT_MODULE_QML_BASE
QT.dbus.depends = core
QT.dbus.module_config =
QT.dbus.CONFIG = dbusadaptors dbusinterfaces
QT.dbus.DEFINES = QT_DBUS_LIB
QT_MODULES += dbus
