cmake_minimum_required(VERSION 3.3)
project(fmi4c C)
set(CMAKE_C_STANDARD 99)

set(target_name fmi4c)

option(FMI4C_BUILD_DOCUMENTATION "Build Doxygen documentation" OFF)
option(FMI4C_BUILD_TEST "Build test executable" OFF)
option(FMI4C_BUILD_SHARED "Build as shared library (DLL)" ON)

if (${FMI4C_BUILD_DOCUMENTATION})
    add_subdirectory(doc)
endif()

set(SRCFILES
    src/fmi4c.c
    src/fmi4c_utils.c
    src/fmi4c_private.h
    src/fmi4c_utils.h
    src/fmi4c_placeholders.h
    include/fmi4c.h
    include/fmi4c_public.h
    include/fmi4c_common.h
    include/fmi4c_types.h
    include/fmi4c_types_fmi1.h
    include/fmi4c_types_fmi2.h
    include/fmi4c_types_fmi3.h
    include/fmi4c_functions_fmi1.h
    include/fmi4c_functions_fmi2.h
    include/fmi4c_functions_fmi3.h
    3rdparty/ezxml/ezxml.c
    3rdparty/ezxml/ezxml.h)
if (MSVC)
    SET(SRCFILES ${SRCFILES} 3rdparty/dirent/dirent.h)
endif()

if (FMI4C_BUILD_SHARED)
    add_library(${target_name} SHARED ${SRCFILES})
else()
    add_library(${target_name} STATIC ${SRCFILES})
endif()

target_compile_definitions(${target_name} PUBLIC HAVE_MEMMOVE=1 EZXML_NOMMAP USE_FILE32API)
if (FMI4C_BUILD_SHARED)
    # Only set DLLEXPORT when producing the library, when consumed dllimport will be assumed
    target_compile_definitions(${target_name} PRIVATE FMI4C_DLLEXPORT)
else()
    # When using as a static library (on windows) FMI4C_STATIC must be defined, otherwise dllimport will be assumed
    target_compile_definitions(${target_name} PUBLIC FMI4C_STATIC)
    # Must use position independent code if intend to include static fmi4c lib into shared (dll) consumer
    set_target_properties(${target_name} PROPERTIES POSITION_INDEPENDENT_CODE ON)
endif()

target_include_directories(${target_name} PUBLIC include)
target_include_directories(${target_name} PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/3rdparty>)
target_include_directories(${target_name} PRIVATE src)

install(TARGETS ${target_name}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
install(DIRECTORY include
        DESTINATION .)
install(DIRECTORY 3rdparty/fmi
        DESTINATION include)

if (${FMI4C_BUILD_TEST})
  enable_testing()
  add_subdirectory(test)
  if (WIN32 AND FMI4C_BUILD_SHARED)
    # On Windows there is no RPATH, so fmi4c.dll must be copied to the test directory if test should be runnable from any directory
    add_custom_command(TARGET fmi4c POST_BUILD
                       COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:fmi4c> ${CMAKE_CURRENT_BINARY_DIR}/test)
  endif()
endif()
