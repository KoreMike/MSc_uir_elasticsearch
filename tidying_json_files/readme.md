###exporting and tidying staff index

Open terminal and run 'curl-solr-export-staff.txt'

Convert resulting json file to newline format as per 'convert_json_to_newline.txt'

Then run 'delete-staff-duplicates.py'

Use notepad++ to find and replace all instances of metatag.Staff and Job.Title with JobTitle

The resulting json file is then cleaned and deduplicated and ready for import

###importing index

In order to run the script to load index to Elasticsearch,
make sure node is installed (https://goo.gl/PiVMtB)

Then run "npm install elasticsearch" to get the JavaScript Elasticsearch library

You can use "node" command to run the import script (load_articles_to_es.js or load_staff_to_es.js)
