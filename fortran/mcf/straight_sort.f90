subroutine straight_sort(arr)
implicit none
real, dimension(:), intent(inout) :: arr
integer :: i, j, n
real :: a
n= size(arr)
do j= 2, n
   a= arr(j)
   do i= j - 1, 1, -1
      if (arr(i) <= a) exit
      arr(i + 1)= arr(i)
   end do
   arr(i + 1)= a
end do
return
end subroutine straight_sort
