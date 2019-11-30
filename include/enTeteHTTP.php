<?php
function codeStatusHTTP($url)
{
	//Extraction de la ligne contenant le status
	$codeStatus = get_headers($url, 1)[0];

	//Elimination des autres informations (version HTTP, texte status)
	$codeStatus = preg_replace('#.+([0-9]{3}).*#', '$1', $codeStatus);
	return $codeStatus;
}

function tailleFichierDistant($url) {
	static $regex = '/^Content-Length: *+\K\d++$/im';
	if (!$fp = @fopen($url, 'rb')) {
		return false;
	}
	if (isset($http_response_header) && preg_match($regex, implode("\n", $http_response_header), $matches)) {
		return (int)$matches[0];
	}
	return strlen(stream_get_contents($fp));
}
?>
