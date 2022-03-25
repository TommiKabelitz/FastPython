!A generic program to demonstrate the integration between python and fortran for
!example.
!Compiled into exe.x using "gfortran -o exe.x genericExecutable.f90"
!Compatable with ifort also.
program genericExecutable
  implicit None

  character(len=256) :: inputFile
  integer            :: fileunit = 101
  integer            :: nx,ny,nz,nt

  
  read(*,*) inputFile
  write(*,*) "Given input file is: ", trim(inputFile)
  write(*,*) "Reading from file"
  open(101,file=trim(inputFile),action='read',status='old',form='formatted')
  read(101,*) nx
  read(101,*) ny
  read(101,*) nz
  read(101,*) nt
  close(101)
  write(*,*) "The file contains:"
  write(*,*) nx
  write(*,*) ny
  write(*,*) nz
  write(*,*) nt

  write(*,*) "Beginning calculations..."
  write(*,*) "Finished calculations"
end program genericExecutable
