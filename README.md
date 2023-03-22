# WP-killer
 vulnerability scanner for wordpress

# Usage 

```
usage: main.py [-h] [-t THREADS] [-u URL] [-f FILE]

options:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads
  -u URL, --url URL     Target url
  -f FILE, --file FILE  Target file
```

# Example
* targets from file
```
python3 main.py -f found_websites.txt
```
* target from input
```
python3 main.py -u dp11.ir
```

![alt text](https://i.imgur.com/x97Pqnv.png)
