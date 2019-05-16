#!/usr/bin/expect

set ip [lindex $argv 0]

spawn ssh root@127.0.0.$ip

expect {
"*yes/no" { send "yes\r"; exp_continue}
"*password:" { send "sunmap\r" }
}
interact
