export NDK_HOME=/home/briarmoss/Documents/android-ndk-r25b
export PATH=$NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH

export CFLAGS="--sysroot=$NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/sysroot -I$NDK_HOME/sysroot/usr/include -I$NDK_HOME/sysroot/usr/include/aarch64-linux-android"
export LDFLAGS="--sysroot=$NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64/sysroot -L$NDK_HOME/sysroot/usr/lib/aarch64-linux-android -L$NDK_HOME/sysroot/usr/lib"
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH


p4a apk --private $PWD --package=org.test.myapp --name "My App" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy --arch=armeabi-v7a --arch=arm64-v8a --copy-libs --sdk_dir=$ANDROIDSDK --ndk_dir=$NDK_HOME --android_api=$ANDROIDAPI --ndk-api=$NDKAPI
