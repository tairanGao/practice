# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = E:\Software\CLion\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = E:\Software\CLion\bin\cmake\win\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = E:\Github\practice\notes\Lintcode_C++

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = E:\Github\practice\notes\Lintcode_C++\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles\Lintcode_C__.dir\depend.make

# Include the progress variables for this target.
include CMakeFiles\Lintcode_C__.dir\progress.make

# Include the compile flags for this target's objects.
include CMakeFiles\Lintcode_C__.dir\flags.make

CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.obj: CMakeFiles\Lintcode_C__.dir\flags.make
CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.obj: ..\1343_SumofTwoStrings.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=E:\Github\practice\notes\Lintcode_C++\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Lintcode_C__.dir/1343_SumofTwoStrings.cpp.obj"
	C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\cl.exe @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoCMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.obj /FdCMakeFiles\Lintcode_C__.dir\ /FS -c E:\Github\practice\notes\Lintcode_C++\1343_SumofTwoStrings.cpp
<<

CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Lintcode_C__.dir/1343_SumofTwoStrings.cpp.i"
	C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\cl.exe > CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.i @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E E:\Github\practice\notes\Lintcode_C++\1343_SumofTwoStrings.cpp
<<

CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Lintcode_C__.dir/1343_SumofTwoStrings.cpp.s"
	C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\cl.exe @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoNUL /FAs /FaCMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.s /c E:\Github\practice\notes\Lintcode_C++\1343_SumofTwoStrings.cpp
<<

# Object files for target Lintcode_C__
Lintcode_C___OBJECTS = \
"CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.obj"

# External object files for target Lintcode_C__
Lintcode_C___EXTERNAL_OBJECTS =

Lintcode_C__.exe: CMakeFiles\Lintcode_C__.dir\1343_SumofTwoStrings.cpp.obj
Lintcode_C__.exe: CMakeFiles\Lintcode_C__.dir\build.make
Lintcode_C__.exe: CMakeFiles\Lintcode_C__.dir\objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=E:\Github\practice\notes\Lintcode_C++\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Lintcode_C__.exe"
	E:\Software\CLion\bin\cmake\win\bin\cmake.exe -E vs_link_exe --intdir=CMakeFiles\Lintcode_C__.dir --rc=C:\PROGRA~2\WI3CF2~1\10\bin\100183~1.0\x86\rc.exe --mt=C:\PROGRA~2\WI3CF2~1\10\bin\100183~1.0\x86\mt.exe --manifests  -- C:\PROGRA~2\MICROS~2\2019\BUILDT~1\VC\Tools\MSVC\1428~1.293\bin\Hostx86\x86\link.exe /nologo @CMakeFiles\Lintcode_C__.dir\objects1.rsp @<<
 /out:Lintcode_C__.exe /implib:Lintcode_C__.lib /pdb:E:\Github\practice\notes\Lintcode_C++\cmake-build-debug\Lintcode_C__.pdb /version:0.0  /machine:X86 /debug /INCREMENTAL /subsystem:console  kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib 
<<

# Rule to build all files generated by this target.
CMakeFiles\Lintcode_C__.dir\build: Lintcode_C__.exe

.PHONY : CMakeFiles\Lintcode_C__.dir\build

CMakeFiles\Lintcode_C__.dir\clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Lintcode_C__.dir\cmake_clean.cmake
.PHONY : CMakeFiles\Lintcode_C__.dir\clean

CMakeFiles\Lintcode_C__.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" E:\Github\practice\notes\Lintcode_C++ E:\Github\practice\notes\Lintcode_C++ E:\Github\practice\notes\Lintcode_C++\cmake-build-debug E:\Github\practice\notes\Lintcode_C++\cmake-build-debug E:\Github\practice\notes\Lintcode_C++\cmake-build-debug\CMakeFiles\Lintcode_C__.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles\Lintcode_C__.dir\depend

