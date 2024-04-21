# This is an autogenerated file. Do not edit

get_filename_component(_cur_dir ${CMAKE_CURRENT_LIST_FILE} PATH)
set(_root_dir "${_cur_dir}/../../../")
get_filename_component(ROOT_DIR ${_root_dir} ABSOLUTE)

 
set(ALAUDIO_INCLUDE_DIRS "${ROOT_DIR}/include;" CACHE STRING "" FORCE)
mark_as_advanced(ALAUDIO_INCLUDE_DIRS)
   
set(ALAUDIO_LIBRARIES
  ${ROOT_DIR}/lib/libalaudio.so
  CACHE STRING "" FORCE)

mark_as_advanced(ALAUDIO_LIBRARIES)
 
set(ALAUDIO_PACKAGE_FOUND TRUE CACHE INTERNAL "" FORCE)
 
set(ALAUDIO_DEPENDS "ALEXTRACTOR;ALTHREAD;ALPROXIES;ALCOMMON;BOOST_SIGNALS;RTTOOLS;ALVALUE;ALERROR;QI;BOOST;BOOST_ATOMIC;BOOST_DATE_TIME;BOOST_CHRONO;BOOST_FILESYSTEM;BOOST_SYSTEM;BOOST_REGEX;BOOST_PROGRAM_OPTIONS;OPENSSL;BOOST_LOCALE;BOOST_THREAD;ICU;PTHREAD;DL;RT" CACHE INTERNAL "" FORCE)
 