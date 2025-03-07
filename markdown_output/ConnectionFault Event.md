Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConnectionFault Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueueManager Interface](topic1643.md) : ConnectionFault Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that is raised when a connection fault has been detected. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ConnectionFault As EventHandler(Of Exception)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueueManager](topic1643.md)
    Dim handler As EventHandler(Of Exception)
     
    AddHandler instance.ConnectionFault, handler  
  
C#|   
---|---  
      
    
    event EventHandler<Exception> ConnectionFault  
  
# Event Data

The event handler receives an argument of type Exception containing data related to this event. The following **Exception** properties provide information specific to this event.

Property| Description  
---|---  
Data|   
HelpLink|   
HResult|   
InnerException|   
Message|   
Source|   
StackTrace|   
TargetSite|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotQueueManager Interface](topic1643.md)   
[IAutopilotQueueManager Members](topic1644.md)


