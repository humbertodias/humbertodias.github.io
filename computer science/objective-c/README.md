# Objective-C Trainning

Learn ObjC by examples


## Hello World

<pre>
cat << EOF > hello.m
#import &lt;Foundation/Foundation.h&gt;
#import &lt;CoreLocation/CoreLocation.h&gt;

int main (int argc, const char * argv[]) {
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

    CLLocationManager *locationManager = [[CLLocationManager alloc] init];
    NSLog(@"Hello world!");

    [pool drain];

    return 0;
}
EOF
</pre>


## How to compile

<pre>
$ gcc hello.m -o hello -ObjC -framework Foundation -framework CoreLocation
$ ./hello
2015-09-28 00:29:53.782 hello[17106:763144] Hello world!
</pre>