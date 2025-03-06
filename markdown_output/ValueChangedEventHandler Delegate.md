       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValueChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) : ValueChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle a value changed event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ValueChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ValueChangedEventArgs](topic9575.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ValueChangedEventHandler](topic9590.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ValueChangedEventHandler( 
       object _sender_ ,
       [ValueChangedEventArgs](topic9575.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValueChangedEventHandler Members](topic9590.md)   
[DriveWorks.Forms.DataModel Namespace](topic9371.md)


