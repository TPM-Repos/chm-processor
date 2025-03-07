Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAutopilotService.PriorityTagsRemovedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : IAutopilotService.PriorityTagsRemovedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tags_
    The collection of removed priority tags.

Glossary Item Box

Represents a method that will handle the [PriorityTagsRemoved](topic1686.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub IAutopilotService.PriorityTagsRemovedEventHandler( _
       ByVal _tags_ As IEnumerable(Of String) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [IAutopilotService.PriorityTagsRemovedEventHandler](topic1981.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void IAutopilotService.PriorityTagsRemovedEventHandler( 
       IEnumerable<string> _tags_
    )  
  
#### Parameters

 _tags_
    The collection of removed priority tags.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService.PriorityTagsRemovedEventHandler Members](topic1981.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


