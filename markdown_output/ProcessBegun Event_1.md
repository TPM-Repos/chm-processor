Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessBegun Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [EventProxyReportWriter Class](topic10392.md) : ProcessBegun Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a process is begun. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ProcessBegun As [ProcessEventHandler](topic10509.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [EventProxyReportWriter](topic10392.md)
    Dim handler As [ProcessEventHandler](topic10509.md)
     
    AddHandler instance.ProcessBegun, handler  
  
C#|   
---|---  
      
    
    public event [ProcessEventHandler](topic10509.md) ProcessBegun  
  
# Event Data

The event handler receives an argument of type [ProcessEventArgs](topic10424.md) containing data related to this event. The following **ProcessEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ProcessClass](topic10431.md)| Gets the process class.   
[ProcessDescription](topic10432.md)| Gets the process description.   
[ProcessTarget](topic10433.md)| Gets the process target.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EventProxyReportWriter Class](topic10392.md)   
[EventProxyReportWriter Members](topic10393.md)


