FreeNAS Build System
====================

This page is constantly being edited and worked on. 


ToC
--------
+ [setup](#setup)
+ [installation](#installation)
+ [updates](#updates)
+ [dependencies](#dependencies)
+ [build](#build)

# Compiling
Instructions for a clean FreeBSD image:


## basic setup<a name="#setup">
```
install FreeBSD 9.3 into virtual-machine (VMWare)
Setup optional components

* doc
* lib32
* ports
* src
```

## installation<a name="#installation">
```
freebsd-update fetch
freebsd-update install

portsnap fetch extract
portsnap fetch update
```

## packages<a name="#update">
```
cd /usr/ports/ports-mgmt/pkg/ 
make deinstall
make install clean

pkg2ng
pkg install bash nano git gcc subversion
```

## dependencies<a name="#dependencies">
```
cd /usr/ports/devel/xdg-utils
make && make install


git clone https://github.com/MadMarty/madsonic-installer-freenas.git
cd madsonic-installer-freenas/FREEBSD_9.3/src

cd libsh/
make && make install

cd ../pbi-wrapper
make && make install

cd ../pbi-manager
make && make install
```

## build<a name="#build">

* A 'media' user and group need to be added to '/usr/ports/UIDs' and '/usr/ports/GIDs' before compiling Ports or PBIs.

    - /usr/ports/UIDs
        - <code>media:*:816:816::0:0:media Daemon:/nonexistent:/usr/sbin/nologin</code>
        - <code>sync:*:817:817::0:0:sync Daemon:/nonexistent:/usr/sbin/nologin</code>
    - /usr/ports/GIDs
        - <code>media:*:816:</code>
        - <code>sync:*:817:</code>
		
* Make
	- <code>pbi_makeport -c ./plugins/madsonic -o ./pbi --pkgdir ./pkg/madsonic www/madsonic</code>
