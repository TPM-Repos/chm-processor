Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAutopilotService.PriorityTagsAddedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : IAutopilotService.PriorityTagsAddedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tags_
    The collection of added priority tags.

Glossary Item Box

Represents a method that will handle the [PriorityTagsAdded](topic1685.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub IAutopilotService.PriorityTagsAddedEventHandler( _
       ByVal _tags_ As IEnumerable(Of String) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [IAutopilotService.PriorityTagsAddedEventHandler](topic1980.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void IAutopilotService.PriorityTagsAddedEventHandler( 
       IEnumerable<string> _tags_
    )  
  
#### Parameters

 _tags_
    The collection of added priority tags.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService.PriorityTagsAddedEventHandler Members](topic1980.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


