Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PriorityOnlyProcessingChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : PriorityOnlyProcessingChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the 'Process Priority Tags Only' setting has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PriorityOnlyProcessingChanged As [IAutopilotService.PriorityOnlyProcessingChangedEventHandler](topic1979.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim handler As [IAutopilotService.PriorityOnlyProcessingChangedEventHandler](topic1979.md)
     
    AddHandler instance.PriorityOnlyProcessingChanged, handler  
  
C#|   
---|---  
      
    
    event [IAutopilotService.PriorityOnlyProcessingChangedEventHandler](topic1979.md) PriorityOnlyProcessingChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


