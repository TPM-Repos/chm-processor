Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAutopilotService.BlockedTagsRemovedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : IAutopilotService.BlockedTagsRemovedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tags_
    The collection of removed blocked tags.

Glossary Item Box

Represents a method that will handle the [BlockedTagsRemoved](topic1678.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub IAutopilotService.BlockedTagsRemovedEventHandler( _
       ByVal _tags_ As IEnumerable(Of String) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [IAutopilotService.BlockedTagsRemovedEventHandler](topic1978.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void IAutopilotService.BlockedTagsRemovedEventHandler( 
       IEnumerable<string> _tags_
    )  
  
#### Parameters

 _tags_
    The collection of removed blocked tags.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService.BlockedTagsRemovedEventHandler Members](topic1978.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


