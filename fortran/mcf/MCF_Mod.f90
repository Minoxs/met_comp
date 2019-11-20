!********************** MÓDULO METODOS_COMPUTACIONAIS_FISICA ************************
! Contém constantes nomeadas e interfaces das rotinas incluídas na Apostila:
!                         Introdução à Física Computacional                         
! Ref: http://professor.ufrgs.br/rgaelzer/pages/comp-phys
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Outubro/2019
MODULE Metodos_Computacionais_Fisica
use, intrinsic :: iso_fortran_env, only: dp => real64
implicit none
real(dp), parameter :: zero=  0.0e+00_dp, half=  0.5e+00_dp, one=  1.0e+00_dp, &
                       r3o2=  1.5e+00_dp, two=   2.0e+00_dp, r5o2= 2.5e+00_dp, &
                       three= 3.0e+00_dp, r7o2=  3.5e+00_dp, four= 4.0e+00_dp, &
                       r9o2=  4.5e+00_dp, five=  5.0e+00_dp, six=  6.0e+00_dp, &
                       seven= 7.0e+00_dp, eight= 8.0e+00_dp, nine= 9.0e+00_dp, &
                       ten=   1.0e+01_dp
real(dp), parameter :: pi=     3.14159265358979323846264338327950288419717_dp
real(dp), parameter :: rtpio2= 0.88622692545275801364908374167057259139877_dp ! raiz(pi)/2
real(dp), parameter :: pid2=   1.57079632679489661923132169163975144209858_dp ! pi/2
complex(dp), parameter :: z0= (zero, zero), z1= (one, zero), zi= (zero, one)
! Blocos de interfaces
abstract interface
   pure function fabst(x)
   import :: dp
   real(dp) :: fabst
   real(dp), intent(in) :: x
   end function fabst
!***
   function fzabst(z)
   import :: dp
   complex(dp) :: fzabst
   complex(dp), intent(in) :: z
   end function fzabst
!***
   subroutine fdfabst(x, fx, dfdx)
   import :: dp
   real(dp), intent(in) :: x
   real(dp), intent(out) :: fx, dfdx
   end subroutine fdfabst
!***
   subroutine vfdfabst(x, fx, dfdx)
   import :: dp
   real(dp), intent(in) :: x
   real(dp), dimension(:), intent(in)  :: fx
   real(dp), dimension(:), intent(out) :: dfdx
   end subroutine vfdfabst
end interface
!
interface
   subroutine dfdx_rich(f, x, h_ini, errest, dfdx, err_sai)
   import :: dp, fabst
   real(dp), intent(in)  :: x, h_ini, errest
   real(dp), intent(out) :: dfdx, err_sai
   procedure(fabst) :: f
   end subroutine dfdx_rich
!***
   module function simpson(f, n, a, b)
   real(dp)             :: simpson
   integer, intent(in)  :: n
   real(dp), intent(in) ::  a, b
   procedure(fabst)     :: f
   end function simpson
!***
   module function trapez(f, n, a, b)
   real(dp)             :: trapez
   integer, intent(in)  :: n
   real(dp), intent(in) ::  a, b
   procedure(fabst)     :: f
   end function trapez
!***
   function trapez_rom(f, a, b, n_ordem)
   import :: dp, fabst
   real(dp)             :: trapez_rom
   integer, intent(in)  :: n_ordem
   real(dp), intent(in) :: a, b
   procedure(fabst)     :: f
   end function trapez_rom
!***
   function pntmed_rom(f, a, b, n_ordem)
   import :: dp, fabst
   real(dp)             :: pntmed_rom
   integer, intent(in)  :: n_ordem
   real(dp), intent(in) :: a, b
   procedure(fabst)     :: f
   end function pntmed_rom
!***
   function pntmed_inf_rom(f, a, n_ordem)
   import :: dp, fabst
   real(dp)             :: pntmed_inf_rom
   integer, intent(in)  :: n_ordem
   real(dp), intent(in) :: a
   procedure(fabst)     :: f
   end function pntmed_inf_rom
!***
   subroutine rk4(x, y, h, ysai, derivs)
   import :: dp, vfdfabst
   real(dp), intent(in)                :: x, h
   real(dp), dimension(:), intent(in)  :: y
   real(dp), dimension(:), intent(out) :: ysai
   procedure(vfdfabst)                  :: derivs
   end subroutine rk4
end interface
! Rotinas auxiliares
interface
   module subroutine troca(a, b)
   real(dp), intent(inout) :: a, b
   end subroutine troca
!***
   module subroutine verifica_tamanhos(vint, string)
   character(len=*), intent(in) :: string
   integer, dimension(:), intent(in) :: vint
   end subroutine verifica_tamanhos
end interface
END MODULE Metodos_Computacionais_Fisica
