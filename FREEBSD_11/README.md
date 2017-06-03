#PREPARATION

* A 'media' user and group need to be added to '/usr/ports/UIDs' and '/usr/ports/GIDs' before compiling Ports or PBIs.

    - /usr/ports/UIDs
        - <code>media:*:816:816::0:0:media Daemon:/nonexistent:/usr/sbin/nologin</code>
        - <code>sync:*:817:817::0:0:sync Daemon:/nonexistent:/usr/sbin/nologin</code>
    - /usr/ports/GIDs
        - <code>media:*:816:</code>
        - <code>sync:*:817:</code>
* Make
    - <code>make **NAME**</code>
