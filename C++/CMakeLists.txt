cmake_minimum_required(VERSION 3.14)
project(ReverseWords)

set(CMAKE_CXX_STANDARD 17)

include(FetchContent)

FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/heads/main.zip
)

FetchContent_MakeAvailable(googletest)

add_executable(test151
  src/_00151_ReverseWordsInAString.cpp
  test/_00151_ReverseWordsInAString_test.cpp
)

target_link_libraries(test151 gtest_main)

enable_testing()
add_test(NAME runTests COMMAND runTests)