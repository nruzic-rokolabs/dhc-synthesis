#!/bin/bash

docker run --network host --rm -e ROOT_CONFLUENCE_URL=https://projectsynthesis.atlassian.net \
   -e SKIP_SSL_VERIFICATION=true \
   -e MAX_REQUESTS_PER_SECOND=10 \
   -e CONNECTION_TIME_TO_LIVE=500 \
   -e USERNAME=nikola.ruzic@rokolabs.com \
   -e PASSWORD=Lm!B!tbuck3tI@mN!k0l@ \
   -e SPACE_KEY=SD \
   -e ANCESTOR_ID=458774 \
   -e PAGE_TITLE_PREFIX="Draft - " \
   -e PAGE_TITLE_SUFFIX=" (V 1.0)" \
   -e PUBLISHING_STRATEGY=REPLACE_ANCESTOR \
   -e ORPHAN_REMOVAL_STRATEGY=KEEP_ORPHANS \
   -e VERSION_MESSAGE="V 1.0" \
   -e NOTIFY_WATCHERS=false \
   -e ATTRIBUTES='{"attribute1": "value1", "attribute2": "value2"}' \
   -e CONVERT_ONLY=false \
   -v /home/nruzic/var/playground/dhc/dhc-synthesis/dhc-synthesis-docs:/var/asciidoc-root-folder \
   confluencepublisher/confluence-publisher:0.0.0-SNAPSHOT
