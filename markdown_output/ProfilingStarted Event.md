Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProfilingStarted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProfilerSpecificationMonitor Class](topic3838.md) : ProfilingStarted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the monitored specification should start being profiled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ProfilingStarted As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProfilerSpecificationMonitor](topic3838.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ProfilingStarted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ProfilingStarted  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProfilerSpecificationMonitor Class](topic3838.md)   
[ProfilerSpecificationMonitor Members](topic3839.md)


