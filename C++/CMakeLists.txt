cmake_minimum_required(VERSION 3.14)
project(LeetCode)

include(CTest)
enable_testing()

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

add_executable(test208
  src/_00208_ImplementTrie.cpp
  test/_00208_ImplementTrie_test.cpp
)

add_executable(test909
  src/_00909_SnakesAndLadders.cpp
  test/_00909_SnakesAndLadders_test.cpp
)

target_link_libraries(test151 gtest_main)
target_link_libraries(test208 gtest_main)
target_link_libraries(test909 gtest_main)

include(GoogleTest)

gtest_discover_tests(test151)
gtest_discover_tests(test208)
gtest_discover_tests(test909)