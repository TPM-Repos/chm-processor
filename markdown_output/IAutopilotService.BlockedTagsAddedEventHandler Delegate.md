Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAutopilotService.BlockedTagsAddedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : IAutopilotService.BlockedTagsAddedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tags_
    The collection of added blocked tags.

Glossary Item Box

Represents a method that will handle the [BlockedTagsAdded](topic1677.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub IAutopilotService.BlockedTagsAddedEventHandler( _
       ByVal _tags_ As IEnumerable(Of String) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [IAutopilotService.BlockedTagsAddedEventHandler](topic1977.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void IAutopilotService.BlockedTagsAddedEventHandler( 
       IEnumerable<string> _tags_
    )  
  
#### Parameters

 _tags_
    The collection of added blocked tags.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService.BlockedTagsAddedEventHandler Members](topic1977.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


