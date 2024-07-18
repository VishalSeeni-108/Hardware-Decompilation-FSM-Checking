import spydrnet as sdn
import plot_connectivity_graph as pcg

#netlist = sdn.parse('fifo.edf')
netlist = sdn.parse("one_counter.edf")

pcg.run()