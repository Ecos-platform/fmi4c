cmake_minimum_required(VERSION 3.19)
project(fmi4c C)
set(CMAKE_C_STANDARD 99)

option(FMI4C_BUILD_DOCUMENTATION "Build Doxygen documentation" OFF)
option(FMI4C_BUILD_TEST "Build test executable" OFF)
option(FMI4C_USE_INCLUDED_ZLIB "Use the included zlib (statically linked) even if a system version is available" OFF)

include(CMakePackageConfigHelpers)
include(GNUInstallDirs)

if (FMI4C_BUILD_DOCUMENTATION)
    add_subdirectory(doc)
endif()

if(NOT FMI4C_USE_INCLUDED_ZLIB)
    find_package(ZLIB MODULE)
endif()
# If zlib can not be found in the system, then build local version
if (NOT ZLIB_FOUND)
    set(zlib_dir "3rdparty/zlib")
    message(STATUS "Using included ZLIB: ${zlib_dir}")
    # Must use position independent code if intend to include static zlib into shared (dll) fmi4c lib
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
    # Add bundled sources, (EXCLUDE_FROM_ALL prevents zlib from being installed with fmi4c)
    add_subdirectory(${zlib_dir} EXCLUDE_FROM_ALL)
    # We highjack the zlibstatic target from the original build system, but it does not have the include directory properties set, so lets add them here
    target_include_directories(zlibstatic INTERFACE
            $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/${zlib_dir}>
            $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/${zlib_dir}>
    )
    # Use alias to match name that find-module uses
    add_library(ZLIB::ZLIB ALIAS zlibstatic)

endif()

add_subdirectory(src)

if (${FMI4C_BUILD_TEST})
  enable_testing()
  add_subdirectory(test)
  if (WIN32 AND BUILD_SHARED_LIBS)
    # On Windows there is no RPATH, so fmi4c.dll must be copied to the test directory if test should be runnable from any directory
    add_custom_command(TARGET fmi4c POST_BUILD
                       COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:fmi4c> ${CMAKE_CURRENT_BINARY_DIR}/test)
  endif()
endif()

configure_package_config_file(cmake/config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/fmi4c-config.cmake"
        INSTALL_DESTINATION "${CMAKE_INSTALL_DATADIR}/fmi4c"
        NO_SET_AND_CHECK_MACRO)

install(
        FILES
        "${CMAKE_CURRENT_BINARY_DIR}/fmi4c-config.cmake"
        DESTINATION
        "${CMAKE_INSTALL_DATADIR}/fmi4c")


install(TARGETS fmi4c EXPORT fmi4c-targets)
if (TARGET zlibstatic)
    install(TARGETS zlibstatic EXPORT fmi4c-targets)
endif()
install(DIRECTORY "include/" DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
install(DIRECTORY "3rdparty/fmi" DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
install(EXPORT fmi4c-targets
        NAMESPACE fmi4c::
        DESTINATION "${CMAKE_INSTALL_DATADIR}/fmi4c")
