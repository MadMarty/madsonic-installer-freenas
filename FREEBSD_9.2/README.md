FreeNAS Build System
====================

This page is constantly being edited and worked on. 


ToC
--------
+ [Setup](#setup)
+ [Dependencies](#dependencies)


## Compiling
Instructions for a clean FreeBSD image:

**Basic setup<a name="#setup">**
```
install FreeBSD 9.2 with ZFS into virtual-machine (VMWare)
Setup optional components

* doc
* lib32
* ports
* src
```

**Dependencies<a name="#dependencies">**
```
#below steps might not be necessary

echo "media:*:816:816::0:0:media Daemon:/nonexistent:/usr/sbin/nologin" >> /usr/ports/UIDs
echo "syncthing:*:817:817::0:0:syncthing daemon:/nonexistent:/usr/sbin/nologin" >> /usr/ports/UIDs
echo "media:*:816:" >> /usr/ports/GIDs
echo "syncthing:*:817:" >> /usr/ports/GIDs
```

**Compile<a name="#compile">**

<code>pbi_makeport -c ./plugins/madsonic -o ./pbi --pkgdir ./pkg www/madsonic-standalone</code>
