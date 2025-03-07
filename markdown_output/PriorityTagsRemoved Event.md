Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PriorityTagsRemoved Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : PriorityTagsRemoved Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when priority tags have been removed from the priority tags collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PriorityTagsRemoved As [IAutopilotService.PriorityTagsRemovedEventHandler](topic1981.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim handler As [IAutopilotService.PriorityTagsRemovedEventHandler](topic1981.md)
     
    AddHandler instance.PriorityTagsRemoved, handler  
  
C#|   
---|---  
      
    
    event [IAutopilotService.PriorityTagsRemovedEventHandler](topic1981.md) PriorityTagsRemoved  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


