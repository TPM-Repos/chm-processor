Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BlockedTagsAdded Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : BlockedTagsAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when new blocked tags have been added to the blocked tags collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event BlockedTagsAdded As [IAutopilotService.BlockedTagsAddedEventHandler](topic1977.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim handler As [IAutopilotService.BlockedTagsAddedEventHandler](topic1977.md)
     
    AddHandler instance.BlockedTagsAdded, handler  
  
C#|   
---|---  
      
    
    event [IAutopilotService.BlockedTagsAddedEventHandler](topic1977.md) BlockedTagsAdded  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


