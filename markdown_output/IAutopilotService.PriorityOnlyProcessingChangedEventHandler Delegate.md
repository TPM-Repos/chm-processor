Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAutopilotService.PriorityOnlyProcessingChangedEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : IAutopilotService.PriorityOnlyProcessingChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The new value of the 'Process Priority Tags Only' setting.

Glossary Item Box

Represents a method that will handle the [PriorityOnlyProcessingChanged](topic1684.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub IAutopilotService.PriorityOnlyProcessingChangedEventHandler( _
       ByVal _value_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [IAutopilotService.PriorityOnlyProcessingChangedEventHandler](topic1979.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void IAutopilotService.PriorityOnlyProcessingChangedEventHandler( 
       bool _value_
    )  
  
#### Parameters

 _value_
    The new value of the 'Process Priority Tags Only' setting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService.PriorityOnlyProcessingChangedEventHandler Members](topic1979.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


