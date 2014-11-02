from cs143sim.actors import Buffer
from cs143sim.actors import Flow
from cs143sim.actors import Host
from cs143sim.actors import Link
from cs143sim.actors import DataPacket
from cs143sim.actors import Router
from cs143sim.simulation import Controller
from cs143sim.simulation import ControlledEnvironment


def basic_buffer():
    return Buffer(env=ControlledEnvironment(controller=Controller()),
                  capacity=1, link=basic_link())


def basic_flow():
    return Flow(env=ControlledEnvironment(controller=Controller()),
                source=basic_host(), destination=basic_host(),
                amount=1.0)


def basic_host():
    return Host(env=ControlledEnvironment(controller=Controller()), address='')


def basic_link():
    return Link(env=ControlledEnvironment(controller=Controller()),
                source=basic_host(), destination=basic_host(),
                delay=1.0, rate=1.0, buffer_capacity=1)


def basic_packet():
    #return Packet(source=basic_host(), destination=basic_host(), number=1,
    #              acknowledgement=object())
    return DataPacket(env=ControlledEnvironment(controller=Controller()),
                      source=basic_host(), destination=basic_host(),
                      number=1, acknowledgement=object(), timestamp=0)


def basic_router():
    return Router(env=ControlledEnvironment(controller=Controller()),
                  address='')


def buffer_overflow():
    buffer_capacity = 2
    number_of_packets = 3
    buffer_ = basic_buffer()
    buffer_.env.controller.packet_loss[buffer_.link] = []
    packets = []
    for _ in range(number_of_packets):
        packet_ = basic_packet()
        packet_.size = 1
        packets.append(packet_)
    buffer_.capacity = buffer_capacity
    for packet_ in packets:
        buffer_.add(packet_)
        print(buffer_.packets)
    for i in range(number_of_packets):
        if i < buffer_capacity:
            assert packets[i] in buffer_.packets
        else:
            assert packets[i] not in buffer_.packets


def link_busy():
    link_ = basic_link()
    assert link_.buffer.capacity == 1
    packet_ = basic_packet()
    packet_.size = 1
    link_.busy = True
    link_.add(packet_)
    assert packet_ in link_.buffer.packets


def test_buffer():
    basic_buffer()
    buffer_overflow()


def test_flow():
    basic_flow()


def test_host():
    basic_host()


def test_link():
    basic_link()
    link_busy()


def test_packet():
    basic_packet()


def test_router():
    basic_router()
