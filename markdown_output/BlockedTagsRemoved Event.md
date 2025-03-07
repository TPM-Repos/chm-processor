Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BlockedTagsRemoved Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : BlockedTagsRemoved Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when blocked tags have been removed from the blocked tags collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event BlockedTagsRemoved As [IAutopilotService.BlockedTagsRemovedEventHandler](topic1978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim handler As [IAutopilotService.BlockedTagsRemovedEventHandler](topic1978.md)
     
    AddHandler instance.BlockedTagsRemoved, handler  
  
C#|   
---|---  
      
    
    event [IAutopilotService.BlockedTagsRemovedEventHandler](topic1978.md) BlockedTagsRemoved  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


