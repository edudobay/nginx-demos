<?php
declare(strict_types=1);

header("content-type: application/json");
echo json_encode([
    'status' => 'ok',
    'lang' => 'php',
    'uri' => $_SERVER['REQUEST_URI'],
    'server_vars' => $_SERVER,
]);
