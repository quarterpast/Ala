#! /usr/bin/env python
# encoding: utf-8
# Copyright (c) 2010: GPL
# Author: SjB <steve@sagacity.ca>
#

VERSION = '0.0.1'
APPNAME = 'ala'

top = '.'
out = '_build_'

def options(opt):
    opt.load('compiler_c')
    opt.load('vala')

def configure(conf):
    conf.load('compiler_c vala')
    conf.check_vala(min_version=(0,10,0))

    conf.check_cfg(package = 'glib-2.0',
            uselib_store = 'GLIB',
            atleast_version = '2.22.0',
            mandatory = 1,
            args = '--cflags --libs')

    conf.check_cfg(package = 'gtk+-3.0',
            uselib_store = 'GTK+',
            atleast_version = '3.0',
            mandatory = 1,
            args = '--cflags --libs')

    conf.check_cfg(package = 'cairo',
            uselib_store = 'CAIRO',
            atleast_version = '1.10.0',
            mandatory = 1,
            args = '--cflags --libs')

    conf.check_cfg(package = 'gdk-3.0',
            uselib_store = 'GDK',
            atleast_version = '3.0',
            mandatory = 1,
            args = '--cflags --libs')

    conf.check_cfg(package = 'indicator3-0.4',
            uselib_store = 'INDICATOR',
            atleast_version = '0.4',
            mandatory = 1,
            args = '--cflags --libs')

    conf.check_cfg(package = 'gee-1.0',
            uselib_store = 'GEE',
            atleast_version = '0.5.3',
            args = '--cflags --libs')

    conf.check_cfg(package = 'unique-3.0',
            uselib_store = 'UNIQUE',
            atleast_version = '0.9',
            args = '--cflags --libs')

    conf.define ('GETTEXT_PACKAGE', APPNAME)

def build(bld):
    src = ['ala-panel.vala',
            'ala-config.vala',
            'ala-indicator-file-model.vala',
            'ala-object-entry.vala']

    task = bld.program(target = 'ala',
            packages = 'glib-2.0 gtk+-3.0 gdk-3.0 cairo gee-1.0 indicator ' \
                       'indicators-gtk unique-3.0',
            uselib = 'GLIB GTK+ GDK CAIRO GEE INDICATOR UNIQUE',
            source = src);
    task.vapi_dirs = ['.',]

