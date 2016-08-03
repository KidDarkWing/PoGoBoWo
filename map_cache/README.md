Google Maps Geocoding/Directions caching
========

### Instructions
1. Install in /maps/ of your webserver
2. Edit /usr/local/lib/python2.7/dist-packages/gmaps/client.py and /usr/local/lib/python2.7/dist-packages/geopy/geocoders/googlev3.py
3. Set scheme to http (if you don't have SSL configured)
4. Set URL to your web server, for example http://127.0.0.1/maps/api/
5. Create a Google Maps Directions API key and activate it:
    1. Create it here: https://console.developers.google.com/projectselector/apis/credentials
    2. Then activate it here (select your project on the dropdown menu): https://console.developers.google.com/apis/api/directions_backend/overview?project=_
6. Then edit index.php and add your API key
7. Make cache directory writeable `chmod 0777 cache`
8. Enable AllowOverride All in your apache.conf
8. Install mod_rewrite `a2enmod mod_rewrite`
9. Restart apache `service apache2 restart`

