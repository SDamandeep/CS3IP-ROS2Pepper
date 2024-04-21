// Generated by gencpp from file naoqi_bridge_msgs/IntArrayStamped.msg
// DO NOT EDIT!


#ifndef NAOQI_BRIDGE_MSGS_MESSAGE_INTARRAYSTAMPED_H
#define NAOQI_BRIDGE_MSGS_MESSAGE_INTARRAYSTAMPED_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace naoqi_bridge_msgs
{
template <class ContainerAllocator>
struct IntArrayStamped_
{
  typedef IntArrayStamped_<ContainerAllocator> Type;

  IntArrayStamped_()
    : header()
    , data()  {
    }
  IntArrayStamped_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , data(_alloc)  {
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> const> ConstPtr;

}; // struct IntArrayStamped_

typedef ::naoqi_bridge_msgs::IntArrayStamped_<std::allocator<void> > IntArrayStamped;

typedef boost::shared_ptr< ::naoqi_bridge_msgs::IntArrayStamped > IntArrayStampedPtr;
typedef boost::shared_ptr< ::naoqi_bridge_msgs::IntArrayStamped const> IntArrayStampedConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace naoqi_bridge_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'naoqi_bridge_msgs': ['/home/dmerej/src/master/tools/qitoolchain/rosbag/workspace/src/naoqi_bridge_msgs/msg'], 'geometry_msgs': ['/home/dmerej/src/master/tools/qitoolchain/rosbag/workspace/src/common_msgs/geometry_msgs/msg'], 'std_msgs': ['/home/dmerej/src/master/tools/qitoolchain/rosbag/workspace/src/std_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1ce4762ce13f3d9e1f17586acc253067";
  }

  static const char* value(const ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1ce4762ce13f3d9eULL;
  static const uint64_t static_value2 = 0x1f17586acc253067ULL;
};

template<class ContainerAllocator>
struct DataType< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "naoqi_bridge_msgs/IntArrayStamped";
  }

  static const char* value(const ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
int32[] data\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct IntArrayStamped_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::naoqi_bridge_msgs::IntArrayStamped_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // NAOQI_BRIDGE_MSGS_MESSAGE_INTARRAYSTAMPED_H
