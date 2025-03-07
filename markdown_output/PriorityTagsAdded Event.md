Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PriorityTagsAdded Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : PriorityTagsAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when new priority tags have been added to the priority tags collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PriorityTagsAdded As [IAutopilotService.PriorityTagsAddedEventHandler](topic1980.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim handler As [IAutopilotService.PriorityTagsAddedEventHandler](topic1980.md)
     
    AddHandler instance.PriorityTagsAdded, handler  
  
C#|   
---|---  
      
    
    event [IAutopilotService.PriorityTagsAddedEventHandler](topic1980.md) PriorityTagsAdded  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


