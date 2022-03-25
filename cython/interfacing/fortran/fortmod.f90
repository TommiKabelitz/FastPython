! Fortran module containing a subroutine to update the Conway's game of life
! grid. Intended as an example of interfacing fortran and python.
! Note: also works for functions
module fortmod
  implicit None

contains
  subroutine updategrid(grid, nx, ny)
    integer, dimension(nx,ny), intent(inout) :: grid !1 represents alive, 0 dead
    integer, intent(in)  :: nx,ny

    integer                                  :: i,j,tot
    integer, dimension(nx)                   :: x_indices
    integer, dimension(ny)                   :: y_indices
    integer, dimension(nx,ny)                :: past_grid

    ! Storing the previous iteration of the grid
    past_grid = grid
    ! Vector valued subscripts for periodic boundary
    x_indices = [nx,(i,i=1,nx),1]
    y_indices = [ny,(i,i=1,ny),1]

    ! Looping through grid
    do j=1,ny
       do i=1,nx
          ! Summing neighbours
          tot = sum( past_grid(x_indices(i-1:i+1), y_indices(j-1:j+1)) ) - past_grid(i,j)

          ! Setting new state based on sum
          if (tot > 3) then
             grid(i,j) = 0
          else if (tot < 3 .and. past_grid(i,j) == 0) then
             grid(i,j) = 0
          else if (tot == 2 .and. past_grid(i,j) == 1) then
             grid(i,j) = 1
          else if (tot == 3) then
             grid(i,j) = 1
          else
             grid(i,j) = 0
          end if
          
       end do
    end do
  end subroutine updategrid

end module fortmod
