exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MTA4IDE2MCAsIDE0ICwgZTUgLCAxYWYgLCAxMWYgLCAxNGEgLCAxMjIgLCAyMiAsIDFlICwgZDkgLCAyNyAsIDEyOSAsIGRkICwgZGEgLCBlYgoxMDggYjMgLiAxNmMgLiAxZCAxYWMgMWQKMTRkICggZTUgKQplNSAuIGQ2ICggJzEzNScgKQoxNmUgPSAiMTUzIgoxMmQgPSAxMjkgLiA1OCAoICkKMWEgYzUKMWFlID0gIjFiNT0iCjFhOCA9ICI2NyIKZmQgPSAiMzgiCjE4OCA9ICJlMiIKMTIxID0gIjVhPSIKMTUyID0gIjU2IgoxYWQgPSAiZjA9PSIKZjkgPSAiMTExPSIKZmEgPSAiZjM9PSIKMTE0ID0gIjI4IgojIDE2NSAxNjgKMTgzIDEwYSAoICkgOgoJMWEJMTYKCTFhCTU1CgkxYQk4ZgoJMWEJNTkKCTFhCWIwCgkxYQkzMgoJMWEJMTM3CgkxYQkzNwoJMWEJZWMKCTFhCTEwYwoJMWEJMjQKCTFhCTdhCgkxYQkxN2MKCTFhCWVlCgllYwk9CWI0CSgJMTcJKAkiMWIzPT0iCSkJKQoJZDMJPQkxMjkJLgkxOTAJKAkxNwkoCSI1MiIJKQkpCgkxYglkMQlkMwk6CgkJMTI5CS4JMjMJKAkpCgkJZDMJPQkxMjkJLgkxOTAJKAkxNwkoCSI1MiIJKQkpCgkxZgk9CTEyOQkuCTE5MAkoCTUJKAkiYWY9IgkpCSkKCTMyCT0JMTZhCSgJIjgyPT0iCSkKCTc2CT0JMTZhCSgJIjE0MT0iCSkKCWVlCT0JMTZhCSgJIjFiNT0iCSkKCTM3CT0JMTI5CS4JMTkwCSgJMTZhCSgJImY3PT0iCSkJKQoJMTdjCT0JMTI5CS4JMTkwCSgJMTZhCSgJImM4PSIJKQkpCgkxNgk9CTE3CSgJIjEwNSIJKQoJMTM3CT0JMWUJLgk5CS4JYQkoCTEyOQkuCTU4CSgJKQksCTE3CSgJImExIgkpCSwJNQkoCSIxODkiCSkJKQoJMTI5CS4JMmYJKAkxNgkrCTE3CSgJImU2PSIJKQkpCgk1NQk9CTE3CSgJIjJjLzM1IgkpCSUJKAkzMgksCTc2CSwJZDMJLAkxZgkpCgk4Zgk9CTUJKAkiMmMvMTI9IgkpCSUJKAkzMgksCTc2CSwJZDMJLAkxZgkpCgk1OQk9CTUJKAkiNDA9PSIJKQklCSgJMzIJLAk3NgksCWQzCSwJMWYJKQoJYjAJPQkxNwkoCSIyMD0iCSkKCTEwYwk9CTUJKAkiMmMvMTI9IgkpCSUJKAkzMgksCTc2CSwJZDMJLAkxZgkpCgk3YQk9CTUJKAkiNzAvN2Y9IgkpCSUJKAkzMgksCTc2CSwJZDMJLAkxZgkpCgkxYgkxNwkoCSJhYz0iCSkJZDEJOTIJYjYJKAkxMmQJKwkiLyIJKwkxNmEJKAkiNTYiCSkJKQkuCWMxCSgJKQk6CgkJNzkJKAkpCgkJMWIJMTAJLQkxMDoJNjgJKwkxNDIJLwkxNjQKCTQJPQkxMjkJLgkxMTkJKAkpCgkxYgk5NgktCTk2OgkxMTgJLQk1NAkuCTEzMAktCWVmCS8JMTViCSoJNzcKCTFiCTQJLgk2NgkoCSJjIgkpCTE1MQkxMDYJOgoJCWQyCSgJNAkpCgk2Ywk6CgkJMTc2CT0JNAkuCTY2CSgJImMiCSkKCQkxOTEJMTc2CSsJIig0KSIKCQkxYgk2NAktCTY0OgkxOGIJJQliNQoJMTI5CS4JZTcJKAkpCgkxYgk4OQktCTg5Ogk5YQktCWEwCSUJZDcKMTgzCWQyCSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwk1CSgJIjEwYiIJKQkrCTUzCSgJNAkpCSkKCTExYQkoCSkKCTFiCWQxCTMyCToKCQkxMjkJLgkyMwkoCSkKCTEwMgk9CWM1CSgJKQoJOWIJPQkoZGEuN2QoIiVkLyUxN2QvJTFhNyIpKQoJNDEJKAkpCgkxYgkxMDIJPT0JMQk6CgkJMTI5CS4JMmYJKAkxNgkrCTUJKAkiY2Y9PSIJKQkpCgkJMTI5CS4JMWI4CSgJYwk9CSJhYiIJLAkxNQk9CTUJKAkiZjY9PSIJKQksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImFlPT0iCSkJKQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAk1CSgJIjFiNT0iCSkJKQksCTExCT0JMzkJKQoJCTEyOQkuCTFiOAkoCWMJPQkiMTJjIgksCTE1CT0JNQkoCSIxMWQ9PSIJKQksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImNkPT0iCSkJKQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAk1CSgJIjFiNT0iCSkJKQksCTExCT0JMzkJKQoJCTEyOQkuCTFiOAkoCWMJPQkiYTciCSwJMTUJPQk1CSgJImM2IgkpCSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiZTAiCSkJKQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAk1CSgJIjFiNT0iCSkJKQksCTExCT0JMzkJKQoJCSMxMjkJLgkxYjgJKAljCT0JImJlIgksCTE1CT0JNQkoCSJhOT0iCSkJLAk3CT0JMWUJLgk5CS4JYQkoCTEzNwksCTE2YQkoCSJlPSIJKQkpCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCTUJKAkiMWI1PSIJKQkpCSwJMTEJPQkzOQkpCgkJMTI5CS4JMWI4CSgJYwk9CSJjZSIJLAkxNQk9CTUJKAkiZTg9IgkpCSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiYTg9PSIJKQkpCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCTUJKAkiMWI1PSIJKQkpCSwJMTEJPQkzOQkpCgkJMTI5CS4JMWI4CSgJYwk9CSJmNCIJLAkxNQk9CTUJKAkiMTBlPSIJKQksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImE2PSIJKQkpCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCTUJKAkiMWI1PSIJKQkpCSwJMTEJPQkzYwkpCgkJMTI5CS4JMTkyCSgJMTI5CS4JYjgJKQoJNmMJOgoJCTEyOQkuCTJmCSgJMTYJKwk1CSgJIjdiIgkpCSkKCQkxMjkJLgk4YgkoCTUJKAkiN2IiCSkJLAk1CSgJImIiCSkJJQkoCTE2CSkJKQoJCTEyOQkuCTIzCSgJKQoJCSNkMwk9CTEyOQkuCTE5MAkoCTE3CSgJIjUyIgkpCSkKCQkjMWYJPQkxMjkJLgkxOTAJKAk1CSgJImFmPSIJKQkpCgkJMTBhCSgJKQoJMWIJMTI5CS4JMTkwCSgJIjE0NiIJKQk9PQkiMTdmIgk6CgkJODQJPQliNwkuCWZiCSgJMTZhCSgJIjRiIgkpCSkKCQkxYglkMQkxZQkuCTkJLgkxNTAJKAk4NAkpCToKCQkJOWUJPQliNgkoCTFlCS4JOQkuCWEJKAkxMjkJLgk1OAkoCSkJLAk1CSgJImExIgkpCSwJMTZhCSgJIjE4MD0iCSkJKQkpCgkJCWEyCT0JOWUJLgljMQkoCSkKCQkJOWUJLgllNAkoCSkKCQkJOWUJPQliNgkoCTg0CSwJIjFiNyIJKQoJCQk5ZQkuCTE2OQkoCWEyCSkKCQkJOWUJLgllNAkoCSkKCQkJMTI5CS4JOGIJKAkxNgksCTE3CSgJIjRjPSIJKQkpCgkJCTFiCTkxCS0JOTE6CWM0CS8JZmYJKwk5ZAkuCTEyOAoJCQkxYgkyNQktCTI1Ogk2ZgkrCTdlCS8JNTQJLgljNAklCTc3CS4JYjUKMTgzCWY0CSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwkxNwkoCSJkOD09IgkpCSsJNTMJKAk0CSkJKQoJMTI5CS4JMjMJKAkpCgkxYgkxCS0JMToJMTI4CSUJNzcJKgljNAoxODMJMTJjCSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwkxNmEJKAkiZmMiCSkJKwk1MwkoCTQJKQkpCgkyOQk9CTE0CS4JNTEJKAk1NQksCTYzCT0JewkiNzIiCToJIjMwL2IzIgl9CSkKCTk0CT0JMTQJLgkzNgkoCTI5CSkKCTczCT0JMWQJLgk4NgkoCTk0CSkKCTJlCT0JNzMJLgk2MQkoCSkKCThlCTYJOTIJNzMJLgk2NQkoCTE2YQkoCSIzZj09IgkpCSkJOgoJCTEzCT0JNgkuCTMxCSgJMTcJKAkiMmE9IgkpCSkJLgkzMwoJCTEzCT0JMjcJLgkxOAkoCTEzCSkKCQkyMQk9CTYJLgkzMQkoCTUJKAkiMzQiCSkJKQkuCTMzCgkJMTI5CS4JMWI4CSgJYwk9CTE3CSgJIjExZT09IgkpCSwJMTUJPQkxMwksCTE4ZAk9CTIxCSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiZT0iCSkJKQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiNWE9IgkpCSkJLAkxMQk9CTM5CSkKCTEyOQkuCTE5MgkoCTEyOQkuCWI4CSkKCTFiCTQzCS0JNDM6CWVmCS0JOWQJKgkxNjQKMTgzCWE3CSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwk1CSgJIjEwMSIJKQkrCTUzCSgJNAkpCSkKCTI5CT0JMTQJLgk1MQkoCThmCSwJNjMJPQl7CSI3MiIJOgkiMzAvYjMiCX0JKQoJOTQJPQkxNAkuCTM2CSgJMjkJKQoJNzMJPQkxZAkuCTg2CSgJOTQJKQoJMmUJPQk3MwkuCTYxCSgJKQoJOGUJNgk5Mgk3MwkuCTY1CSgJMTZhCSgJIjNmPT0iCSkJKQk6CgkJMTc4CT0JNgkuCTMxCSgJMTcJKAkiMmE9IgkpCSkJLgkzMwoJCTFiCTE3OAk9PQkiMTgyIgk6CgkJCQkJMTMyCgkJMTc4CT0JMjcJLgkxOAkoCTE3OAkpCgkJMjEJPQk2CS4JMzEJKAk1CSgJIjM0IgkpCSkJLgkzMwoJCTFiCSIxNDciCTkyCTIxOgoJCQkJMTI5LjJmKCIxYTkJMTRjISIpCgkJCQkxMjkJLgkxYjgJKAljCT0JImEzIgksCTE1CT0JMTc4LAkxOGQJPQkyMQksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImU9IgkpCSkJLAkxOGEJPQkxZQkuCTkJLglhCSgJMTM3CSwJNQkoCSIxYjU9IgkpCSkJLAkxMQk9CTM5CSkJCgkJNmM6CQkKCQkJCTEyOQkuCTFiOAkoCWMJPQk1CSgJImMwPT0iCSkJLAkxNQk9CTE3OAksCTE4ZAk9CTIxCSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiZT0iCSkJKQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiNWE9IgkpCSkJLAkxMQk9CTM5CSkKCTEyOQkuCTE5MgkoCTEyOQkuCWI4CSkKCTFiCTgwCS0JODA6CWM0CSoJNjgJLwk2ZgoxODMJMTQzCSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwkxNmEJKAkiOTM9PSIJKQkrCTUzCSgJNAkpCSkKCTFiCTE3CSgJImFjPSIJKQlkMQk5MgliNgkoCTEyZAkrCSIvIgkrCTE2YQkoCSI1NiIJKQkpCS4JYzEJKAkpCToKCQk3OQkoCSkKCTFiCTM3CT09CSIxN2YiCToKCQkyNgk9CTQJLgk2NgkoCTE2YQkoCSIyYT0iCSkJKQoJCTUwCSgJMjYJKQoJMTkzCT0JNAkuCTY2CSgJMTcJKAkiN2MiCSkJKQoJMjkJPQkxNAkuCTUxCSgJMTkzCSwJNjMJPQl7CSI3MiIJOgkiMzAvYjMiCX0JKQoJOTQJPQkxNAkuCTM2CSgJMjkJKQoJNzMJPQkxZAkuCTg2CSgJOTQJKQoJMmUJPQk3MwkuCTYxCSgJKQoJOGUJNgk5Mgk3MwkuCTY1CSgJMTZhCSgJIjNmPT0iCSkJKQk6CgkJMTMJPQk2CS4JMzEJKAkxNwkoCSIyYT0iCSkJKQkuCTMzCgkJMTMJPQkyNwkuCTE4CSgJMTMJKQoJCTEzCT0JMTMJLgk0NgkoCSJbIgkpCgkJNDQJPQk2CS4JMzEJKAkxNwkoCSIxOGU9PSIJKQkpCS4JMzMKCQkxYwk9CTYJLgkzMQkoCTUJKAkiODg9PSIJKQkpCS4JMzMKCQk0OAk9CTEzCVsJMQldCSsJMTMJWwkyCV0KCQk0OAk9CTQ4CS4JNDYJKAkiXSIJKQoJCTQ4CT0JNDgJWwkyCV0KCQk0OAk9CTQ4CS4JNDYJKAkiMTlkIgkpCgkJMTI5LjJmKDQ4WzBdKyIJIisJNDhbMV0rIgkiKwk0OFsyXSkKCQk0OAk9CTQ4CVsJMgldCgkJZTkJPQkxNwkoCSIxOGM9IgkpCSUJKAkxMwlbCTAJXQkpCSsJNDgKCQlmCT0JNgkuCTMxCSgJMTZhCSgJIjg1PSIJKQkpCS4JMzMKCQkxYglmCToKCQkJZgk9CTI3CS4JMTgJKAlmCSkKCQkJOGMJPQlmCS4JNDYJKAkiKCIJKQoJCQk4Ywk9CTE2YQkoCSIxNDU9IgkpCSsJOGMJWwkwCV0KCQkJNDUJPQlmCS4JNDYJKAkiKVwxYjYiCSkKCQkJNDUJPQk0NQlbCTIJXQkuCTQ2CSgJIigiCSkKCQkJNDUJPQkxNmEJKAkiMTMzIgkpCSsJNDUJWwkwCV0KCQkJNmIJPQk4YwkrCTQ1CgkJNmMJOgoJCQk2Ygk9CSIiCgkJMWIJMTdjCT09CSIxN2YiOgoJCQk0NAk9CTQ0CS4xM2QoIi4xYWEiLCIuMTdiIikKCQkxYgkxYwk6CgkJCTFjCT0JMWMuMTZiKCkKCQkJMTI5CS4JMWI4CSgJYwk9CTE2YQkoCSJjMj09IgkpCSwJMTUJPQllOQksCTE4ZAk9CTQ0CSwJNwk9CTFjCSwJZGUJPQk2YgksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAk1CSgJIjM4IgkpCSkJLAliYQk9CSIiCSwJM2IJPQkzOQksCTExCT0JM2MJKQoJCTZjCToKCQkJMTI5CS4JMWI4CSgJYwk9CTE2YQkoCSJjMj09IgkpCSwJMTUJPQllOQksCTE4ZAk9CTQ0CSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiNjciCSkJKQksCWRlCT0JNmIJLAkxOGEJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJIjM4IgkpCSkJLAliYQk9CSIiCSwJM2IJPQkzOQksCTExCT0JM2MJKQoJIzEyOQkuCTE5MgkoCTEyOQkuCTEyYgkpCgliNwkuCTQyCSgJNQkoCSIyZD09IgkpCSkKCTFiCTk3CS0JOTc6CTdlCS0JZDcJKgk2OAkvCTE4YgklCTZmCS0JMTE4CjE4MwkxNDkJKAk0CSkJOgoJMTI5CS4JMmYJKAkxNgkrCTE3CSgJIjk4IgkpCSsJNTMJKAk0CSkJKQoJMWIJMzcJPT0JIjE3ZiIJOgoJCTI2CT0JNAkuCTY2CSgJMTZhCSgJIjJhPSIJKQkpCgkJNTAJKAkyNgkpCgk0YQk9CTQJLgk2NgkoCTE3CSgJIjdjIgkpCSkKCTI5CT0JMTQJLgk1MQkoCTRhCSwJNjMJPQl7CSI3MiIJOgkiMzAvYjMiCX0JKQoJOTQJPQkxNAkuCTM2CSgJMjkJKQoJNzMJPQkxZAkuCTg2CSgJOTQJKQoJMmUJPQk3MwkuCTYxCSgJKQoJOGUJNgk5Mgk3MwkuCTY1CSgJMTZhCSgJIjNmPT0iCSkJKQk6CgkJMjYJPQk2CS4JMzEJKAkxNwkoCSIyYT0iCSkJKQkuCTMzCgkJMjYJPQkyNwkuCTE4CSgJMjYJKQoJCTI2CT0JMjYJLgkxNWEJKAkiMWE0LTgiCSkKCQk0NAk9CTYJLgkzMQkoCTE2YQkoCSIxOGU9PSIJKQkpCS4JMzMKCQkxYwk9CTYJLgkzMQkoCTE2YQkoCSI4OD09IgkpCSkJLgkzMwoJCWYJPQk2CS4JMzEJKAk1CSgJIjg1PSIJKQkpCS4JMzMKCQkxYglmCToKCQkJZgk9CTI3CS4JMTgJKAlmCSkKCQkxYglmCTE1MQkxMDYJOgoJCQkJZgk9CSIiCgkJMWIJMWMJMTUxCWQxCTEwNgk6CgkJCTEyOQkuCTFiOAkoCWMJPQkiNzgiCSwJMTUJPQkyNgksCTE4ZAk9CTQ0CSwJNwk9CTFjCSwJZGUJPQlmCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCSIxNDguMTVkIgkpCSwJYmEJPQkiIgksCTNiCT0JMzkJLAkxMQk9CTNjCSkKCQk2Ywk6CgkJCTEyOQkuCTFiOAkoCWMJPQkiNzgiCSwJMTUJPQkyNgksCTE4ZAk9CTQ0CSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkiMTJhLjE1ZCIJKQksCWRlCT0JZgksCTE4YQk9CSIiCSwJYmEJPQkiIgksCTNiCT0JMzkJLAkxMQk9CTNjCSkKCTEyOQkuCTE5MgkoCTEyOQkuCTE0ZgkpCgliNwkuCTQyCSgJJzEyNS4xMGYoMTUzKScJKQoJMWIJMTkJLQkxOToJYTAJJQk1NAklCWI1CjE4MwliZQkoCTQJKQk6CgkxMjkJLgkyZgkoCTE2CSsJNQkoCSJhOT0iCSkJKwk1MwkoCTQJKQkpCgk0YQk9CTQJLgk2NgkoCTE3CSgJIjdjIgkpCSkKCSMjMTgxCTE5ZQkKCTI5CT0JMTQJLgk1MQkoCTRhCSwJNjMJPQl7CSI3MiIJOgkiMzAvYjMiCX0JKQoJOTQJPQkxNAkuCTM2CSgJMjkJKQoJNzMJPQkxZAkuCTg2CSgJOTQJKQoJMmUJPQk3MwkuCTYxCSgJKQoJYTQJPQkwCgk4ZQk2CTkyCTczCS4JNjUJKAkxNmEJKAkiM2Y9PSIJKQkpCToKCQkxNzgJPQk2CS4JMzEJKAkxNwkoCSIyYT0iCSkJKQkuCTMzCgkJMWIJMTc4CT09CSIxYjU9Igk6CgkJCWE0CT0JMQoJCQkxYQkyNAoJCQkyNAk9CTYJLgkzMQkoCTUJKAkiMzQiCSkJKQkuCTMzCgkJCWEzCSgJNAkpCgkJCTFiCTgzCS0JODM6CTlhCS8JN2UKCTFiCWE0CT09CTAJOgoJCTEyOQkuCThiCSgJMTYJLAkiMTZkCTFhMAkxYjIJMWIxCTE1NAkxMjYiCSkKCQkxYgk0OQktCTQ5OgliNQoxODMJYTMJKAk0CSkJOgoJMTI5CS4JMmYJKAkxNgkrCSIxYTUJMTRlCTE4NAkxNzIiCSsJNTMJKAk0CSkJKQoJMjQJPQk0CS4JNjYJKAkxNwkoCSI3YyIJKQkpCgkyOQk9CTE0CS4JNTEJKAkyNAksCTYzCT0JewkiNzIiCToJIjMwL2IzIgl9CSkKCTk0CT0JMTQJLgkzNgkoCTI5CSkKCTczCT0JMWQJLgk4NgkoCTk0CSkKCTJlCT0JNzMJLgk2MQkoCSkKCThlCTYJOTIJNzMJLgk2NQkoCTE2YQkoCSIzZj09IgkpCSkJOgoJCTE3OAk9CTYJLgkzMQkoCTE3CSgJIjJhPSIJKQkpCS4JMzMKCQkxNzgJPQkyNwkuCTE4CSgJMTc4CSkKCQkyMQk9CTYJLgkzMQkoCTUJKAkiMzQiCSkJKQkuCTMzCgkJMTI5CS4JMWI4CSgJYwk9CTUJKAkiYzA9PSIJKQksCTE1CT0JMTc4CSwJMThkCT0JMjEJLAk3CT0JMWUJLgk5CS4JYQkoCTEzNwksCTE2YQkoCSJlPSIJKQkpCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCTE2YQkoCSJmMT09IgkpCSkJLAkxMQk9CTM5CSkKCTEyOQkuCTE5MgkoCTEyOQkuCWI4CSkKMTgzCTQxCSgJKQk6CglkYwk9CWViCS4JMTk3CSgJYjYJKAkxMmQJKwkiLyIJKwkxNmEJKAkiNTYiCSkJLAknMWIwJwkpCS4JYzEJKAkpCSkJLgkxMjMJKAkpCgliYgk9CTUJKAkiNWQ9IgkpCgkxYgkoCWRjCSE9CWJiCSkJOgoJCWI5CSgJKQoxODMJMTQwCSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwkxNmEJKAkiMTA3IgkpCSsJNTMJKAk0CSkJKQoJMWIJMzcJPT0JIjE3ZiIJOgoJCTI2CT0JNAkuCTY2CSgJMTZhCSgJIjJhPSIJKQkpCgkJNTAJKAkyNgkpCgkzYQk9CTQJLgk2NgkoCTUJKAkiN2MiCSkJKQoJIzNhCT0JIjE3NDovLzE4Ny4xNWUuMTlmLzEyZi4xYTI/MTliPSIJKwkzYQoJMTI5LjJmKDNhKQoJMTI5CS4JNGUJKAkzYQkpCjE4MwkxNmEJKAk2MAkpCToKCTNkCT0JMjcJLgkxOAkoCTYwCSkKCTc1CTNkCjE4Mwk3OAkoCTQJKQk6CgkxMjkJLgkyZgkoCTE2CSsJMTcJKAkiMTA5IgkpCSsJNTMJKAk0CSkJKQoJMWIJMzcJPT0JIjE3ZiIJOgoJCTI2CT0JNAkuCTY2CSgJMTZhCSgJIjJhPSIJKQkpCgkJNTAJKAkyNgkpCgkzYQk9CTQJLgk2NgkoCTUJKAkiN2MiCSkJKQoJMTI5CS4JNGUJKAkzYQkpCjE4MwliOQkoCSkJOgoJMTI5CS4JMmYJKAk1CSgJIjY5IgkpCSkKCWU1CS4JYjkJKAkpCjE4Mwk3NAkoCSkJOgoJYzkJPQkxNAkuCTUxCSgJNTkJKQoJYzkJLgkxMTUJKAkxNmEJKAkiZjU9PSIJKQksCTUJKAkiMTc5PSIJKQkpCgliMQk9CTE0CS4JMzYJKAljOQkpCglkZgk9CWIxCS4JYzEJKAkpCgljYgk9CWQ5CS4JMTcwCSgJZGYJLgkxNWMJKAknMTM1JwkpCSkKCWIxCS4JZTQJKAkpCgkxYgljYgk6CgkJMTI5CS4JMmYJKAkxNgkrCTE2YQkoCSJkND09IgkpCSkKCQk3NQljYgoxODMJYzUJKAkpCToKCTlmCT0JNzQJKAkpCgk5NQk9CTlmCVsJMTZhCSgJImE1IgkpCV0KCWM1CT0JOTUJWwkxNwkoCSIxNTY9PSIJKQldCgk3NQljNQoxODMJMTcJKAk2MAkpCToKCTNkCT0JMjcJLgkxOAkoCTYwCSkKCTc1CTNkCgkxYgk4NwktCTg3Ogk3ZQkqCTE1YgklCTY4CSUJMThiCS0JZDcKMTgzCWFiCSgJNAkpCToKCTEyOQkuCTJmCSgJMTYJKwkxNwkoCSJhYT09IgkpCSsJNTMJKAk0CSkJKQoJZmUJPQk3NAkoCSkKCTVmCT0JZmUJWwkxNmEJKAkiYTUiCSkJXQoJZjgJPQk1ZglbCTE3CSgJIjEzNiIJKQldCgkzZQk9CTVmCVsJMTZhCSgJIjEwZD0iCSkJXQoJMWIJM2UJOgoJCTNlCT0JMjIJLgkyMgkuCTZlCSgJYjQJKAkzZQkpCSkJLgk3ZAkoCSclMWE2OiUxOWMJJWQuJTE3ZC4lMWE3JwkpCgk2Ywk6CgkJM2UJPQk1CSgJIjE0Yj0iCSkKCTRmCT0JNWYJWwk1CSgJIjExMj0iCSkJXQoJMWIJNGYJPT0JIjAiCToKCQk0Zgk9CTE2YQkoCSIxOTU9IgkpCgk2Ywk6CgkJNGYJPQkxNmEJKAkiMTc1IgkpCgk5Ywk9CTVmCVsJMTcJKAkiYmYiCSkJXQoJZTEJPQk1ZglbCTE2YQkoCSIxMTA9IgkpCV0KCTEyOQkuCTFiOAkoCWMJPQkiIgksCTE1CT0JMTZhCSgJIjcxPSIJKQkrCWUxCSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiZT0iCSkJKQkJLAkxOGEJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJIjFiNT0iCSkJKQksCTExCT0JM2MJKQoJMTI5CS4JMWI4CSgJYwk9CSIiCSwJMTUJPQkxNmEJKAkiNjI9PSIJKQkrCWY4CSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiZT0iCSkJKQkJLAkxOGEJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJIjFiNT0iCSkJKQksCTExCT0JM2MJKQoJMTI5CS4JMWI4CSgJYwk9CSIiCSwJMTUJPQkxNwkoCSI1ZT0iCSkJKwkzZQksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImU9IgkpCSkJCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCTE2YQkoCSIxYjU9IgkpCSkJLAkxMQk9CTNjCSkKCTEyOQkuCTFiOAkoCWMJPQkiIgksCTE1CT0JNQkoCSI0ZD0iCSkJKwk0ZgksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImU9IgkpCSkJCSwJMThhCT0JMWUJLgk5CS4JYQkoCTEzNwksCTE2YQkoCSIxYjU9IgkpCSkJLAkxMQk9CTNjCSkKCTEyOQkuCTFiOAkoCWMJPQkiIgksCTE1CT0JNQkoCSI0Nz09IgkpCSsJOWMJLAk3CT0JMWUJLgk5CS4JYQkoCTEzNwksCTE2YQkoCSJlPSIJKQkpCQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiMWI1PSIJKQkpCSwJMTEJPQkzYwkpCgkjMTI5CS4JMTkyCSgJMTI5CS4JYjgJKQoJYjcJLgk0MgkoCTUJKAkiMmQ9PSIJKQkpCjE4Mwk1MAkoCWRiCSkJOgoJMTI5CS4JMmYJKAkxNgkrCTE2YQkoCSJjNz0iCSkJKQoJMTdlCT0JJzE5OCcJLAknMTY2JwksCScxNTknCSwJJzE2ZicJLAknMTU1JwksCScxMTcnCSwJJzE2MycJLAknMTI3JwksCScxN2EnCSwJJzE4ZicJLAknMTI3JwksCScxYTEnCgkxYgkxOTkJKAkxYWIJOTIJZGIJOGUJMWFiCTkyCTE3ZQkpCToKCQliNwkuCTQyCSgJKAkxYjQnMTcxLjEwMCgiMTM5CTE4NSIsCSIxMmUJMTk2CTEzYgkxMTcJMTNlIiwJMTc3KScJKQkpCgkJMTFjCT0JMTI5CS4JZWQJKAkxMDQJPQkiIgksCTE1CT0JMTcJKAkiZDU9PSIJKQkpCgkJMWIJMTFjCT09CTEyOQkuCTE5MAkoCTE2YQkoCSJmMj09IgkpCSkJOgoJCQk3NQoJCTZjCToKCQkJYjkJKAkpCgk2Ywk6CgkJZGIJPQkiIgoxODMJNzkJKAkpCToKCTEyOQkuCThiCSgJMTcJKAkiMTNmPSIJKQksCTUJKAkiMjgiCSkJKQoJZTUJLgliOQkoCSkKMTgzCWNlCSgJNAkpCToKCSMxNGUJZWEJMTk0Cgk4YQk9CTE0CS4JMzYJKAk1OQkpCglhZAk9CWQ5CS4JMTM4CSgJOGEJKQoJOTkJPQlhZAlbCSdkMCcJXQoJOGUJNWIJOTIJOTkJLgkxNWYJKAkpCToKCQkxMDMJPQk1YglbCScxMTYnCV0KCQkxYgkoCTEwMwk9PQkxCSkJOgoJCQljMwk9CTViCVsJJ2RiJwldCgkJCTJiCT0JNWIJWwknY2EnCV0KCQkJMTI5CS4JMWI4CSgJYwk9CSIxMzQiCSwJMTUJPQljMwksCTE4ZAk9CTJiCSwJNwk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiZT0iCSkJKQksCTE4YQk9CTFlCS4JOQkuCWEJKAkxMzcJLAkxNmEJKAkiYmQ9PSIJKQkpCSwJM2IJPQkzYwksCTExCT0JMzkJKQoxODMJYmMJKAk0CSkJOgoJMTI5CS4JMmYJKAkxNgkrCSIJMTQ0IgkrCTUzCSgJNAkpCSkKCTQxCSgJKQoJOGQJPQk0CS4JNjYJKAk1CSgJIjdjIgkpCSkKCThkCT0JOGQJLgkxNjcJKAkiIyIJKQoJMmIJPQk4ZAlbCTAJXQoJODEJPQk4ZAlbCTEJXQoJM2EJPQk3YQkrCSImMTU3PSIJKwkyYgkrCSImMTNhPTEyMCIJKwkiJjExYj0iCSsJODEKCTEyOQkuCTJmCSgJIjEzMQkiCSsJM2EJKQoJMTI5CS4JNGUJKAkzYQkpCjE4MwkxMzQJKAk0CSkJOgoJIzE0ZQllYQkxNzMKCTJiCT0JNAkuCTY2CSgJNQkoCSI3YyIJKQkpCgkxOTMJPQk1OQkrCSImYz0xM2MmY2E9IgkrCTJiCgk4YQk9CTE0CS4JMzYJKAkxOTMJKQoJYTIJPQlkOQkuCTEzOAkoCThhCSkKCTExMwk9CTIyCS4JMjIJLgkxNjIJKAkpCS0JMjIJLgkxYTMJKAkxODYJPQkzCSkKCTZhCT0JZGQJLgkxNTgJKAkxMTMJLgkxMjQJKAkpCSkKCTZhCT0JYjQJKAk2YQkpCgk1Ywk9CWRhCS4JZGEJKAkpCgk1Ywk9CWI0CSgJNWMJKQoJOGUJYjIJOTIJYTIJOgoJCTU3CT0JYjIJWwknMTUnCV0KCQk1Nwk9CTI3CS4JMTgJKAk1NwkpCgkJZTMJPQliNAkoCWIyCVsJJzExYicJXQkpCgkJMWIJKAllMwk+CTZhCTE5YQllMwk8CTVjCSkJOgoJCQkxYgk5MAktCTkwOgliNQklCTU0CS8JNzcKCQkJMTYxCT0JMjIJLgkyMgkuCTZlCSgJYjQJKAllMwkpCSkJLgk3ZAkoCSclZC4lMTdkCSUxYTY6JTE5YycJKQoJCQljYwk9CTIyCS4JMjIJLgk2ZQkoCWI0CSgJZTMJKQkpCS4JN2QJKAknJTFhNy0lMTdkLSVkOiUxYTYtJTE5YycJKQoJCQk1Nwk9CTE2MQkrCSIJIgkrCTU3CgkJCThkCT0JMmIJKwkiIyIJKwljYwoJCQkxMjkJLgkxYjgJKAljCT0JImJjIgksCTE1CT0JNTcJLAkxOGQJPQk4ZAksCTcJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImU9IgkpCSkJLAkxOGEJPQkxZQkuCTkJLglhCSgJMTM3CSwJMTZhCSgJImJkPT0iCSkJKQksCTNiCT0JMzkJLAkxMQk9CTNjCSkKMTgzCTExYQkoCSkJOgoJNDEJKAkpCjE4Mwk1CSgJNjAJKQk6CgkzZAk9CTI3CS4JMTgJKAk2MAkpCgk3NQkzZAoxMGEJKAkpCSMJNmQ=")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|params|I1IiI|O0oooo0Oo00|thumbnail|8|path|join|UG9zc2libGUgcmVhc29uczogV3JvbmcgaG9zdCxwb3J0LHVzZXJuYW1lIG9yIHBhc3MuICAgICAgICAgIFBsZWFzZSByZWNvbmZpZ3VyZSAlcyBwbHVnaW4gd2l0aCBjb3JyZWN0IGRldGFpbHMh|action|d|bG9nby5wbmc|iiiiiIIii|10|folder|dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM|Ii11iii11I|urllib2|title|pnimi|O0O|b64decode|19|global|if|oOoOooOo0o0|ElementTree|os|I1ii11iIi11i|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9wb3dieGswZDBieDgxNzkva2luZ1ZlcnNpb24udHh0P2RsPTE|oOo00Oo00O|datetime|open_settings_dialog|tvkategoorialink|25|IIIII|base64|VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h|IiIiIi|dGl0bGU|IiIIIi1iIi|JXM6JXMvZW5pZ21hMi5waHA|Q29udGFpbmVyLlNldFZpZXdNb2RlKDU1KQ|iI11iiiI1II|log|application|find|lehekylg|text|cGxheWxpc3RfdXJs|dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz|urlopen|vanemalukk|aG9tZXRoZWF0ZXIuanBn|True|I1I111|isPlayable|False|i11iiI111I|oO0OOoo0OO|Y2hhbm5lbA|JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw|gksie0s011saew|executebuiltin|43|I1IIIii|I11iii1Ii|partition|W0NPTE9SID0gd2hpdGVdTWF4IGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ|OOOO|49|o0OOoo0OO0OOO|c3BlY2lhbDovL3VzZXJkYXRhL2FkdmFuY2Vkc2V0dGluZ3MueG1s|TmV3IGFkdmFuY2VkIHN0cmVhbWluZyBzZXR0aW5ncyBhZGRlZC4|W0NPTE9SID0gd2hpdGVdVHJpYWwgYWNjb3VudDogWy9DT0xPUl0|play_resolved_url|O0ii1ii1ii|ooooooO0oo|Request|a2FzdXRhamFuaW1p|repr|Oo0ooO0oo0oO|televisioonilink|YWRkb24ueG1s|OOO00O0O|get_runtime_path|andmelink|dGhlYXRlci5qcGc|O000OOo00oo|o0O0OOO0Ooo|YmE0YzFiYTVkYTg5ODIzZWQ0ZjVlMmExMjhkNDBlMGM|W0NPTE9SID0gd2hpdGVdRXhwaXJlczogWy9DT0xPUl0|o000O0o|channel|getroot|W0NPTE9SID0gd2hpdGVdU3RhdHVzOiBbL0NPTE9SXQ|headers|64|findall|get|ZGVmYXVsdGxvZ28ucG5n|I1iII1iiII|WW91ciBrb2RpIHZlcnNpb24gaXMgb3V0ZGF0ZWQh|o00oooO0Oo|I1IIiiIiii|else|dd678faae9ac167bc83abf78e5cb2f3f0688d3a3|fromtimestamp|OO00O0O0O00Oo|JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA|W0NPTE9SID0gd2hpdGVdVXNlcjogWy9DT0xPUl0|Accept|iI|iIi1iIiii111|return|iIiiiI|Oo0oO0ooo|II11i1iIiII1|Iii1ii1II11i|arhiivilink|TG9naW4gZmFpbGVk|dXJs|strftime|OOoooooO|dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM|80|O0i1II1Iiii1I11|aHR0cDovL3hwb3J0cy5kZG5zLm5ldA|83|O0OoOoo00o|ZGVzY3JpcHRpb24|parse|87|ZGVzY19pbWFnZQ|89|iIiIIIi|message|O000OO0|II1I|for|filmilink|90|91|in|TGl2ZSBDaGFubmVscyBNZW51IA|II|O0o0O00Oo0o0|96|97|Vk9EIGNoYW5uZWxzIG1lbnUg|O00OOOoOoo0O|I111i1i1111i|ii11i1i1ii00ooo00o0o0o0o|oooooOoo0ooo|iiIIi1IiIi11|file|OOoOO0oo0ooO|Ii1Ii1iiii11|cmVzb3VyY2Vz|iiiI11|I11i1I1I|o0OO00oO|dXNlcl9pbmZv|c2V0dGluZ3NfaWNvbi5wbmc|O0O00o0OOO0|YXJjaGl2ZV9pY29uLnBuZw|VFYgU2hvd3M|TXkgYWNjb3VudCBNZW51IA|O0ooo0O0oo0|eHBvcnRzdHY|ooo00OOOooO|YWNjb3VudF9pY29uLnBuZw|c2FsYXNvbmE|uuenduslink|iiII1i1|iiIiII1|xml|int|Ooo0|open|xbmc|LIST|exit|extra|I1II11IiII|ooOOoooooo|dHZjLmpwZw|oo0OooOOo0|bWF4X2Nvbm5lY3Rpb25z|T29PbzAwbw|read|T09PME9Pbw|ooOOO00Ooo|oOOOO|oOOo|VmlkZW8gT24gRGVtYW5k|UGFyZW50YWwgbG9jayA|c3RyaWltaXYybGp1bmQ|iIIIi1|stream_id|OOO00O|i1Iii1i1I|bGl2ZV9pY29uLnBuZw|oo00O00oO|TG9naW4gU3VjY2Vzcw|available_channels|not|o0oOoO00o|Oo|amRhdGEgbG9hZGVkIA|UGFyZW50YWwgbG9jaw|setdefaultencoding|I1I1i1|U2V0dGluZ3MgbWVudQ|json|time|name|IIii1Ii1|calendar|plot|o00oOO0o|dm9kX2ljb24ucG5n|I1I1IiI1|bm9wb3N0ZXIuanBn|iii|close|sys|U3RhcnRpbmcgdXA|close_item_list|VFYgQ2F0Y2ggVXA|OOO00|archive|hashlib|version|keyboard_input|tvshows|o00ooo0|ZGVmYXVsdC5weQ|c2VyaWVzLmpwZw|dmFuZW1ha29vZA|ZmFuYXJ0LnBuZw|i1I111I|VXNlci1BZ2VudA|TXkgQWNjb3VudA|dmFuZW1hbHVraw|iI1iII1|i1iII1IiiIiI1|iIiiiI1IiI1I1|translatePath|TGl2ZSBNZW51|iI11I1II1I1I|oo0oOo|i1iiIII111ii|Notification|Vk9EIE1lbnUg|OOo0o0|oo0OOo|default_text|WHBvcnRzIFRW|None|UExBWV9MSVZF|import|UExBWSBWT0Qg|I11i|TWFpbiBNZW51|tvlink|ZXhwX2RhdGU|U2V0dGluZ3M|SetViewMode|dXNlcm5hbWU|aWNvbi5wbmc|aXNfdHJpYWw|iiIiI|o0OoOoOO00|add_header|tv_archive|adult|o0OO0|get_params|IiI1i|start|oOOo0|TGl2ZSBUVg|STExSUkxaQ|xbmcplugin|120|iIIii1IIi|xbmcaddon|hexdigest|timetuple|Container|available|Porn|i1Ii|plugintools|noposter|EPISODES|OoOo|ii|Channels|relocate|I1i1iI1i|Lopplink|continue|TkVYVDog|IIII|utf8|c3RhdHVz|LOAD_LIVE|load|Parental|duration|contain|get_epg|replace|content|RVJST1I|OOO0OOo|MjU0NjE|I1Ii111|I11II1i|TESTING|Tk9XOiA|improve|scat_id|theater|OoOo00o|xbmcgui|TmV2ZXI|SUBCAT|reload|tv|MOVIES|exists|is|o0OO00|515|series|ADULTS|YXV0aA|stream|timegm|Adults|encode|o00|decode|jpg|leeztv|values|urllib|IIi|utcnow|adults|OOo|Entry|Adult|split|point|write|o0OOO|strip|etree|There|oo000|ADULT|loads|XBMC|cats|list|http|WWVz|i1|2000|Ii1iIIIi1ii|S29kaSBwbHVnaW4gYnkgTWlra00|PORN|m3u8|striimiv2ljund|m|III1iII1I1ii|true|YWR2YW5jZWRzZXR0aW5ncy54bWw|TODO|QWxs|def|show|Lock|days|iptv|oooo|YXJ0|fanart|ooO0Oooo00|W0NPTE9SIGdyZXldJXMgWy9DT0xPUl0|url|c3RyZWFtX3VybA|porn|get_setting|exec|set_view|IIiiiiiiIi1I1|cat|Tm8|may|md5|XXX|any|and|loc|M|min|ADD|com|are|xxx|php|timedelta|utf|Get|H|Y|o0O|IS|ts|s|as|oo|O0|re|rb|TV|no|Mw|u|YmFja2dyb3VuZC5qcGc|n|w|add_item".split("|")))