Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationStepChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) : NavigationStepChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle the event raised when a navigation step is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub NavigationStepChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [NavigationStepEventArgs](topic10205.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [NavigationStepChangedEventHandler](topic10264.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void NavigationStepChangedEventHandler( 
       object _sender_ ,
       [NavigationStepEventArgs](topic10205.md) _e_
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

[NavigationStepChangedEventHandler Members](topic10264.md)   
[DriveWorks.Navigation Namespace](topic10114.md)


