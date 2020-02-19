<?php


$k="80e32263";
$kh="6f8af44abea0";
$kf="351039f4a7b5";
$p="0UlYyJHG87EJqEz6";

	function x($t,$k){
		$c=strlen($k);
		$l=strlen($t);
		$o="";
		for($i=0;$i<$l;){
			for($j=0;($j<$c&&$i<$l);$j++,$i++)
					{
						$o.=$t{$i}^$k{$j};
					}
				}
		return $o;
	}

	if(preg_match("/$kh(.+)$kf/",file_get_contents("./file.txt"),$m)==1){
		
		eval('$o = gzuncompress(@x(@base64_decode($m[1]),$k));');
		
		#print($o);

		$r=base64_encode(x(gzcompress($o),$k));
		print($r);
		#print("$p$kh$r$kf");
}



?>