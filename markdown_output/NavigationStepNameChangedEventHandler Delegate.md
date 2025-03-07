Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationStepNameChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) : NavigationStepNameChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle the event raised when a navigation step's name is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub NavigationStepNameChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [NavigationStepNameChangedEventArgs](topic10213.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [NavigationStepNameChangedEventHandler](topic10265.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void NavigationStepNameChangedEventHandler( 
       object _sender_ ,
       [NavigationStepNameChangedEventArgs](topic10213.md) _e_
    )  
  
#### Parameters

 _sender_
    The source of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NavigationStepNameChangedEventHandler Members](topic10265.md)   
[DriveWorks.Navigation Namespace](topic10114.md)


