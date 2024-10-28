
set(SRCFILES
        "fmi4c.c"
        "fmi4c_utils.c"

        "${PROJECT_SOURCE_DIR}/3rdparty/minizip/miniunz.c"
        "${PROJECT_SOURCE_DIR}/3rdparty/minizip/ioapi.c"
        "${PROJECT_SOURCE_DIR}/3rdparty/minizip/mztools.c"
        "${PROJECT_SOURCE_DIR}/3rdparty/minizip/unzip.c"
        "${PROJECT_SOURCE_DIR}/3rdparty/ezxml/ezxml.c"
)
if (WIN32)
    list(APPEND SRCFILES "${PROJECT_SOURCE_DIR}/3rdparty/minizip/iowin32.c")
endif()

add_library(fmi4c ${SRCFILES})

target_compile_definitions(fmi4c PUBLIC HAVE_MEMMOVE=1 EZXML_NOMMAP USE_FILE32API)
if (BUILD_SHARED_LIBS)
    # Only set DLLEXPORT when producing the library, when consumed dllimport will be assumed
    target_compile_definitions(fmi4c PRIVATE FMI4C_DLLEXPORT)
else()
    # When using as a static library (on windows) FMI4C_STATIC must be defined, otherwise dllimport will be assumed
    target_compile_definitions(fmi4c PUBLIC FMI4C_STATIC)
    # Must use position independent code if intend to include static fmi4c lib into shared (dll) consumer
    set_target_properties(fmi4c PROPERTIES POSITION_INDEPENDENT_CODE ON)
endif()

target_include_directories(fmi4c
        PUBLIC
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include>"
        "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
        PRIVATE
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../3rdparty>"
        "${CMAKE_CURRENT_SOURCE_DIR}"
)


# Internal dependecy (PRIVATE) on zlib and ${CMAKE_DL_LIBS}) for libdl on Linux
target_link_libraries(fmi4c PRIVATE ZLIB::ZLIB ${CMAKE_DL_LIBS})
