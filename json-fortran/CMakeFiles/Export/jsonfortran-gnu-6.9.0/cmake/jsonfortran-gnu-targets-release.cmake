#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "jsonfortran" for configuration "Release"
set_property(TARGET jsonfortran APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(jsonfortran PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so.6.9.0"
  IMPORTED_SONAME_RELEASE "libjsonfortran.so.6.9"
  )

list(APPEND _IMPORT_CHECK_TARGETS jsonfortran )
list(APPEND _IMPORT_CHECK_FILES_FOR_jsonfortran "${_IMPORT_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.so.6.9.0" )

# Import target "jsonfortran-static" for configuration "Release"
set_property(TARGET jsonfortran-static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(jsonfortran-static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "Fortran"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS jsonfortran-static )
list(APPEND _IMPORT_CHECK_FILES_FOR_jsonfortran-static "${_IMPORT_PREFIX}/jsonfortran-gnu-6.9.0/lib/libjsonfortran.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
