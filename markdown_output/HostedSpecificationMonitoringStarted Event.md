Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HostedSpecificationMonitoringStarted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProfilerSpecificationMonitor Class](topic3838.md) : HostedSpecificationMonitoringStarted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the profiler should start monitoring a specification that is being hosted in this specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event HostedSpecificationMonitoringStarted As [SpecificationContextEventHandler](topic11821.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProfilerSpecificationMonitor](topic3838.md)
    Dim handler As [SpecificationContextEventHandler](topic11821.md)
     
    AddHandler instance.HostedSpecificationMonitoringStarted, handler  
  
C#|   
---|---  
      
    
    public event [SpecificationContextEventHandler](topic11821.md) HostedSpecificationMonitoringStarted  
  
# Event Data

The event handler receives an argument of type [SpecificationContextEventArgs](topic11284.md) containing data related to this event. The following **SpecificationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic11291.md)| Get the specification context.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProfilerSpecificationMonitor Class](topic3838.md)   
[ProfilerSpecificationMonitor Members](topic3839.md)


