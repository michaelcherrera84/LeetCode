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

add_executable(test909
  src/_00909_SnakesAndLadders.cpp
  test/_00909_SnakesAndLadders_test.cpp
)

target_link_libraries(test151 gtest_main)
target_link_libraries(test909 gtest_main)

enable_testing()
add_test(NAME test151 COMMAND test151)
add_test(NAME test909 COMMAND test909)