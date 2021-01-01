library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity full_adder_tb is end entity;

architecture arc of full_adder_tb is

	component full_adder
		port (
			a, b: in std_logic;
			sum, carry: out std_logic);
	end component;

	signal a, b, sum, carry: std_logic;
	signal counter: unsigned(1 downto 0):= (others=>'0');
begin
	c1_and : full_adder port map(a=>a, b=>b, sum=>sum, carry=>carry);
	a <= counter(0);
	b <= counter(1);
	process is
	begin
		for k in 0 to 3 loop
			wait for 1 fs;
			counter <= counter + 1;
		end loop;

		assert false report "Finished testing 'full_adder'";
		wait;

	end process;
end architecture;