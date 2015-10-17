# MSc_uir_elasticsearch

### Project Details

This project makes use of the elasticsearch autocomplete features detailed in the
following tutorial:

http://blog.qbox.io/multi-field-partial-word-autocomplete-in-elasticsearch-using-ngrams

And customises the calaca UI plugin to display results:

https://github.com/romansanchez/Calaca

#### Prerequisites

**jq json editor** with regex enabled by onigoroam library:

1. sudo apt-get install libonig-dev
2. Download and extract source tarball from https://stedolan.github.io/jq/download/
3. cd to extracted source folder
--* ./configure
--* make
--* sudo make install

**node.js**

https://goo.gl/PiVMtB

Then run "npm install elasticsearch" to get the JavaScript Elasticsearch library
