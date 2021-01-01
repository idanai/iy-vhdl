library ieee;
use ieee.std_logic_1164.all;

entity full_adder is
	port (
		a, b: in std_logic;
		sum, carry: out std_logic);
end entity;

architecture behaviour of full_adder is
begin
	sum <= a xor b;
	carry <= a and b;
end behaviour;