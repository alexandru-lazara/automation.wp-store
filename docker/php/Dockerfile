
FROM php:8.2.5-fpm

# System dependencies
RUN apt-get update && apt-get install -y \
    curl \
    zlib1g-dev \
    libpng-dev \
    libzip-dev \
    libicu-dev \
    libmagickwand-dev

# PHP extensions
RUN docker-php-ext-configure gd &&  \
    docker-php-ext-install gd mysqli exif zip intl &&  \
    pecl install imagick &&  \
    docker-php-ext-enable imagick
