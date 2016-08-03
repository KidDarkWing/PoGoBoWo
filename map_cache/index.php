<?

	$apikey = '__REPLACE_YOUR_GOOGLE_DIRECTIONS_APIKEY__';

	$cache = $_GET;
	unset($cache['key']);
	
	$request = 'https://maps.googleapis.com/maps/'.$_GET['r'];
	$cache_name = '';

	$sep = '?';
	foreach ($cache as $k=>$v) {
		if (!$v) unset($cache[$k]);
		if ($k!='r') {
			$request .= $sep.''.urlencode($k).'='.urlencode($v);
			$sep = '&';
		}
	}

	ksort($cache);
	$sep = '';
	foreach ($cache as $k=>$v) {
		$v = str_replace('/','_',$v);
		$cache_name .= $sep.''.$k.'-'.$v;
		$sep = '-';
	}
	

	$f = 'cache/'.$cache_name.'.json';
	
	$request .= '&key='.$apikey;

	$debug = 0;
	if ($debug) {
		echo '<pre>';
		echo $request."\n";
		echo $cache_name."\n";
		echo $f."\n";
		print_r($cache);
		exit;
	}
	

	if (file_exists($f)) {
		header('Content-Type: application/json; charset=UTF-8');
		readfile($f);
		exit;
	}
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $request);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$output = curl_exec($ch);
	curl_close ($ch);
	
	file_put_contents($f, $output);
	header('Content-Type: application/json; charset=UTF-8');
	echo $output;
	exit;

