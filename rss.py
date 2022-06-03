<?php header('Content-type: application/rss+xml');
echo "<?phpxml version=\"1.0\" encoding=\"UTF-8\"?>\n"; ?>
<rss version="2.0"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	>
<channel>
<?php
	require_once("config.php");
	$title = mb_convert_encoding(linkpage_title,"UTF-8","auto");
	$linkpage_url = mb_convert_encoding(linkpage_url,"UTF-8","auto");
	$description = mb_convert_encoding(description,"UTF-8","auto");
?>
	<title><?php echo $title; ?></title>
	<link><?php  echo $linkpage_url; ?></link>
	<description><?php  echo $description; ?></description>
	<language>ja</language>
<?php
	$list_data = file(listfile);
	$cate_data = file(categoryfile);
	$i = 0;
	foreach ($list_data as $value) {
		if ($i >= rss_list) {
		    break;
		}
		list($l_cate_url,$url,$name,$caption,$time,$user_pass,$host) = explode(",",mb_convert_encoding($value,"UTF-8","auto"));
		    foreach ($cate_data as $value) {
			    list($cate_name_j,$cate_url,$cate_item) = explode(",",mb_convert_encoding($value,"UTF-8","auto"));
				if ($cate_url == $l_cate_url) { break; }
		    }
		$cate_url_guid = $cate_url;
		$caption = str_replace("<br />","", $caption);
		echo "<item>\n";
		echo "<title>".$name."</title>\n";
		echo "<link>".$linkpage_url.$cate_url."/</link>\n";
		echo "<category>".$cate_name_j."</category>\n";
		echo "<guid isPermaLink=\"false\">".$linkpage_url."index.php?mode=cate&amp;kt=".$cate_url_guid."</guid>\n";
		echo "<description>".$url.$caption."</description>\n";
		echo "</item>\n";
		$i++;
	}
?>
	</channel>
</rss>
