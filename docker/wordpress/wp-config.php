<?php
/** Enable W3 Total Cache */
define('WP_CACHE', true); // Added by W3 Total Cache

/** Database settings. */
define( 'DB_NAME',          'wordpress');
define( 'DB_USER', 			'wordpress');
define( 'DB_PASSWORD', 		'wordpress');
define( 'DB_HOST', 			'mysql:3306');
define( 'DB_CHARSET', 		'utf8');
define( 'DB_COLLATE', 		'') ;

/** Redis settings. */
define('WP_REDIS_HOST',     'redis');
define('WP_REDIS_PORT',     '6379');


/** Authentication unique keys and salts. */
/** https://api.wordpress.org/secret-key/1.1/salt/ */
define('AUTH_KEY',         	'{He$?%v?Q`?a[*o{F^tMmv/aAx,KO-|jch6n!GpC@-hP}2pk{@tTY|<Z/Sm,j)Fq');
define('SECURE_AUTH_KEY',  	'Isuk/0!*DUXpA}su7cnPvQ ? ?pP{O<P`O+lD#s6Y`W^WLD=o+X!Po|ut]t]fX|0');
define('LOGGED_IN_KEY',    	'kemtUr<|:>D|v+zD4_!RP(nvrgCv/=6)<|SbJV%&2a|Co53c7q<&e2!Xp!z|Mb72');
define('NONCE_KEY',        	'm`j:-#SgQ%-[<&>;#M-.Kjs7qA#]|f:|s&t@2I~<$1vtn+|.k Wqq_|3S9}b]Y90');
define('AUTH_SALT',        	'mz|$)vDk+}M^-@lR2mNK~x@r}zagK?WHTW*r6rt43@;a+L662hh[z26#~gatw|_I');
define('SECURE_AUTH_SALT', 	'xWfRB>t8I>RTYau=&|,>BvxA<DJ5$t9*~bsi1akJ.k{Y1sPOjj++y80-YjOh:*Ww');
define('LOGGED_IN_SALT',   	'i%$+>Uq:r1AS e!<g}5j]cc*~6C-|JgEx4]`D7yttfBAGOQ`?vx7/l+]Y<R-b@rR');
define('NONCE_SALT',       	')Vk&|NBh_ +dfXSzhze`<p~bsqT8~[aPS{@n[~=jrI=DRtn W0!xDqhiSl8yeoU%');


/** For developers: WordPress debugging mode. */
define( 'WP_DEBUG', 		'');

/** WordPress database table prefix. */
$table_prefix = 'wp_';

/** Alert WordPress about using a proxy server and HTTPS */
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false) {
	$_SERVER['HTTPS'] = 'on';
}

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
