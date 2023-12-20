
FROM wordpress:6.4.2-fpm

ADD wp-content.tar.gz /var/www/html
RUN chown -R www-data:www-data /var/www/html/wp-content

RUN rm /usr/src/wordpress/wp-content/plugins/hello.php
RUN rm -rf /usr/src/wordpress/wp-content/plugins/akismet

RUN rm -rf /var/www/html/wp-content/themes/twentytwentyone
RUN rm -rf /usr/src/wordpress/wp-content/themes/twentytwentytwo
RUN rm -rf /usr/src/wordpress/wp-content/themes/twentytwentythree
RUN rm -rf /usr/src/wordpress/wp-content/themes/twentytwentyfour
