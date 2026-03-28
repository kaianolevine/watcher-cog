# watcher-cog pipeline context

watcher-cog is the Drive trigger layer in the MiniAppPolis ecosystem.
It sits between Google Drive and Prefect Cloud.

## Where it fits

File appears in watched Drive folder
-> watcher-cog detects change (1-minute poll via Drive API)
-> watcher-cog calls Prefect API to create flow run
-> Prefect executes the target cog's flow

## What it does not do

watcher-cog does not process files. It only detects new files and
fires a trigger. All processing logic lives in the target cog's
Prefect flow.

## Watched folders

Configured in src/watcher_cog/config.py via the WATCHERS list.
Each WatcherConfig maps one Drive folder to one Prefect deployment.
