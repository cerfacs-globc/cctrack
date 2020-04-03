# Install script for directory: /data/home/globc/page/tracking/json-fortran-6.9.0

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so.6.9.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so.6.9"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib" TYPE SHARED_LIBRARY FILES
    "/data/home/globc/page/tracking/json-fortran/lib/libjsonfortran.so.6.9.0"
    "/data/home/globc/page/tracking/json-fortran/lib/libjsonfortran.so.6.9"
    "/data/home/globc/page/tracking/json-fortran/lib/libjsonfortran.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so.6.9.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so.6.9"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/data/softs/local/binutils225/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib" TYPE STATIC_LIBRARY FILES "/data/home/globc/page/tracking/json-fortran/lib/libjsonfortran.a")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib" TYPE DIRECTORY FILES "/data/home/globc/page/tracking/json-fortran/include/")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets.cmake"
         "/data/home/globc/page/tracking/json-fortran/CMakeFiles/Export/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake" TYPE FILE FILES "/data/home/globc/page/tracking/json-fortran/CMakeFiles/Export/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake" TYPE FILE FILES "/data/home/globc/page/tracking/json-fortran/CMakeFiles/Export/jsonfortran-gnu-6.9.0/cmake/jsonfortran-gnu-targets-release.cmake")
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/cmake" TYPE FILE FILES
    "/data/home/globc/page/tracking/json-fortran/pkg/jsonfortran-gnu-config.cmake"
    "/data/home/globc/page/tracking/json-fortran/jsonfortran-gnu-config-version.cmake"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jsonfortran-gnu-6.9.0/lib/pkgconfig" TYPE FILE FILES "/data/home/globc/page/tracking/json-fortran/json-fortran.pc")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/data/home/globc/page/tracking/json-fortran/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
