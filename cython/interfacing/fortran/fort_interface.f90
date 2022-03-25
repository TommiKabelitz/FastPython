! Fortran module which interfaces the module of interest (fortmod) with the
! pertinent c types from iso_c_binding.

module fortmod_interface
  use iso_c_binding, only: c_int !Importing whichever types are required
  use fortmod, only: updategrid
  implicit None

contains
  ! Interface function which takes c types and passes them to the original
  ! routine. Rest of signature should be identical.
  ! Note also the bind(c) which makes the function c callable.
  subroutine c_updategrid(grid, nx, ny) bind(c)
    integer(c_int), dimension(nx,ny), intent(inout) :: grid
    integer(c_int), intent(in)  :: nx,ny
    call updategrid(grid, nx, ny)
  end subroutine c_updategrid

end module fortmod_interface
